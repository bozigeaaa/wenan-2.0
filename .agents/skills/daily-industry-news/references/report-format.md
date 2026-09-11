# 日报数据合同

每轮先写 .news-output/daily-YYYY-MM-DD.json，通过 scripts/daily_news.py publish 发布。使用 UTF-8 JSON，禁止 JSON 外附解释。可参照 outputs/news/ 中已有日报的结构，事实与日期只采用本轮取得的内容。

顶层必填：schemaVersion=1；collectedDate 为北京时间实际收录日 YYYY-MM-DD；collectedAt 为带时区的实际采集时间；timeZone=Asia/Shanghai；window 为实际检索窗口说明；scope 为实际范围；channels 为三列数组（渠道名、实际访问状态、取得内容或失败原因）；items 为所有收录条目；run 为本轮执行状态。

定时批次的 run.slot 必填09:00或14:00，使用 due 返回的批次；手动首轮可不填。completedSlots 由发布程序合并当天实际成功完成的批次，不手工冒填。上午完成后下午仍须采集。

run.status 取 completed / partial / failed；run.startedAt、run.completedAt 为实际起止时间；run.message 说明覆盖结果或未完成原因；run.newCount、run.updatedCount 按实际事件数量填写。run.completedAt 是本轮结束时间，不是新闻核验时间。若所有候选都处理完，即使其中有 unconfirmed，仍可是 completed；采集工作未做完则不可标 completed。lastVerifiedAt 由发布程序按条目计算。

items 每条必填：

- id：当天稳定编号字符串（001、002等），同日重跑保留原编号，新事件接续；跨日引用保留 relatedId 或说明原编号。
- category、tags：分类与分类数组；region：地区。
- title：忠实的中文新闻标题；original：原始标题；source、sourceType、url：来源名、来源性质和原文 HTTP(S) 链接。
- published：已核实的文章发布时间；event、eventLabel：事件日、生效日或准确的阶段说明。未披露时明确“未披露”，不能根据抓取日补造。
- summary：中文摘要，严格落在已确认范围内；review：本轮实际核验操作和结论。
- status：verified / unconfirmed；statusText：给用户看的准确状态；update：本轮新收录、核验更新或沿用等实际状态。
- products：二维数组，每个元素为 [产品名称, 事实到用途或项目判断的适配理由]；空数组表示无直接产品适配。background 解释行业价值或不能适配的原因。
- verification：result 与 status 完全相同；checkedAt 为实际核验时间（ISO 8601，必须含时区）；method 为核验方式；confirmedScope 为已确认范围；reason 为结论及依据；missing 为仍缺少的具体证据，通过时为空字符串。
- reviewUrls：可选二维数组 [来源名称, HTTP(S) URL]，只录本轮实际读过并使用的复核来源。不能将搜索页面或工具内部编号当作原文链接。
- boundary：可选事实边界；shipping：航运适用条件二维数组；progress：状态变化；productFit：具体型号仍需清单时可单独说明，不因此否定已核验基本公告。

证据文件放 outputs/news/evidence-YYYY-MM-DD/；访问日志记录渠道、具体入口/关键词、工具/模式、抓取时间、正文/列表/摘要/受限层级与结果。JSON 和 HTML 中不得只写“待系统核验”“稍后核实”。未通过记录也必须完成本轮可执行查证，列出实际缺口。

renderer 拒绝缺核验时间、缺方法/结论、状态矛盾、笼统待核验枚举、无来源链接、未通过却无缺失原因等输入。程序只能校验字段完整，真假和证据强度须由收集执行者读原文判断。

## 双工具记录

顶层 retrievalTools 必填数组。每项包含 tool（scrapling / firecrawl / web-search / browser）、status（completed / failed / unavailable）、entries（本次实际 URL 或检索词数组）、evidence（已保存的检索记录路径或具体证据说明）。只有实际取得网页、列表、原文或检索结果才能标 completed。环境自检和读取旧缓存不算本轮成功检索。

run.status=completed 时，必须至少有两种不同工具成功并留有非空入口与证据；同一工具不同模式不重复计数。未达到条件只能写 partial/failed，列出原因。双工具记录不替代每条新闻的独立事实核验。
