import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('daily_news', ROOT / 'scripts/daily_news.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def report(day='2026-09-10'):
    return {'schemaVersion': 1, 'collectedDate': day, 'collectedAt': day+'T01:00:00+00:00',
            'timeZone': 'Asia/Shanghai', 'window': 'test window', 'scope': 'test scope',
            'channels': [['Official', 'direct', 'body read']],
            'retrievalTools': [
                {'tool': 'scrapling', 'status': 'completed', 'entries': ['https://example.com/news'], 'evidence': 'fixture read'},
                {'tool': 'firecrawl', 'status': 'completed', 'entries': ['Saudi construction'], 'evidence': 'fixture search'}],
            'run': {'status': 'completed', 'completedAt': day+'T01:10:00+00:00'},
            'items': [{'id': '001', 'title': 'Example', 'original': 'Original',
                       'source': 'Official', 'sourceType': 'official', 'url': 'https://example.com/news',
                       'published': day, 'event': day, 'eventLabel': 'event', 'region': 'Saudi',
                       'category': '工程项目', 'tags': ['工程项目'], 'products': [], 'background': 'background',
                       'update': 'new', 'summary': 'scope', 'review': 'read official body',
                       'status': 'verified', 'statusText': '已核验',
                       'verification': {'result': 'verified', 'checkedAt': day+'T01:05:00+00:00',
                                        'method': 'official', 'confirmedScope': 'scope',
                                        'reason': 'read official body', 'missing': ''}}]}


class DailyNewsTest(unittest.TestCase):
    def test_rejects_unfinished_verification_and_missing_evidence(self):
        for change in ('pending', 'time', 'reason', 'url', 'contradiction'):
            r = report(); n = r['items'][0]
            if change == 'pending': n['status'] = 'pending'
            if change == 'time': del n['verification']['checkedAt']
            if change == 'reason': n['verification']['reason'] = ''
            if change == 'url': n['url'] = 'javascript:alert(1)'
            if change == 'contradiction': n['verification']['result'] = 'unconfirmed'
            with self.subTest(change=change), self.assertRaises(ValueError): m.validate(r)

    def test_completed_collection_requires_two_distinct_successful_tools(self):
        for case in ('missing', 'one', 'same', 'failed', 'no_evidence'):
            r = report()
            if case == 'missing': del r['retrievalTools']
            if case == 'one': r['retrievalTools'] = r['retrievalTools'][:1]
            if case == 'same': r['retrievalTools'][1]['tool'] = 'scrapling'
            if case == 'failed': r['retrievalTools'][1]['status'] = 'failed'
            if case == 'no_evidence': r['retrievalTools'][1]['evidence'] = ''
            with self.subTest(case=case), self.assertRaises(ValueError): m.validate(r)
        r = report(); r['run']['status'] = 'partial'; r['retrievalTools'] = r['retrievalTools'][:1]
        m.validate(r)

    def test_unconfirmed_needs_specific_missing_evidence(self):
        r = report(); n = r['items'][0]
        n['status'] = n['verification']['result'] = 'unconfirmed'
        with self.assertRaises(ValueError): m.validate(r)
        n['verification']['missing'] = 'No independent or official confirmation'
        m.validate(r)

    def test_html_preserves_every_item_and_escapes_script_content(self):
        r = report(); r['items'][0]['summary'] = '</script><script>alert(1)</script>'
        html = m.render({'2026-09-10': r}, '2026-09-10')
        self.assertNotIn('</script><script>alert(1)', html)
        self.assertIn('checkedAt', html)
        self.assertIn('currentItems().find', html)
        self.assertNotIn('__NEWS_COLLECTIONS__', html)

    def test_morning_completion_does_not_skip_afternoon(self):
        with tempfile.TemporaryDirectory() as temp:
            folder = Path(temp); news = folder/'news'
            morning = report(); morning['run']['slot'] = '09:00'
            m.publish(morning, news, folder)
            self.assertFalse(m.due(news, '2026-09-10', '09:00')['due'])
            self.assertTrue(m.due(news, '2026-09-10', '14:00')['due'])
            afternoon = report(); afternoon['run']['slot'] = '14:00'
            m.publish(afternoon, news, folder)
            self.assertFalse(m.due(news, '2026-09-10', '14:00')['due'])
            self.assertFalse(m.due(news, '2026-09-10', '09:00')['due'])
            self.assertTrue(m.due(news, '2026-09-11', '09:00')['due'])

    def test_failed_afternoon_can_retry_without_repeating_morning(self):
        with tempfile.TemporaryDirectory() as temp:
            folder = Path(temp); news = folder/'news'
            morning = report(); morning['run']['slot'] = '09:00'
            m.publish(morning, news, folder)
            afternoon = report(); afternoon['run'].update(slot='14:00', status='failed')
            m.publish(afternoon, news, folder)
            self.assertTrue(m.due(news, '2026-09-10', '14:00')['due'])
            self.assertFalse(m.due(news, '2026-09-10', '09:00')['due'])

    def test_invalid_publish_keeps_existing_html(self):
        with tempfile.TemporaryDirectory() as temp:
            folder = Path(temp); news = folder/'news'; news.mkdir()
            target = folder/'daily-news-demo.html'; target.write_text('previous valid report')
            r = report(); r['items'][0]['verification']['checkedAt'] = ''
            with self.assertRaises(ValueError): m.publish(r, news, folder)
            self.assertEqual(target.read_text(), 'previous valid report')

    def test_multi_day_archive_and_id_preservation(self):
        with tempfile.TemporaryDirectory() as temp:
            folder = Path(temp); news = folder/'news'
            m.publish(report('2026-09-09'), news, folder)
            m.publish(report(), news, folder)
            html = (folder/'daily-news-demo.html').read_text(encoding='utf-8')
            self.assertIn('"2026-09-09":', html)
            self.assertIn('"2026-09-10":', html)
            self.assertEqual(json.loads((news/'2026-09-09.json').read_text(encoding='utf-8'))['items'][0]['id'], '001')

if __name__ == '__main__': unittest.main()
