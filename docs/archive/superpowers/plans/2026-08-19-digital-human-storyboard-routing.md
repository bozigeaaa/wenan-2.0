# 数字人口播分镜路由 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 让 `$wenan-skill` 在同一对话收到“生成分镜脚本”等明确请求时，自动读取最近一版已确认文案并调用独立分镜 Skill，输出固定的数字人口播分镜表。

**Architecture:** 新建 `digital-human-storyboard` 专项 Skill，负责输入校验、中文分段、三语字幕、数字人画面建议与后续素材库边界。`wenan-skill` 仅作为单一入口路由器，在口语化改写和产品／科普路由之前识别分镜请求；`AGENTS.md` 与交接文档记录同一对话的触发方式。项目现有 Python 测试通过断言关键技能文本和路由约束，防止将来规则回退。

**Tech Stack:** Markdown Skill instructions、OpenAI Skill UI YAML、Python `pytest` 文本契约测试。

## Global Constraints

- 使用 `$wenan-skill` 作为唯一用户入口；用户无需记忆或手动调用专项 Skill。
- 同一对话中“生成分镜脚本”默认处理最近一版已确认的第二步定稿；多版定稿无法判断时只要求指定版本。
- 分镜只拆分定稿，不选题、不重写、不口语化改写、不补充事实。
- 成功结果只输出：`镜号｜时间码｜中文字幕｜英文字幕｜阿拉伯语字幕｜分镜｜画面／素材建议`。
- 时间码使用 `00:00.0–00:04.2`，按 0.1 秒连续且无重叠；没有中文原声时按每秒 4 个中文字符等值和每个语义停顿 0.3 秒预估。
- 中文字幕按时间合并后必须完整覆盖定稿，不漏字、不增字、不调换锁定事实、条件或结论。
- 无素材库时不得编造素材编号；有素材库但缺已审核素材卡或最近两条发布记录时，只能写“待补拍”或“中性示意图替代”。
- 不创建素材库、使用日志、视频、配音、字幕文件或剪辑工程文件。
- 本计划中的提交仅限本地 Git 提交，不执行 `git push`。

---

### Task 1: 新建分镜专项 Skill 与文本契约测试

**Files:**
- Create: `.agents/skills/digital-human-storyboard/SKILL.md`
- Create: `.agents/skills/digital-human-storyboard/agents/openai.yaml`
- Modify: `tests/test_local_delivery_rules.py`

**Interfaces:**
- Consumes: `AGENTS.md`、第二步确认后的标题、中文正文和资料出处（如有）。
- Produces: 固定七列 Markdown 分镜表，或仅返回阻塞说明。
- Used by: `$wenan-skill` 的新增分镜路由。

- [ ] **Step 1: 写入失败的专项 Skill 契约测试**

在 `tests/test_local_delivery_rules.py` 的路径常量区增加：

```python
STORYBOARD_SKILL = PROJECT_ROOT / ".agents/skills/digital-human-storyboard/SKILL.md"
STORYBOARD_AGENT = PROJECT_ROOT / ".agents/skills/digital-human-storyboard/agents/openai.yaml"
```

并在文件末尾增加：

```python
def test_digital_human_storyboard_skill_has_the_confirmed_contract() -> None:
    assert STORYBOARD_SKILL.exists(), "Missing digital-human storyboard skill"
    assert STORYBOARD_AGENT.exists(), "Missing digital-human storyboard UI metadata"

    storyboard = read(STORYBOARD_SKILL)
    agent = read(STORYBOARD_AGENT)

    assert_contains(storyboard, "不重新选题、不重写文案", "storyboard no-rewrite boundary")
    assert_contains(storyboard, "镜号｜时间码｜中文字幕｜英文字幕｜阿拉伯语字幕｜分镜｜画面／素材建议", "fixed storyboard table")
    assert_contains(storyboard, "每秒 4 个中文字符", "storyboard timing estimate")
    assert_contains(storyboard, "不漏字、不增字", "Chinese subtitle coverage")
    assert_contains(storyboard, "最近两条已发布视频", "asset repetition boundary")
    assert_contains(storyboard, "待补拍", "asset fallback")
    assert_contains(agent, "分镜", "storyboard UI label")
```

- [ ] **Step 2: 运行测试，确认在文件缺失时失败**

Run:

```powershell
python -m pytest tests/test_local_delivery_rules.py::test_digital_human_storyboard_skill_has_the_confirmed_contract -v
```

Expected: FAIL，提示 `Missing digital-human storyboard skill`。

- [ ] **Step 3: 创建最小可用的分镜 Skill**

创建 `.agents/skills/digital-human-storyboard/SKILL.md`，并写入以下职责与边界：

```markdown
---
name: digital-human-storyboard
description: Use when a confirmed Chinese B2B short-video script needs a digital-human storyboard with Chinese, English and Arabic subtitle text, shot guidance and visual suggestions.
---

# 数字人口播分镜 Skill

## 输入

只处理第二步确认后的标题、完整中文口播正文和资料出处（如有）。
若只有标题、未确认草稿、高风险事实缺来源或来源与正文直接冲突，只输出阻塞说明。

## 不得做的事

不重新选题、不重写文案、不口语化改写、不新增事实、项目现场、库存、交付或客户案例。

## 输出

成功时只输出：
镜号｜时间码｜中文字幕｜英文字幕｜阿拉伯语字幕｜分镜｜画面／素材建议
```

在同一文件加入以下明确规则：

```markdown
## 时间与中文字幕

- 时间码使用 `00:00.0–00:04.2`，精确到 0.1 秒并连续无重叠。
- 无中文原声时，按每秒 4 个中文字符等值和每个语义停顿 0.3 秒预估。
- 每行中文仅对应本行时间段；非空行按时间合并后完整覆盖定稿，不漏字、不增字、不调换锁定事实、条件或结论。

## 翻译与画面

- 英文和阿拉伯语不改变数字、型号、公司名、法规缩写、条件、比较、承诺或其他锁定事实。
- 数字人是主叙述者；素材只用于解释、证明或换节奏。
- 没有可用证据时写“中性示意图”或“待补拍”，不得编造素材编号、项目现场、库存、交付或客户案例。

## 素材库边界

- 素材库未建立时只写画面描述。
- 素材库建立后，只有同时取得已审核素材卡和最近两条已发布视频的使用记录时，才可调用素材编号。
- 调用素材时避开最近两条已发布视频已经使用的片段。
```

创建 `.agents/skills/digital-human-storyboard/agents/openai.yaml`：

```yaml
interface:
  display_name: "数字人分镜 Skill"
  short_description: "将确认的口播定稿拆成数字人分镜表与三语字幕"
  default_prompt: "请使用 $digital-human-storyboard，将已确认的口播文案生成分镜表。"
```

- [ ] **Step 4: 运行测试，确认专项 Skill 契约通过**

Run:

```powershell
python -m pytest tests/test_local_delivery_rules.py::test_digital_human_storyboard_skill_has_the_confirmed_contract -v
```

Expected: PASS。

- [ ] **Step 5: 本地提交此独立交付物**

```powershell
git add .agents/skills/digital-human-storyboard/SKILL.md .agents/skills/digital-human-storyboard/agents/openai.yaml tests/test_local_delivery_rules.py
git commit -m "feat: add digital human storyboard skill"
```

不要执行 `git push`。

### Task 2: 将分镜路由预置到统一入口

**Files:**
- Modify: `.agents/skills/wenan-skill/SKILL.md`
- Modify: `AGENTS.md`
- Modify: `docs/wenan-skill-完整交接文档_2026-08-14.md`
- Modify: `tests/test_local_delivery_rules.py`

**Interfaces:**
- Consumes: 用户的明确分镜请求和同一对话最近一版已确认文案。
- Produces: `$digital-human-storyboard` 路由指令，或多版定稿时的版本确认说明。
- Depends on: Task 1 的 `.agents/skills/digital-human-storyboard/SKILL.md`。

- [ ] **Step 1: 写入失败的统一入口路由测试**

在 `tests/test_local_delivery_rules.py` 增加：

```python
def test_wenan_router_prioritizes_confirmed_script_storyboarding() -> None:
    router = read(WENAN_ROUTER)
    project_rules = read(PROJECT_RULES)
    handoff = read(HANDOFF_DOCUMENT)

    assert_contains(router, "$digital-human-storyboard", "storyboard route")
    assert_contains(router, "生成分镜脚本", "direct storyboard command")
    assert_contains(router, "最近一版已确认", "latest-confirmed-script rule")
    assert_contains(router, "不调用口语化改写", "storyboard route priority")
    assert_contains(project_rules, "数字人分镜", "project storyboard workflow")
    assert_contains(project_rules, "生成分镜脚本", "project direct storyboard command")
    assert_contains(handoff, "生成分镜脚本", "handoff direct storyboard command")
```

- [ ] **Step 2: 运行测试，确认路由规则尚未存在时失败**

Run:

```powershell
python -m pytest tests/test_local_delivery_rules.py::test_wenan_router_prioritizes_confirmed_script_storyboarding -v
```

Expected: FAIL，提示缺少 `storyboard route`。

- [ ] **Step 3: 修改统一入口、项目规则与交接文档**

在 `.agents/skills/wenan-skill/SKILL.md` 的路由表最前面增加分镜行，触发词包含“生成分镜脚本、分镜、拆分分镜、镜头表、剪辑表、字幕表、画面建议”，并指定 `$digital-human-storyboard`。在 `Required Decisions` 前增加优先级说明：同一对话直接说“生成分镜脚本”时，使用最近一版已确认的第二步定稿；多版定稿无法判断时只要求指定版本；分镜路由不调用口语化改写、不重写产品或科普文案。

在 `AGENTS.md` 的内容类型判断中新增“数字人分镜”条目，并在默认工作流后补充：确认文案后，用户在同一对话发送“生成分镜脚本”即可进入第三步；分镜只输出固定七列表或阻塞说明。

在 `docs/wenan-skill-完整交接文档_2026-08-14.md` 的新对话／日常使用说明后补充：分镜不要求新窗口；第二步确认后可在同一对话直接输入“生成分镜脚本”，默认使用最近确认版本。

- [ ] **Step 4: 运行路由测试及完整测试文件**

Run:

```powershell
python -m pytest tests/test_local_delivery_rules.py::test_wenan_router_prioritizes_confirmed_script_storyboarding -v
python -m pytest tests/test_local_delivery_rules.py -v
```

Expected: 两条命令均 PASS。

- [ ] **Step 5: 本地提交路由与文档交付物**

```powershell
git add .agents/skills/wenan-skill/SKILL.md AGENTS.md docs/wenan-skill-完整交接文档_2026-08-14.md tests/test_local_delivery_rules.py
git commit -m "feat: route confirmed scripts to storyboard workflow"
```

不要执行 `git push`。

### Task 3: 以确认文案做手动契约验证

**Files:**
- Verify: `.agents/skills/digital-human-storyboard/SKILL.md`
- Verify: `.agents/skills/wenan-skill/SKILL.md`
- Verify: `AGENTS.md`

**Interfaces:**
- Consumes: 同一对话最近一版已确认文案。
- Produces: 固定七列分镜表；素材库不存在时只给画面描述、待补拍或中性示意图。

- [ ] **Step 1: 运行“生成分镜脚本”成功路径检查**

在新对话中先完成并确认一份不含高风险事实的中文短口播定稿，然后输入：

```text
生成分镜脚本
```

Expected: 仅输出七列表；中文分句按时间顺序覆盖定稿；没有编造素材编号；不出现文案重写说明。

- [ ] **Step 2: 运行高风险事实缺来源的阻塞路径检查**

在新对话提供一份包含未附来源的产品参数或公司能力的“已确认文案”，然后输入：

```text
生成分镜脚本
```

Expected: 仅返回要求补充对应来源的阻塞说明，不输出七列表。

- [ ] **Step 3: 本地提交验证记录所依赖的实现文件**

```powershell
git status --short
```

Expected: 除用户已有的未提交修改外，不出现本功能遗漏的未跟踪实现文件；不要执行 `git push`。

## Plan Self-Review

- Spec coverage: Task 1 覆盖独立分镜 Skill、固定七列、时间码、中文覆盖、三语与素材边界；Task 2 覆盖同一对话的预置路由和不误触发口语化／产品文案；Task 3 覆盖成功与阻塞路径。
- Placeholder scan: 计划没有 `TBD`、`TODO` 或未定义接口；所有测试名称、文件路径和命令已给出。
- Type consistency: 所有任务使用同一名称 `digital-human-storyboard`、同一触发词“生成分镜脚本”和同一七列表列序。
