---
name: ah-scale
description: |
  Alex Hormozi scaling workflow with default IMA knowledge-base retrieval. Use when the user asks how to scale a service, product, knowledge business, team, operations, delivery, retention, LTV, hiring, systems, operators, bottlenecks, or move from manual work to repeatable growth.
---

# ah-scale

Diagnose the bottleneck that prevents repeatable growth.

## Default Source

Default IMA knowledge base:

```text
AlexHormozi 知识库 | 百万美元报价
```

Use `ima-skill/SKILL.md` and `ima-skill/knowledge-base/SKILL.md` for retrieval. Search terms usually include `scale`, `operator`, `systems`, `retention`, `LTV`, `hiring`, `delivery`, `规模化`, `留存`, `招聘`.

## Core Framework

Scaling sequence:

```text
Acquisition -> Conversion -> Delivery -> Retention -> Talent -> Systems
```

Do not scale a broken offer or a non-repeatable delivery process.

## Output Template

```markdown
# Scale Diagnosis

## IMA 检索摘要

## 当前瓶颈

## System Map

## What To Stop Doing Manually

## Retention / LTV Levers

## 30-Day Systems Plan
```

## Quality Bar

- If there is no consistent sale, route to `$ah-offer` or `$ah-leads`.
- If delivery quality is weak, fix fulfillment before increasing traffic.
