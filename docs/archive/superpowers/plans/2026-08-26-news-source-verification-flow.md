# 新闻来源、核验卡与产品选择实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 在保留“大类优先”流程的前提下，把新闻发现、真实性复核、产品适配、用户选品和无结果反馈固化为可验证的单一流程。

**Architecture:** `AGENTS.md` 只保存全局不变量；`hotspot-sourcing.md` 是渠道、核验卡和访问反馈的详细主来源；热点 Skill 与 `wenan-skill` 只保存调用顺序和阶段停止条件；产品关联判断由 `impact-filter.md` 与 `b2b-topic-conversion-loop.md` 共同承担。交接文档与桌面模板只记录入口和状态，不复制完整规则。

**Tech Stack:** Markdown agent instructions, Python `pytest`, Codex skill validator.

## Global Constraints

- 大类选择保持第一步，新闻检索不能提前到大类之前。
- P0 只包含 Google / Google News、X、MEED、Etimad。
- 新闻必须同时通过真实性复核与产品适配，才输出核验卡。
- 核验卡不包含单独的“证据边界”字段。
- 进入核验卡并被选中的新闻，后续文案必须明确带出用户选定产品。
- 登录受限时请求用户自行登录或授权现有会话，不索取凭证。
- 仅修改内层 `wenan-skill` 项目，不提交外层未跟踪副本。

---

### Task 1: 新闻规则合同测试

**Files:**
- Create: `tests/test_news_source_flow_rules.py`

**Interfaces:**
- Consumes: 当前 Markdown 规则文件。
- Produces: 对来源优先级、核验卡、产品选择、无结果反馈和登录边界的回归保护。

- [ ] **Step 1: 写失败测试**

测试应验证：P0 精确为四类渠道；核验卡字段完整且没有“证据边界”；产品多选后必须等待用户选择；产品大类锁定时不自动换品；无结果反馈只列实际检索渠道；登录受限不索取凭证；旧的“热点稿默认不带产品”不再生效。

- [ ] **Step 2: 运行测试确认 RED**

Run: `pytest tests/test_news_source_flow_rules.py -q`

Expected: 因正式规则尚未包含新流程而失败。

### Task 2: 全局与详细新闻规则

**Files:**
- Modify: `AGENTS.md`
- Modify: `.agents/skills/global-hotspot-industry-impact-script/references/hotspot-sourcing.md`
- Modify: `.agents/skills/global-hotspot-industry-impact-script/references/impact-filter.md`
- Modify: `.agents/skills/references/b2b-topic-conversion-loop.md`

**Interfaces:**
- Consumes: 用户确认的渠道层级、核验卡字段和产品范围。
- Produces: 一个全局入口和一个详细主来源。

- [ ] **Step 1: 在 `AGENTS.md` 写全局不变量和触发指针**
- [ ] **Step 2: 在 `hotspot-sourcing.md` 维护完整渠道层级、核验卡、无结果反馈和访问授权**
- [ ] **Step 3: 在两个影响筛选文件中维护产品适配与大类锁定逻辑**

### Task 3: 路由与阶段边界

**Files:**
- Modify: `.agents/skills/global-hotspot-industry-impact-script/SKILL.md`
- Modify: `.agents/skills/wenan-skill/SKILL.md`

**Interfaces:**
- Consumes: `hotspot-sourcing.md` 与产品适配规则。
- Produces: `选大类 → 核验新闻 → 用户选新闻/产品 → 标题 → 交接单 → 带产品文案`。

- [ ] **Step 1: 删除热点 Skill 的默认纯新闻成稿路径**
- [ ] **Step 2: 加入核验卡输出后的强制停止与用户选品**
- [ ] **Step 3: 在入口 Skill 锁定新闻、产品和后续标题/文案范围**

### Task 4: 交接和桌面入口同步

**Files:**
- Modify: `docs/wenan-skill-完整交接文档_2026-08-14.md`
- Modify outside repository: `C:\Users\Windows\Desktop\标题新对话 直接发.txt`
- Modify outside repository: `C:\Users\Windows\Desktop\文案新对话直接发.txt`

**Interfaces:**
- Consumes: 正式规则文件。
- Produces: 不复制完整细则的启动入口与维护记录。

- [ ] **Step 1: 在交接文档记录本次变更并指向正式规则**
- [ ] **Step 2: 标题初始化同步新闻核验卡和选品阶段**
- [ ] **Step 3: 文案初始化锁定交接单已选新闻和产品**

### Task 5: 验证

**Files:**
- Test: `tests/test_news_source_flow_rules.py`
- Test: `tests/test_local_delivery_rules.py`

**Interfaces:**
- Consumes: 所有修改后的规则。
- Produces: 测试、Skill 格式和工作区差异证据。

- [ ] **Step 1: 运行新闻规则测试确认 GREEN**
- [ ] **Step 2: 运行全量 `pytest -q`**
- [ ] **Step 3: 对三个修改过的 Skill 运行 `quick_validate.py`**
- [ ] **Step 4: 检查 `git diff --check`、`git diff --stat` 和 `git status --short`**
