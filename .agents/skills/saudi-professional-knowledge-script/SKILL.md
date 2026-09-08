---
name: saudi-professional-knowledge-script
description: Use when generating, diagnosing, revising, or selecting titles for Chinese B2B short-video口播 scripts about Saudi temporary construction, camp approval, collective housing, supply chains, compliance, materials, engineering boundaries, logistics, customs, local content, or project management. Verify the title premise and exact engineering scenario before drafting, fulfil the title's locked semantic promise, and include company or product content only when it passes the same-chain role and evidence checks.
---

# Saudi Professional Knowledge Script

## Purpose

Create professional Chinese口播 scripts that build trust by explaining Saudi engineering, temporary camp, approval, supply-chain, compliance, material, or project-boundary topics. The script should sound like an experienced practitioner simplifying a real rule or mechanism. Any company or product content that qualifies for inclusion must be a concrete part of the same answer rather than a detached advertisement.

## 适用场景

本 Skill 的适用场景以 frontmatter `description` 与下方原有任务边界为准。

生成、改写或选择标题前，必须读取 `../references/generation-trigger-registry.md`，按可观察的事实关系、受众动作和证据形态选择结构与表达处理；本 Skill 只补充专业场景、审批边界、术语解释和事实深度差异。

## Routing

Use this as the general professional科普 skill. If the topic is specifically about:

- Fire safety, SBC 801, Civil Defense, Salamah: use `$saudi-camp-fire-script`.
- Thin-walled light steel houses or G550 wall/roof systems: use `$saudi-light-steel-script`.
- TBOX/K-series toilets, showers, sanitary units: use `$saudi-sanitary-unit-script`.

## Required Sources

- Read `knowledge/AI资料导航索引.md`.
- Read `knowledge/沙特临建行业认知.xlsx` for Saudi approval, SBC, Civil Defense, SABER/SASO, tax, customs, local content, and project cognition.
- Read relevant product and company files when checking a possible placement or when qualified company or product content will be used.
- Browse current reliable sources when discussing current policy, agencies, public programs, fines, enforcement, market changes, or latest news.

## Workflow

1. Run the title-premise gate before drafting.
   - Identify the title's exact subject, factual premise, customer concern, and one answer the viewer should retain.
   - Verify whether the premise matches the real engineering or approval process. Do not manufacture a late application, missing handoff, rework, rejection, extra cost, or other conflict merely to make the title dramatic.
   - If the premise is false, uncommon, or not supported, stop and explain why; recommend a fact-based angle instead of forcing a script.
   - Do not change a user-confirmed title unless the user authorizes it.
   - If the user says "先检查", "先分析", "先确认", "先判断标题", or otherwise asks for validation before generation, output only the diagnosis, recommended core conclusion, and proposed reasoning path. Do not write the script in the same turn, even when the title is viable; wait for explicit confirmation.
   - If the user asks for title candidates only, generate candidates only. Within the same topic, audience, and evidence boundary, candidates may explore different true, draftable promises and topic-appropriate angles; provide each title, the judgment variable or observation it commits to, its evidence-backed non-basic conclusion, and its information relationship. After one candidate is selected, update the current task's temporary content state; the user can request the body next without moving or resubmitting an intermediate document.

2. Lock the exact scenario and boundaries.
   - Distinguish fixed residential buildings, residential compounds, project mobile cabins, and other temporary facilities.
   - Distinguish applicant/responsible-party identity, property or site-use relationship, product ownership, approval requirements, application documents, inspection items, and operating conditions. These are different concepts; never merge them for convenience.
   - Distinguish local manufacture/local delivery from imported or cross-border supply.
   - Do not transfer a rule from one scenario to another without an official or primary source that explicitly supports the transfer.
   - A general service page may cover multiple facility categories. Do not repeat its generic ownership/lease checklist in a mobile-cabin script unless the source explicitly states that the item applies to mobile cabins or the title directly asks about that document.

3. Verify facts to the depth needed by the title.
   - Read `references/fact-rules.md`.
   - Use an official service summary only as a routing source. If it says only "health, technical, and safety requirements," follow the linked official guide and extract concrete, relevant checks before using that phrase as the script's value.
   - Exact regulation names, thresholds, agency roles, approval outcomes, fines, timelines, documents, inspection items, and responsible parties must be verified.
   - Internally map every factual sentence to a source. If a sentence is only inference, either remove it or clearly narrow it; do not use inference to fill runtime.

4. Fulfil one locked semantic promise.
   - Read `references/script-pattern.md`.
   - Let the available evidence and required answer determine the information relationship; do not turn a route name into a visible template or automatically use "first, second, third."
   - Keep only substantive claims that directly answer the title promise, provide evidence needed for that answer, or explain why that evidence changes the answer. Documents, responsibility, process, products, or consequences may appear only when they pass that test.
   - Translate necessary technical terms into plain spoken Chinese immediately. Give the viewer a concrete judgment, check, or action rather than abstract words.
   - Let the evidence relationship determine where the scenario and viewer need become clear. Paragraphs follow continuous meaning and spoken breath; natural transitions do not need to add a separate professional fact. Remove repetition and anxiety that do not help fulfil the promise.

5. Apply the company and product answer boundary.
   - 只在用户明确要求公司/产品、产品本身就是本期主题，或新闻流程已锁定适配产品时，才读取 `.agents/skills/references/company-soft-placement.md` 做详细植入资格审查。普通中立科普不主动寻找品牌桥。
   - For a topic originating from construction, infrastructure, urban-development, transport, logistics, industrial-city, or project news, read `.agents/skills/references/b2b-topic-conversion-loop.md` before choosing an angle or company mention.
   - If a company or product candidate cannot help fulfil the same decision variable and required answer, omit it. When the user explicitly requires that product or company, offer an evidence-supported alternative angle or explain that the requested bridge cannot be supported.

6. Re-audit the whole draft after every substantive revision.
   - Do not patch only the sentence the user flagged. Re-read the title, opening, every transition, conclusion, and interaction prompt as one chain.
   - Remove new repetition, concept switching, scene mixing, unsupported implications, and endings that introduce a different topic.
   - Expand runtime only by deepening verified content that answers the title; never add adjacent facts or invented project behavior to reach a target length.

7. Output the complete script by default.
   - When the user asks for a revision, return the full revised version rather than an isolated replacement unless they explicitly request one sentence only.
   - If the script uses regulations, official programs, policy facts, approval requirements, specifications, company/product facts, or current external facts, append a short `资料出处` footer listing only the sources actually used.

8. Run the professional B2B quality gate before finalizing.
   - Read `.agents/skills/references/b2b-content-quality-gate.md`.
   - Keep the verified title conclusion above hook appeal. Confirm that the title, opening, scenario boundary, explanation, and final line fulfil the same semantic promise; any qualified company or product content that is used must pass the same check.
   - Do not make an approval, document, responsibility, or inspection hook sound universal or more consequential than the evidence supports.

## Tone

Calm, expert, grounded, practical, and conversational. Write from the customer's real decision context, not from the supplier's or narrator's superior position. Avoid "内幕", "惊天", official brochure language, robotic summaries, and exaggerated fear. The value is verified clarity and usable judgment.

## Reference Files

- `references/script-pattern.md`: evidence-triggered professional explanation routes and fact-depth checks.
- `references/fact-rules.md`: policy, compliance, and engineering fact boundaries.
- `.agents/skills/references/b2b-content-quality-gate.md`: shared title, B2B decision-value, logic-flow, and publishing-risk gate.
- `.agents/skills/references/b2b-topic-conversion-loop.md`: construction-news relevance gate, education/marketing account routing, evidence-bridge and review rules.
- `.agents/skills/references/expression-craft.md`: paragraph-transition and spoken-language techniques.
- `.agents/skills/references/hook-pattern-library.md`: opening-hook patterns and weak-hook list.
