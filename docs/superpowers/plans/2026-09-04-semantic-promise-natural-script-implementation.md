# Semantic Promise and Natural Script Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Remove active hard-writing templates and add a structure-neutral semantic promise gate that prevents a script from changing the title's decision variable.

**Architecture:** Keep one fixed safety workflow while leaving the visible script shape open. The shared registry owns the semantic promise contract and post-draft reverse-answer gate; router, manifest, quality gate, Humanizer, specialist skills, patterns, ledger, and tests only expose or consume that contract without duplicating it.

**Tech Stack:** Markdown agent instructions, JSON workflow manifest/state ledger, Python rule tests, Codex subagent pressure scenarios.

## Global Constraints

- Facts, evidence strength, applicability boundaries, responsibility, and causality remain hard invariants.
- One script fulfills one content promise; it is not required to use questions, fixed paragraphs, a fixed ending, a CTA, or uniform sentence lengths.
- Lock semantic target, not visible prose order: object/context, decision dimension, required answer, answer boundary, and adjacent non-substitutes.
- Default corpus length is a post-draft completeness diagnostic; an explicit user length remains a pre-draft constraint.
- Company/product placement is a conditional branch, not a universal content slot.
- Use `apply_patch` for all edits and preserve unrelated user changes.
- This directory is not a Git repository; commit/worktree steps are inapplicable and must be recorded as skipped rather than simulated.

---

### Task 1: Add red regression coverage

**Files:**
- Modify: `tests/test_triggered_generation_pipeline.py`
- Create: `tests/test_semantic_promise_rules.py`

**Interfaces:**
- Consumes: current manifest, registry, router, shared references, specialist skills, pattern files.
- Produces: failing assertions for the new semantic state, stage order, removed hard templates, conditional placement, post-draft default length, and surface-skeleton review.

- [ ] Add a manifest assertion requiring `lock_semantic_promise`, `check_promise_answerability`, and `validate_promise_fulfillment`, with fulfillment after oralization/content-coverage and before fact recheck.
- [ ] Add literal state-field assertions for object/context, decision dimension, required answer, answer boundary, and adjacent non-substitutes.
- [ ] Add project-wide assertions that active generation files no longer contain short-sentence mandates, `Prefer` finished frames, pre-draft ending selection, paragraph-action quotas, the two user-deleted rules, or pattern `End with...` menus.
- [ ] Add assertions that default corpus length is post-draft only and detailed placement eligibility is conditional.
- [ ] Run `python tests/run_rule_tests.py` and confirm failure is caused by the missing contract and retained hard-template phrases.

### Task 2: Implement the shared semantic promise workflow

**Files:**
- Modify: `AGENTS.md`
- Modify: `.agents/skills/wenan-skill/SKILL.md`
- Modify: `.agents/skills/references/generation-trigger-registry.md`
- Modify: `.agents/skills/references/generation-manifest.json`
- Modify: `.agents/skills/references/b2b-content-quality-gate.md`
- Modify: `.agents/skills/references/expression-craft.md`
- Modify: `.agents/skills/references/company-soft-placement.md`
- Modify: `content-state/script-structure-ledger.json`

**Interfaces:**
- Consumes: design specification and red tests from Task 1.
- Produces: one shared semantic promise contract and observable invocation stages used by all complete-script entries.

- [ ] Replace “one core question” with “one content promise” where it shapes generation, while preserving domain-specific factual questions where they are ordinary prose.
- [ ] Remove pre-draft action sequence and ending task from the universal generation sequence.
- [ ] Define the semantic promise fields and require the provable conclusion to directly answer the locked decision dimension.
- [ ] Replace paragraph-action checking with claim-level relevance: substantive facts, parameters, cases, and product claims must answer, evidence, or explain the locked promise.
- [ ] Move default corpus length selection out of pre-draft state; retain explicit user length before drafting and run reference-corpus completeness only after oralization.
- [ ] Make placement detail conditional on explicit company/product intent, product-topic work, or selected-product news flow.
- [ ] Add post-draft reverse-answer extraction and comparison before final fact recheck; forbid a closing sentence from masking a dimension mismatch.
- [ ] Change dedup fields from preplanned action/ending tasks to post-draft extracted relationship, evidence, company role, ending form, and surface skeleton.
- [ ] Run the focused tests and make them green without adding fixed prose order.

### Task 3: Remove specialist and Humanizer template anchors

**Files:**
- Modify: `.agents/skills/saudi-light-steel-script/SKILL.md`
- Modify: `.agents/skills/saudi-sanitary-unit-script/SKILL.md`
- Modify: `.agents/skills/saudi-camp-fire-script/SKILL.md`
- Modify: `.agents/skills/saudi-professional-knowledge-script/SKILL.md`
- Modify: `.agents/skills/saudi-breakout-story-script/SKILL.md`
- Modify: `.agents/skills/saudi-product-seeding-script/SKILL.md`
- Modify: `.agents/skills/global-hotspot-industry-impact-script/SKILL.md`
- Modify: `.agents/skills/saudi-brand-proof-script/SKILL.md`
- Modify: `.agents/skills/humanizer/SKILL.md`
- Modify: the eight specialist `references/*pattern.md` files enumerated in `tests/test_triggered_generation_pipeline.py`.

**Interfaces:**
- Consumes: the shared registry contract from Task 2.
- Produces: specialist files containing only domain facts/risks and a Humanizer that repairs whole-script discourse without choosing a new answer.

- [ ] Delete finished question examples, `Prefer` prose frames, uniform short-sentence mandates, default pressure subjects, and pre-draft ending selection.
- [ ] Replace question/pressure framing with content-promise, decision-task, or provable-judgment wording.
- [ ] Remove duplicated public structure routes and `End with...` menus from every specialist pattern; keep only domain-specific evidence and risk boundaries plus a pointer to the shared registry.
- [ ] Add Humanizer surface-skeleton review for repeated `先A再B`, `别只A要B`, `不是A而是B`, `A能不能B`, and `所以＋复述` functions without banning individual words.
- [ ] Allow the smallest continuous-range rewrite, including whole-script reorganization when repetition crosses paragraphs, while preserving factual invariants.
- [ ] Run focused tests and inspect all modified skill frontmatter and pointers.

### Task 4: Behavioral verification and full regression

**Files:**
- Modify if a proven gap remains: only files already listed in Tasks 1–3.
- Verify: all project rule tests and fresh-context agent pressure scenarios.

**Interfaces:**
- Consumes: completed rule set and tests.
- Produces: evidence that the rules are wired, the known drift is rejected, a matching title is accepted, and prose shape remains free.

- [ ] Run the full `python tests/run_rule_tests.py` suite and require zero failures.
- [ ] Run a fresh-context scenario with the title “NEOM数据中心开工，打包箱该不该马上定？” and a body that actually answers product suitability/modular value; require rejection for decision-dimension mismatch.
- [ ] Run the same body with a title that promises modular-space suitability; require the semantic alignment check to accept the dimension while leaving factual verification separate.
- [ ] Run a correct timing-focused body containing a product fact only where it changes the timing answer; require acceptance without a fixed question-answer or paragraph structure.
- [ ] Run a natural-transition scenario to confirm prose is not rejected merely because a sentence or paragraph adds no new professional fact.
- [ ] Perform final spec review for duplicate authority, accidental new templates, stale old phrases, and scope creep.

