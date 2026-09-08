---
name: saudi-brand-proof-script
description: Use when generating or revising Chinese B2B short-video口播 scripts that build Eastern Camel / Shenzhen Junhan brand trust through Saudi local factory, local stock, local delivery, local installation, Chinese coordination, cross-border supply-chain support, full-process team, or parent-company backing, while avoiding empty self-praise.
---

# Saudi Brand Proof Script

## Purpose

Create brand背书 scripts that let buyers infer reliability from specific, verified capabilities and responsibility evidence. A project scene is optional and may be used only when verified.

本 Skill 由用户的品牌背书任务触发，因此读取 `.agents/skills/references/company-soft-placement.md` 检查植入资格。只有公司或产品具备已核实证据，并直接帮助完成本期内容承诺时才写入；资格不成立时，说明缺失证据或提出有证据的替代角度。

## 适用场景

本 Skill 的适用场景以 frontmatter `description` 与下方原有任务边界为准。

生成或改写前，必须读取 `../references/generation-trigger-registry.md`，按可观察的事实关系、受众动作和证据形态选择结构与表达处理；本 Skill 只补充品牌能力证据、责任链和承诺边界。

## Required Sources

- Read `knowledge/AI资料导航索引.md`.
- Read `knowledge/东方骆驼公司简介.txt` for Eastern Camel / ALJMAL / Saudi local positioning and product scope.
- Read `knowledge/深圳钧瀚科技有限公司企业基础概况.docx` for Shenzhen Junhan role, overseas business, supply chain, procurement, logistics, and Saudi delivery support.
- Read `knowledge/钧瀚产品优势分级分类总表_v4.xlsx` for verified advantages, reliability level, conflict records, and brand-name mapping.
- Read `content-state/company-claim-evidence-ledger.json` and `.agents/skills/references/company-claim-evidence-ledger.md` before using any company capability, inventory, capacity, installation, delivery, or parts claim.
- Browse current sources if mentioning current Saudi policy, local-content programs, public project procurement, or market claims.

## Workflow

1. Identify one trust problem and its available evidence.
   - Local delivery uncertainty, cross-border communication, after-sales response, stock, installation coordination, quotation risk, or multi-product camp delivery.
   - If the trust problem is local Saudi delivery, do not automatically mention customs clearance. Customs documents belong to import/cross-border procurement; local delivery should focus on project documents, delivery notes, installation coordination, and handover records.

2. Select an evidence relationship.
   - Read `references/proof-pattern.md` and use the route supported by the sources: responsibility chain, capability mechanism, same-basis comparison, verified case, or boundary-first proof.
   - Do not invent a project scene or force split responsibility when neither is present in the evidence.

3. Verify the capability.
   - Read `references/fact-rules.md`.
   - Read `.agents/skills/references/local-manufacturing-delivery-proof.md`.
   - Do not invent factory size, stock quantity, team size, certifications, project cases, delivery time, or client feedback.

4. Make the evidence do the proof.
   - Use a documented mechanism, responsibility, comparison, case, or boundary rather than adjectives.

5. Output the complete script by default.
   - If the script uses company facts, factory area, stock/delivery/install capability, brand/entity names, policy/current-market claims, or other verifiable facts, append a short `资料出处` footer listing only the sources actually used.

6. Run the professional B2B quality gate before finalizing.
   - Read `.agents/skills/references/b2b-content-quality-gate.md`.
   - Audit each substantive claim against the same buyer trust promise: it must answer it, provide necessary proof, or explain why that proof changes the judgment. Natural transitions do not need to add another professional fact; a scene or mechanism is required only when the evidence needs it.
   - Do not let a stronger hook turn verified capability into a guarantee or unsupported market comparison.

## Tone

Confident but restrained. The script can be persuasive, but should feel like operational evidence, not corporate宣传片.

## Reference Files

- `references/proof-pattern.md`: evidence-triggered brand-proof routes and domain checks.
- `references/fact-rules.md`: company capability, local factory, and brand-name boundaries.
- `.agents/skills/references/b2b-content-quality-gate.md`: shared title, B2B decision-value, logic-flow, and publishing-risk gate.
- `.agents/skills/references/local-manufacturing-delivery-proof.md`: local manufacturing, stock, parts, fulfilment, and service responsibility boundaries.
- `.agents/skills/references/company-claim-evidence-ledger.md`: source binding, project-confirmation, periodic-review, and claim-extension boundaries.
- `.agents/skills/references/expression-craft.md`: paragraph-transition and spoken-language techniques.
- `.agents/skills/references/hook-pattern-library.md`: opening-hook patterns and weak-hook list.
