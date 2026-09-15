---
name: saudi-brand-proof-script
description: Use when generating or revising Chinese B2B short-video口播 scripts that build Eastern Camel / Shenzhen Junhan brand trust through Saudi local factory, local stock, local delivery, local installation, Chinese coordination, cross-border supply-chain support, full-process team, or parent-company backing, while avoiding empty self-praise.
---

# Saudi Brand Proof Script

## Purpose

Create brand背书 scripts that directly explain how the company's business, products, or services address the current topic, using user-provided business information or relevant company sources. A project scene is optional and may be used only when verified.

本 Skill 由用户的品牌背书任务触发，因此读取 `.agents/skills/references/company-soft-placement.md` 检查植入资格。按该公共规则直接使用用户业务信息，讲清公司怎样回应本篇问题；普通介绍不另设证明文件门槛。

## 适用场景

本 Skill 的适用场景以 frontmatter `description` 与下方原有任务边界为准。

生成或改写前，必须读取 `../references/generation-trigger-registry.md`，按可观察的事实关系、受众动作和证据形态选择结构与表达处理；本 Skill 只补充品牌能力证据、责任链和承诺边界。

## Required Sources

- Read `knowledge/AI资料导航索引.md` and `.agents/skills/references/company-soft-placement.md`. Use the user's ordinary business information directly under the shared rule.
- Read only the relevant original company or product material when information is missing, naming conflicts need resolution, or precise technical claims require checking.
- Use `.agents/skills/references/company-claim-evidence-ledger.md` and `content-state/company-claim-evidence-ledger.json` for historical metrics or claims actually being cited; ledger membership is not a prerequisite for ordinary business copy.
- Browse current sources if mentioning current Saudi policy, local-content programs, public project procurement, or market claims. Reuse already verified facts within their original scope.



## Workflow

1. Identify one trust problem and its available evidence.
   - Local delivery uncertainty, cross-border communication, after-sales response, stock, installation coordination, quotation risk, or multi-product camp delivery.
   - If the trust problem is local Saudi delivery, do not automatically mention customs clearance. Customs documents belong to import/cross-border procurement; local delivery should focus on project documents, delivery notes, installation coordination, and handover records.

2. Select a natural way to explain the company's contribution.
   - Read `references/proof-pattern.md`; let the information determine the explanation, without selecting from a fixed role menu or matching each issue to a preset capability.
   - Do not invent a project scene or force split responsibility when neither is present in the evidence.

3. Apply the ordinary-business and high-risk fact boundaries.
   - Read `references/fact-rules.md`.
   - Read `.agents/skills/references/local-manufacturing-delivery-proof.md`.
   - Do not invent factory size, stock quantity, team size, certifications, project cases, delivery time, or client feedback.

4. Explain what the company does for this specific issue.
   - Use a clear actor and action. Company content can appear early and continue into the explanation; do not force an audit checklist, fixed capability paragraph, or caveat section.

5. Output the complete script by default.
   - If the script uses company facts, factory area, stock/delivery/install capability, brand/entity names, policy/current-market claims, or other verifiable facts, append a short `资料出处` footer listing only the sources actually used.

6. Run the professional B2B quality gate before finalizing.
   - Read `.agents/skills/references/b2b-content-quality-gate.md`.
   - Audit each substantive claim against the same buyer trust promise: it must answer it, provide necessary proof, or explain why that proof changes the judgment. Natural transitions do not need to add another professional fact; a scene or mechanism is required only when the evidence needs it.
   - Do not let a stronger hook turn verified capability into a guarantee or unsupported market comparison.

## Tone

Direct, confident, and easy to say aloud. Marketing emphasis is allowed within the supplied facts; do not dilute business actions into assessment language or unsupported guarantees.

## Reference Files

- `references/proof-pattern.md`: evidence-triggered brand-proof routes and domain checks.
- `references/fact-rules.md`: company capability, local factory, and brand-name boundaries.
- `.agents/skills/references/b2b-content-quality-gate.md`: shared title, B2B decision-value, logic-flow, and publishing-risk gate.
- `.agents/skills/references/local-manufacturing-delivery-proof.md`: local manufacturing, stock, parts, fulfilment, and service responsibility boundaries.
- `.agents/skills/references/company-claim-evidence-ledger.md`: source binding, project-confirmation, periodic-review, and claim-extension boundaries.
- `.agents/skills/references/expression-craft.md`: paragraph-transition and spoken-language techniques.
- `.agents/skills/references/hook-pattern-library.md`: opening-hook patterns and weak-hook list.
