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

If missing, pause and ask:

```text
这个 offer 任务需要商业案例库，但本地共享案例库还没有下载。是否现在下载？下载一次后 ahskill、dkskill、lhskill、openskill 都可以共用。
```

If the user agrees, route to `$commercial-case-library` and run its downloader, then continue. If the user declines, continue with Hormozi source material only and say no commercial-case retrieval was used.

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
