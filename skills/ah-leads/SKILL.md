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

If missing, pause and ask:

```text
这个获客任务需要商业案例库，但本地共享案例库还没有下载。是否现在下载？下载一次后 ahskill、dkskill、lhskill、openskill 都可以共用。
```

If the user agrees, route to `$commercial-case-library` and run its downloader, then continue. If the user declines, continue with Hormozi source material only and say no commercial-case retrieval was used.

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
