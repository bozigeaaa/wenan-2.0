# 下载后启用新闻抓取

本项目附带 Humanizer 和 Scrapling 的技能指令；第三方运行依赖由每位用户在自己的电脑上安装。技能文件随 GitHub ZIP 分发，不会自动安装 Python、浏览器或 Firecrawl，也不会继承维护者的账号。

## 第一次使用

1. 下载并完整解压仓库，在 Codex 中打开包含 AGENTS.md、knowledge 和 .agents 的项目根目录。保留隐藏的 .agents 文件夹，不要只复制一个 SKILL.md。
2. Humanizer 已随项目提供，无需 pip、Node.js、API Key 或单独下载。文案入口按项目内 .agents/skills/humanizer/SKILL.md 调用；同名全局技能不能替代本项目的中文 B2B 规则。
3. Scrapling 需要 Python 3.10+、pip 和 venv。在项目根目录运行下方安装命令；也可直接对 Codex 说“按项目内 Scrapling 技能准备新闻抓取环境并测试”。安装只创建项目内 .news-venv，不修改全局 Python。
4. 安装后重新打开项目或开始新任务，使宿主重新发现项目技能。若宿主没有显示技能列表，直接让 Codex 读取项目内对应 SKILL.md；纯聊天环境没有本地文件和命令执行能力时，无法执行本地爬虫。

### Windows

使用系统已安装的 Python 启动器：

~~~powershell
py -3 scripts/news_tools.py setup
py -3 scripts/news_tools.py check
~~~

如果没有 py 而有 python，可替换命令前缀为 python。PowerShell 不需要激活虚拟环境，也不需要调整脚本执行策略。

### macOS / Linux

~~~bash
python3 scripts/news_tools.py setup
python3 scripts/news_tools.py check
~~~

如果系统提示缺少 pip 或 venv，按当前操作系统提供的 Python 安装说明补齐，再重试。虚拟环境不能从维护者或其他操作系统复制过来；应在新的项目副本中重新安装。路径支持空格和中文，脚本根据自身位置定位项目。

## 读取公开页面

下面以 python 为前缀，各系统可按上文替换；所有输出相对项目根目录保存。

~~~bash
python scripts/news_tools.py get "https://example.com" ".news-output/example.md"
~~~

打开输出文件并核对正文。命令完成、HTTP 200 和网页正文核验成功是不同状态；例子只测试抓取能力，不代表找到可用新闻。

需要 JavaScript 渲染时，先安装浏览器依赖，再读取：

~~~bash
python scripts/news_tools.py setup --browser
python scripts/news_tools.py fetch "https://example.com" ".news-output/example-browser.md"
~~~

浏览器依赖下载可能较大，Linux 可能还需要系统组件。已经安装 Chromium 系浏览器时，可使用当前电脑实际路径替代下载浏览器；不要复制其他用户的路径：

~~~text
python scripts/news_tools.py fetch "URL" ".news-output/page.md" --browser-path "当前电脑的浏览器可执行文件绝对路径"
~~~

check 只检查项目文件、Python 导入和离线 HTML 解析。浏览器是否可启动、某个新闻网站是否可访问，分别以实际读取结果为准。浏览器安装失败时仍可使用普通 get 或宿主的其他工具继续检索。

## Firecrawl 是可选渠道

本项目没有打包 Firecrawl 账号或服务。宿主已有可用 Firecrawl 工具时可直接使用；未提供时，可选择安装本地 CLI。先安装 Node.js 18+ 和 npm，再在项目根目录执行：

~~~bash
npm install --prefix .news-tools firecrawl-cli@1.19.31
node .news-tools/node_modules/firecrawl-cli/dist/index.js --status
node .news-tools/node_modules/firecrawl-cli/dist/index.js scrape "https://example.com" --only-main-content -o .news-output/firecrawl-example.md
~~~

先按前面的 Scrapling 示例建立 .news-output，或自行创建该目录。实际服务是否需要认证、是否有免费额度、是否允许目标站点，以当前 CLI 和服务返回为准；本次测试可匿名执行部分命令，不代表所有用户都有相同权限或额度。需要服务凭证时由用户在自己的环境配置，不放进项目或聊天。缺少凭证、额度耗尽或工具不可用时，继续使用 Scrapling 或宿主现有网页工具。

## 调用关系与验收

- 新闻任务：wenan-skill → 新闻核验技能 → hotspot-sourcing.md → 按需要读取项目内 Scrapling 技能并执行运行入口。
- 完整口播稿：wenan-skill → 项目内 Humanizer → 共享 expression-craft.md。Humanizer 由宿主模型执行，不是一个 Python 改写程序。
- 发布前检查：两个技能及其引用文件完整；干净副本中能够新建虚拟环境、通过 check、读取测试正文；另外核对新闻流程是否按事实与产品适配筛选。Windows 验证通过不能替代 macOS/Linux 的实际运行验证。
- 在副本中输入“用项目内 humanizer 把‘请您对附件进行查阅，并将修改意见反馈给我’改得自然些”，应读取本项目技能，保留“看附件并反馈意见”的含义；这类模型行为应在实际宿主中检查，文件检查不代表效果保证。

详细渠道优先级、失败后的切换和新闻数量口径见 [hotspot-sourcing.md](../../global-hotspot-industry-impact-script/references/hotspot-sourcing.md)，不在安装文档另立一套规则。

## 上游来源与版本

- Scrapling：根据 [D4Vinci/Scrapling v0.4.15](https://github.com/D4Vinci/Scrapling/tree/v0.4.15) 官方技能的安装与公开页面读取方式改编；本项目精简为普通抓取和浏览器渲染，添加项目独立入口，保留 [BSD 3-Clause 许可证](../LICENSE.txt)。运行依赖入口为技能目录的 requirements.txt，间接依赖也通过 constraints.txt 固定到本轮验证版本；升级时重新做安装与抓取检查。
- Humanizer：项目内已有 [blader/humanizer](https://github.com/blader/humanizer) 2.11.2 的中文 B2B 适配版，保留 [MIT 许可证](../../humanizer/LICENSE)。
- Firecrawl：可选 CLI 验证版本 1.19.31；使用说明以 [官方项目](https://github.com/firecrawl/cli) 为准。

不分发虚拟环境、浏览器二进制、个人配置、登录凭证或新闻抓取缓存。工具版本和网站策略会变化，需要时重新实测并更新依赖；不承诺绕过所有访问限制。
