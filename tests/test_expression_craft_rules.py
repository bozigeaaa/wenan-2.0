from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
AGENTS = PROJECT_ROOT / "AGENTS.md"
ROUTER = PROJECT_ROOT / ".agents/skills/wenan-skill/SKILL.md"
EXPRESSION = PROJECT_ROOT / ".agents/skills/references/expression-craft.md"
HOOK_LIB = PROJECT_ROOT / ".agents/skills/references/hook-pattern-library.md"
PLACEMENT = PROJECT_ROOT / ".agents/skills/references/company-soft-placement.md"
NEGATIVE = PROJECT_ROOT / ".agents/skills/references/negative-examples.md"
WORDLIST = PROJECT_ROOT / ".agents/skills/references/compliance-wordlist.md"
GATE = PROJECT_ROOT / ".agents/skills/references/b2b-content-quality-gate.md"
README = PROJECT_ROOT / "README.md"
DOCS_NAV = PROJECT_ROOT / "docs/README.md"
HISTORICAL_HANDOFF = PROJECT_ROOT / "docs/wenan-skill-完整交接文档_2026-08-14.md"
TRIGGER_REGISTRY = PROJECT_ROOT / ".agents/skills/references/generation-trigger-registry.md"
SPECIALIST_FILES = [
    PROJECT_ROOT / ".agents/skills/saudi-breakout-story-script/SKILL.md",
    PROJECT_ROOT / ".agents/skills/global-hotspot-industry-impact-script/SKILL.md",
    PROJECT_ROOT / ".agents/skills/saudi-professional-knowledge-script/SKILL.md",
    PROJECT_ROOT / ".agents/skills/saudi-light-steel-script/SKILL.md",
    PROJECT_ROOT / ".agents/skills/saudi-sanitary-unit-script/SKILL.md",
    PROJECT_ROOT / ".agents/skills/saudi-camp-fire-script/SKILL.md",
    PROJECT_ROOT / ".agents/skills/saudi-product-seeding-script/SKILL.md",
    PROJECT_ROOT / ".agents/skills/saudi-brand-proof-script/SKILL.md",
]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def assert_contains(content: str, expected: str, name: str) -> None:
    assert expected in content, f"Missing {name}: {expected}"


def test_expression_craft_libraries_exist() -> None:
    for path, label in (
        (EXPRESSION, "expression-craft"),
        (HOOK_LIB, "hook-pattern-library"),
        (NEGATIVE, "negative-examples"),
        (WORDLIST, "compliance-wordlist"),
    ):
        assert path.exists(), f"Missing technique library: {label}"


def test_agents_md_wires_expression_libraries_and_new_constraints() -> None:
    agents = read(AGENTS)
    assert_contains(agents, "expression-craft.md", "expression-craft wiring")
    assert_contains(agents, "hook-pattern-library.md", "hook library wiring")
    assert_contains(agents, "negative-examples.md", "negative-examples wiring")
    assert_contains(agents, "compliance-wordlist.md", "wordlist wiring")
    assert_contains(agents, "平台适配", "platform adaptation rule")
    assert_contains(agents, "发布前核对清单", "high-risk parameter checklist")
    assert_contains(agents, "公共规则权威", "single-authority rule")


def test_router_wires_expression_libraries_and_hardware_route() -> None:
    router = read(ROUTER)
    assert_contains(router, "expression-craft.md", "router expression wiring")
    assert_contains(router, "hook-pattern-library.md", "router hook wiring")
    assert_contains(router, "五金配套", "hardware route")
    assert_contains(router, "$saudi-product-seeding-script", "hardware routing target")


def test_specialist_skills_reference_soft_placement_instead_of_copying_full_rule() -> None:
    for path in SPECIALIST_FILES:
        content = read(path)
        assert_contains(content, "植入资格", f"conditional placement in {path.name}")
        assert_contains(content, "company-soft-placement.md", f"soft-placement reference in {path.name}")
        assert "公司和产品必须参与回答同一个核心问题" not in content, path
        assert "不能只作为名称、口号或结尾广告出现" not in content, (
            f"full soft-placement rule still duplicated in {path.name}"
        )


def test_specialist_skills_delegate_shared_generation_triggers() -> None:
    assert TRIGGER_REGISTRY.exists()
    for path in SPECIALIST_FILES:
        assert_contains(read(path), "generation-trigger-registry.md", f"trigger registry in {path.name}")


def test_soft_placement_is_evidence_gated_instead_of_always_triggered() -> None:
    placement = read(PLACEMENT)
    assert_contains(placement, "植入资格", "placement eligibility test")
    assert_contains(placement, "没有当期确认资料时不写", "unverified-variable omission")
    assert_contains(placement, "不得先写未经核实的卖点", "no unsupported placement")


def test_negative_examples_capture_user_confirmed_techniques() -> None:
    negative = read(NEGATIVE)
    assert_contains(negative, "报告式列举", "report-style enumeration symptom")
    assert_contains(negative, "机械口语化", "mechanical oralization symptom")
    assert_contains(negative, "错误闭环", "forced closure symptom")
    assert_contains(negative, "朗读节奏误修", "rhythm overcorrection symptom")


def test_readme_maintenance_adds_knowledge_sync_checklist() -> None:
    readme = read(README)
    assert_contains(readme, "知识库同步 checklist", "knowledge-sync checklist")
    assert_contains(readme, "company-claim-evidence-ledger.json", "claim-ledger sync item")
    assert_contains(readme, "hotspot-ledger.json", "hotspot-ledger sync item")
    assert_contains(readme, "docs/README.md", "docs-nav sync item")


def test_old_handoff_is_marked_as_history_not_runtime_authority() -> None:
    handoff = read(HISTORICAL_HANDOFF)
    assert_contains(handoff, "历史存档，非现行规则", "historical handoff status")
    assert_contains(handoff, "不得作为生成、路由、输出、测试或维护指令读取", "non-runtime boundary")


def test_docs_navigation_points_to_the_current_authority_chain() -> None:
    nav = read(DOCS_NAV)
    assert_contains(nav, "现行执行权威", "current authority heading")
    assert_contains(nav, "generation-trigger-registry.md", "trigger-registry authority")
    assert "当前唯一最新交接文档" not in nav

def test_expression_rules_preserve_adaptive_structure_and_evidence_strength() -> None:
    placement = read(PLACEMENT)
    gate = read(GATE)
    assert_contains(gate, "不设固定结构", "adaptive body structure")
    assert_contains(placement, "植入资格", "placement relevance gate")
    wordlist = read(WORDLIST)
    assert_contains(wordlist, "字眼与来源强度匹配", "wordlist strength-matching section")
    assert_contains(wordlist, "要求 / 必须", "requirement-vs-suggestion discipline")
    assert_contains(wordlist, "很可能", "likely-word discipline")
