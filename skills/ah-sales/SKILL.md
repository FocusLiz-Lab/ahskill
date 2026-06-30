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
