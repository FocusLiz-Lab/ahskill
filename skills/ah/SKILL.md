---
name: ah
description: |
  Alex Hormozi 商业增长 Skill 工具箱主入口。用于报价设计、获客系统、销售转化、定价、规模化、LTV、留存、商业路线图、内容选题、资料检索和 Hormozi 风格商业诊断。默认使用 IMA 知识库「AlexHormozi 知识库 | 百万美元报价」，并可在 IMA 不可用时读取本地原子库。触发词包括 $ah、/ah、Alex Hormozi、Hormozi、100M Offers、100M Leads、报价、获客、高客单价、定价、规模化、学习地图和商业诊断。
---

# ah Alex Hormozi 商业增长工具箱

这是 Alex Hormozi 商业增长工具箱的主入口。先判断用户当前的业务瓶颈，再路由到最合适的 workflow skill；如果上下文足够，直接在同一回答中完成对应工作流。

## 默认 IMA 知识库

所有 workflow skills 默认读取：

```text
AlexHormozi 知识库 | 百万美元报价
```

用户不需要每次输入这个知识库名称。如果用户明确指定其他 IMA 知识库，则优先使用用户指定的知识库。

## 必要依赖

所有需要资料依据的 workflow 都使用 `ima-skill` 做检索：

- `ima-skill/SKILL.md`
- `ima-skill/knowledge-base/SKILL.md`

不要臆造 IMA API。不要向用户暴露内部 `knowledge_base_id`、`media_id` 或 `folder_id`。

如果没有安装 `ima-skill` 或凭证缺失，先提示用户安装并配置 IMA：

```text
请安装 ima 技能
下载地址：https://app-dl.ima.qq.com/skills/ima-skills-1.1.7.zip
API Key 获取：https://ima.qq.com/agent-interface
```

## 路由表

| User intent | Route to | Use when |
|---|---|---|
| Learning path, reading order, where to start | `$ah-learning-map` | User asks how to study Hormozi, what to read first, or how to navigate the knowledge base. |
| Business path, 30/60/90-day roadmap, next steps | `$ah-roadmap` | User needs a plan connecting market, offer, leads, sales, delivery, retention, and scale. |
| Offer, package, guarantee, bonus, naming, validation | `$ah-offer` | User wants a stronger offer, productized service, knowledge product, course, template, or consulting package. |
| Leads, traffic, lead magnet, acquisition channel | `$ah-leads` | User has weak traffic, low inquiry volume, poor lead quality, or wants a lead-generation plan. |
| Sales, DMs, objections, closing, follow-up | `$ah-sales` | User gets leads but cannot convert them, needs scripts, objection handling, or qualification. |
| Pricing, price raise, profit, margin, tiers | `$ah-pricing` | User asks how to price, increase price, improve profit, or design a money model. |
| Scale, systems, hiring, retention, LTV, operations | `$ah-scale` | User has sales but delivery, retention, repeatability, or team/system bottlenecks. |
| Content, hooks, scripts, posts, launch assets | `$ah-content` | User wants content ideas, content map, short videos, titles, launch content, or educational posts. |
| Explicit IMA search/read/cite/troubleshooting | `$ah-ima` | User specifically asks to search, read, cite IMA, or debug IMA retrieval. |

## Commercial Case Library Gate

If the user asks for external commercial cases, benchmark projects, case teardowns, monetization examples, offer/pricing examples, lead-generation examples, sales examples, 生财有术案例, or asks to "找案例/拆案例/参考案例/对标/商业案例库", use the shared `$commercial-case-library` dependency before answering. Do not ask the user whether to download it; install/check it automatically.

Check for:

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

## Clarify Once

If the user is vague, ask one question:

```text
你现在最想处理哪一块：学习地图、商业路线图、报价/offer、获客/leads、销售成交、定价利润、规模化运营、内容，还是从 IMA 资料里找原文？
```

After the answer, route immediately.

## Handoff Format

```text
这个问题交给 $skill-name。
原因：{one sentence}
需要输入：{what the user should provide next, if anything}
```

## Quality Bar

- Do not solve everything inside the router when a specialist skill is a better fit.
- Default to IMA-grounded workflow skills for substantive Hormozi claims.
- Do not imitate Alex Hormozi's persona.
- Do not invent quotes, episode titles, dates, revenue numbers, or book claims.
- Do not expose IMA internal IDs unless the user explicitly asks for debugging.
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
