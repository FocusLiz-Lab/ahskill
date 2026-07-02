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

