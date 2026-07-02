---
name: ah-pricing
description: |
  Alex Hormozi pricing and money-model workflow with default IMA knowledge-base retrieval. Use when the user asks how to price, raise prices, improve margins, design price tiers, choose low-ticket vs high-ticket, create risk reversal, improve profit, cash flow, monetization, or apply $100M Money Models and $100M Offers pricing logic.
---

# ah-pricing

Design price around value, proof, margin, and buyer risk.

## Default Source

Default IMA knowledge base:

```text
AlexHormozi 知识库 | 百万美元报价
```

Use `ima-skill/SKILL.md` and `ima-skill/knowledge-base/SKILL.md` for retrieval. Search terms usually include `pricing`, `raise prices`, `margin`, `profit`, `money model`, `cash flow`, `定价`, `提价`, `利润率`.

## Commercial Case Library Gate

If the pricing task needs external pricing examples, business model cases, monetization examples, tier examples, 生财有术案例, or 商业案例库 evidence, first check the shared `$commercial-case-library` dependency:

```text
~/.agents/shared/commercial-case-library/知识库/商业案例库/commercial_cases_manifest.json
```

If missing, pause and ask:

```text
这个定价任务需要商业案例库，但本地共享案例库还没有下载。是否现在下载？下载一次后 ahskill、dkskill、lhskill、openskill 都可以共用。
```

If the user agrees, route to `$commercial-case-library` and run its downloader, then continue. If the user declines, continue with Hormozi source material only and say no commercial-case retrieval was used.

## Core Framework

Price diagnosis:

```text
Buyer value -> Believability -> Delivery cost -> Risk reversal -> Tier ladder -> Price test
```

## Output Template

```markdown
# Pricing Plan

## IMA 检索摘要

## 当前价格问题

## Value Gap

## Recommended Tiers
- Entry:
- Core:
- Premium:

## Risk Reversal

## 7-Day Price Test
```

## Quality Bar

- Do not raise price without improving perceived value or proof.
- Price tiers must map to different buyer readiness.
- If promise is vague, route to `$ah-offer`.
