# 专业 B2B 脚本质量门 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将可提升专业 B2B 脚本质量的 dbskill 能力融入现有专项 skill，同时保持事实核验优先。

**Architecture:** 以一份共享质量门承载新增通用规则，项目总规则定义全局优先级，九个 skill 仅接入质量门而不复制规则。口语化改写 skill 保持后处理职责。

**Tech Stack:** Markdown、现有 Codex skill 目录结构。

## Global Constraints

- 不修改 `knowledge/` 中的原始资料。
- 不弱化既有事实、参数、法规、热点和公司能力核验规则。
- 不将商业诊断、执行力、长期记录或多 Agent 治理加入单篇写稿流程。
- 默认不输出内部检查；触发事实规则时继续输出实际使用的资料出处。

---

### Task 1: 新增共享 B2B 内容质量门

**Files:**
- Create: `.agents/skills/references/b2b-content-quality-gate.md`

- [ ] 定义真实性优先级、选题门、标题与开头规则、B2B 决策压力检查、逻辑流检查及发布风险检查。
- [ ] 明确质量门不能增加或强化事实，且不替代各 skill 的专项来源和硬边界。

### Task 2: 更新项目总规则

**Files:**
- Modify: `AGENTS.md`

- [ ] 在默认工作流和脚本文案规则中加入共享质量门的调用时机。
- [ ] 明确仅在用户要求选题/标题候选/审校时显示中间结果。

### Task 3: 接入九个专项 skill

**Files:**
- Modify: `.agents/skills/*/SKILL.md`

- [ ] 为八个生成型专项 skill 加入定稿前质量门。
- [ ] 为口语化改写 skill 加入事实不变前提下的逻辑流和 AI 腔表达审校。
- [ ] 在每个 skill 的 Reference Files 中加入共享质量门入口。

### Task 4: 静态验收

**Files:**
- Verify: `AGENTS.md`、`.agents/skills/references/b2b-content-quality-gate.md`、所有 `SKILL.md`

- [ ] 搜索全部 skill 是否引用质量门。
- [ ] 检查共享质量门是否禁止未验证事实、虚构案例、绝对承诺和竞品贬损。
- [ ] 检查未触及 `knowledge/` 原始资料。
