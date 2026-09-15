from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / ".agents/skills"
REFS = SKILLS / "references"


def test_user_business_information_does_not_require_a_separate_proof_file():
    placement = (REFS / "company-soft-placement.md").read_text(encoding="utf-8")
    assert "用户提供的业务信息" in placement
    assert "不再要求用户逐句提交证明材料" in placement
    assert "默认阻断条件" in placement
    assert "不自行编造客户、项目、成交数据、认证、库存或实际交付结果" in placement
    registry = (REFS / "generation-trigger-registry.md").read_text(encoding="utf-8")
    assert "或公司能力没有证据时" not in registry
    assert "company-soft-placement.md" in registry


def test_company_copy_is_direct_and_not_an_internal_review_checklist():
    placement = (REFS / "company-soft-placement.md").read_text(encoding="utf-8")
    for phrase in ("需要核实", "需要评估", "明确责任", "确认范围", "具备相关能力", "提供相应支持"):
        assert phrase in placement
    assert "内部工作过程不进入广告段" in placement
    assert "同类表达" in placement
    humanizer = (SKILLS / "humanizer/SKILL.md").read_text(encoding="utf-8")
    assert "company-soft-placement.md" in humanizer
    assert "不把公司动作改回" in humanizer


def test_diversity_depends_on_the_article_not_competitor_uniqueness():
    placement = (REFS / "company-soft-placement.md").read_text(encoding="utf-8")
    assert "不建立“某类问题就讲某项能力”的固定对应表" in placement
    assert "不固定公司段的位置、长度、句数和讲述顺序" in placement
    assert "不把参考例句作为以后反复套用的成稿模板" in placement
    assert "## 广告剥离测试" not in placement
    assert "答案确实变弱，植入有效" not in placement
    registry = (REFS / "generation-trigger-registry.md").read_text(encoding="utf-8")
    assert "只比较我们自己的近期已确认或已发布稿" in registry
    assert "替换新闻名或产品名" in registry
    assert "硬性否决" in registry


def test_sales_ending_and_optional_numbers_survive_oral_review():
    expression = (REFS / "expression-craft.md").read_text(encoding="utf-8")
    assert "销售导向" in expression and "联系东方骆驼" in expression
    assert "不强制客户先提交一整套资料" in expression
    assert "默认优先选择与本题有关的评论互动" not in expression
    assert "可有可无的数量、尺寸、产能、天数不强行补齐" in expression
    assert "不影响事实含义时可用量级或约数" in expression
    assert "不得因此改变关键新闻数据、技术参数或比较口径" in expression


def test_specialists_do_not_reintroduce_blanket_company_evidence_gates():
    removed_rules = (
        "只有公司或产品具备已核实证据",
        "公司或产品还须有已核实证据",
        "公司能力没有证据时",
        "库存、交期、生产、配送、安装、售后等具体公司能力还必须逐项核验",
    )
    for file in SKILLS.rglob("*.md"):
        text = file.read_text(encoding="utf-8")
        for rule in removed_rules:
            assert rule not in text, f"Conflicting company gate in {file}: {rule}"
    ledger = (REFS / "company-claim-evidence-ledger.md").read_text(encoding="utf-8")
    assert "不是普通公司介绍的成稿前置条件" in ledger
    news = (SKILLS / "global-hotspot-industry-impact-script/references/hotspot-sourcing.md").read_text(encoding="utf-8")
    assert "原文核验" in news


def test_verified_news_is_reused_without_weakening_new_fact_checks():
    registry = (REFS / "generation-trigger-registry.md").read_text(encoding="utf-8")
    hotspot = (SKILLS / "global-hotspot-industry-impact-script/SKILL.md").read_text(encoding="utf-8")
    humanizer = (SKILLS / "humanizer/SKILL.md").read_text(encoding="utf-8")
    for text in (registry, hotspot):
        assert "不重复核验卡" in text
        assert "新增实质性事实或实时进展再核验" in text
    assert "skip completed verification and selection steps" in hotspot
    assert "新闻、法规、认证、精确技术参数和具体项目结果不得自动视为已核实" in humanizer
    assert "不构成公司参与、供货或服务该新闻项目的证明" in hotspot
