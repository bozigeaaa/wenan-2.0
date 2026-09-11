"""Validate collected news, publish an offline HTML archive, and check daily due state."""
import argparse
from datetime import date, datetime, timedelta, timezone
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / '.agents/skills/daily-industry-news/assets/daily-news.html'
NEWS = ROOT / 'outputs/news'
OUTPUT = ROOT / 'outputs'
BEIJING = timezone(timedelta(hours=8))
CONFIG = ROOT / '.agents/skills/daily-industry-news/references/collection-config.json'
SETTINGS = json.loads(CONFIG.read_text(encoding='utf-8'))
SLOTS = tuple(SETTINGS['dailyRunTimes'])
PRODUCTS = {'打包箱', '移动卫浴', '五金', '薄壁轻钢'}


def timestamp(value):
    try:
        parsed = datetime.fromisoformat(value.replace('Z', '+00:00'))
        if parsed.tzinfo is None:
            raise ValueError('Timezone required')
        return parsed
    except (TypeError, AttributeError, ValueError) as error:
        raise ValueError('Invalid timestamp: ' + str(value)) from error


def validate(report):
    date.fromisoformat(report['collectedDate'])
    timestamp(report['collectedAt'])
    if report.get('timeZone') != 'Asia/Shanghai':
        raise ValueError('Report timezone must be Asia/Shanghai')
    if report.get('run', {}).get('status') not in {'completed', 'partial', 'failed'}:
        raise ValueError('Run must have a final status')
    timestamp(report['run'].get('completedAt'))
    retrievals = report.get('retrievalTools', [])
    if not isinstance(retrievals, list):
        raise ValueError('Retrieval tools must be an array')
    successful_tools = set()
    for retrieval in retrievals:
        if retrieval.get('tool') not in SETTINGS['retrieval']['allowedTools']:
            raise ValueError('Use a canonical retrieval tool ID')
        if retrieval.get('status') == 'completed':
            if not retrieval.get('entries') or not retrieval.get('evidence'):
                raise ValueError('Completed retrieval needs actual queries or URLs and evidence')
            successful_tools.add(retrieval['tool'])
    if report['run']['status'] == 'completed' and len(successful_tools) < SETTINGS['retrieval']['minimumTools']:
        raise ValueError('Complete news collection requires two distinct successful retrieval tools')
    if report['run'].get('slot') not in (None, *SLOTS):
        raise ValueError('Invalid scheduled run slot')
    if any(slot not in SLOTS for slot in report.get('completedSlots', [])):
        raise ValueError('Invalid completed run slot')
    for key in ('window', 'scope'):
        if not report.get(key):
            raise ValueError('Missing report field: ' + key)
    if not isinstance(report.get('channels'), list) or any(not isinstance(row, list) or len(row) != 3 for row in report['channels']):
        raise ValueError('Channels must contain name, access status and actual result')
    if not isinstance(report.get('items'), list):
        raise ValueError('Items must be an array')
    ids = set()
    for item in report['items']:
        for key in ('id', 'title', 'original', 'source', 'sourceType', 'published', 'event',
                    'eventLabel', 'region', 'category', 'summary', 'review', 'statusText', 'update'):
            if not isinstance(item.get(key), str) or not item[key].strip():
                raise ValueError('Missing item field: ' + key)
        if not re.fullmatch(r'[A-Za-z0-9_-]+', item['id']) or item['id'] in ids:
            raise ValueError('Invalid or duplicate news ID: ' + item['id'])
        ids.add(item['id'])
        if item.get('status') not in {'verified', 'unconfirmed'}:
            raise ValueError('Every item must finish verification before publication')
        verification = item.get('verification', {})
        if verification.get('result') != item['status']:
            raise ValueError('Verification result disagrees with visible status')
        timestamp(verification.get('checkedAt'))
        for key in ('method', 'reason'):
            if not verification.get(key):
                raise ValueError('Missing verification evidence: ' + key)
        if item['status'] == 'verified' and not verification.get('confirmedScope'):
            raise ValueError('Verified news needs a confirmed scope')
        if item['status'] == 'unconfirmed' and not verification.get('missing'):
            raise ValueError('Unconfirmed news needs a specific evidence gap')
        urls = [item.get('url', '')] + [row[1] for row in item.get('reviewUrls', [])]
        if any(not isinstance(url, str) or not url.startswith(('https://', 'http://')) for url in urls):
            raise ValueError('News sources must use public HTTP(S) URLs')
        if not isinstance(item.get('tags'), list) or not isinstance(item.get('products'), list):
            raise ValueError('Tags and products must be arrays')
        for product in item['products']:
            if len(product) != 2 or product[0] not in PRODUCTS or not product[1]:
                raise ValueError('Each product needs a supported category and factual fit reason')
    return report


def due(news_dir=NEWS, today=None, slot=None):
    now = datetime.now(BEIJING)
    today = today or now.date().isoformat()
    if slot is None:
        slot = next((value for value in reversed(SLOTS) if now.strftime('%H:%M') >= value), None)
    if slot is None:
        return {'due': False, 'date': today, 'slot': None, 'reason': 'before_first_schedule'}
    if slot not in SLOTS:
        raise ValueError('Invalid scheduled run slot')
    target = news_dir / (today + '.json')
    if target.exists():
        try:
            report = validate(json.loads(target.read_text(encoding='utf-8')))
            completed = set(report.get('completedSlots', []))
            if report['run']['status'] == 'completed' and report['run'].get('slot'):
                completed.add(report['run']['slot'])
            if report['collectedDate'] == today and slot in completed:
                return {'due': False, 'date': today, 'slot': slot, 'reason': 'slot_completed', 'report': str(target)}
        except (KeyError, ValueError):
            pass
    return {'due': True, 'date': today, 'slot': slot, 'reason': 'slot_missing_or_incomplete'}


def render(collections, day):
    for report in collections.values():
        validate(report)
    payload = json.dumps(collections, ensure_ascii=False, separators=(',', ':'))
    payload = payload.replace('<', chr(92) + 'u003c').replace('>', chr(92) + 'u003e').replace('&', chr(92) + 'u0026')
    return TEMPLATE.read_text(encoding='utf-8').replace('__NEWS_COLLECTIONS__', payload).replace('__REPORT_DATE__', day)


def atomic_write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + '.tmp')
    temporary.write_text(content, encoding='utf-8')
    temporary.replace(path)


def publish(report, news_dir=NEWS, output_dir=OUTPUT):
    validate(report)
    day = report['collectedDate']
    first = date.fromisoformat(day) - timedelta(days=14)
    collections = {}
    for path in sorted(news_dir.glob('????-??-??.json')):
        if first.isoformat() <= path.stem <= day:
            archived = json.loads(path.read_text(encoding='utf-8'))
            if archived['collectedDate'] != path.stem:
                raise ValueError('Archive filename disagrees with collection date')
            collections[path.stem] = archived
    completed = set(collections.get(day, {}).get('completedSlots', []))
    completed.update(report.get('completedSlots', []))
    if report['run']['status'] == 'completed' and report['run'].get('slot'):
        completed.add(report['run']['slot'])
    report['completedSlots'] = sorted(completed)
    collections[day] = report
    report['lastVerifiedAt'] = max((n['verification']['checkedAt'] for n in report['items']),
                                   key=timestamp, default=report['run']['completedAt'])
    html = render(collections, day)
    atomic_write(news_dir / (day + '.json'), json.dumps(report, ensure_ascii=False, indent=2) + chr(10))
    atomic_write(output_dir / ('daily-news-' + day + '.html'), html)
    # Update the latest page last; invalid or interrupted drafts never replace it.
    atomic_write(output_dir / 'daily-news-demo.html', html)
    return {'date': day, 'total': len(report['items']),
            'verified': sum(n['status'] == 'verified' for n in report['items']),
            'unconfirmed': sum(n['status'] == 'unconfirmed' for n in report['items']),
            'html': str(output_dir / 'daily-news-demo.html')}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=('check', 'due', 'publish', 'render'))
    parser.add_argument('input', nargs='?')
    parser.add_argument('--slot', choices=SLOTS, help='Scheduled Beijing edition to check')
    parser.add_argument('--news-dir', type=Path, default=NEWS)
    parser.add_argument('--output-dir', type=Path, default=OUTPUT)
    args = parser.parse_args()
    if args.command == 'check':
        for path in (TEMPLATE, ROOT / '.agents/skills/daily-industry-news/SKILL.md'):
            if not path.is_file(): raise ValueError('Missing project file: ' + str(path))
        result = {'ready': True, 'root': str(ROOT), 'python': sys.executable, 'today': datetime.now(BEIJING).date().isoformat()}
    elif args.command == 'due':
        result = due(args.news_dir, slot=args.slot)
    else:
        if not args.input: parser.error('A collected JSON input is required')
        report = json.loads(Path(args.input).read_text(encoding='utf-8'))
        result = publish(report, args.news_dir, args.output_dir)
    print(json.dumps(result, ensure_ascii=False))


if __name__ == '__main__':
    if hasattr(sys.stdout, 'reconfigure'): sys.stdout.reconfigure(encoding='utf-8')
    main()
