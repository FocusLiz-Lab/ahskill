---
name: ah-sales
description: |
  Alex Hormozi sales workflow with default IMA knowledge-base retrieval. Use when the user wants to improve sales calls, DMs, qualification, objection handling, closing, downsells, follow-up, high-ticket selling, scripts, consultative selling, or conversion from leads to buyers.
---

# ah-sales

Improve conversion from lead to buyer.

## Default Source

Default IMA knowledge base:

```text
AlexHormozi 知识库 | 百万美元报价
```

Use `ima-skill/SKILL.md` and `ima-skill/knowledge-base/SKILL.md` for retrieval. Search terms usually include `sales`, `close`, `objection`, `qualification`, `downsell`, `high ticket`, `成交`, `异议`, `销售`.

## Commercial Case Library Gate

If the sales task needs external sales examples, conversion examples, DM/call case studies, objection-handling examples, 生财有术案例, or 商业案例库 evidence, first check the shared `$commercial-case-library` dependency:

```text
~/.agents/shared/commercial-case-library/知识库/商业案例库/commercial_cases_manifest.json
```

If missing, pause and ask:

```text
这个销售任务需要商业案例库，但本地共享案例库还没有下载。是否现在下载？下载一次后 ahskill、dkskill、lhskill、openskill 都可以共用。
```

If the user agrees, route to `$commercial-case-library` and run its downloader, then continue. If the user declines, continue with Hormozi source material only and say no commercial-case retrieval was used.

## Core Framework

Diagnose the sales path:

```text
Lead intent -> Qualification -> Pain -> Desired result -> Objection -> Close -> Follow-up
```

Common failure modes:

- Talking to unqualified leads.
- Selling features instead of outcome.
- No problem diagnosis before price.
- Weak risk reversal.
- No follow-up system.

## Output Template

```markdown
# Sales Diagnosis

## IMA 检索摘要

## 当前转化瓶颈

## Qualification Questions

## Objection Map

## DM / Call Script

## Follow-Up Sequence
```

## Quality Bar

- Do not write manipulative scripts.
- Make the buyer's problem and next step clear before closing.
- If leads are low quality, route to `$ah-leads`.
