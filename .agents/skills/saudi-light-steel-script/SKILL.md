---
name: saudi-light-steel-script
description: Generate or revise Chinese B2B short-video口播 scripts for Saudi thin-walled light steel houses, long-term camps, office/dormitory units, wall/roof/envelope systems, G550/C-shaped steel, glass wool, cement fiber board, PVC windows, steel doors, insulation, wind/sand/high-temperature performance, and comparisons with packing containers, ordinary prefab, or current Saudi market alternatives. Use when the user wants one reliable, single-point, expert-style script about light-steel product logic, parameters, selection, application scenarios, or competitor/market comparison for Eastern Camel.
---

# Saudi Light Steel Script

## Purpose

Create professional Chinese口播 scripts about thin-walled light steel houses in Saudi project scenarios. The speaker should sound like someone who understands Saudi engineering delivery: practical, specific, and calm, not like a brochure or salesperson.

This skill is for single-point product logic. Each script fulfills one light-steel content promise, which may be a judgment, explanation, comparison, responsibility boundary, or site process. Eastern Camel material, design, delivery, or local service content may appear only when a placement trigger exists and its same-chain role and evidence pass the placement gate.

## Required Local Sources

Before writing or revising a light-steel script, inspect the project navigation file when available:

- `knowledge/AI资料导航索引.md`

Prioritize these source files:

- `knowledge/薄壁轻钢房屋产品介绍.txt` for product structure, materials, wall/roof/envelope system, door/window, and house-type facts.
- `knowledge/沙特临建行业认知.xlsx` for Saudi light-steel industry cognition, approval, site, climate, and compliance boundaries.
- `knowledge/钧瀚产品优势分级分类总表_v4.xlsx` for advantages, reliability level, and conflict records.
- `knowledge/深圳钧瀚科技有限公司企业基础概况.docx` for company role, sales cognition, delivery logic, and Saudi project boundaries.
- `knowledge/东方骆驼公司简介.txt` for Eastern Camel local factory, brand positioning, and Saudi local delivery.

If a requested light-steel parameter is not confirmed in local sources, do not invent or paraphrase it into a weaker claim. Omit it from the script, obtain supporting evidence, narrow the content promise, or stop.

## 适用场景

Use this skill for topics such as:

- Light-steel and packing-container suitability in medium/long-term camps, office areas, or higher-image projects.
- The relationship among wall systems, glass wool, cement fiber board, PVC windows, steel doors, and roof systems.
- The effect of Saudi heat, sand, corrosion, AC load, and site management on product selection.
- Evidence boundaries for G550, C-shaped steel, wall thickness, insulation, fire resistance, wind resistance, or seismic claims.
- Verified local-factory, coordination, or delivery capability when it materially affects light-steel project certainty.
- Evidence-based comparison with current Saudi market alternatives.

If the topic is mainly SBC 801, Civil Defense, Salamah, fire separation, egress, or fire inspection, prefer `$saudi-camp-fire-script`.

生成或改写前，必须读取 `../references/generation-trigger-registry.md`，按可观察的事实关系、受众动作和证据形态选择结构与表达处理；本 Skill 只补充薄壁轻钢参数、围护机制、选型场景和比较风险差异。

## Core Rule

One video fulfills one light-steel content promise. Do not turn one script into a full product catalog.

仅当 `../references/generation-trigger-registry.md` 打开 `placement_eligibility` 条件分支时，才读取 `.agents/skills/references/company-soft-placement.md` 并检查植入资格。公司或产品还须有已核实证据，并在同一判断变量的答案中承担必要角色；资格不成立就不植入。

Title, opening, parameters, product landing, and any final line must fulfill the same semantic promise and address the title's decision variable. Material that belongs to the same product or project but answers a different decision variable belongs in another script.

## Workflow

1. Establish the content promise.
   - Execute the semantic-promise and answerability stages in `../references/generation-trigger-registry.md`.
   - Keep one light-steel judgment variable and only the verified material needed to fulfill it. Use the semantic form that fits the task; treat any final line as optional until the body has fulfilled the promise.

2. Verify facts.
   - Read `references/fact-check-rules.md`.
   - Treat steel grade, wall thickness, glass-wool thickness, wind resistance, seismic grade, fire performance, install time, capacity, and cost as high-risk facts.
   - Check each parameter one by one against local sources, conflict records, user-provided facts, or reliable current sources before writing it.
   - Do not avoid parameters merely because they are high-risk. If a parameter is real, relevant, and verified, use it precisely.
   - If a parameter cannot be verified, do not write it as fact.

3. Check market comparison needs.
   - If the script mentions current competitors, Saudi market alternatives, or mainstream local solutions, browse current reliable sources first.
   - Do not name competitors, prices, or performance conclusions without current evidence.
   - Compare risk structures and suitable scenarios, not by insulting competitors.

4. Build the script.
   - Read `references/script-pattern.md`.
   - Let the information relationship choose the order: a comparison, mechanism, sequence, scene, or decision rule may come first. If the placement branch was triggered and Eastern Camel product or company capability passes its gate, use it inside the same answer; otherwise omit it. Do not reserve qualified content for a fixed closing advertisement or force a common paragraph template.

5. Follow project output rules.
   - By default, output the complete script text.
   - When the script uses regulations, specifications, company/product parameters, material data, competitor/current-market facts, or other external facts, append a short `资料出处` footer listing only the sources actually used.
   - Do not show self-check or risk notes unless the user asks.

6. Run the professional B2B quality gate before finalizing.
   - Read `.agents/skills/references/b2b-content-quality-gate.md`.
   - Confirm that the title, opening, selected evidence relationship, and any qualified company or product content fulfill the same verified light-steel content promise. If the script has an additional final line, it must do the same.
   - Do not use a hook to imply unverified structural, fire, approval, cost, or market consequences.

## Tone

- Professional, direct, and grounded.
- Like a Saudi engineering practitioner explaining one real selection issue.
- Default to a senior Saudi local supplier / project delivery perspective. Do not unnecessarily expose a China-to-Saudi shipment angle.
- Do not sound cheerful, promotional, or brochure-like.
- Let sentence length follow meaning and speaking breath; preserve a complete technical judgment when an artificial split would make it harder to follow.
- Express technical judgments through concrete subjects, actions, conditions, and consequences. Explain a necessary technical term in plain Chinese when it first affects the promise.

## Hard Boundaries

- Do not dump all light-steel parameters into one script.
- Do not remove useful parameters just because they require verification; verify them and keep the ones that directly support the single point.
- Do not say "best", "only answer", "perfect", "100% safe", or "guaranteed approval".
- Do not invent G550/Q235B decisions, wall thickness, glass-wool thickness, wind/seismic ratings, fire ratings, install time, cost, or production capacity.
- Do not claim Saudi regulations force a specific material unless sourced.
- Do not say "规范要求" without identifying whether the support comes from a verified code, owner requirement, drawing requirement, or calculation boundary. For light steel, distinguish SBC 308/309/301/306/303 only when the applicable source has been verified; otherwise do not attribute the judgment to a specific code.
- Do not write "清关资料" for Saudi local factory/local manufacturing/local delivery unless the script is explicitly about imported goods or cross-border procurement. Use "项目资料包、产品规格书、材料参数表、结构计算、消防资料、安装方法书、交付验收记录" instead.
- Do not write "照搬国内现成配置" as a general market fact. Any narrower claim about supplier experience or configuration habits still requires evidence for its actor, scope, and conditions.
- Do not guarantee "15-20 years" or any lifecycle, warranty, or corrosion period unless confirmed in source material. If unresolved, omit it from the script, obtain supporting evidence, narrow the content promise, or stop; do not replace it with vague long-term-use language.
- Do not write "local Saudi options are bad" or insult local contractors, Chinese contractors, or competitors.
- Do not use old generic competitor stereotypes. Current market claims require current research.
- Do not use a fire-safety compliance frame when the topic is actually insulation, structure, delivery, or usage scenario.

## Reference Files

- `references/script-pattern.md`: evidence-triggered light-steel decision routes and parameter checks.
- `references/fact-check-rules.md`: parameter, competitor, and high-risk claim handling.
- `.agents/skills/references/b2b-content-quality-gate.md`: shared title, B2B decision-value, logic-flow, and publishing-risk gate.
- `.agents/skills/references/expression-craft.md`: paragraph-transition and spoken-language techniques.
- `.agents/skills/references/hook-pattern-library.md`: opening-hook patterns and weak-hook list.
