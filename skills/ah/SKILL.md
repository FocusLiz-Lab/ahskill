---
name: ah
description: |
  Alex Hormozi skill toolbox main router with default IMA knowledge-base grounding. Use when the user asks about Alex Hormozi, Hormozi frameworks, $100M Offers, $100M Leads, $100M Money Models, offers, leads, pricing, sales, customer acquisition, scaling, LTV, retention, money models, entrepreneurship mindset, learning paths, business roadmaps, content ideas, source search, or Hormozi-style diagnosis. By default, use the IMA knowledge base named "AlexHormozi 知识库 | 百万美元报价". Triggers include $ah, /ah, AlexHormozi, Alex Hormozi, Hormozi, 100M Offers, 100M Leads, 100M Money Models, 报价, 获客, 高客单价, 定价, 规模化, 学习地图, and 商业诊断.
---

# ah

Act as the main router for the Alex Hormozi skill toolbox. Identify the user's bottleneck and route to the most relevant workflow skill. If enough context exists, execute the routed workflow in the same answer.

## Default IMA Knowledge Base

All workflow skills default to:

```text
AlexHormozi 知识库 | 百万美元报价
```

Users do not need to mention this knowledge-base name. If they explicitly name another IMA knowledge base, use that name instead.

## Required Dependency

All source-grounded workflows use `ima-skill` for retrieval:

- `ima-skill/SKILL.md`
- `ima-skill/knowledge-base/SKILL.md`

Do not invent IMA APIs. Do not expose internal `knowledge_base_id`, `media_id`, or `folder_id` to the user.

If `ima-skill` is not installed or credentials are missing, tell the user to install/configure IMA first:

```text
请安装 ima 技能
下载地址：https://app-dl.ima.qq.com/skills/ima-skills-1.1.7.zip
API Key 获取：https://ima.qq.com/agent-interface
```

## Route Map

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
