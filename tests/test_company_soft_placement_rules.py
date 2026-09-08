from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROJECT_RULES = PROJECT_ROOT / "AGENTS.md"
SOFT_PLACEMENT = PROJECT_ROOT / ".agents/skills/references/company-soft-placement.md"
WENAN_ROUTER = PROJECT_ROOT / ".agents/skills/wenan-skill/SKILL.md"
QUALITY_GATE = PROJECT_ROOT / ".agents/skills/references/b2b-content-quality-gate.md"
TOPIC_LOOP = PROJECT_ROOT / ".agents/skills/references/b2b-topic-conversion-loop.md"
CLAIM_GUIDE = PROJECT_ROOT / ".agents/skills/references/company-claim-evidence-ledger.md"
LOCAL_DELIVERY = PROJECT_ROOT / ".agents/skills/references/local-manufacturing-delivery-proof.md"
SANITARY_FACTS = PROJECT_ROOT / ".agents/skills/saudi-sanitary-unit-script/references/fact-check-rules.md"
PRODUCT_SKILL = PROJECT_ROOT / ".agents/skills/saudi-product-seeding-script/SKILL.md"
HOTSPOT_SKILL = PROJECT_ROOT / ".agents/skills/global-hotspot-industry-impact-script/SKILL.md"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def assert_contains(content: str, expected: str, name: str) -> None:
    assert expected in content, f"Missing {name}: {expected}"


def test_soft_placement_has_one_shared_rule_and_all_required_exceptions() -> None:
    assert SOFT_PLACEMENT.exists(), "Missing shared company soft-placement rule"
    rules = read(SOFT_PLACEMENT)

    assert_contains(rules, "新闻核验卡例外", "news-card exception")
    assert_contains(rules, "不再重复证明公司与新闻项目存在关系", "no duplicate news-company proof")
    assert_contains(rules, "没有当期确认资料时不写", "unverified live-variable omission")
    assert_contains(rules, "不得先写未经核实的卖点，再用免责句兜底", "no disclaimer workaround")
    assert_contains(rules, "产品本身是标题对象", "product-title exception")
    assert_contains(rules, "临时审校", "internal stripping review")
    assert_contains(rules, "不删除知识库", "knowledge-base preservation")
    assert_contains(rules, "产品本身是标题对象", "product-led topic handling")
    assert_contains(rules, "品牌背书或公司案例", "brand-proof exception")


def test_soft_placement_rule_is_connected_to_the_runtime_entry_and_gates() -> None:
    for path, label in (
        (PROJECT_RULES, "project rules"),
        (WENAN_ROUTER, "wenan router"),
        (QUALITY_GATE, "quality gate"),
        (TOPIC_LOOP, "news conversion loop"),
        (PRODUCT_SKILL, "product skill"),
        (HOTSPOT_SKILL, "hotspot skill"),
    ):
        assert_contains(read(path), "company-soft-placement.md", label)

    hotspot = read(HOTSPOT_SKILL)
    assert_contains(hotspot, "东方骆驼才可随产品自然展示一次", "qualified hotspot company mention")
    assert_contains(hotspot, "不构成公司参与、供货或服务该新闻项目的证明", "hotspot no project-participation inference")


def test_live_project_variables_are_omitted_instead_of_disclaimed() -> None:
    project_rules = read(PROJECT_RULES)
    claim_guide = read(CLAIM_GUIDE)
    topic_loop = read(TOPIC_LOOP)
    local_delivery = read(LOCAL_DELIVERY)
    sanitary_facts = read(SANITARY_FACTS)

    assert_contains(project_rules, "没有当期确认资料时不写", "project variable omission")
    assert_contains(claim_guide, "没有当期确认资料时不写", "claim-ledger omission")
    assert_contains(topic_loop, "没有当期确认资料时不写", "topic-loop omission")
    assert_contains(local_delivery, "没有当期确认资料时不写", "local-delivery omission")
    assert_contains(sanitary_facts, "不写具体时长", "sanitary install-time omission")
    assert "具体方案仍按项目要求确认" not in topic_loop
