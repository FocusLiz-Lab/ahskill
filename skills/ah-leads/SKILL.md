---
name: ah-leads
description: |
  Alex Hormozi lead-generation workflow with default IMA knowledge-base retrieval. Use when the user wants more leads, better leads, lead magnets, acquisition channels, marketplace traffic, content funnels, paid ads, warm outreach, cold outreach, referrals, affiliates, audience growth, or $100M Leads applications.
---

# ah-leads

Diagnose and design the lead-generation system.

## Default Source

Default IMA knowledge base:

```text
AlexHormozi 知识库 | 百万美元报价
```

Use `ima-skill/SKILL.md` and `ima-skill/knowledge-base/SKILL.md` for retrieval. Search terms usually include `100M Leads`, `lead magnet`, `core four`, `affiliate`, `warm outreach`, `cold outreach`, `paid ads`, `content`, `获客`, `潜在客户`.

## Commercial Case Library Gate

If the lead-generation task needs external acquisition examples, channel examples, lead magnet examples, growth case studies, ad/content funnel cases, 生财有术案例, or 商业案例库 evidence, first check the shared `$commercial-case-library` dependency:

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

Map the user's situation:

```text
Audience -> Channel -> Lead Magnet -> Capture -> Nurture -> Sales Conversion
```

Separate four problems:

- Exposure problem: not enough people see it.
- Click problem: title/hook/creative is weak.
- Lead problem: no reason to raise hand.
- Quality problem: wrong promise or wrong audience.

## Output Template

```markdown
# Leads Diagnosis

## IMA 检索摘要

## 当前获客瓶颈

## Channel Choice

## Lead Magnet

## 7-Day Lead Test

## Metrics
- Exposure:
- Click:
- Lead:
- Consult:
- Sale:
```

## Quality Bar

- Do not prescribe more content before identifying the channel and offer.
- Every lead plan must include one measurable test.
- If the user's offer is weak, route back to `$ah-offer`.

