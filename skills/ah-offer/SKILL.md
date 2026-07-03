---
name: ah-offer
description: |
  Alex Hormozi offer-design workflow with local atom-library retrieval; IMA retrieval only when explicitly requested. Use when the user wants to design, improve, price, package, name, or validate an offer, including low-ticket products, knowledge bases, consulting, courses, templates, services, guarantees, bonuses, scarcity, urgency, risk reversal, value equation, or $100M Offers applications.
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

If the offer task needs external offer examples, pricing examples, benchmark offers, product teardowns, monetization cases, 生财有术案例, or 商业案例库 evidence, use the shared `$commercial-case-library` dependency before answering. Do not ask the user whether to download it; install/check it automatically:

```text
~/.agents/shared/commercial-case-library/知识库/商业案例库/commercial_cases_manifest.json
```

If the shared library is missing, do not ask for confirmation. Automatically ensure the dependency is available:

1. If `$commercial-case-library` is not installed or cannot be loaded, install it immediately without asking the user:

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
## Hormozi Methodology First

Every answer must use Alex Hormozi methodology as the primary reasoning layer. For /ah requests, first ground the diagnosis, framing, and recommendation in Alex Hormozi sources or workflow principles:

1. Prefer the local expert atom library and packaged method notes by default. Use the IMA knowledge base `AlexHormozi 知识库 | 百万美元报价` only when the user explicitly asks to search/read/cite/troubleshoot IMA.
2. If IMA is unavailable, rate-limited, permission-blocked, has weak/no hits, or local fallback is needed, use the local Alex Hormozi expert atom library and auto-bootstrap it when missing.
3. Only after the Alex Hormozi layer is established, add commercial cases when the question would benefit from proof, benchmarks, platform/channel examples, monetization examples, acquisition examples, or Chinese-market context.
4. Commercial cases are supporting evidence only. Do not let commercial cases replace Alex Hormozi methodology, and do not answer purely from the commercial case library unless no Alex Hormozi source is available; if that happens, label the answer as case-supported inference rather than Alex Hormozi-grounded.
5. In final answers, keep the distinction clear: Hormozi 方法论 for the core principle and 商业案例支撑 for examples.

## Dependency Auto-Bootstrap

If IMA is unavailable, rate-limited, permission-blocked, has weak/no hits, or the user explicitly wants local/offline retrieval, ensure the local Alex Hormozi expert atom library exists before answering. GitHub installs should include it when bundled; also check ~/.agents/skills/ah/知识库/原子库/atoms.jsonl and ~/.agents/skills/ah-download-atoms/知识库/原子库/atoms.jsonl. If both are missing, treat this as a light/partial install and call $ah-download-atoms or run python tools/download_full_atoms.py from the installed ah-download-atoms skill directory. Do not ask the user whether to download; do it automatically when local fallback is required.

If the request involves acquisition, traffic, channel choice, platform choice, Xiaohongshu/小红书, WeChat Official Account/公众号, private domain/私域, conversion, lead generation, product launch, business examples, benchmark projects, case studies, monetization examples, 生财有术案例, or any answer would benefit from case evidence, use $commercial-case-library automatically before answering. Do not ask the user whether to download it.
