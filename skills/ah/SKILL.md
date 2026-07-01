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
