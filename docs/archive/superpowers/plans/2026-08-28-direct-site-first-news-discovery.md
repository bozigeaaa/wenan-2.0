# Direct-Site-First News Discovery Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Keep the existing P0—P4 source order while making direct website access the primary discovery method and generic search an explicitly labeled gap-filling method.

**Architecture:** The detailed access-method contract lives in `hotspot-sourcing.md`; the hotspot Skill and project rules state the mandatory entry boundary; rule-contract tests prevent generic search results from being reported as direct channel access. The Git repository remains the source of truth, while the current parent-project Skill copy receives the same runtime wording after repository tests pass.

**Tech Stack:** Markdown Agent Skills, Python rule-contract tests, Git.

## Global Constraints

- Keep P0 as Google / Google News, X, MEED, and Etimad, followed by the existing P1—P4 order.
- Directly enter the current-tier websites before using generic web search, other search engines, aggregators, or `site:` queries to fill gaps.
- A generic search-tool hit is not proof that Google, Google News, X, MEED, Etimad, Bing, or another named channel was directly visited.
- Keep the existing A/B/C evidence levels, verification card, product-fit gate, and company-exposure rules unchanged.
- Only report channels and access methods actually used.
- Run all rule tests before commit and push to `origin/main` without force.

---

### Task 1: Lock the discovery-method contract with a failing test

**Files:**
- Modify: `tests/test_news_source_flow_rules.py`

**Interfaces:**
- Consumes: repository Markdown rules as UTF-8 text.
- Produces: assertions for direct-site-first discovery, external-search gap filling, access-method labels, and unchanged P0—P4 order.

- [ ] Add a test that requires `直接进站优先＋外部检索补漏`, the four P0 channels, direct checks of site search/latest/category/notice/archive entries, and the three record states `直接访问完成`, `外部检索线索`, and `访问未完成`.
- [ ] Assert that a generic web-search result cannot be reported as a direct visit to a named channel.
- [ ] Assert that the hotspot Skill and `AGENTS.md` connect to this access-method contract.
- [ ] Run `python tests/run_rule_tests.py` and confirm the new test fails because the active rules do not yet contain the contract.

### Task 2: Implement the repository source-of-truth rules

**Files:**
- Modify: `.agents/skills/global-hotspot-industry-impact-script/references/hotspot-sourcing.md`
- Modify: `.agents/skills/global-hotspot-industry-impact-script/SKILL.md`
- Modify: `AGENTS.md`
- Modify: `docs/wenan-skill-完整交接文档_2026-08-14.md`
- Test: `tests/test_news_source_flow_rules.py`

**Interfaces:**
- Consumes: the existing P0—P4 discovery order and A/B/C verification model.
- Produces: one unambiguous discovery workflow shared by the router, hotspot Skill, handoff, and tests.

- [ ] Rewrite the opening sourcing section so each priority tier is directly visited first and externally searched second.
- [ ] Preserve the exact P0 channel set and P1—P4 order.
- [ ] Add truthful access-method reporting and prohibit translating search-tool hits into direct-channel claims.
- [ ] State in the hotspot Skill and `AGENTS.md` that direct site access is mandatory before generic-search gap filling.
- [ ] Update the current handoff document with the same operational summary without duplicating the full source table.
- [ ] Run the focused rule suite and confirm the new test and all existing news tests pass.

### Task 3: Synchronize the current project runtime copy

**Files:**
- Modify: `../.agents/skills/global-hotspot-industry-impact-script/references/hotspot-sourcing.md`
- Modify: `../.agents/skills/global-hotspot-industry-impact-script/SKILL.md`
- Modify: `../AGENTS.md`

**Interfaces:**
- Consumes: the tested repository wording from Task 2.
- Produces: the same access-method behavior in the Skill copy currently discovered from `C:/Users/Windows/Documents/New project/.agents/skills`.

- [ ] Apply the same minimal direct-site-first and truthful-recording rules to the active parent-project files.
- [ ] Verify the parent copy contains the required phrases and still references the same P0—P4 and A/B/C boundaries.
- [ ] Do not copy unrelated repository files or overwrite unrelated parent-project changes.

### Task 4: Verify, commit, and upload

**Files:**
- Verify all files changed by Tasks 1—3.

**Interfaces:**
- Consumes: tested repository rules and synchronized runtime copy.
- Produces: one GitHub commit containing the repository changes; parent-project runtime edits remain local because they are outside the repository.

- [ ] Run `python tests/run_rule_tests.py` and require zero failures.
- [ ] Run `git diff --check` and scan active repository rules for contradictory old wording.
- [ ] Review `git status --short` and stage only the intended repository files.
- [ ] Commit with a concise news-discovery message.
- [ ] Fetch `origin/main`, push `main` without force, then verify local `HEAD` equals `origin/main`.
