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

If the sales task needs external sales examples, conversion examples, DM/call case studies, objection-handling examples, 生财有术案例, or 商业案例库 evidence, use the shared `$commercial-case-library` dependency before answering. Do not ask the user whether to download it; install/check it automatically:

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
## Hormozi Methodology First

Every answer must use Alex Hormozi methodology as the primary reasoning layer. For /ah requests, first ground the diagnosis, framing, and recommendation in Alex Hormozi sources or workflow principles:

1. Prefer the default IMA knowledge base `AlexHormozi 知识库 | 百万美元报价`.
2. If IMA is unavailable, rate-limited, permission-blocked, has weak/no hits, or local fallback is needed, use the local Alex Hormozi expert atom library and auto-bootstrap it when missing.
3. Only after the Alex Hormozi layer is established, add commercial cases when the question would benefit from proof, benchmarks, platform/channel examples, monetization examples, acquisition examples, or Chinese-market context.
4. Commercial cases are supporting evidence only. Do not let commercial cases replace Alex Hormozi methodology, and do not answer purely from the commercial case library unless no Alex Hormozi source is available; if that happens, label the answer as case-supported inference rather than Alex Hormozi-grounded.
5. In final answers, keep the distinction clear: Hormozi 方法论 for the core principle and 商业案例支撑 for examples.

## Dependency Auto-Bootstrap

If IMA is unavailable, rate-limited, permission-blocked, has weak/no hits, or the user explicitly wants local/offline retrieval, ensure the local Alex Hormozi expert atom library exists before answering. GitHub installs should include it when bundled; also check ~/.agents/skills/ah/知识库/原子库/atoms.jsonl and ~/.agents/skills/ah-download-atoms/知识库/原子库/atoms.jsonl. If both are missing, treat this as a light/partial install and call $ah-download-atoms or run python tools/download_full_atoms.py from the installed ah-download-atoms skill directory. Do not ask the user whether to download; do it automatically when local fallback is required.

If the request involves acquisition, traffic, channel choice, platform choice, Xiaohongshu/小红书, WeChat Official Account/公众号, private domain/私域, conversion, lead generation, product launch, business examples, benchmark projects, case studies, monetization examples, 生财有术案例, or any answer would benefit from case evidence, use $commercial-case-library automatically before answering. Do not ask the user whether to download it.
