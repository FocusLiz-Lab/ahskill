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

## Commercial Case Library Gate

If the scaling task needs external scale examples, delivery/retention cases, hiring/system cases, benchmark companies, 生财有术案例, or 商业案例库 evidence, first check the shared `$commercial-case-library` dependency:

```text
~/.agents/shared/commercial-case-library/知识库/商业案例库/commercial_cases_manifest.json
```

If missing, pause and ask:

```text
这个规模化任务需要商业案例库，但本地共享案例库还没有下载。是否现在下载？下载一次后 ahskill、dkskill、lhskill、openskill 都可以共用。
```

If the user agrees, route to `$commercial-case-library` and run its downloader, then continue. If the user declines, continue with Hormozi source material only and say no commercial-case retrieval was used.

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
