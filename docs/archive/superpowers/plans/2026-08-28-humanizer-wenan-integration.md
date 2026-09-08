# Humanizer Wenan Integration Implementation Plan

> **For agentic workers:** Execute inline in the current session. Do not dispatch subagents, commit, or upload; the user requires all pending changes to remain local until the full modification series is complete.

**Goal:** Replace the duplicate oralization pipeline with a project-local Humanizer 2.11.2 Skill adapted for focused, easy-to-follow Chinese B2B scripts and paired before/after output.

**Architecture:** Vendor the upstream Markdown Skill and MIT license into `.agents/skills/humanizer/`, add concise wenan-specific precedence rules, and route all complete-copy expression work through that single Skill. Shared project rules continue to own facts, news, product choice, company exposure, and content logic.

**Tech Stack:** Markdown Agent Skills, YAML UI metadata, Python rule-contract tests.

## Global Constraints

- Preserve all existing uncommitted news and title changes.
- Do not commit or upload.
- Do not add fixed body templates, paragraph categories, prerequisite questions, connector libraries, intensity ladders, or sentence-length caps.
- Keep the upstream Humanizer version and MIT notice traceable.

---

### Task 1: Add failing rule-contract tests

**Files:**
- Create: `tests/test_humanizer_output_rules.py`
- Modify: `tests/run_rule_tests.py`

- [ ] Assert the formal Humanizer Skill, license, adaptation rules and UI metadata exist.
- [ ] Assert complete-copy output includes `原文案` and `优化后文案` and no longer routes through the old rewriter.
- [ ] Assert hooks may use suspense without needing evidence in the hook itself, while fabricated outcomes remain forbidden.
- [ ] Assert the script stays on one subject without fixed structures or prerequisite questions.
- [ ] Assert low-cognitive-load Chinese wording and necessary-term-only behavior.
- [ ] Run the new tests and verify they fail because the integration is missing.

### Task 2: Create the formal Humanizer Skill

**Files:**
- Create: `.agents/skills/humanizer/SKILL.md`
- Create: `.agents/skills/humanizer/LICENSE`
- Create: `.agents/skills/humanizer/agents/openai.yaml`

- [ ] Vendor upstream Humanizer 2.11.2 behavior and attribution.
- [ ] Add wenan precedence, Chinese B2B, focus, hook, source and paired-output constraints.
- [ ] Keep Humanizer expression-only; do not move news, title, product or company decisions into it.
- [ ] Run the focused tests and verify the Skill contract passes.

### Task 3: Rewire project rules and output

**Files:**
- Modify: `AGENTS.md`
- Modify: `.agents/skills/wenan-skill/SKILL.md`
- Modify: `.agents/skills/references/b2b-content-quality-gate.md`
- Modify: `.agents/skills/digital-human-storyboard/SKILL.md`
- Modify: `docs/wenan-skill-完整交接文档_2026-08-14.md`

- [ ] Replace the old two-stage expression pipeline with `$humanizer`.
- [ ] Add the approved paired output format.
- [ ] Replace evidence-required hook wording with suspense-safe wording.
- [ ] Replace rigid oralization rules with focused, low-cognitive-load outcome rules.
- [ ] Preserve storyboard immutability and clarify which confirmed version it uses.
- [ ] Run focused and existing tests.

### Task 4: Retire duplicate rules and verify

**Files:**
- Delete: `.agents/skills/script-oralization-rewriter/`
- Delete: `.agents/skills/references/b2b-humanizer-expression-gate.md`
- Modify: affected current handoff and rule tests only where active behavior changed.

- [ ] Remove active references to retired paths.
- [ ] Run the complete rule-test suite.
- [ ] Run `quick_validate.py` for `humanizer`, `wenan-skill`, and affected Skills.
- [ ] Run `git diff --check` and inspect `git status` without committing.
