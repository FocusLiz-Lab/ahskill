---
name: ah-content
description: |
  Alex Hormozi content workflow with default IMA knowledge-base retrieval. Use when the user wants content ideas, hooks, scripts, posts, short videos, titles, content angles, launch content, educational content, offer content, lead-generation content, or to turn Hormozi materials into reusable content assets.
---

# ah-content

Turn Hormozi source material into content that supports an offer or acquisition goal.

## Default Source

Default IMA knowledge base:

```text
AlexHormozi 知识库 | 百万美元报价
```

Use `ima-skill/SKILL.md` and `ima-skill/knowledge-base/SKILL.md` for retrieval. Search terms should match the user's offer and platform, plus `hook`, `content`, `ads`, `brand`, `launch`, `标题`, `内容`, `短视频`.

## Commercial Case Library Gate

If the content task needs external business cases, benchmark posts/products, teardown angles, lead-generation cases, 生财有术案例, or 商业案例库 evidence, first check the shared `$commercial-case-library` dependency:

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

Content should do one job:

```text
Attract right buyer -> Create problem awareness -> Increase belief -> Move to offer
```

## Output Template

```markdown
# Hormozi Content Map

## IMA 检索摘要

## Content Goal

## Buyer Belief Gaps

## 5 Content Pillars

## 30 Topic Ideas

## 10 Hooks

## CTA
```

## Quality Bar

- Do not create content detached from an offer.
- Every topic should move the buyer closer to awareness, trust, or action.
- If the offer is unclear, route to `$ah-offer`.

