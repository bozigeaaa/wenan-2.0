---
name: saudi-product-seeding-script
description: Use when generating or revising Chinese B2B product-seeding short-video口播 scripts for Saudi project buyers who are comparing solutions, prices, suppliers, or configurations, and the script must support a real buying judgment with verified product, tradeoff, risk, lifecycle, or responsibility evidence without becoming a hard ad.
---

# Saudi Product Seeding Script

## Purpose

Create product种草 scripts for viewers already comparing solutions. The script should not dump parameters or shout slogans. It should help a buyer understand one evidenced tradeoff, condition, mechanism, responsibility, or wrong-choice risk that fulfils the locked content promise.

本 Skill 由产品主题触发，因此进入 `placement_eligibility` 条件分支并读取 `.agents/skills/references/company-soft-placement.md` 做植入资格检查。产品或公司只有通过同链角色与证据检查才写入；不具备资格就不植入，不把品牌名称或能力当成固定收尾。

## 适用场景

本 Skill 的适用场景以 frontmatter `description` 与下方原有任务边界为准。

生成或改写前，必须读取 `../references/generation-trigger-registry.md`，按可观察的事实关系、受众动作和证据形态选择结构与表达处理；本 Skill 只补充采购压力、产品事实、转化边界和比较风险差异。

## Routing

Use this as the general product-seeding skill. If the product topic is specifically:

- Fire/camp compliance: use `$saudi-camp-fire-script`.
- Thin-walled light steel: use `$saudi-light-steel-script`.
- TBOX/K-series sanitary units: use `$saudi-sanitary-unit-script`.

Use this skill for cross-product, general procurement, supplier selection, local delivery, logistics cost, after-sales, and "why this type of solution is worth considering" topics.

## Product Landing Gate

Read `.agents/skills/references/company-soft-placement.md` before planning any company or branded-product mention.

Before mentioning Eastern Camel, TBOX, factory, stock, local delivery, `15000㎡`, or any specific company/product capability, check:

1. Does the proposed product or company content pass the placement qualification, same-chain role, and evidence checks? If not, do not include it.
2. Does the company/product stay inside the locked object, scenario, decision variable, and evidence boundary without adding a new pain point or unrelated scenario?
3. Does this company/product fact directly answer the content promise or provide evidence needed for that answer?

If the product/company fact cannot help fulfil the same content promise, omit that placement. Change the angle only when the user explicitly requires that product or company and a verified alternative angle exists; otherwise do not force a close.

Factory area and `15000㎡` are only relevant when the point is local manufacturing scale, production capacity, or delivery certainty. Do not use them for unrelated topics such as maintenance, compliance, hygiene, material logic, or general procurement risk.

## Required Sources

- Read `knowledge/AI资料导航索引.md`.
- Read `knowledge/钧瀚产品优势分级分类总表_v4.xlsx` for verified advantages, reliability level, conflict records, and product/brand mapping.
- Read the relevant product fact file before using any product parameter.
- Read `knowledge/深圳钧瀚科技有限公司企业基础概况.docx` and `knowledge/东方骆驼公司简介.txt` for company/service capabilities when needed.
- Browse current reliable sources for current competitor, market, price, policy, or mainstream solution claims.

## Workflow

1. Lock the buyer-facing content promise.
   - Identify the exact object, scenario, decision action or variable, required answer, evidence boundary, and adjacent questions that must stay outside this script.

2. Select the supported decision relationship.
   - Read `references/seeding-pattern.md` and choose a same-basis comparison, causal risk, conditional selection, lifecycle account, responsibility chain, or product mechanism.
   - A wrong-choice cost is optional and must not be invented. Do not list every product advantage.

3. Verify product facts.
   - Read `references/fact-rules.md`.
   - Every parameter must directly answer the locked content promise, provide necessary evidence for it, or explain why that evidence changes the answer.

4. Evaluate the company and product in their possible decision role.
   - Include product or company content only when it has verified evidence and helps fulfil the same content promise; never use a name-only insertion or a separate advertisement.
   - If the current angle cannot support that role, omit the placement. When the user explicitly requires the product or company, offer a verified alternative angle or explain that the requested connection cannot be supported.

5. Output the complete script by default.
   - If the script uses specifications, company/product parameters, price/cost claims, current market facts, competitor comparisons, logistics quantities, delivery capabilities, or other external facts, append a short `资料出处` footer listing only the sources actually used.

6. Run the professional B2B quality gate before finalizing.
   - Read `.agents/skills/references/b2b-content-quality-gate.md`.
   - Audit substantive claims against the same decision variable and required answer; do not require a wrong-choice cost or mechanism when another evidence relationship is stronger. Natural transitions do not need to add a separate professional fact.
   - Do not convert a conditional risk reduction into a guarantee, exaggerated loss, or competitor accusation for stronger conversion.

## Tone

Professional, practical, buyer-aware. More persuasive than科普, but never cheap-sales, insulting, or exaggerated.

## Reference Files

- `references/seeding-pattern.md`: evidence-triggered buying-decision routes and conversion boundaries.
- `references/fact-rules.md`: product fact and competitor comparison boundaries.
- `.agents/skills/references/b2b-content-quality-gate.md`: shared title, B2B decision-value, logic-flow, and publishing-risk gate.
- `.agents/skills/references/expression-craft.md`: paragraph-transition and spoken-language techniques.
- `.agents/skills/references/hook-pattern-library.md`: opening-hook patterns and weak-hook list.
