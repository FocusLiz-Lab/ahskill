---
name: ah-offer
description: |
  Alex Hormozi offer-design workflow with default IMA knowledge-base retrieval. Use when the user wants to design, improve, price, package, name, or validate an offer, including low-ticket products, knowledge bases, consulting, courses, templates, services, guarantees, bonuses, scarcity, urgency, risk reversal, value equation, or $100M Offers applications.
---

# ah-offer

Design an offer that is specific, believable, and easy to test.

## Default Source

Default IMA knowledge base:

```text
AlexHormozi 知识库 | 百万美元报价
```

Use `ima-skill/SKILL.md` and `ima-skill/knowledge-base/SKILL.md` for retrieval. Search terms usually include `100M Offers`, `value equation`, `guarantee`, `bonus`, `scarcity`, `urgency`, `pricing`, `报价`, `价值`, `保证`.

## Commercial Case Library Gate

If the offer task needs external offer examples, pricing examples, benchmark offers, product teardowns, monetization cases, 生财有术案例, or 商业案例库 evidence, first check the shared `$commercial-case-library` dependency:

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

Use the value equation:

```text
Value = Dream Outcome x Perceived Likelihood / (Time Delay x Effort & Sacrifice)
```

Then strengthen the offer with:

```text
Buyer -> Pain -> Promise -> Mechanism -> Proof -> Bonus -> Guarantee -> Price -> Test
```

## Output Template

```markdown
# Offer Card

## IMA 检索摘要

## Buyer

## Pain

## Promise

## Mechanism

## What They Get

## Bonuses

## Guarantee / Risk Reversal

## Price

## Landing Page Spine
1. Pain:
2. New mechanism:
3. Promise:
4. What they get:
5. Why now:
6. CTA:

## 7-Day Validation Plan
```

## Quality Bar

- Do not sell a "thing"; sell a result.
- The promise must be judged by the buyer.
- The first version should be sellable before it is complete.
- Do not make income guarantees unless the user has proof and risk capacity.

