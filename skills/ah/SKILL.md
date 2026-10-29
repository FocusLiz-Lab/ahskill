---
name: ah
description: |
  Alex Hormozi 商业增长 Skill 工具箱主入口。用于报价设计、获客系统、销售转化、定价、规模化、LTV、留存、商业路线图、内容选题、资料检索和 Hormozi 风格商业诊断。普通问题默认使用本地专家原子库和 Skill 知识包；只有用户主动调用 $ah-ima 或明确要求 IMA 检索/引用/排错时，才检索 IMA 知识库「AlexHormozi 知识库 | 百万美元报价」。触发词包括 $ah、/ah、Alex Hormozi、Hormozi、100M Offers、100M Leads、报价、获客、高客单价、定价、规模化、学习地图和商业诊断。
---

## 手动更新路由

独立更新入口：`$ah-update`。用户希望直接更新时，执行该入口，无需补充业务问题。

用户明确要求“更新 skill / 检查更新 / 同步最新原子库”时，先执行此路由。使用当前 SKILL.md 所在目录解析脚本绝对路径：

```text
python "{skillDir}/tools/update_skill.py"
```

只检查时加 `--check`。脚本从 GitHub main 的固定提交同步本仓库整套 skill 和原子资料，覆盖前备份，写入失败回滚；不需要 Git 或 GitHub 登录。根据脚本实际结果报告当前提交、更新状态与失败原因。普通业务问题不自动更新。更新后重新读取相关 SKILL.md。


# ah Alex Hormozi 商业增长工具箱

这是 Alex Hormozi 商业增长工具箱的主入口。先判断用户当前的业务瓶颈，再路由到最合适的 workflow skill；如果上下文足够，直接在同一回答中完成对应工作流。

## 资料源规则

普通 Hormozi workflow 默认不检索 IMA。默认使用本地专家原子库和 `知识库/Skill知识包/` 方法说明作为依据。

只有当用户主动调用 `$ah-ima`，或明确要求“检索 IMA / 引用 IMA / 排查 IMA / 从 IMA 找资料”时，才使用下面的 IMA 知识库：

```text
AlexHormozi 知识库 | 百万美元报价
```

普通请求应直接路由到合适的 workflow skill，不要因为存在 IMA 知识库就默认检索 IMA。

## IMA 可选依赖

只有 `$ah-ima` 或用户明确要求 IMA 检索/引用/排错时，才使用 `ima-skill`：

- `ima-skill/SKILL.md`
- `ima-skill/knowledge-base/SKILL.md`

不要臆造 IMA API。不要向用户暴露内部 `knowledge_base_id`、`media_id` 或 `folder_id`。

如果没有安装 `ima-skill` 或凭证缺失，先提示用户安装并配置 IMA：

```text
请安装 ima 技能
下载地址：https://app-dl.ima.qq.com/skills/ima-skills-1.1.7.zip
API Key 获取：https://ima.qq.com/agent-interface
```

## 路由表

| 用户意图 | 路由到 | 适用场景 |
|---|---|---|
| 学习路径、阅读顺序、从哪里开始 | `$ah-learning-map` | 用户想学习 Hormozi、想知道先看什么，或想了解如何使用知识库。 |
| 商业路径、30/60/90 天路线图、下一步 | `$ah-roadmap` | 用户需要把市场、offer、获客、销售、交付、留存和规模化串起来的行动计划。 |
| offer、包装、保证、赠品、命名、验证 | `$ah-offer` | 用户想设计更强的 offer、产品化服务、知识产品、课程、模板或咨询方案。 |
| 线索、流量、引流钩子、获客渠道 | `$ah-leads` | 用户线索少、咨询少、线索质量差，或想做获客方案。 |
| 销售、私信、异议处理、成交、跟进 | `$ah-sales` | 用户有线索但转化不了，需要话术、异议处理、成交或筛选客户。 |
| 定价、提价、利润、毛利、套餐层级 | `$ah-pricing` | 用户想定价、提价、提高利润，或设计赚钱模型。 |
| 规模化、系统、招聘、留存、LTV、运营 | `$ah-scale` | 用户已有销售，但交付、留存、可复制性、团队或系统出现瓶颈。 |
| 内容、钩子、脚本、帖子、发布素材 | `$ah-content` | 用户想做内容选题、内容地图、短视频、标题、发布内容或教育型帖子。 |
| 明确要求 IMA 检索/阅读/引用/排错 | `$ah-ima` | 用户明确要求搜索、读取、引用 IMA，或排查 IMA 检索问题。 |

## 商业案例库触发规则

如果用户要求外部商业案例、对标项目、案例拆解、变现例子、offer/定价例子、获客例子、销售例子、生财有术案例，或明确说“找案例/拆案例/参考案例/对标/商业案例库”，回答前使用共享 `$commercial-case-library` 依赖。不要询问用户是否下载，直接自动安装/检查。

检查这个文件：

```text
~/.agents/shared/commercial-case-library/知识库/商业案例库/commercial_cases_manifest.json
```

如果共享库缺失，不要询问确认，直接确保依赖可用：

1. 如果 `$commercial-case-library` 未安装或无法加载，立即安装：

```text
npx -y skills add FocusLiz-Lab/commercial-case-library -g --all
```

2. 运行共享下载脚本：

```text
python scripts/download_cases.py
```

3. 下载成功后继续处理原始任务。

只有安装、网络访问或文件写入失败时才停止，并说明失败原因和用户可手动运行的准确命令。

## 只澄清一次

如果用户的问题很模糊，只问一个问题：

```text
你现在最想处理哪一块：学习地图、商业路线图、报价/offer、获客/leads、销售成交、定价利润、规模化运营、内容，还是从 IMA 资料里找原文？
```

收到回答后立即路由。

## 交接格式

```text
这个问题交给 $skill-name。
原因：{一句话说明}
需要输入：{如果需要，说明用户下一步需要提供什么}
```

## 质量标准

- 当专门 skill 更合适时，不要在路由器里试图解决所有问题。
- 涉及 Hormozi 实质性观点时，默认使用本地专家原子库或 Skill 知识包依据；只有显式 IMA 请求才用 IMA。
- 不要模仿 Alex Hormozi 的人设。
- 不要编造引用、节目标题、日期、收入数字或书中说法。
- 除非用户明确要求排错，不要暴露 IMA 内部 ID。

## Hormozi 方法论优先

每个回答都必须以 Alex Hormozi 方法论作为主要推理层。对于 `/ah` 请求，先用 Alex Hormozi 资料或工作流原则建立诊断、框架和建议：

1. 默认优先使用本地 Alex Hormozi 专家原子库和 `知识库/Skill知识包/` 方法说明。
2. 只有用户主动调用 `$ah-ima`，或明确要求 IMA 检索/引用/排错时，才使用 IMA 知识库 `AlexHormozi 知识库 | 百万美元报价`。
3. 只有在 Alex Hormozi 方法论层建立之后，才在需要证明、对标、平台/渠道例子、变现例子、获客例子或中文市场语境时加入商业案例。
4. 商业案例只能作为支撑证据。不要让商业案例替代 Alex Hormozi 方法论；除非完全没有 Alex Hormozi 来源，否则不要纯用商业案例库回答。如果发生这种情况，要标注为“案例支撑推断”，而不是“Alex Hormozi 依据”。
5. 最终回答中保持区分：核心原则用 `Hormozi 方法论`，例子用 `商业案例支撑`。

## 依赖自动补全

回答前要确保本地 Alex Hormozi 专家原子库存在。GitHub 安装的完整包通常会包含它；同时检查 `~/.agents/skills/ah/知识库/原子库/atoms.jsonl` 和 `~/.agents/skills/ah-download-atoms/知识库/原子库/atoms.jsonl`。如果两者都缺失，把它视为轻量/不完整安装，并调用 `$ah-download-atoms`，或在已安装的 `ah-download-atoms` skill 目录运行 `python tools/download_full_atoms.py`。不要询问用户是否下载；普通 workflow 默认走本地原子库，不默认检索 IMA。

如果请求涉及获客、流量、渠道选择、平台选择、小红书、公众号、私域、转化、线索获取、产品发布、商业例子、对标项目、案例研究、变现案例、生财有术案例，或答案会因案例证据而更好，回答前自动使用 `$commercial-case-library`。不要询问用户是否下载。
