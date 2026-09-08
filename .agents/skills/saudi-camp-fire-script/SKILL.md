---
name: saudi-camp-fire-script
description: Use when generating or revising Chinese short-video口播 scripts for Saudi self-built camps, temporary camps, prefab houses, modular houses, and site accommodation when the topic involves fire safety, SBC 801, Civil Defense, Salamah, fire-resistance, fire separation, egress, alarm/firefighting systems, fire-rated materials, or fire inspection.
---

# Saudi Camp Fire Script

## Purpose

Create professional Chinese short-video口播 scripts for Saudi camp fire-safety topics. The target audience is industry professionals: Chinese EPC/general contractor project managers, procurement teams, and camp operators working in Saudi Arabia.

The script must feel like practical expert knowledge, not a generic advertisement. Each script fulfills one fire-safety content promise, which may be a judgment, explanation, comparison, responsibility boundary, inspection boundary, or site process. Eastern Camel products or capabilities may appear only when a placement trigger exists and their fire-safety role and supporting evidence pass the placement gate.

## 适用场景

本 Skill 的适用场景以 frontmatter `description` 与下方原有任务边界为准。

生成或改写前，必须读取 `../references/generation-trigger-registry.md`，按可观察的事实关系、受众动作和证据形态选择结构与表达处理；本 Skill 只补充消防法规、审批路径、材料证据和高风险承诺边界。

## Required Local Sources

Before writing or revising a script, inspect the project navigation file when available:

- `knowledge/AI资料导航索引.md`

For Saudi fire-safety topics, prioritize these source files:

- `沙特临建行业认知.xlsx` for SBC 801, Civil Defense / Salamah, Saudi compliance, and topic boundaries.
- `钧瀚产品优势分级分类总表_v4.xlsx` for advantages, conflict records, and information reliability.
- `拼装房屋产品介绍.txt` for prefab house / packing house product facts.
- `薄壁轻钢房屋产品介绍.txt` when the requested topic is light steel housing.
- `东方骆驼公司简介.txt` and `深圳钧瀚科技有限公司企业基础概况.docx` when checking or using a company or product placement.

If a requested fact is not in the local sources, browse official or reliable sources before using it. If it remains unsupported, omit it from the script, obtain supporting evidence, narrow the content promise, or stop; a confirmation note does not make the claim publishable.

## Core Rule

One video fulfills one fire-safety content promise. Do not turn one script into a full SBC 801 overview.

仅当 `../references/generation-trigger-registry.md` 打开 `placement_eligibility` 条件分支时，才读取 `.agents/skills/references/company-soft-placement.md` 并检查植入资格。公司或产品还须有已核实的消防相关角色，并在同一判断变量的答案中承担必要作用；资格不成立就不植入，不用无关能力填补。

Acceptable single points include:

- Space use and fire-risk zoning.
- Fire-resistance and fire separation.
- Material/test/report/BOQ/site consistency.
- Firestopping at joints and penetrations.
- Egress width, exit path, and signage.
- Alarm, extinguisher, fire water, or emergency lighting configuration.
- Civil Defense inspection logic.

Read `references/fire-topic-library.md` when choosing or splitting topics.

## Workflow

1. Establish the content promise.
   - Execute the semantic-promise and answerability stages in `../references/generation-trigger-registry.md`.
   - Keep one fire-safety judgment variable and only the verified material needed to fulfill it. Use the semantic form that fits the task; treat any final line as optional until the body has fulfilled the promise.
   - If the user gives multiple independent promises, split them into a series and write only the requested one.

2. Apply the company/product answer gate only when triggered.
   - Follow the observable trigger conditions in `../references/generation-trigger-registry.md`. When the registry does not open this branch, skip the detailed placement check and do not add a company or product by default.
   - 对公司与产品分别执行植入资格、同链角色和证据检查；只有通过者才能写入正文。
   - 公司、产品、工厂、库存、本地交付、`15000㎡` 等具体事实仍须按资料和证据边界核验；没有帮助回答同一判断变量的事实就不写。
   - 如果公司或产品候选无法参与兑现内容承诺，直接取消该植入；不得仅为保留植入转换角度或增加无关痛点。
   - Factory area and `15000㎡` are only relevant when the point is local manufacturing scale, production capacity, or delivery certainty. Do not use them as a generic credibility close.

3. Verify the fact level.
   - Separate confirmed facts, likely claims, and high-risk claims.
   - High-risk claims include exact fire-resistance minutes, temperatures, material densities, UL/ASTM numbers, "must", "prohibited", "停工拆除", "绝对不能", and competitor accusations.
   - Use only confirmed high-risk facts. If evidence remains insufficient, omit the claim from the script, obtain supporting evidence, narrow the content promise, or stop. Do not repair missing evidence with softer wording or a confirmation marker.
   - Read `references/fact-check-rules.md`.

4. Build the script around the verified fire-safety content promise.
   - Use the information relationship that best fulfills the promise: requirement, mechanism, comparison, sequence, responsibility, or scene can lead. Any qualified company or product content that is used belongs inside that same explanation; do not force a common skeleton or reserve it for a closing advertisement.

5. Keep the tone.
   - Chinese口播, direct and easy to listen to.
   - Professional, concrete, and slightly sharp.
   - Avoid academic wording unless immediately translated into site language.
   - Let sentence length follow meaning and speaking breath. Express technical judgments through concrete subjects, actions, conditions, and consequences.

6. Self-check before returning.
   - The draft fulfills one semantic content promise; naming a standard without explaining its relevance is insufficient.
   - Every substantive product, company, and factory claim participates in the same decision variable and stays within its evidence boundary.
   - When the script uses regulations, fire-resistance data, standards, test reports, product parameters, or current external facts, append a short `资料出处` footer listing only the sources actually used.
   - Exact numbers and certifications are confirmed, the audience is not portrayed as naive, and no competitor wrongdoing is invented.
   - Read `.agents/skills/references/b2b-content-quality-gate.md` and validate that title, opening, body, and any final line fulfill the same verified fire-safety promise.
   - Any hook stays within the verified decision, inspection, or configuration boundary rather than implying an unsupported stop-work, fine, rectification, or approval outcome.

## Output Format

Follow the project-wide output rules in `AGENTS.md` and `$wenan-skill`: return one title, one final spoken script, and only the required `资料出处`. Keep internal self-check fields private unless the user explicitly requests a storyboard, table, diagnosis, self-check, or version comparison.

If the user only asks for a revision, keep the output shorter and include only the revised script plus a brief note about what changed.

## Hard Boundaries

- Do not say "used our product and it will definitely pass Civil Defense".
- Do not invent exact SBC 801 clause numbers, minutes, temperatures, material density, or certification reports.
- Do not accuse the market of common fraud or malicious material substitution unless the user provides evidence.
- When evidence does not support competitor wrongdoing, compare only the verified configuration, evidence, responsibility, or application boundaries; do not create an exposé frame.
- Use exclusivity or standard-answer language only when an authoritative source establishes that exclusivity. Otherwise state the supported compliance direction and applicable conditions without upgrading it to a unique solution.
- Do not write "清关资料" as part of a fire approval package unless the topic is imported goods or cross-border procurement. For local delivery or local manufacturing, use "消防资料、产品规格书、材料性能资料、结构图纸/计算、BOQ、安装方法书、交付验收记录".
- Do not say "规范要求" without naming the relevant code/approval path or explaining whether it is a Civil Defense, SBC 801, owner, consultant, or drawing requirement.
- Do not use "普通填充" without explaining what it means and why it matters.
- Do not portray project professionals as unaware that fire-rated materials matter unless a verified case supports that portrayal. Identify the actual information gap for the selected content promise.
- Do not compare by insulting Saudi local contractors, Chinese contractors, or competitors.
- Do not write a broad checklist unless the user explicitly asks for a series overview.
- Do not use Eastern Camel, local factory, or `15000㎡` as a generic ending; use them inside the answer only when they directly answer this script's one point.
- End when the last necessary fact, judgment, or boundary fulfills the content promise. Add a CTA only when the user explicitly requests one or a directly related audience task remains unfinished.

## Reference Files

- `references/script-pattern.md`: evidence-triggered fire-safety routes and high-risk claim checks.
- `references/fact-check-rules.md`: how to handle high-risk fire-safety facts.
- `references/fire-topic-library.md`: single-point topic library for future scripts.
- `.agents/skills/references/b2b-content-quality-gate.md`: shared title, B2B decision-value, logic-flow, and publishing-risk gate.
- `.agents/skills/references/expression-craft.md`: paragraph-transition and spoken-language techniques.
- `.agents/skills/references/hook-pattern-library.md`: opening-hook patterns and weak-hook list.
