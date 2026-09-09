"""Project-local Scrapling setup and CLI entry point (Python 3.10+)."""
import argparse
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
ENV = ROOT / ".news-venv"
BIN = ENV / ("Scripts" if sys.platform == "win32" else "bin")
PYTHON = BIN / ("python.exe" if sys.platform == "win32" else "python")
SCRAPLING = BIN / ("scrapling.exe" if sys.platform == "win32" else "scrapling")
REQUIREMENTS = ROOT / ".agents/skills/scrapling/requirements.txt"


def invoke(args):
    # libcurl uses the Windows native encoding for certificate file paths.
    # Keep UTF-8 for text output without changing that filesystem assumption.
    subprocess.run([str(arg) for arg in args], cwd=ROOT, check=True,
                   env={**os.environ, "PYTHONIOENCODING": "utf-8",
                        "PYTHONUTF8": "0" if sys.platform == "win32" else "1"})


def check():
    for relative in (
        ".agents/skills/humanizer/SKILL.md",
        ".agents/skills/humanizer/LICENSE",
        ".agents/skills/references/expression-craft.md",
        ".agents/skills/scrapling/SKILL.md",
        ".agents/skills/scrapling/LICENSE.txt",
    ):
        if not (ROOT / relative).is_file():
            raise RuntimeError(f"Missing project file: {relative}. Download the complete project.")
    print("Humanizer: project skill and shared writing rules available (no extra runtime).", flush=True)
    if not PYTHON.is_file() or not SCRAPLING.is_file():
        raise RuntimeError("Scrapling is not installed here. Run: python scripts/news_tools.py setup")
    invoke([PYTHON, "-c", "from scrapling.fetchers import Fetcher, DynamicFetcher; "
            "from scrapling.parser import Selector; import markdownify; "
            "from importlib.metadata import version; "
            "assert Selector('<h1>runtime-ok</h1>').css('h1::text').get() == 'runtime-ok'; "
            "print('Scrapling imports and parser OK; version=' + version('scrapling'))"])
    print("Runtime: " + str(PYTHON), flush=True)
    print("Browser binaries and access to individual news sites require separate live tests.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    setup = commands.add_parser("setup", help="Install dependencies into this project's .news-venv")
    setup.add_argument("--browser", action="store_true", help="Also install Scrapling browser dependencies")
    commands.add_parser("check", help="Check project files, runtime imports and HTML parsing offline")
    for mode in ("get", "fetch"):
        command = commands.add_parser(mode, help="Read a URL using the project runtime")
        command.add_argument("url")
        command.add_argument("output", help="Output path; relative paths are based on the project root")
        if mode == "fetch":
            command.add_argument("--browser-path", help="An existing Chromium-compatible browser executable")
    args = parser.parse_args()
    if sys.version_info < (3, 10):
        raise RuntimeError("Python 3.10+ is required.")
    if args.command == "setup":
        if not PYTHON.is_file():
            invoke([sys.executable, "-m", "venv", ENV])
        invoke([PYTHON, "-m", "pip", "install", "-r", REQUIREMENTS])
        if args.browser:
            invoke([SCRAPLING, "install"])
        check()
    elif args.command == "check":
        check()
    else:
        if not SCRAPLING.is_file():
            raise RuntimeError("Run python scripts/news_tools.py setup first.")
        if not args.url.startswith(("https://", "http://")):
            raise RuntimeError("Use an http:// or https:// URL.")
        output = Path(args.output)
        if not output.is_absolute():
            output = ROOT / output
        output.parent.mkdir(parents=True, exist_ok=True)
        command = [SCRAPLING, "extract", args.command, args.url, output, "--ai-targeted", "--timeout",
                   "25" if args.command == "get" else "25000"]
        if args.command == "fetch":
            command += ["--headless", "--wait", "1000"]
            if args.browser_path:
                command += ["--executable-path", args.browser_path]
        invoke(command)
        print(f"Extraction command completed: {output}")
        print("Read the file to verify the content. This does not establish news validity or product fit.")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
    try:
        main()
    except (RuntimeError, OSError, subprocess.CalledProcessError) as error:
        print(f"News tools: {error}", file=sys.stderr)
        sys.exit(1)
