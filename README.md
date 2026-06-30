# ahskill

Alex Hormozi 商业工作流 Skill 工具箱。

`ahskill` 是一组面向 Agent 的 workflow skills，用来基于 IMA 知识库学习 Alex Hormozi 资料、设计 offer、搭建获客系统、提升销售转化、设计定价、拆解规模化运营，并生成内容资产。

适用于 Codex、Claude Code、Cursor、Trae Solo 等支持 skill / system prompt 工作流的 Agent。

---

## 安装

### 通用安装

发布后，可以用下面的命令安装整套 skills：

```bash
npx -y skills add FocusLiz-Lab/ahskill -g --all
```

安装后可以直接使用：

```text
$ah 数字产品获客很差，按 Hormozi 框架拆一下。
```

### 手动安装

也可以手动复制或导入 `skills/` 目录下的 skill 文件夹：

```text
skills/
├── ah/
├── ah-learning-map/
├── ah-roadmap/
├── ah-offer/
├── ah-leads/
├── ah-sales/
├── ah-pricing/
├── ah-scale/
├── ah-content/
└── ah-ima/
```

每个文件夹都是一个独立 skill，根目录都有 `SKILL.md`。

---

## IMA 配置

整套 workflow skills 默认读取这个 IMA 知识库：

```text
AlexHormozi 知识库 | 百万美元报价
```

用户不需要在每次提问时输入知识库名称。如果想使用其他 IMA 知识库，在问题里直接写知识库名称即可。

### 加入 / 访问知识库

扫描下面的二维码，加入或访问对应知识库：

![知识库二维码](docs/knowledge-base-qrcode.png)

### 安装 IMA Skill

```text
请安装 ima 技能
下载地址：https://app-dl.ima.qq.com/skills/ima-skills-1.1.7.zip
API Key 获取：https://ima.qq.com/agent-interface
```

使用前需要满足：

- 已安装官方 `ima-skill`
- 已配置 IMA `Client ID` 和 `API Key`
- 当前 IMA 账号有权限访问目标知识库

本仓库不包含、也不会保存任何 IMA API Key。

---

## 工具箱

| Skill | 用途 |
|---|---|
| `$ah` | 主入口。根据用户问题自动路由到合适的 Hormozi workflow。 |
| `$ah-learning-map` | 学习地图：先学什么、阅读顺序、学习产出。 |
| `$ah-roadmap` | 商业路线图：市场、offer、获客、销售、交付、留存、规模化。 |
| `$ah-offer` | Offer 设计：承诺、价值方程、bonus、guarantee、验证计划。 |
| `$ah-leads` | 获客系统：lead magnet、渠道、内容、外联、affiliate。 |
| `$ah-sales` | 销售转化：资格筛选、私聊/电话脚本、异议处理、跟进。 |
| `$ah-pricing` | 定价利润：价格梯度、提价测试、利润率、money model。 |
| `$ah-scale` | 规模化运营：系统、交付、留存、LTV、招聘、运营。 |
| `$ah-content` | 内容系统：hook、帖子、脚本、launch 内容和教育内容。 |
| `$ah-ima` | 可选 IMA 检索入口：搜索、阅读、引用或排查 IMA。 |

---

## 常见路径

### 从学习到实践

```text
ah-learning-map
    ↓
ah-offer
    ↓
ah-leads
```

### 从产品到成交

```text
ah-offer
    ↓
ah-leads
    ↓
ah-sales
```

### 从成交到放大

```text
ah-pricing
    ↓
ah-scale
    ↓
ah-content
```

### 显式 IMA 检索

```text
ah-ima
    ↓
对应 workflow skill
```

---

## 使用示例

```text
$ah-learning-map 系统学习 $100M Offers，先看哪些？
```

```text
$ah-offer 为一个低价知识产品设计更强的 offer。
```

```text
$ah-leads 产品曝光不少，但咨询很少，设计一个获客测试。
```

```text
$ah-sales 买家一直问但不下单，设计一套私聊成交路径。
```

```text
$ah-content 围绕这个 offer 做 30 个短内容选题。
```

---

## 资料边界

本仓库只包含 skill instructions 和 workflow 抽象。

本仓库不包含 Alex Hormozi 的原书、PDF、付费材料、YouTube 转录稿、X/Twitter 归档、私有资料文件夹或任何受版权保护的原始资料库。

这些 skills 会在运行时从用户自己的 IMA 知识库检索资料。用户需要自行确保有权访问知识库。

请不要提交：

- IMA API Key
- 私有资料文件
- 原始 PDF、转录稿、视频或归档
- 个人环境配置
- 任何未经授权的第三方内容

---

## 许可证

本项目默认采用 CC BY-NC 4.0 许可证，除非后续另行添加其他许可证。

许可证只覆盖本仓库原创的 skill instructions 和 workflow 抽象，不授权任何第三方原始资料。
