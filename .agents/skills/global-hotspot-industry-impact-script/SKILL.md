---
name: global-hotspot-industry-impact-script
description: Use when current international or Saudi project news must be found, verified, screened for a real link to temporary-building products, shown in a Chinese verification card, and then turned into a one-point product-linked B2B script after the user selects the product.
---

# Global Hotspot Industry Impact Script

## Purpose

Turn current international hotspots and Saudi project news into verified, product-selectable topics for people doing Saudi temporary construction, camps, prefabricated buildings, logistics, procurement, or site delivery. The value is not "chasing news"; it is proving one news-to-project-to-product chain before title or script work begins.

Default first output is a Chinese news verification card, not a completed script. After the user selects a product whose fit has passed verification, title candidates must preserve that product and its verified fit reason, and the product must help fulfil the same selected impact promise in the script. 这一“新闻已选产品”分支须按 `.agents/skills/references/company-soft-placement.md` 检查同链角色和证据；东方骆驼名称仅在品牌归属与植入资格成立时自然出现，具体公司能力必须单独核验。不得暗示东方骆驼与新闻项目存在参与关系。
新闻核验卡完成产品适配后，只有品牌归属已核实且公司名称也通过植入资格检查，东方骆驼才可随产品自然展示一次；这不构成公司参与、供货或服务该新闻项目的证明，任何具体公司能力仍须单独核验。

## 适用场景

本 Skill 的适用场景以 frontmatter `description` 与下方原有任务边界为准。

进入标题或脚本生成阶段前，必须读取 `../references/generation-trigger-registry.md`，按可观察的事实关系、受众动作和证据形态选择结构与表达处理；本 Skill 只补充热点核验、产品适配和新闻风险差异。

## Core Positioning

This is an upstream verification, product-selection, topic, and title skill:

1. Start from the user-selected content category.
2. Find and verify current news.
3. Keep only news with a defensible product link.
4. Output the verification card and stop for product selection.
5. After the user selects the news and product, generate evidence-supported content directions.
6. Lock only the user-selected direction, then finalize a title and route to the matching product script skill.

It is not a product conversion skill, market panic generator, or news summary.

## Required Sources

Always browse for current hotspot facts. Use current date and absolute dates when comparing "latest", "today", "recently", or "now".

Also inspect project sources when industry framing is needed:

- `knowledge/AI资料导航索引.md`
- `knowledge/沙特临建行业认知.xlsx`
- `knowledge/钧瀚产品优势分级分类总表_v4.xlsx` and the relevant product source for a user-selected, fit-approved product; read company sources only when evaluating or using a separately qualified company mention or capability.

## Workflow

1. Verify the hotspot.
- Read `references/hotspot-sourcing.md`.
- Read `.agents/skills/references/company-soft-placement.md` before any company name or company capability enters a title or script.
   - Read `references/hotspot-ledger.md` and `content-state/hotspot-ledger.json` before looking for a topic.
   - Complete the P0 discovery pool in `hotspot-sourcing.md` first, then expand P1—P4 only as needed.
   - 直接进入当前优先级渠道，检查站内搜索、最新内容、分类页、公告页或归档；完成直接进站检查后，再用网页检索工具、其他搜索引擎、新闻聚合入口或 `site:` 查询补漏。
   - A search-tool hit is only an external-search lead. Do not report Google, Google News, X, MEED, Etimad, Bing, or another named channel as directly visited unless it was actually opened and checked.
   - Treat search results only as candidates. Open or scrape the original source before confirming its date, actor, status, and source link.
   - Confirm what happened, where, when, and what is still uncertain.
   - Never treat rumor, social media speculation, or one sensational headline as fact.

2. Test industry and product relevance.
   - Read `references/impact-filter.md`.
   - Keep only hotspots that affect Saudi projects through a concrete chain: shipping, port access, customs, insurance, material cost, energy price, approval, labor, safety, project schedule, procurement, or camp operation.
   - Require a second chain from that project effect to at least one verified product: 打包箱、移动卫浴、五金或薄壁轻钢.
   - If the product category is already locked, do not substitute news for another product. Use the feedback and evergreen fallback in the sourcing rules.

3. Output the news verification card and stop.
   - Use the exact card contract in `references/hotspot-sourcing.md`.
   - List every genuinely eligible product with a separate reason.
   - The card locks only verified facts, unsupported inferences, and product-fit reasons. It must not preselect or display a content promise, structure route, hook, conclusion, or ending.
   - 输出新闻核验卡后停止，等待用户选择新闻和产品；不得自行选择或 continue to titles.

4. Generate content directions after the user selects the news and product.
   - 用户选择新闻和产品后，才生成内容方向；核验卡阶段不得提前替用户锁定。
   - Each direction explains one evidence-supported impact point, not the entire event. Only the direction the user selects enters the temporary content state.

5. Finalize the title.
   - Read `references/title-selection.md`.
   - When the hotspot is about shipping, ports, imports, cross-border procurement, or delivery responsibility, read `.agents/skills/references/local-manufacturing-delivery-proof.md` before choosing the title.
   - 用户选定新闻和产品后，按 `$wenan-skill` 生成标题方向候选；方向满意但标题不满意时再生成 3–5 个同方向标题。
   - 新闻标题不固定句式或强制写成项目问题；标题须对象明确，并保持已核验新闻、所选产品及结合理由。

6. Write or route the script.
   - Read `references/script-pattern.md`.
   - For Saudi construction, urban development, infrastructure, industrial-city, transport, logistics, or project news, read `.agents/skills/references/b2b-topic-conversion-loop.md` before selecting the script angle. Record the project stage and reject any product link that is not naturally supported by the selected site-support, delivery, or operation impact variable.
   - Route the selected product to `$saudi-light-steel-script`, `$saudi-sanitary-unit-script`, `$saudi-product-seeding-script`, or the closest verified product route.
   - The selected product must explain the same impact point in the body; do not reserve it for a closing advertisement.
   - 用户选定且适配通过的产品必须用其已核实机制帮助完成同一判断变量与必须答案。是否出现东方骆驼名称，须另行通过品牌归属、同链角色与植入资格检查；库存、交期、生产、配送、安装、售后等具体公司能力还必须逐项核验。不得把公司名称单独追加为广告，也不得由新闻事实推导公司已参与、供货或服务该项目。

7. Prevent repetition and downgrade stale news.
   - Before drafting, use the ledger to check whether the same event or angle has already been used.
   - A 0-7 day event may be a current hotspot only after status verification. An 8-30 day event needs a material ongoing development. News older than 30 days must be treated as background, not recent news.
   - If no eligible hotspot remains, route in this order: verified official project/policy/logistics signal -> evergreen decision topic -> local-manufacturing proof topic supported by company materials.
   - Do not force a news script just because the user asks for a hotspot.

8. Output rules.
   - Before product selection, output only verified news cards or the search-feedback contract; then stop.
   - After product selection, produce title-direction options and stop at the router's title stage; refinement and final-title counts follow `$wenan-skill`.
   - The final script includes a short `资料出处` footer with the discovery report and verification sources actually used.
   - Cite only sources used for the selected hotspot facts and the industry/product chain; include source name, publication/access date when available, and link.

9. Run the professional B2B quality gate before finalizing.
   - Read `.agents/skills/references/b2b-content-quality-gate.md`.
   - Keep the verified hotspot and its one concrete industry impact above title appeal or urgency.
   - Check that the title, opening, impact chain, and ending fulfil the same core content and communication promise for procurement, delivery, camp operation, or project management.

## Hard Boundaries

- Use the selected product as a reasoned project answer, never as a hard sell based on war, disaster, sanctions, or diplomatic conflict.
- Do not write "closed", "blocked", "shutdown", "停关", "全面中断", or "项目停摆" unless current reliable sources prove that exact status.
- Do not turn "possible impact" into "has already caused".
- Do not claim price increases, delays, insurance changes, fines, or route changes without current evidence.
- Do not discuss sensitive military or diplomatic conclusions beyond what reliable sources establish.
- Do not imply the project has purchased, used, requested, or received the selected product unless the verified sources prove that exact fact.

## Reference Files

- `references/hotspot-sourcing.md`: current-news sourcing and verification rules.
- `references/impact-filter.md`: one-point industry impact filter and scoring.
- `references/title-selection.md`: title drafting and finalization rules.
- `references/script-pattern.md`: evidence-triggered hotspot-to-project routes and news risk checks.
- `.agents/skills/references/b2b-content-quality-gate.md`: shared title, B2B decision-value, logic-flow, and publishing-risk gate.
- `.agents/skills/references/local-manufacturing-delivery-proof.md`: conditional local manufacturing and delivery-responsibility differentiation rule.
- `references/hotspot-ledger.md`: candidate discovery, original-source verification, freshness, deduplication, and monitor boundaries.
- `content-state/hotspot-ledger.json`: shared local event and usage ledger; read before drafting and update after a script is finalized.
- `.agents/skills/references/b2b-topic-conversion-loop.md`: construction-news classification, temporary-facility relevance gate, account routing, evidence bridge, and post-publication review fields.
- `.agents/skills/references/expression-craft.md`: paragraph-transition and spoken-language techniques.
- `.agents/skills/references/hook-pattern-library.md`: opening-hook patterns and weak-hook list.
