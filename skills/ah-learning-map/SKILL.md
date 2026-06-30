---
name: ah-learning-map
description: |
  Alex Hormozi learning-map workflow with default IMA knowledge-base retrieval. Use when the user asks where to start, what Hormozi materials to study first, how to learn $100M Offers, $100M Leads, $100M Money Models, how to build a reading sequence, or how to turn the Hormozi knowledge base into a study plan, lesson map, or output-driven learning path.
---

# ah-learning-map

Turn the Hormozi knowledge base into a focused learning path tied to the user's goal.

## Default Source

Default IMA knowledge base:

```text
AlexHormozi 知识库 | 百万美元报价
```

Use `ima-skill/SKILL.md` and `ima-skill/knowledge-base/SKILL.md` for retrieval. Search IMA before recommending specific materials. Do not expose internal IMA IDs.

## Intake

Ask only for missing information:

```text
1. 你学习 Hormozi 的目标是什么：offer、获客、销售、定价、规模化、内容，还是整体商业框架？
2. 你现在处于哪一阶段：没看过、看了一点、已经在卖产品、已经有业务？
3. 你想要什么输出：学习路径、读书顺序、实战任务、内容选题、offer 方案？
```

## Routes

- Offer path: `$100M Offers` -> value equation -> guarantees/bonuses/scarcity/urgency -> one offer card.
- Leads path: `$100M Leads` -> lead magnets -> core four -> channel tests -> one acquisition plan.
- Sales path: sales/closing transcripts -> objections -> qualification -> one sales script.
- Pricing path: pricing/margin/profit materials -> one price test.
- Scaling path: LTV/retention/systems/operators -> one bottleneck map.
- Creator/content path: hooks/content/brand/ads materials -> 30 content angles.

## Output Template

```markdown
# Hormozi 学习地图

## 你的目标

## IMA 检索摘要
- 知识库：
- 检索词：
- 命中的材料：
- 可用证据：
- 不确定/缺失：

## 先看这 5 个
1.
2.
3.
4.
5.

## 7 天启动计划

## 30 天学习顺序

## 每次学习必须产出的东西

## 下一步 Skill
```

## Quality Bar

- Do not recommend "全部从头看".
- Learning must produce an output: offer card, lead magnet, sales script, price test, content plan, or bottleneck map.
- If IMA retrieval is unavailable, state the limitation clearly.
