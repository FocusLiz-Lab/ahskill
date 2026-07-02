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

