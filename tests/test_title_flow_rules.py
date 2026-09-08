from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROJECT_RULES = PROJECT_ROOT / "AGENTS.md"
WENAN_ROUTER = PROJECT_ROOT / ".agents/skills/wenan-skill/SKILL.md"
QUALITY_GATE = PROJECT_ROOT / ".agents/skills/references/b2b-content-quality-gate.md"
HOTSPOT_SKILL = PROJECT_ROOT / ".agents/skills/global-hotspot-industry-impact-script/SKILL.md"
TITLE_SELECTION = PROJECT_ROOT / ".agents/skills/global-hotspot-industry-impact-script/references/title-selection.md"
SKILLS_ROOT = PROJECT_ROOT / ".agents/skills"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_title_direction_confirmation_continues_in_the_same_task() -> None:
    router = read(WENAN_ROUTER)

    assert "生成标题方向" in router
    assert "标题方向确认" in router
    assert "同一任务内临时内容状态" in router
    assert "标题交接单" not in router


def test_title_quantity_contract_has_one_meaning_per_stage() -> None:
    router = read(WENAN_ROUTER)

    assert "一组承诺一致的标题" in router
    assert "承诺一致" in router


def test_titles_are_short_clear_and_not_locked_to_a_sentence_form() -> None:
    gate = read(QUALITY_GATE)

    assert "标题通常为 19–36" in gate
    assert "19–36" in gate
    assert "不限制疑问、陈述、判断、反差、场景或其他句式" in gate
    assert "可立即识别的对象、受众或场景" in gate
    for abstract_word in ("交付", "成本", "风险", "配置", "进度"):
        assert abstract_word in gate


def test_title_tension_is_allowed_without_reversing_facts() -> None:
    gate = read(QUALITY_GATE)

    assert "已核实事实本身存在悬念、反差或风险差异时" in gate
    assert "没有这种事实关系时使用直接判断" in gate
    assert "不能放大后果、反转或编造事实" in gate
    assert "可能发生" in gate and "已经发生" in gate


def test_news_title_cannot_bypass_verification_or_change_product_direction() -> None:
    router = read(WENAN_ROUTER)
    title_selection = read(TITLE_SELECTION)
    hotspot = read(HOTSPOT_SKILL)

    assert "先核验原链接" in router
    assert "新闻标题不设置固定结构" in title_selection
    assert "不强制写成项目问题" in title_selection
    assert "产品名称不强制出现在标题文字中" in title_selection
    assert "所选产品及结合理由" in title_selection
    assert "已经采购、使用、要求或收到" in title_selection
    assert "用户选定新闻和产品后" in hotspot


def test_title_and_hook_share_a_promise_but_hook_stands_alone() -> None:
    project_rules = read(PROJECT_RULES)
    gate = read(QUALITY_GATE)

    for content in (project_rules, gate):
        assert "同一个核心内容和传播承诺" in content
        assert "不要求使用相同文字或句式" in content
        assert "不能依赖标题或封面补充语境" in content
        assert "行业对象、目标受众或具体场景" in content
        assert "即使观众没有看到标题" in content


def test_title_direction_outputs_one_title() -> None:
    router = read(WENAN_ROUTER)
    assert "一组承诺一致的标题" in router
    assert "完整文案：标题、一份最终口播文案、必要资料出处" in router
    assert "承诺一致" in router


def test_active_generation_contract_has_no_short_title_variant() -> None:
    active_files = (
        PROJECT_RULES,
        *(path for path in SKILLS_ROOT.rglob("*") if path.suffix in {".md", ".yaml", ".json"}),
    )
    for path in active_files:
        content = read(path)
        for removed_contract in (
            "短标题",
            "长短标题",
            "标题成对",
            "short title",
            "short_title",
            "长标题",
            "long title",
            "long_title",
        ):
            assert removed_contract not in content, f"{path}: {removed_contract}"


def test_title_tasks_can_start_from_a_direct_command_without_an_initialization_file() -> None:
    project_rules = read(PROJECT_RULES)
    router = read(WENAN_ROUTER)

    assert "无需发送初始化文件" in project_rules
    assert "复制初始化文本" in router


def test_old_title_question_contract_and_long_examples_are_removed() -> None:
    project_rules = read(PROJECT_RULES)
    title_selection = read(TITLE_SELECTION)
    hotspot = read(HOTSPOT_SKILL)

    assert "回答标题本身提出的判断" not in project_rules
    assert "title, opening, impact chain, and ending answer the same" not in hotspot
    assert "answer the title itself" not in read(WENAN_ROUTER)
    assert "推进标题答案" not in read(QUALITY_GATE)
    assert "never over 22 without a necessary proper name" not in title_selection
    assert "红海风险上升后，沙特项目方该怎么判断本地供应商有没有真交付能力" not in title_selection
    assert "临建交付别只看船期：本地生产、配送和安装谁来接" not in title_selection
