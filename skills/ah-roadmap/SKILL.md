---
name: ah-roadmap
description: |
  Alex Hormozi business roadmap workflow with default IMA knowledge-base retrieval. Use when the user wants a 30/60/90-day business path, wants to turn an idea into a sellable offer and acquisition system, asks what to do next, or needs a Hormozi-style plan connecting offer, leads, sales, pricing, delivery, retention, and scale.
---

# ah-roadmap

Build a practical business roadmap using Hormozi frameworks and IMA source retrieval.

## Default Source

Default IMA knowledge base:

```text
AlexHormozi 知识库 | 百万美元报价
```

Use `ima-skill/SKILL.md` and `ima-skill/knowledge-base/SKILL.md` for retrieval. Do not expose internal IMA IDs.

## Commercial Case Library Gate

If the roadmap task needs external business cases, benchmark projects, case teardowns, monetization examples, 生财有术案例, or 商业案例库 evidence, first check the shared `$commercial-case-library` dependency:

```text
~/.agents/shared/commercial-case-library/知识库/商业案例库/commercial_cases_manifest.json
```

If the shared library is missing, do not ask for confirmation. Automatically ensure the dependency is available:

1. If `$commercial-case-library` is not installed or cannot be loaded, install it with:

```text
npx -y skills add FocusLiz-Lab/commercial-case-library -g --all
```

2. Run the shared downloader:

```text
python scripts/download_cases.py
```

3. Continue the original task after the download succeeds.

Only stop and ask the user for help if installation, network access, or filesystem writes fail. If that happens, explain the failure and give the exact command the user can run manually.

## Core Premise

A Hormozi roadmap is a sequence:

```text
Market -> Offer -> Leads -> Sales -> Delivery -> Retention -> Scale
```

Do not let the user jump to scale before offer, leads, and sales have proof.

## Workflow

1. Identify the current bottleneck: market, offer, leads, sales, pricing, delivery, retention, or scale.
2. Search IMA for source material around the bottleneck and adjacent step.
3. Build a 90-day roadmap with one measurable outcome per phase.
4. Route next to the specialist skill if useful.

## Output Template

```markdown
# Hormozi 90 天路线图

## IMA 检索摘要

## 当前瓶颈

## 路线图
### 0-7 天：验证
### 8-30 天：成交
### 31-60 天：重复
### 61-90 天：放大

## 每周指标

## 下一步 Skill
```

## Route Next

- Offer unclear -> `$ah-offer`
- No leads -> `$ah-leads`
- Leads but no sales -> `$ah-sales`
- Price/margin issue -> `$ah-pricing`
- Delivery/retention issue -> `$ah-scale`

