# Impact Filter

## One-Point Rule

One script explains one impact point. Do not cover all possible consequences of a hotspot.

Good single points:

- Delivery time uncertainty.
- Freight/insurance cost pressure.
- Port and route planning.
- Procurement lead time.
- Material availability.
- Energy cost sensitivity.
- Camp expansion timing.
- Compliance or safety attention.

Bad combined point:

- "This event affects freight, energy, labor, customs, local factories, insurance, all materials, and project schedules."

## Industry Relevance Test

Before filtering, inherit the locked semantic promise (语义承诺): object and context, decision action or variable, the answer this script must provide, evidence strength and applicability boundary, and adjacent issues that cannot substitute for this one.

Keep a hotspot only if it has a clear evidence relationship (证据关系):

```text
verified hotspot fact
-> operational pathway
-> Saudi project/camp/temporary construction effect
-> how that evidence changes or supports the locked answer, strength, or boundary
```

The final link is determined by the current semantic promise and available evidence. It may support a judgment, a checkable basis, an applicability boundary, or decision-relevant causal understanding. It is not a default takeaway. This filter does not prescribe a question form, checklist, or paragraph structure (不规定问题形式、清单或段落).

Reject if:

- The event is only entertainment, celebrity, or general political drama with no project chain.
- The link to Saudi construction is forced.
- The only usable angle would be product promotion.
- The event shares a project, product, location, or industry keyword with the topic but does not change or support the locked answer.

## 产品适配硬门

适配产品范围仅限打包箱、移动卫浴、五金、薄壁轻钢。产品名称只限定核验范围，不构成默认选品、标题角度或正文结构。

本项目的新闻候选还必须形成：

```text
已核实新闻事实
→ 具体项目动作、采购动作、施工阶段、现场条件或交付需求
→ 产品如何为同一语义承诺提供答案、证据或适用边界
```

只有这条链成立，新闻才进入核验卡。项目规模大、同属建筑行业、出现相近产品词或发生在沙特，均不能单独证明产品适配。

多个产品适配时，逐项写明结合理由，输出核验卡后等待用户选择；系统不得自行选择，也不得把全部适配产品默认塞进一条文案。用户选定后锁定该产品；只有用户明确选择多个产品时，且它们共同帮助完成同一判断变量和必须答案，才可按整体营地或配套方案处理。

产品大类已锁定时，只展示与该产品适配的新闻。其他产品方向只作简短提示，不展开核验卡、不得自动替换当前方向。用户保持原产品时转入该产品的常青议题；用户明确切换后才重新进入新闻核验流程。

具体五金品类必须回到知识库逐项核实。资料只能证明泛化“五金业务”时，不得自行补写某种锚栓、连接件、工具或耗材。

## Impact Score

Internally score 0-2 for each:

- Saudi relevance.
- Construction/camp relevance.
- Operational clarity.
- Audience usefulness.
- Fact reliability.

Use only topics scoring 7 or higher out of 10 and passing the product-fit gate. If no topic qualifies, use the search-feedback contract in `hotspot-sourcing.md` instead of forcing one.

## Audience Fit

Choose the audience from the responsibility actually affected by the verified operational pathway. Audience usefulness is judged against the locked answer, not against a universal project-person takeaway. Do not turn every hotspot into a reminder to recheck something, and do not infer an output question, checklist, or paragraph sequence from an audience label.
