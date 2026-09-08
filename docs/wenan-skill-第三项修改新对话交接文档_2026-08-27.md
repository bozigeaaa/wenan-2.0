# wenan-skill 第三项修改记录（历史存档，2026-08-27）

> **状态：历史存档，非现行规则。** 本文只记录 2026-08-27 当时一次修改会话的目录、Git 状态、操作要求和阶段结论，不得作为生成、路由、输出、测试或维护指令读取。下文所有命令式表述、旧路径、旧流程、停止条件和测试结果均已失效。
>
> 现行行为只以项目根目录 `AGENTS.md`、`.agents/skills/wenan-skill/SKILL.md` 及其明确指向的共享规则为准。不得从本文恢复用户可见标题交接单、跨对话复制流程或固定输出版本。

以下内容保持原貌作为历史记录。本文件当时用于继续逐项修改 `wenan-skill`；其中第一项和第二项的状态描述仅代表当时工作现场。

## 一、实际工作目录

只使用内层独立 Git 项目：

`C:\Users\Windows\Documents\New project\wenan-skill`

不要修改外层项目：

`C:\Users\Windows\Documents\New project`

外层项目目前只把 `wenan-skill/` 识别为未跟踪文件夹。不得把整个内层项目提交进外层项目，也不得删除该文件夹。

## 二、开始前必须读取和核验

完成读取和核验前，不要修改任何文件。

先完整读取：

1. `AGENTS.md`
2. `knowledge/AI资料导航索引.md`
3. `docs/wenan-skill-完整交接文档_2026-08-14.md`
4. `.agents/skills/wenan-skill/SKILL.md`
5. `.agents/skills/global-hotspot-industry-impact-script/SKILL.md`
6. `.agents/skills/global-hotspot-industry-impact-script/references/hotspot-sourcing.md`
7. `.agents/skills/global-hotspot-industry-impact-script/references/impact-filter.md`
8. `.agents/skills/global-hotspot-industry-impact-script/references/script-pattern.md`
9. `.agents/skills/global-hotspot-industry-impact-script/references/title-selection.md`
10. `.agents/skills/global-hotspot-industry-impact-script/references/hotspot-ledger.md`
11. `.agents/skills/references/b2b-content-quality-gate.md`
12. `.agents/skills/references/b2b-topic-conversion-loop.md`
13. `tests/test_news_source_flow_rules.py`
14. `tests/test_title_flow_rules.py`
15. `tests/test_local_delivery_rules.py`
16. `tests/run_rule_tests.py`

然后执行：

- `git status --short --branch`
- `git diff`
- `git log -1 --oneline`

当前 Git diff 是用户已经确认的第一项和第二项修改，必须整体视为有效工作，不得覆盖、撤销或恢复旧规则。

如果第三项涉及 Skill、`AGENTS.md` 或其他供 AI 使用的规则文档，先完整读取并使用本机的 `$writing-for-agents`；涉及 Skill 结构时同时读取对应 Skill 编写规范。

## 三、当前 Git 状态

- 内层项目分支：`main`
- 最新提交：`ad861a7 refactor-wenan-skill-routing`
- 当前分支仍与 `origin/main` 指向同一已提交版本。
- 工作区同时保留第一项和第二项产生的未提交修改。
- 不要因为工作区不干净而重置、回滚、覆盖或清理文件。
- 外层项目当前仍只显示 `?? wenan-skill/`，没有发现两个项目副本混用。

## 四、第一项已确认：新闻搜集、核验与产品选择

现行流程：

`选择文案大类 → 搜集并复核新闻 → 判断产品适配 → 输出新闻核验卡 → 用户选择新闻和产品 → 标题方向候选 → 标题交接单 → 明确带产品的完整文案`

必须保持的摘要：

1. 第一优先发现渠道为 Google / Google News、X、MEED、Etimad；发现渠道不等于事实证明来源。
2. 新闻必须回到原链接、官方公告或独立来源复核，同时通过真实性和产品适配，才能生成新闻核验卡。
3. 新闻核验卡须包含发布渠道、原链接、原标题及直译、发布时间、摘要、解析、复核来源、可结合产品及逐项理由、核验结论。
4. 可选择产品只有打包箱、移动卫浴、五金、薄壁轻钢，由用户选择；系统不得自行选择或静默更换。
5. 用户已选产品大类时，只展示适配该产品的新闻；其他产品线索只能简要提示。
6. 没有合格新闻时，反馈真实检索日期、实际渠道、方向、结果、未采用原因和其他产品线索；只写真正检索过的渠道。
7. 登录受限时可请用户自行登录或授权已登录会话，不得索取密码、验证码或 Token；未进入渠道应写“因登录限制未完成检索”。
8. 用户选定新闻和产品后，标题和完整文案必须保持该产品及结合理由；产品必须参与解决同一个项目内容，不能退回纯新闻播报或只在结尾追加产品名。
9. 公司名称是否出现仍按公司证据台账判断，与产品必须出现是两套规则。

第一项详细规则的唯一权威来源：

`.agents/skills/global-hotspot-industry-impact-script/references/hotspot-sourcing.md`

`AGENTS.md` 只保留入口和总原则，不要把全部渠道及核验卡字段再次复制进去。

## 五、第二项已确认：标题生成与 0–3 秒钩子

### 1. 标题流程与数量

- 原“细分议题”和首轮“标题候选”合并为一个 `标题方向候选` 阶段。
- 标题方向默认生成 6 个；只有确有足够不同且可成稿的方向时最多 8 个，不为凑数加入无关方向。
- 用户对方向和标题都满意时，直接生成标题交接单。
- 用户认可方向但不满意标题表达时，生成 3–5 个同方向短标题，只改变表达，不更换方向。
- 最终定稿只输出 1 个标题。
- 旧的“10 个选题方向”“12 个标题候选”等数量口径已经删除。

### 2. 标题长度、句式和可读性

- 抖音标题默认控制在 18 个字符以内，必要时最多 22 个字符；这是项目内部编辑标准，不宣称为抖音官方限制。
- 标题要短、顺口、常用词优先，避免修饰语堆叠、倒装和一条标题塞入多项内容。
- 一条标题只保留一个清楚的核心内容，但不限制标题句式；疑问、陈述、判断、反差、场景或其他自然句式都可以使用。
- 标题必须让观众立即识别行业对象、目标受众或具体场景。
- `交付`、`成本`、`风险`、`配置`、`进度` 等抽象词不能单独承担语境；产品名不出现时，要用沙特工地、工程营地、临建设施、项目采购等具体范围补足。

### 3. 新闻标题与产品关系

- 新闻标题只能建立在用户已经选定的新闻核验卡和产品上；用户直接要求新闻标题时也不得绕过新闻核验卡。
- 新闻标题不设置“新闻钩子＋项目问题”等固定结构，也不强制写成项目问题。
- 标题可以突出新闻、变化、反差、受众处境、产品场景或项目判断中的任一重点。
- 产品名称不强制直接写进标题，但标题方向必须保持用户选定产品及结合理由。
- 不得暗示新闻项目已经采购、使用、要求或收到所选产品，除非核验来源明确证明。
- 不得静默更换产品，也不能写成与所选产品无关的纯新闻评论。
- 对 8–30 天前的新闻仍需保留必要时间语境，不能伪装成刚刚发生。

### 4. 传播张力与事实边界

- 允许使用悬念、反差、风险感和情绪化口语，可以有适度“标题党”张力。
- 标题不必写完整证据链，可以省略不改变事实性质的背景。
- 具体事件、主体、数字和确定性结果仍须有依据。
- 可以放大关注点，但不能反转或编造事实；不能把“可能发生”写成“已经发生”。
- 标题制造的期待必须由正文兑现，不能借无关热点制造产品机会感。
- 原有冗长禁用表达清单已收口为少量事实红线，不再过度压制传播性。

### 5. 标题与 0–3 秒开篇钩子

- 标题、开篇钩子和正文须保持同一个核心内容和传播承诺，但不要求使用相同文字或句式。
- 标题负责点击和快速识别；钩子负责把观众带入具体场景、变化或反差。
- 钩子不能只是重复标题，可以补充标题因长度限制而省略的背景、对象或产品。
- 钩子不能依赖标题或封面补充语境；第一句必须出现行业对象、目标受众或具体场景。
- 即使观众没有看到标题，也应立即知道内容属于哪个行业和场景。
- 钩子可以比标题更具体、更有张力，但不能更换核心内容、产品方向或编造结果。
- 已删除“正文必须回答标题提出的问题”“推进标题答案”等会把标题限定成问题句或判断句的旧口径，统一改为“兑现标题承诺的核心内容”。

第二项规则按职责分布：

- 全局标题长度、可读性、张力和钩子关系：`.agents/skills/references/b2b-content-quality-gate.md`
- 新闻标题及产品保持规则：`.agents/skills/global-hotspot-industry-impact-script/references/title-selection.md`
- 标题方向阶段和跨对话交接：`.agents/skills/wenan-skill/SKILL.md`
- 新闻选择进入标题方向的衔接：`.agents/skills/references/b2b-topic-conversion-loop.md`
- 项目级入口和总原则：`AGENTS.md`

不要把某一文件中的详细规则无差别复制到所有入口文件。

## 六、来源追溯结论

用户曾询问截图中的“四、明确禁用的标题表达”是什么时候、由谁写入。核验结论：

- 该完整标题及清单不是仓库中的原文，而是上一对话中助手根据多份现行规则临时归纳的展示内容。
- 底层相关规则来自多个历史提交，不能把截图中的整段文字归到某一次 Git 提交或某一位仓库作者名下。
- 后续如再次追溯，必须区分“仓库原文”“助手归纳”和“用户确认后的新规则”。

## 七、当前累计修改文件

当前 Git 工作区中的已修改文件包括：

- `AGENTS.md`
- `.agents/skills/wenan-skill/SKILL.md`
- `.agents/skills/global-hotspot-industry-impact-script/SKILL.md`
- `.agents/skills/global-hotspot-industry-impact-script/agents/openai.yaml`
- `.agents/skills/global-hotspot-industry-impact-script/references/hotspot-ledger.md`
- `.agents/skills/global-hotspot-industry-impact-script/references/hotspot-sourcing.md`
- `.agents/skills/global-hotspot-industry-impact-script/references/impact-filter.md`
- `.agents/skills/global-hotspot-industry-impact-script/references/script-pattern.md`
- `.agents/skills/global-hotspot-industry-impact-script/references/title-selection.md`
- `.agents/skills/references/b2b-content-quality-gate.md`
- `.agents/skills/references/b2b-topic-conversion-loop.md`
- `docs/wenan-skill-完整交接文档_2026-08-14.md`
- `tests/test_local_delivery_rules.py`

当前新增但尚未提交：

- `docs/superpowers/plans/2026-08-26-news-source-verification-flow.md`
- `tests/run_rule_tests.py`
- `tests/test_news_source_flow_rules.py`
- `tests/test_title_flow_rules.py`
- `docs/wenan-skill-第三项修改新对话交接文档_2026-08-27.md`

桌面两份初始化文件不属于 Git 项目，本次第二项标题修改没有更新它们。第三项不得擅自修改桌面文件：

- `C:\Users\Windows\Desktop\文案新对话直接发.txt`
- `C:\Users\Windows\Desktop\标题新对话 直接发.txt`

## 八、当前验证结果

第二项完成后的最新验证结果：

- 规则测试：`27 passed, 0 failed`
- `$wenan-skill` 格式校验：通过
- `$global-hotspot-industry-impact-script` 格式校验：通过
- 旧标题口径残留扫描：无匹配
- `git diff --check`：通过，仅出现 Windows 的 LF/CRLF 提示

验证使用的规则测试命令：

`C:\Users\Windows\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe tests\run_rule_tests.py`

Skill 校验脚本需要 PyYAML 和 UTF-8 模式。当前仅用于校验的临时依赖位于：

`C:\Users\Windows\AppData\Local\Temp\codex-wenan-validator-pyyaml`

该目录不属于 Git 项目。第三项修改完成后必须重新运行全部检查，不能沿用本交接文档中的旧结果。

## 九、第三项修改的执行方式

第三项具体内容尚未提供。

读取完成后先向用户简短报告：

1. 当前实际工作目录。
2. 当前 Git 分支和最新提交。
3. 已读取的规则文件。
4. 已识别的第一项新闻规则和第二项标题规则未提交修改。
5. 是否发现两个项目副本混用。
6. 是否发现前两项规则存在意外冲突、缺失或旧口径残留。

报告后停止，等待用户说明第三项要修改的内容。

用户提出第三项后，先完成：

1. 复述用户想解决的问题。
2. 找出当前规则分别写在哪些文件。
3. 判断应该新增、修改还是覆盖现有规则。
4. 说明是否会与第一项新闻规则、第二项标题规则或其他现行流程冲突。
5. 给出整合后的拟修改内容，让用户完整确认。

用户明确说“确认修改”以前，只分析和提出方案，不修改文件。

用户确认后，只修改第三项直接相关的文件；保留第一项和第二项已经确认的规则，不顺便重构其他内容。

不要主动提交、推送 GitHub、删除文件、修改桌面初始化文件、生成标题或生成文案。
