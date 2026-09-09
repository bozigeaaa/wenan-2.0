---
name: storyboard-html-layout
description: Render confirmed storyboard tables as the default standalone HTML layout with Chinese, English and Arabic views and material-code cards. Use when delivering or restyling a storyboard after its content is ready.
---

# 分镜表默认 HTML 呈现

用户已确认此布局为以后分镜表的默认交付格式。用户当次明确指定其他格式时遵从当次要求。内容拆分、核验和翻译仍由原分镜流程负责。

## 默认交付

生成自包含 HTML 文件，提供绝对路径链接；能预览时在应用内打开。最终回复简短，不重复粘贴整张宽表。文件可离线用浏览器打开，不依赖本机预览端口或外部 CDN。

复用 assets/storyboard.html 和 scripts/render.mjs，保持用户确认的布局：
- 浅灰背景、深蓝绿色表头、交替浅色行、充足内边距。
- 默认中文审稿；提供 English、العربية、完整七列切换。
- 固定表头、镜号及不换行时间码；宽表横向滚动。
- 完整七列顺序：镜号、时间码、中文字幕、英文字幕、阿拉伯语字幕、分镜、画面／素材建议。语言视图只隐藏另两种字幕，不删数据。
- 阿语独立 RTL、右对齐，拉丁文字和数字保持正确方向。
- 每镜最右列顶部为绿色“推荐素材”编号卡片，下方保留画面建议。没有已确认素材时显示“待关联素材”；需要补拍或示意图时保留相应说明。
- 顶部显示本稿标题、实际镜数、总时长；估时须标清口径。全片共用说明可集中在折叠区，保留原意。

## 数据与生成

先将完整分镜保存为 UTF-8 JSON，字段如下：
- title：本稿标题；brand：本稿适用品牌或栏目，可省略。不得沿用上一稿公司或项目名。
- duration：总时长字符串，可省略并取末镜结束时间。
- notes：全片制作说明字符串数组，可省略。
- rows：七个字符串组成的行数组，按上述七列顺序，保留所有镜头、原文、译文、时间码与画面说明。
- materials：可省略；以镜号为键，每项可含 codes（真实素材编号字符串数组）、usage（已确认的截取或插入说明）、status（无编号时的状态）。

运行：node <本技能目录>/scripts/render.mjs <输入.json> <输出.html>

素材编号只有在素材确实存在、内容已查看且满足原分镜流程调用条件时才填入；编号卡片不代表素材已自动插入视频。用户明确要求演示布局时可用示例编号，并在该项设 example: true；正式稿不得默认带入示例。模板中没有上篇文案、固定镜数、固定品牌或演示编号。

## 验证

打开输出文件，检查镜数和七列内容完整、四种视图切换正常、阿语不挤入相邻列、素材卡位于最右列顶部。确认内容与输入一致，改格式不改文案。不要把上次 localhost 端口写入长期规则。
