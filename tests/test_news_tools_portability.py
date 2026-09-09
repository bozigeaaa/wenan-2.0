"""Portable entry point checks without using a maintainer's installed runtime."""
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def test_fresh_copy_from_unrelated_cwd_reports_missing_local_runtime():
    with tempfile.TemporaryDirectory(prefix="news-portability-") as temporary:
        destination = Path(temporary) / "new user 空格" / "project"
        for relative in (
            "scripts/news_tools.py",
            ".agents/skills/humanizer/SKILL.md",
            ".agents/skills/humanizer/LICENSE",
            ".agents/skills/references/expression-craft.md",
            ".agents/skills/scrapling/SKILL.md",
            ".agents/skills/scrapling/LICENSE.txt",
        ):
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / relative, target)
        result = subprocess.run(
            [sys.executable, str(destination / "scripts/news_tools.py"), "check"],
            cwd=temporary, capture_output=True, text=True, encoding="utf-8",
        )
        assert result.returncode == 1, result.stdout + result.stderr
        assert "Humanizer: project skill" in result.stdout
        assert "Scrapling is not installed here" in result.stderr
        assert "scripts/news_tools.py setup" in result.stderr
        assert not (destination / ".news-venv").exists(), "Read-only check created an environment"


def test_incomplete_project_has_actionable_error():
    with tempfile.TemporaryDirectory(prefix="news-incomplete-") as temporary:
        destination = Path(temporary)
        (destination / "scripts").mkdir()
        shutil.copyfile(ROOT / "scripts/news_tools.py", destination / "scripts/news_tools.py")
        result = subprocess.run(
            [sys.executable, str(destination / "scripts/news_tools.py"), "check"],
            cwd=temporary, capture_output=True, text=True, encoding="utf-8",
        )
        assert result.returncode == 1
        assert "Download the complete project" in result.stderr
