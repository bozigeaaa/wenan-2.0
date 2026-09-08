---
name: saudi-sanitary-unit-script
description: Generate or revise Chinese B2B short-video口播 scripts for Saudi mobile toilets, TBOX/K-series sanitary units, portable toilets, mobile shower rooms, modular bathrooms, campsite sanitation, washroom compliance, odor/drainage/ventilation, packing size, container loading, 304 stainless steel floors, anti-corrosion, field maintenance, and comparisons with current Saudi market sanitary solutions. Use when the user wants one reliable, single-point, expert-style script about sanitary-unit product logic, parameters, selection, application scenarios, or competitor/market comparison for Eastern Camel.
---

# Saudi Sanitary Unit Script

## Purpose

Create professional Chinese口播 scripts about TBOX / K-series mobile toilets, mobile shower rooms, and modular sanitary units in Saudi project scenarios. The speaker should sound like a Saudi engineering practitioner explaining a real camp-management or project-delivery issue, not like a salesperson reading a catalog.

This skill is for single-point sanitary product logic. Each script fulfills one sanitary content promise, which may be a judgment, explanation, comparison, responsibility boundary, or site process. Eastern Camel product or delivery capability may appear only when a placement trigger exists and its same-chain role and evidence pass the placement gate.

## Required Local Sources

Before writing or revising a sanitary-unit script, inspect the project navigation file when available:

- `knowledge/AI资料导航索引.md`

Prioritize these source files:

- `knowledge/K系列卫生间参数.xlsx` for TBOX/K-series models, dimensions, packing dimensions, configurations, and product parameters.
- `knowledge/K系列设计文稿.docx` for K-series positioning, product logic, scenario language, and approved product advantages.
- `knowledge/钧瀚产品优势分级分类总表_v4.xlsx` for advantages, conflict records, reliability level, price/install-time conflicts, and brand-name mapping.
- `knowledge/深圳钧瀚科技有限公司企业基础概况.docx` for company role, sanitary product line, Saudi delivery, and sales cognition.
- `knowledge/TBOX 移动卫浴.pdf`, `knowledge/模块化卫生间应用介绍.pdf`, `knowledge/拆装式移动厕所.pdf`, and `knowledge/拆装式移动厕所配置表.pdf` for visuals, product appearance, layout, scenario, and brochure style. Do not use image-heavy PDFs as the only parameter source.

If a requested model, size, install time, price, material, or compliance claim is not confirmed in local sources, do not invent it. Verify it or leave it out.

## 适用场景

Use this skill for topics such as:

- The project role of campsite sanitary units in Saudi projects.
- Odor, drainage, ventilation, sealing, cleaning, and maintenance issues in mobile toilets.
- How to choose squat toilet, sitting toilet, shower, dual-unit, or combined sanitary configurations.
- K-series / TBOX model comparison and scenario selection.
- Packing size, transport, container loading, fast deployment, and emergency site use.
- 304 stainless steel floor, anti-corrosion, anti-rust, high-temperature use, and outdoor durability claims.
- Local stock, local installation, Chinese coordination, and after-sales response for sanitary units.
- Current Saudi market alternatives or competitor comparison, when researched.

生成或改写前，必须读取 `../references/generation-trigger-registry.md`，按可观察的事实关系、受众动作和证据形态选择结构与表达处理；本 Skill 只补充移动卫浴参数、营地运营压力、维护边界和场景选型差异。

## Core Rule

One video fulfills one sanitary-unit content promise. Do not turn one script into a full K-series catalog.

仅当 `../references/generation-trigger-registry.md` 打开 `placement_eligibility` 条件分支时，才读取 `.agents/skills/references/company-soft-placement.md` 并检查植入资格。公司或产品还须有已核实证据，并在同一判断变量的答案中承担必要角色；资格不成立就不植入。

Title, opening, parameters, product claims, and any final line must fulfill the same semantic promise and address the title's decision variable. Material that belongs to the same product or project but answers a different decision variable belongs in another script.

## Pressure Subject Rule

Sanitary topics often fail when the script chooses the wrong emotional subject.

When responsibility or operating pressure is material to the content promise, locate it on the role that actually carries it:

- Project manager: compliance checks, client complaints, responsibility, urgent rectification.
- Camp manager: daily cleaning, maintenance, odor, drainage, usage intensity.
- Procurement owner: wrong model choice, later repair cost, replacement pressure.

Do not write workers as the main active complaint or strike subject unless the user provides a real case. Workers may be direct users, but the business pressure usually lands on managers and procurement.

## Local Perspective Rule

Default to a Saudi local supplier / project delivery perspective. Do not unnecessarily frame the product as "from China", "sent from China", or "domestic configuration". If the issue is local delivery, discuss deployment, maintenance, cleaning, spare parts, and project responsibility in Saudi terms.

## Workflow

1. Establish the content promise.
   - Execute the semantic-promise and answerability stages in `../references/generation-trigger-registry.md`.
   - Keep one sanitary judgment variable and only the verified material needed to fulfill it. Use the semantic form that fits the task; treat any final line as optional until the body has fulfilled the promise.

2. Verify facts.
   - Read `references/fact-check-rules.md`.
   - Treat model names, sizes, packing dimensions, install time, price, material, 304 stainless steel, anti-corrosion, ventilation, drainage, compliance, fines, and inspection outcomes as high-risk facts.
   - Check each parameter one by one against local sources, conflict records, user-provided facts, or reliable current sources before writing it.
   - Do not avoid parameters merely because they are high-risk. If a parameter is real, relevant, and verified, use it precisely.
   - If a parameter cannot be verified, do not write it as fact.

3. Check policy or market comparison needs.
   - If the script mentions Saudi labor/camp sanitation requirements, fines, inspections, current competitors, market alternatives, or mainstream local sanitary solutions, browse current reliable sources first.
   - Do not name regulations, fines, competitors, prices, or performance conclusions without current evidence.
   - Compare risk structures and suitable scenarios, not by insulting competitors.

4. Build the script.
   - Read `references/script-pattern.md`.
   - Let the information relationship choose the order: a mechanism, comparison, sequence, scene, or decision rule may come first. Include TBOX / K-series or Eastern Camel content only when the placement branch was triggered and it passes the same-chain role and evidence checks; otherwise omit it. Do not reserve qualified content for a fixed closing advertisement or force a common paragraph template.

5. Follow project output rules.
   - By default, output the complete script text.
   - When the script uses regulations, specifications, K-series/TBOX parameters, material data, container-loading facts, competitor/current-market facts, or other external facts, append a short `资料出处` footer listing only the sources actually used.
   - Do not show self-check or risk notes unless the user asks.

6. Run the professional B2B quality gate before finalizing.
   - Read `.agents/skills/references/b2b-content-quality-gate.md`.
   - Confirm that the title, opening, selected evidence relationship, and any qualified company or product content fulfill the same verified sanitary content promise. If the script has an additional final line, it must do the same.
   - Do not use odor, maintenance, inspection, or worker-pressure language to imply unverified complaints, stoppages, fines, or guarantees.

## Tone

- Direct, grounded, and slightly serious.
- Sanitization topics can be awkward; acknowledge the real problem without becoming crude, sensational, or visually disgusting.
- Like someone who has seen Saudi camp operations and knows what project managers actually worry about.
- Let sentence length follow meaning and speaking breath; preserve a complete operational judgment when an artificial split would make it harder to follow.
- Express technical and operational judgments through concrete subjects, actions, conditions, and consequences. Explain a necessary product term in plain Chinese when it first affects the promise.

## Hard Boundaries

- Do not turn sanitary scripts into a full product catalog.
- Do not make sanitation content vulgar, fear-mongering, or visually disgusting for attention.
- Do not write workers as collectively striking, protesting, or actively forcing project shutdown unless there is a real case.
- Do not invent Saudi policy names, legal requirements, fine amounts, inspection outcomes, or compliance guarantees.
- Do not say "guaranteed inspection pass", "100% odorless", "zero maintenance", or "permanent anti-corrosion".
- Match maintenance language to the evidence strength. Without a verified absolute performance result, state only the supported direction of risk reduction, cleaning convenience, or maintenance effect, with its applicable conditions.
- Do not invent K-series model parameters, dimensions, packing sizes, install time, price, material, or capacity.
- Do not write "local Saudi options are bad" or insult local contractors, Chinese contractors, or competitors.
- Do not use old generic competitor stereotypes. Current market claims require current research.

## Reference Files

- `references/script-pattern.md`: evidence-triggered sanitary-unit decision routes and operating-risk checks.
- `references/fact-check-rules.md`: model, parameter, compliance, competitor, and high-risk claim handling.
- `.agents/skills/references/b2b-content-quality-gate.md`: shared title, B2B decision-value, logic-flow, and publishing-risk gate.
- `.agents/skills/references/expression-craft.md`: paragraph-transition and spoken-language techniques.
- `.agents/skills/references/hook-pattern-library.md`: opening-hook patterns and weak-hook list.
