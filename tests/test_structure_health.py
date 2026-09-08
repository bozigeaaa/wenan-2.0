import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = PROJECT_ROOT / ".agents/skills"
SHARED_REFS = SKILLS_ROOT / "references"
README = PROJECT_ROOT / "README.md"
KNOWLEDGE_INDEX = PROJECT_ROOT / "knowledge/AI资料导航索引.md"

# 必须存在的专项 skill 目录名
REQUIRED_SKILLS = [
    "wenan-skill",
    "digital-human-storyboard",
    "global-hotspot-industry-impact-script",
    "humanizer",
    "saudi-brand-proof-script",
    "saudi-breakout-story-script",
    "saudi-camp-fire-script",
    "saudi-light-steel-script",
    "saudi-product-seeding-script",
    "saudi-professional-knowledge-script",
    "saudi-sanitary-unit-script",
]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _path_refs(content: str) -> set[str]:
    """提取 markdown 反引号或普通文本中的相对文件路径引用（带扩展名）。"""
    refs = set()
    refs |= set(re.findall(r"`([A-Za-z0-9_./\-]+\.(?:md|json|txt|xlsx|docx|pdf|py))`", content))
    refs |= set(re.findall(r"([A-Za-z0-9_./\-]*knowledge/[A-Za-z0-9_./\-]+\.(?:md|json|txt|xlsx|docx|pdf))", content))
    refs |= set(re.findall(r"(content-state/[A-Za-z0-9_./\-]+\.(?:json|md))", content))
    return {p.rstrip("。，、；)）】") for p in refs if "$" not in p and "{" not in p}


def _resolve(skill_dir: Path, ref: str) -> Path | None:
    """把 SKILL.md 中的相对引用解析为绝对路径；无法确定基准时返回 None（不判错）。"""
    if ref.startswith(".agents/") or ref.startswith("knowledge/") or ref.startswith("content-state/") or ref.startswith("docs/"):
        return (PROJECT_ROOT / ref)
    if ref.startswith("AGENTS.md"):
        return PROJECT_ROOT / ref
    if ref.startswith("references/"):
        return skill_dir / ref
    return None


def test_every_skill_has_skill_md_and_agents_interface() -> None:
    for name in REQUIRED_SKILLS:
        skill_dir = SKILLS_ROOT / name
        assert (skill_dir / "SKILL.md").exists(), f"{name} missing SKILL.md"
        assert (skill_dir / "agents/openai.yaml").exists(), f"{name} missing agents/openai.yaml"


def test_every_skill_md_has_valid_frontmatter() -> None:
    for skill_md in sorted(SKILLS_ROOT.glob("*/SKILL.md")):
        content = read(skill_md)
        assert content.startswith("---"), f"{skill_md.name} does not start with frontmatter"
        assert re.search(r"^name:\s*\S+", content, flags=re.MULTILINE), f"{skill_md.name} missing name:"
        assert re.search(r"^description:", content, flags=re.MULTILINE), f"{skill_md.name} missing description:"


def test_skill_references_resolve_to_existing_files() -> None:
    missing = []
    for skill_dir in sorted(SKILLS_ROOT.iterdir()):
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            continue
        for ref in sorted(_path_refs(read(skill_md))):
            target = _resolve(skill_dir, ref)
            if target is not None and not target.exists():
                missing.append(f"{skill_md.relative_to(PROJECT_ROOT)} -> {ref}")
    assert not missing, "Unresolvable file references:\n" + "\n".join(missing)


def test_agents_interface_display_names_are_chinese() -> None:
    non_chinese = []
    for yaml_file in sorted(SKILLS_ROOT.glob("*/agents/openai.yaml")):
        content = read(yaml_file)
        display = re.search(r'display_name:\s*"([^"]*)"', content)
        if display is None or not re.search(r"[\u4e00-\u9fff]", display.group(1)):
            non_chinese.append(str(yaml_file.relative_to(PROJECT_ROOT)))
    assert not non_chinese, "openai.yaml display_name should be Chinese: " + ", ".join(non_chinese)


def test_readme_skill_list_matches_current_state() -> None:
    readme = read(README)
    assert "script-oralization-rewriter" not in readme, "README still lists removed script-oralization-rewriter"
    for expected in ("wenan-skill", "humanizer", "digital-human-storyboard", "global-hotspot-industry-impact-script"):
        assert f"`{expected}`" in readme, f"README missing skill entry: {expected}"


def test_knowledge_index_core_files_exist() -> None:
    index = read(KNOWLEDGE_INDEX)
    core_files = [
        "沙特临建行业认知.xlsx",
        "钧瀚产品优势分级分类总表_v4.xlsx",
        "拼装房屋产品介绍.txt",
        "薄壁轻钢房屋产品介绍.txt",
        "K系列卫生间参数.xlsx",
        "K系列设计文稿.docx",
        "深圳钧瀚科技有限公司企业基础概况.docx",
        "东方骆驼公司简介.txt",
    ]
    for name in core_files:
        assert (PROJECT_ROOT / "knowledge" / name).exists(), f"knowledge file missing: {name}"
        assert name in index, f"knowledge index missing entry: {name}"


def test_navigation_path_prefix_is_consistent() -> None:
    for skill_md in sorted(SKILLS_ROOT.glob("*/SKILL.md")):
        content = read(skill_md)
        # 不应当出现不带 knowledge/ 前缀的“AI资料导航索引”引用
        for m in re.finditer(r"`([^`]*AI资料导航索引\.md)`", content):
            assert m.group(1).startswith("knowledge/"), (
                f"{skill_md.relative_to(PROJECT_ROOT)} uses non-qualified navigation path: {m.group(1)}"
            )
