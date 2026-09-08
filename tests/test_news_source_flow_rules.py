import re
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROJECT_RULES = PROJECT_ROOT / "AGENTS.md"
WENAN_ROUTER = PROJECT_ROOT / ".agents/skills/wenan-skill/SKILL.md"
HOTSPOT_SKILL = PROJECT_ROOT / ".agents/skills/global-hotspot-industry-impact-script/SKILL.md"
HOTSPOT_INTERFACE = PROJECT_ROOT / ".agents/skills/global-hotspot-industry-impact-script/agents/openai.yaml"
HOTSPOT_SOURCING = PROJECT_ROOT / ".agents/skills/global-hotspot-industry-impact-script/references/hotspot-sourcing.md"
IMPACT_FILTER = PROJECT_ROOT / ".agents/skills/global-hotspot-industry-impact-script/references/impact-filter.md"
TITLE_SELECTION = PROJECT_ROOT / ".agents/skills/global-hotspot-industry-impact-script/references/title-selection.md"
TOPIC_LOOP = PROJECT_ROOT / ".agents/skills/references/b2b-topic-conversion-loop.md"
HOTSPOT_LEDGER = PROJECT_ROOT / "content-state/hotspot-ledger.json"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def section(content: str, heading: str) -> str:
    match = re.search(
        rf"^{re.escape(heading)}\s*$\n(?P<body>.*?)(?=^#{{1,3}}\s|\Z)",
        content,
        flags=re.MULTILINE | re.DOTALL,
    )
    assert match, f"Missing section: {heading}"
    return match.group("body")


def test_p0_discovery_pool_is_exactly_the_four_user_selected_channels() -> None:
    sourcing = read(HOTSPOT_SOURCING)
    p0 = section(sourcing, "### P0：第一优先渠道")

    for expected in ("Google / Google News", "X", "MEED", "Etimad"):
        assert expected in p0, f"P0 missing {expected}"

    for lower_tier_source in ("SPA", "Arab News", "Saudi Gazette", "Al Eqtisadiah", "Argaam"):
        assert lower_tier_source not in p0, f"P0 includes lower-tier source {lower_tier_source}: {p0!r}"


def test_discovery_directly_visits_each_tier_before_external_search_fills_gaps() -> None:
    sourcing = read(HOTSPOT_SOURCING)
    hotspot = read(HOTSPOT_SKILL)
    project_rules = read(PROJECT_RULES)

    assert "直接进站优先＋外部检索补漏" in sourcing
    for expected in (
        "站内搜索",
        "最新新闻",
        "主题分类",
        "公告页",
        "新闻归档",
        "直接访问完成",
        "外部检索线索",
        "访问未完成",
        "网页检索工具",
        "site:",
    ):
        assert expected in sourcing

    assert "不能记录为已直接访问该渠道" in sourcing
    assert "搜索工具命中某个网站" in sourcing
    assert "直接进入当前优先级渠道" in hotspot
    assert "直接进站优先" in project_rules

    headings = [
        "### P0：第一优先渠道",
        "### P1：沙特当地媒体",
        "### P2：项目业主、主管机构和企业官网",
        "### P3：中东专业媒体和项目数据库",
        "### P4：国际媒体及其他可追溯来源",
    ]
    positions = [sourcing.index(heading) for heading in headings]
    assert positions == sorted(positions)


def test_news_card_is_chinese_review_ready_and_has_no_evidence_boundary_field() -> None:
    sourcing = read(HOTSPOT_SOURCING)
    card = section(sourcing, "## 新闻核验卡")

    for expected in (
        "发布渠道",
        "新闻原链接",
        "原标题",
        "原标题中文直译",
        "发布时间",
        "内容摘要",
        "新闻内容解析",
        "复核来源",
        "可结合的产品",
        "结合理由",
        "核验结论",
    ):
        assert expected in card, f"News card missing {expected}"

    assert "证据边界" not in card, "News card still exposes the removed evidence-boundary field"


def test_product_selection_precedes_content_angle_selection() -> None:
    project_rules = read(PROJECT_RULES)
    sourcing = read(HOTSPOT_SOURCING)
    hotspot = read(HOTSPOT_SKILL)
    ledger = read(HOTSPOT_LEDGER)
    card_section = section(sourcing, "## 新闻核验卡")
    card_match = re.search(
        r"```text\s*\n新闻核验卡\s*\n(?P<card>.*?)```",
        card_section,
        flags=re.DOTALL,
    )
    assert card_match, "Missing news-card template"
    card = card_match.group("card")

    assert "可讲角度" not in card
    assert "推荐角度" not in card
    assert "不得增加“可讲角度”" in card_section
    assert "- 推荐角度：" not in project_rules
    assert '"recommended_angle"' not in ledger
    assert "用户选择新闻和产品后，才生成内容方向" in hotspot


def test_verified_news_requires_user_product_selection_before_titles() -> None:
    impact = read(IMPACT_FILTER)
    router = read(WENAN_ROUTER)
    hotspot = read(HOTSPOT_SKILL)

    for product in ("打包箱", "移动卫浴", "五金", "薄壁轻钢"):
        assert product in impact

    assert "等待用户选择" in impact
    assert "不得自行选择" in impact
    assert "用户选定产品" in router
    assert "输出新闻核验卡后停止" in hotspot


def test_locked_product_category_is_not_silently_replaced_by_other_product_news() -> None:
    impact = read(IMPACT_FILTER)
    router = read(WENAN_ROUTER)

    assert "产品大类已锁定" in impact
    assert "不得自动替换" in impact
    assert "其他产品方向" in impact
    assert "常青议题" in router


def test_no_result_feedback_and_login_boundaries_are_explicit() -> None:
    sourcing = read(HOTSPOT_SOURCING)
    feedback = section(sourcing, "## 新闻搜集反馈")
    access = section(sourcing, "## 登录与访问限制")

    for expected in ("检索日期", "已检索渠道", "检索结果", "未采用的主要原因"):
        assert expected in feedback

    assert "实际检索过" in feedback
    assert "授权使用已经登录的浏览器会话" in access
    assert "密码、验证码、Token" in access
    assert "未完成检索" in access


def test_selected_news_must_produce_a_product_led_script() -> None:
    project_rules = read(PROJECT_RULES)
    hotspot = read(HOTSPOT_SKILL)
    interface = read(HOTSPOT_INTERFACE)
    title_selection = read(TITLE_SELECTION)
    topic_loop = read(TOPIC_LOOP)

    assert "进入新闻核验卡" in project_rules
    assert "后续文案必须明确带出用户选定的产品" in project_rules
    assert "Default to no product mention" not in hotspot
    assert "默认不带产品" not in interface
    assert "先停下来让我选择新闻和产品" in interface
    assert "user-selected product" in title_selection
    assert "新闻事实 → 项目判断 → 产品价值" in topic_loop


def test_selected_news_product_allows_company_to_appear_without_a_second_project_link() -> None:
    router = read(WENAN_ROUTER)
    topic_loop = read(TOPIC_LOOP)

    assert "不得暗示东方骆驼已参与、供货或服务新闻项目" in router
    assert "东方骆驼可随产品自然展示一次" in topic_loop
    assert "不再重复证明公司与新闻项目存在关系" in topic_loop
    assert "不要求公司证据桥" in topic_loop
