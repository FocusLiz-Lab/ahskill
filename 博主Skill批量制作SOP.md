# 博主 Skill 批量制作 SOP

这份 SOP 用于把不同博主、作者、课程体系或知识库批量制作成可发布的 Agent Skill 工具箱。目标是每个项目都能同时支持：

- GitHub 仓库发布
- `npx -y skills add <owner>/<repo> -g --all` 安装
- SkillHub 单 skill zip 上传
- 默认读取指定 IMA 知识库
- 不暴露隐私字段、私有环境配置、API Key 或未授权资料

---

## 1. 项目输入表

每做一个新博主，先填写这张表。

| 字段 | 示例 | 说明 |
|---|---|---|
| 项目名 | `ahskill` | GitHub 仓库名、发布名 |
| 主入口 skill | `ah` | 用户最常调用的短命令 |
| 博主名 | `Alex Hormozi` | README 和 skill 描述使用 |
| 中文定位 | `商业增长 / offer / 获客` | 一句话说明这个 skill 解决什么 |
| 默认 IMA 知识库 | `AlexHormozi 知识库 | 百万美元报价` | workflow 默认检索的知识库名称 |
| GitHub 仓库 | `<owner>/<repo>` | 例如 `FocusLiz-Lab/ahskill` |
| 二维码文件 | `docs/knowledge-base-qrcode.png` | 用于 README 展示知识库入口 |
| SkillHub 主包名 | `<repo>-skillhub-root.zip` | 根目录必须有 `SKILL.md` |
| 许可证 | `CC BY-NC 4.0` | 默认推荐非商业授权 |

---

## 2. 标准技能矩阵

优先保持每个博主项目都有一套稳定入口，方便批量生产和用户理解。

| Skill 类型 | 命名模板 | 用途 |
|---|---|---|
| 主入口 | `<prefix>` | 自动识别问题并路由到具体 workflow |
| 学习地图 | `<prefix>-learning-map` | 先学什么、阅读顺序、学习产出 |
| 路线图 | `<prefix>-roadmap` | 30/60/90 天行动路径 |
| Offer | `<prefix>-offer` | 产品、服务、课程、咨询、社群的 offer 设计 |
| 获客 | `<prefix>-leads` | 流量、线索、lead magnet、渠道策略 |
| 销售 | `<prefix>-sales` | 私聊、电话、异议处理、跟进转化 |
| 定价 | `<prefix>-pricing` | 定价、利润、套餐、价格测试 |
| 规模化 | `<prefix>-scale` | 交付、系统、留存、LTV、团队 |
| 内容 | `<prefix>-content` | 选题、hook、短视频、长文、发布计划 |
| IMA 桥接 | `<prefix>-ima` | 显式搜索、引用、排错 IMA 检索 |

如果某个博主不适合完整商业链路，可以删减，但建议至少保留：

- `<prefix>`
- `<prefix>-learning-map`
- `<prefix>-content`
- `<prefix>-offer`
- `<prefix>-ima`

---

## 3. 目录结构标准

GitHub 仓库建议结构：

```text
<repo>/
├── README.md
├── 使用说明.md
├── VERSION
├── docs/
│   └── knowledge-base-qrcode.png
└── skills/
    ├── <prefix>/
    │   ├── SKILL.md
    │   ├── agents/
    │   │   └── openai.yaml
    │   └── references/
    │       └── archive-map.md
    ├── <prefix>-learning-map/
    │   ├── SKILL.md
    │   └── agents/openai.yaml
    ├── <prefix>-offer/
    │   ├── SKILL.md
    │   └── agents/openai.yaml
    └── <prefix>-ima/
        ├── SKILL.md
        ├── agents/openai.yaml
        └── references/query-map.md
```

SkillHub 上传包建议结构：

```text
<repo>-skillhub-root.zip
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   └── archive-map.md
├── README.md
├── 使用说明.md
├── VERSION
├── docs/
│   └── knowledge-base-qrcode.png
└── skills/
    └── ...
```

注意：SkillHub 校验通常要求 zip 根目录直接包含 `SKILL.md`。

---

## 4. SKILL.md 编写规范

每个 skill 的 `SKILL.md` 必须包含 YAML frontmatter：

```markdown
---
name: <skill-name>
description: |
  <一句话说明这个 skill 做什么。必须写清楚触发条件、适用问题、默认 IMA 知识库名称、命令别名。>
---

# <skill-name>
```

正文建议固定包含：

- 默认 IMA 知识库
- 必需依赖：`ima-skill`
- 输入要求
- 工作流步骤
- 输出格式
- 质量标准
- 禁止事项

主入口 `<prefix>` 必须包含路由表：

```markdown
| 用户意图 | 路由到 | 使用场景 |
|---|---|---|
| 学习路径 | `$<prefix>-learning-map` | 用户问先学什么、怎么系统学习 |
| Offer | `$<prefix>-offer` | 用户要设计产品、服务、课程、咨询 |
| 获客 | `$<prefix>-leads` | 用户流量差、线索少、渠道弱 |
| 内容 | `$<prefix>-content` | 用户要选题、脚本、长文、短内容 |
| IMA 检索 | `$<prefix>-ima` | 用户明确要找资料、引用、排错 |
```

---

## 5. IMA 规则

所有 workflow skills 默认使用项目输入表里的 IMA 知识库：

```text
<默认 IMA 知识库>
```

统一规则：

- 用户不需要每次输入知识库名称。
- 如果用户明确指定另一个 IMA 知识库，则优先使用用户指定的名称。
- 不编造 IMA API。
- 不暴露 `knowledge_base_id`、`media_id`、`folder_id` 等内部 ID。
- 如果 IMA skill 未安装或凭证缺失，提示用户安装和配置 IMA。

统一提示：

```text
请安装 ima 技能
下载地址：https://app-dl.ima.qq.com/skills/ima-skills-1.1.7.zip
API Key 获取：https://ima.qq.com/agent-interface
```

---

## 6. README 标准结构

`README.md` 面向 GitHub 访客，建议使用中文。

推荐结构：

```markdown
# <repo>

<博主名> 风格 <中文定位> Skill 工具箱。

本仓库打包了一组面向 Agent 的 workflow skills，用于基于 IMA 知识库学习 <博主名> 风格资料，并完成 <核心用途列表>。

适用于 Codex、Claude Code、Cursor、Trae Solo 等支持 skill / system prompt 工作流的 Agent。

---

## 安装

## IMA 配置

## 加入 / 访问知识库

## 工具箱

## 常见路径

## 使用示例

## 资料边界

## 许可证
```

README 必须包含：

- 安装命令
- 默认 IMA 知识库名称
- 二维码图片
- skill 列表表格
- 使用示例
- 版权和资料边界

---

## 7. 使用说明标准结构

`使用说明.md` 面向普通用户，写得更直接。

推荐结构：

```markdown
# <repo> 使用说明

## 这是什么
## 适合谁
## 安装方式
## IMA 知识库配置
## 常用命令
## 典型场景
## 常见问题
## 发布边界
```

常用命令必须给真实示例：

```text
$<prefix>-learning-map 系统学习这个知识库，先看哪些？
$<prefix>-offer 用户要做一个低价知识库产品，帮他设计更强的 offer。
$<prefix>-content 围绕这个 offer 做 30 个短内容选题。
```

示例中不要出现隐私字段、具体账号、私有业务、未授权平台数据。

---

## 8. 敏感信息扫描清单

发布前必须确认仓库和 zip 中不包含：

- 姓名、手机号、邮箱、社交账号等隐私字段
- API Key、Client Secret、token
- 私有资料文件
- 原始 PDF、视频、转录稿、课程材料
- 私有知识库导出文件
- 个人环境配置
- 未授权第三方内容
- 和项目无关的平台、业务或客户信息

建议扫描关键词：

```text
隐私字段
设备环境配置
私有环境配置
API Key
token
secret
password
private
```

---

## 9. 校验流程

每个 skill 都要校验：

```bash
python <skill-creator>/scripts/quick_validate.py <skill-folder>
```

整包上传前检查：

- `skills/` 下每个 skill 都有 `SKILL.md`
- 每个 `SKILL.md` 的 `name` 和文件夹名一致
- 每个 skill 都有 `agents/openai.yaml`
- README 图片路径存在
- `VERSION` 已更新
- SkillHub zip 根目录有 `SKILL.md`

---

## 10. GitHub 发布流程

1. 创建仓库：`<owner>/<repo>`
2. 确认根目录文件：

```text
README.md
使用说明.md
VERSION
docs/
skills/
```

3. 推送到 `main`
4. 打开 GitHub 页面检查：

- README 是否中文
- 二维码是否显示
- 文件名是否简洁
- 没有私有资料目录

5. 测试安装命令：

```bash
npx -y skills add <owner>/<repo> -g --all
```

---

## 11. SkillHub 发布流程

SkillHub 通常需要上传 zip。推荐生成一个根目录包含 `SKILL.md` 的包：

```text
<repo>-skillhub-root.zip
```

上传前打开 zip 检查第一层：

```text
SKILL.md
agents/
references/
README.md
使用说明.md
VERSION
docs/
skills/
```

如果页面提示“必须包含 SKILL.md 文件”，说明 `SKILL.md` 不在 zip 根目录，需要重新打包。

---

## 12. 批量制作步骤

每个新博主按下面顺序执行：

1. 填写项目输入表。
2. 确定 `<repo>` 和 `<prefix>`。
3. 复制一个已有项目作为模板。
4. 全局替换：

```text
旧项目名 -> 新项目名
旧 prefix -> 新 prefix
旧博主名 -> 新博主名
旧 IMA 知识库名 -> 新 IMA 知识库名
旧 GitHub 仓库 -> 新 GitHub 仓库
```

5. 根据博主领域调整技能矩阵。
6. 修改每个 `SKILL.md` 的 description、workflow 和输出格式。
7. 替换二维码图片。
8. 更新 README 和 `使用说明.md`。
9. 运行敏感信息扫描。
10. 运行 skill 校验。
11. 上传 GitHub。
12. 生成 SkillHub zip。
13. 上传 SkillHub。
14. 用 3 个真实提示词测试。

---

## 13. 三个必测提示词

每个项目发布前至少测试：

```text
$<prefix>-learning-map 系统学习这个知识库，先看哪些？
```

```text
$<prefix>-offer 用户要做一个知识产品，帮他设计一个更强的 offer。
```

```text
$<prefix> 用户不知道问题出在产品、获客还是销售，帮他诊断一下。
```

输出要满足：

- 会默认使用指定 IMA 知识库
- 不编造原文引用
- 能给结构化下一步
- 不暴露内部 ID
- 不要求用户重复输入已经默认配置的信息

---

## 14. 交付物清单

最终每个博主项目至少交付：

- GitHub 仓库链接
- SkillHub 上传 zip
- README 中文说明
- `使用说明.md`
- 知识库二维码
- 默认 IMA 知识库名称
- skill 列表
- 校验结果

---

## 15. 推荐命名规则

| 对象 | 规则 | 示例 |
|---|---|---|
| GitHub 仓库 | `<short-name>skill` | `ahskill`, `dkskill` |
| 主入口 | 2-8 个小写字符 | `ah`, `dankoe` |
| 子 skill | `<prefix>-<workflow>` | `ah-offer` |
| SkillHub zip | `<repo>-skillhub-root.zip` | `ahskill-skillhub-root.zip` |
| 二维码 | `knowledge-base-qrcode.png` | `docs/knowledge-base-qrcode.png` |

命名只使用小写字母、数字和连字符。避免空格、中文文件夹名和特殊符号用于 skill 文件夹。
