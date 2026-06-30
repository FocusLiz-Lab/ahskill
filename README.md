# ahskill

Alex Hormozi-style business workflow skill toolbox.

`ahskill` packages a set of Agent skills for learning Alex Hormozi-style materials, designing offers, building lead-generation systems, improving sales conversion, pricing products, scaling operations, and creating content assets.

It is designed for Codex, Claude Code, Cursor, Trae Solo, and other agents that support skill / system-prompt style workflows.

---

## Install

### Universal Install

After this repository is published, users can install all skills with:

```bash
npx -y skills add FocusLiz-Lab/ahskill -g --all
```

Then use:

```text
$ah 数字产品获客很差，按 Hormozi 框架拆一下。
```

### Manual Install

Copy or import the skill folders under `skills/`:

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

Each folder is a standalone skill with a root `SKILL.md`.

---

## IMA Configuration

All workflow skills default to this IMA knowledge base:

```text
AlexHormozi 知识库 | 百万美元报价
```

Users do not need to type the knowledge-base name in every prompt. If they want to use another IMA knowledge base, they can name it directly in the request.

### Join / Access Knowledge Base

Scan the QR code below to access or identify the knowledge-base entry point:

![Knowledge Base QR Code](docs/knowledge-base-qrcode.png)

### Install IMA Skill

```text
请安装 ima 技能
下载地址：https://app-dl.ima.qq.com/skills/ima-skills-1.1.7.zip
API Key 获取：https://ima.qq.com/agent-interface
```

Requirements:

- Official `ima-skill` installed
- IMA `Client ID` and `API Key` configured
- Current IMA account has access to the target knowledge base

This repository does not include or store any IMA API keys.

---

## Toolbox

| Skill | Purpose |
|---|---|
| `$ah` | Main router. Routes the request to the right Hormozi workflow. |
| `$ah-learning-map` | Learning map: what to study first, reading sequence, output tasks. |
| `$ah-roadmap` | Business roadmap: market, offer, leads, sales, delivery, retention, scale. |
| `$ah-offer` | Offer design: promise, value equation, bonuses, guarantee, validation plan. |
| `$ah-leads` | Lead generation: lead magnets, channels, content, outreach, affiliates. |
| `$ah-sales` | Sales conversion: qualification, DM/call scripts, objections, follow-up. |
| `$ah-pricing` | Pricing and profit: tiers, price tests, margins, money models. |
| `$ah-scale` | Scale: systems, delivery, retention, LTV, hiring, operations. |
| `$ah-content` | Content system: hooks, posts, scripts, launch and educational content. |
| `$ah-ima` | Optional IMA retrieval entry: search, read, cite, or troubleshoot IMA. |

---

## Common Paths

### Learning To Practice

```text
ah-learning-map
    ↓
ah-offer
    ↓
ah-leads
```

### Product To Sales

```text
ah-offer
    ↓
ah-leads
    ↓
ah-sales
```

### Sales To Scale

```text
ah-pricing
    ↓
ah-scale
    ↓
ah-content
```

### Explicit IMA Retrieval

```text
ah-ima
    ↓
corresponding workflow skill
```

---

## Examples

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

## Source Boundary

This repository contains only skill instructions and workflow abstractions.

It does not include Alex Hormozi's original books, PDFs, paid materials, YouTube transcripts, X/Twitter archives, private source folders, or any copyrighted source corpus.

The skills retrieve source material from the user's own IMA knowledge base at runtime. Users are responsible for ensuring they have the right to upload and use their own materials.

Do not commit:

- IMA API keys
- Private source files
- Original PDFs, transcripts, videos, or archives
- Local machine paths
- Any unauthorized third-party content

---

## License

This project is licensed under CC BY-NC 4.0 unless a different license is added.

The license applies only to the original skill instructions and workflow abstractions in this repository. It does not grant rights to any third-party source materials.
