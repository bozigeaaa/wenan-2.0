---
name: saudi-breakout-story-script
description: Use when generating or revising Chinese short-video口播 scripts about Saudi local life, current hot topics, counterintuitive Saudi observations, industry stories, construction-site anecdotes, or expat work/life angles where the goal is audience growth and attention, with company or product content included only when it passes the same-chain role and evidence checks.
---

# Saudi Breakout Story Script

## Purpose

Create Chinese short-video scripts that help 东方骆驼 accounts break out of a narrow product audience by telling Saudi local life, hot topic, counterintuitive, or industry-observation stories. The goal is attention and trust. When company or product content qualifies for inclusion, it must contribute to the same content promise instead of becoming a separate sales paragraph.

## 适用场景

本 Skill 的适用场景以 frontmatter `description` 与下方原有任务边界为准。

生成或改写前，必须读取 `../references/generation-trigger-registry.md`，按可观察的事实关系、受众动作和证据形态选择结构与表达处理；本 Skill 只补充故事事实边界、文化风险和破圈语境差异。

## Core Rule

只在用户明确要求公司/产品、产品本身就是本期主题，或新闻流程已锁定适配产品时，才读取 `.agents/skills/references/company-soft-placement.md` 做详细植入资格审查。只有公司或产品具备已核实证据，并帮助完成同一内容承诺时才写入；其他故事稿不主动寻找品牌桥。

## Required Sources

Before writing:

- Read `knowledge/AI资料导航索引.md` when local Saudi industry facts may matter.
- Read `knowledge/沙特临建行业认知.xlsx` for Saudi construction, temporary camp, approval, government, supply-chain, or engineering context.
- Read the relevant company, product, and claim-evidence sources when checking a possible placement or using company or product content in the story.
- Browse current reliable sources when the topic involves today's news, current policy, trending events, public figures, sports, visas, labor rules, prices, market changes, or anything likely to change.

## Workflow

1. Lock the audience-facing content promise.
   - Identify the verified Saudi detail or relationship the viewer will understand, and the exact observation, judgment, or boundary the script must leave behind.
   - Curiosity may come from a scene, cause, condition, contrast, or time change; do not require a surprise, conflict, or misunderstood rule.

2. Verify the factual spine.
   - Read `references/fact-boundaries.md`.
   - Do not invent personal encounters, local rumors, fines, crackdowns, or "everyone knows" claims.

3. Choose the story relationship.
   - Read `references/story-pattern.md` and select only a route supported by the material.
   - Use one core point. A local behavior, business logic, industry boundary, contrast, or event sequence is optional rather than a required beat.

4. When a placement trigger is present, evaluate company and product content without changing the content promise.
   - If the topic touches temporary camps or construction, test whether a relevant product or company practice has a verified, necessary role in the same industry logic. Include only candidates that pass; otherwise keep the story unbranded.

5. Output the complete script by default.
   - If the script uses current news, policy, prices, market changes, regulations, or other factual claims that required browsing or local source verification, append a short `资料出处` footer listing only those sources.

6. Run the professional B2B quality gate before finalizing.
   - Read `.agents/skills/references/b2b-content-quality-gate.md`.
   - Keep audience curiosity subordinate to the verified story spine; do not invent a universal local behavior, project consequence, or cultural conflict for the hook.
   - If company or product content is present, confirm that it directly supports the same observation, judgment, or boundary; otherwise remove it rather than forcing a new angle.
   - When the story touches industry work, keep its title, opening, body, and final line on the same semantic promise. Sharing the same project, product, or industry vocabulary is not enough.

## Tone

Curious, vivid, grounded, and human. It can be sharper and more entertaining than product scripts, but must not mock Saudi people, local religion, local suppliers, workers, or Chinese contractors.

## Reference Files

- `references/story-pattern.md`: evidence-triggered story routes and culture-risk checks.
- `references/fact-boundaries.md`: current-news, anecdote, and culture-safety boundaries.
- `.agents/skills/references/b2b-content-quality-gate.md`: shared title, B2B decision-value, logic-flow, and publishing-risk gate.
- `.agents/skills/references/expression-craft.md`: paragraph-transition and spoken-language techniques.
- `.agents/skills/references/hook-pattern-library.md`: opening-hook patterns and weak-hook list.
