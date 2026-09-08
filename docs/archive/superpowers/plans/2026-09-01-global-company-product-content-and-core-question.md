# Global Company/Product Content and Core-Question Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans (inline execution authorized by the user).

**Goal:** Update the global writing rules so every generated Chinese B2B short-video script includes substantive company and product content by default, unless the user explicitly opts out, while keeping one core question, plain-language clarity, calibrated evidence, and no hard-sell insertion.

**Architecture:** `AGENTS.md` remains the project-wide source of truth. The router, shared quality gates, company-placement references, topic-conversion loop, and each script skill must agree with it. Humanizer remains an expression-only pass and must not add facts or change the content boundary.

**Tech Stack:** Markdown rule files, Python rule-test runner (`tests/run_rule_tests.py`), Git.

## Global Constraints

- Preserve factual, source, news, parameter, project-participation, and platform-risk boundaries.
- Do not introduce a fixed paragraph template or fixed company/product position.
- Keep the user-approved Humanizer edits and existing unrelated worktree changes untouched.
- Do not stage `content-state/hotspot-ledger.json`, `.firecrawl/`, `wenan-skill/`, or the user handoff document.

---

### Task 1: Add failing regression tests for the new global contract

**Files:**
- Create: `tests/test_global_company_product_content_rules.py`
- Test runner: `tests/run_rule_tests.py`

**Steps:**
1. Assert the global rules define default company/product inclusion with explicit opt-out, substantive answer relevance, no fixed structure, one core-question closure, plain-language accessibility, calibrated claims, and reject/convert behavior when no valid bridge exists.
2. Assert all routed script skills remove contradictory “pure science/product-free/optional landing” defaults and state the shared contract.
3. Run `python tests/run_rule_tests.py`; confirm the new tests fail before rule edits.

### Task 2: Update project-wide truth and generation rules

**Files:**
- Modify: `AGENTS.md`
- Modify: `.agents/skills/wenan-skill/SKILL.md`

**Steps:**
1. Replace opt-in company/product language with default substantive inclusion and explicit opt-out.
2. Add the core-question derivation gate: every title, fact, news detail, product feature, company capability, and ending must help answer the same question; reject or narrow a topic when this cannot be done.
3. State that runtime is unrestricted; simplicity means low cognitive load, not short copy.
4. Keep the existing evidence, source, no-invention, and news-project non-participation boundaries.
5. Run the rule tests.

### Task 3: Align shared references and placement logic

**Files:**
- Modify: `.agents/skills/references/company-soft-placement.md`
- Modify: `.agents/skills/references/b2b-content-quality-gate.md`
- Modify: `.agents/skills/references/b2b-topic-conversion-loop.md`

**Steps:**
1. Make company/product a default body requirement unless explicit opt-out, while requiring a real answer role and allowing position/order to follow information relationships.
2. Replace hard ad-stripping as a qualification gate with the effective-relevance test: removing the company/product should leave the issue understandable, but the solution should become incomplete or weaker.
3. Preserve the news exception and prohibit inferring participation, supply, installation, or service in the reported project.
4. Add broad-audience plain-language and core-question closure checks without deleting necessary technical precision.
5. Run the rule tests.

### Task 4: Align every content-type skill

**Files:**
- Modify: `.agents/skills/saudi-breakout-story-script/SKILL.md`
- Modify: `.agents/skills/global-hotspot-industry-impact-script/SKILL.md`
- Modify: `.agents/skills/saudi-professional-knowledge-script/SKILL.md`
- Modify: `.agents/skills/saudi-light-steel-script/SKILL.md`
- Modify: `.agents/skills/saudi-sanitary-unit-script/SKILL.md`
- Modify: `.agents/skills/saudi-camp-fire-script/SKILL.md`
- Modify: `.agents/skills/saudi-product-seeding-script/SKILL.md`
- Modify: `.agents/skills/saudi-brand-proof-script/SKILL.md`

**Steps:**
1. Remove contradictory product-free, pure-science, and optional-company defaults.
2. Require each final body to use company/product content as part of the answer, not as a trailing name or generic slogan.
3. Let the story, news, compliance, product, and brand skills choose different information relationships and lengths; do not impose a shared paragraph skeleton.
4. Add topic conversion/rejection behavior when a verified company/product bridge cannot answer the core question.
5. Run all tests and search for leftover contradictory rules.

### Task 5: Verify, commit, and push

**Steps:**
1. Run `python tests/run_rule_tests.py` and `git diff --check`.
2. Inspect the diff and status; stage only this plan, the global rule/reference/skill files, and the related Humanizer/test changes already made for this task.
3. Commit with a focused message.
4. Push the current `main` branch to `origin` without touching unrelated worktree files.
5. Report the commit, push result, test result, and preserved unrelated changes.
