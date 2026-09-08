from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
AGENTS = PROJECT_ROOT / "AGENTS.md"
README = PROJECT_ROOT / "README.md"
SKILLS_ROOT = PROJECT_ROOT / ".agents/skills"
ROUTER = SKILLS_ROOT / "wenan-skill/SKILL.md"
HUMANIZER = SKILLS_ROOT / "humanizer/SKILL.md"
STORYBOARD = SKILLS_ROOT / "digital-human-storyboard/SKILL.md"
TRIGGER_REGISTRY = SKILLS_ROOT / "references/generation-trigger-registry.md"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_readme_describes_one_task_and_one_final_deliverable() -> None:
    readme = read(README)
    assert "同一个项目、同一个任务中连续完成" in readme
    assert "不需要复制或转发中间交接单" in readme
    assert "不要求每个技法模块都启动" in readme
    assert "默认交付一份最终文案" in readme
    assert "script-oralization-rewriter" not in readme
    assert "固定双版本输出" in readme


def test_active_generation_rules_delegate_to_one_trigger_registry() -> None:
    assert TRIGGER_REGISTRY.exists()
    for path in (AGENTS, ROUTER):
        assert "generation-trigger-registry.md" in read(path), path


def test_project_skills_do_not_copy_the_old_topic_weight_table() -> None:
    for path in sorted(SKILLS_ROOT.glob("*/SKILL.md")):
        assert "话题类型与技法权重对照表" not in read(path), path


def test_packaging_first_rules_are_not_executable() -> None:
    active = "\n".join(
        read(path)
        for path in (
            AGENTS,
            ROUTER,
            SKILLS_ROOT / "references/expression-craft.md",
            SKILLS_ROOT / "references/hook-pattern-library.md",
            SKILLS_ROOT / "references/company-soft-placement.md",
            SKILLS_ROOT / "references/b2b-content-quality-gate.md",
        )
    )
    for deprecated in (
        "每条文案至少用 3 种不同逻辑",
        "连续 3 次不重复",
        "隔三跳一",
        "先选“钩子”→再选“软植入策略”",
        "最后根据开头情绪",
        "每次轮换使用，禁止连续用同一种",
    ):
        assert deprecated not in active


def test_humanizer_preserves_factual_meaning_while_repairing_expression() -> None:
    humanizer = read(HUMANIZER)
    for invariant in ("事实命题", "限定条件", "因果强度", "责任关系"):
        assert invariant in humanizer
    assert "重排段落" in humanizer
    assert "不得自动视为已核实" in humanizer


def test_storyboard_keeps_the_confirmed_copy_unchanged() -> None:
    storyboard = read(STORYBOARD)
    assert "不改写" in storyboard
    assert "不得再次调用 `$humanizer`" in storyboard
