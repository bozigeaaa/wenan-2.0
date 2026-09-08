from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
REF = ROOT / '.agents/skills/references'


def test_oral_style_contract_has_checkable_limits_and_fact_boundary():
    text = (REF / 'expression-craft.md').read_text(encoding='utf-8')
    for term in ('反问句禁用', '全文设问最多 2 处', '句子长短按意思和口播节奏安排', '每 100 字 2–4 处', '一个明确动作', '不能改变事实命题、限定条件、因果强度或责任关系'):
        assert term in text, term


def test_old_style_opt_outs_do_not_override_user_preference():
    paths = [ROOT / 'AGENTS.md', REF / 'expression-craft.md', REF / 'generation-trigger-registry.md', ROOT / '.agents/skills/humanizer/SKILL.md']
    for path in paths:
        text = path.read_text(encoding='utf-8').split('# Humanizer:')[0]
        for stale in ('不设统一句长', '不强插短句', '默认索要互动', '只有用户明确需要 CTA'):
            assert stale not in text, (path, stale)


def test_style_is_wired_into_review_and_hook():
    for path in (REF / 'generation-trigger-registry.md', REF / 'b2b-content-quality-gate.md', REF / 'hook-pattern-library.md', ROOT / '.agents/skills/humanizer/SKILL.md'):
        assert 'expression-craft.md' in path.read_text(encoding='utf-8'), path


def test_default_length_and_storyboard_scope():
    manifest = json.loads((REF / 'generation-manifest.json').read_text(encoding='utf-8'))
    assert '300' in manifest['length_policy']['reference_corpus_default']['rule']
    text = (REF / 'expression-craft.md').read_text(encoding='utf-8')
    assert '分镜' in text and '不改写已确认文案' in text


def test_sentence_splitting_uses_meaning_not_numeric_thresholds():
    text = (REF / 'expression-craft.md').read_text(encoding='utf-8')
    for stale in ('平均句长', '20 字', '25 字', '20字', '25字'):
        assert stale not in text, stale
    for required in ('主干不清', '难以自然换气', '能顺着说清的句子保留', '不为缩短句长切断条件和逻辑'):
        assert required in text, required
