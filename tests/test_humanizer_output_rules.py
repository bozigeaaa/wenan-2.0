from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROJECT_RULES = PROJECT_ROOT / "AGENTS.md"
WENAN_ROUTER = PROJECT_ROOT / ".agents/skills/wenan-skill/SKILL.md"
QUALITY_GATE = PROJECT_ROOT / ".agents/skills/references/b2b-content-quality-gate.md"
HUMANIZER_SKILL = PROJECT_ROOT / ".agents/skills/humanizer/SKILL.md"
HUMANIZER_LICENSE = PROJECT_ROOT / ".agents/skills/humanizer/LICENSE"
HUMANIZER_UI = PROJECT_ROOT / ".agents/skills/humanizer/agents/openai.yaml"
OLD_REWRITER = PROJECT_ROOT / ".agents/skills/script-oralization-rewriter"
OLD_HUMANIZER_GATE = PROJECT_ROOT / ".agents/skills/references/b2b-humanizer-expression-gate.md"
STORYBOARD = PROJECT_ROOT / ".agents/skills/digital-human-storyboard/SKILL.md"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_upstream_humanizer_is_vendored_as_the_formal_expression_skill() -> None:
    assert HUMANIZER_SKILL.exists()
    assert HUMANIZER_LICENSE.exists()
    assert HUMANIZER_UI.exists()

    skill = read(HUMANIZER_SKILL)
    license_text = read(HUMANIZER_LICENSE)
    interface = read(HUMANIZER_UI)

    assert "name: humanizer" in skill
    assert 'version: "2.11.2"' in skill
    assert "https://github.com/blader/humanizer" in skill
    assert "### 35. Rejecting fake alternatives" in skill
    assert "Copyright (c) 2025 Siqi Chen" in license_text
    assert 'display_name: "Humanizer 文案优化"' in interface
    assert "$humanizer" in interface


def test_wenan_humanizer_adaptation_locks_facts_and_chinese_b2b_boundaries() -> None:
    skill = read(HUMANIZER_SKILL)

    for expected in (
        "wenan 中文 B2B 模式",
        "项目规则优先于上游通用规则",
        "不得新增、删除、弱化或强化",
        "中文引号",
        "报告式列举",
        "只重写出现症状",
        "高风险项未通过前只做诊断",
    ):
        assert expected in skill

    assert "事实、逻辑、产品、公司边界和资料出处确认后" not in skill
    assert "专业名词直接影响本期内容时才保留" not in skill
    assert "不设置必须满足后才能继续的前置条件" not in skill
    assert "明显缺来源的高风险事实保持原强度" not in skill
    assert "表达已改，事实未核验" not in skill


def test_opening_hook_constraint_only_forbids_fabricated_content() -> None:
    skill = read(HUMANIZER_SKILL)

    assert "不能补造新闻、现场、客户反馈、数字或结果" in skill
    assert "可以使用悬念、提问、反差、信息差或暂缓答案" not in skill


def test_humanizer_is_available_without_a_fixed_double_version_contract() -> None:
    router = read(WENAN_ROUTER)
    assert "$humanizer" in router
    assert "$script-oralization-rewriter" not in router
    assert "原文案、优化后文案" not in router


def test_opening_hook_can_use_suspense_without_fabricating_results() -> None:
    humanizer = read(HUMANIZER_SKILL)
    assert "只在钩子存在朗读症状时调整表达" in humanizer
    assert "不能补造新闻、现场、客户反馈、数字或结果" in humanizer
    assert "不重新选择角度" in humanizer


def test_copy_stays_on_one_subject_without_a_fixed_body_template() -> None:
    for path in (PROJECT_RULES, QUALITY_GATE):
        content = read(path)
        assert "多个可以独立成稿的观点" in content, path
        assert "一个清晰、有意义或有决策价值的观点" in content, path
        assert "不设固定结构" in content, path
        assert "判断 → 原因 → 动作" not in content, path


def test_retired_expression_layers_are_removed() -> None:
    assert not OLD_REWRITER.exists()
    assert not OLD_HUMANIZER_GATE.exists()

    active_paths = (PROJECT_RULES, WENAN_ROUTER, QUALITY_GATE)
    for path in active_paths:
        content = read(path)
        assert "script-oralization-rewriter" not in content, path
        assert "b2b-humanizer-expression-gate" not in content, path


def test_storyboard_uses_the_confirmed_version_without_rewriting_it() -> None:
    storyboard = read(STORYBOARD)

    assert "不改写" in storyboard
    assert "不得再次调用 `$humanizer`" in storyboard
