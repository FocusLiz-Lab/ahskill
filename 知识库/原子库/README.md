# 原子库说明

这个目录存放 Alex Hormozi 风格 workflow 的抽象知识原子，用于让 skill 在没有完整 IMA 检索结果时，仍能使用稳定的结构化方法论进行分析。

当前 `atoms.jsonl` 是发布安全的种子原子库：它不是逐条从推文、视频文稿或书籍原文自动抽取的结果，而是面向 skill workflow 的抽象方法论单元。

如果后续要制作严格的来源型原子库，应从用户有权使用的推文归档、视频文稿、笔记或 IMA 检索结果中提炼，并只发布抽象后的知识原子，不发布原始材料。

## 资料边界

本目录只包含抽象后的方法论单元，不包含 Alex Hormozi 的原书、PDF、付费材料、YouTube 转录稿、社交媒体原文、课程原文或任何受版权保护的原始资料。

如果需要基于具体资料回答，请优先使用默认 IMA 知识库：

```text
AlexHormozi 知识库 | 百万美元报价
```

## 文件结构

```text
原子库/
├── README.md
└── atoms.jsonl
```

## 字段说明

`atoms.jsonl` 每行是一个 JSON 对象。

| 字段 | 类型 | 说明 |
|---|---|---|
| id | string | 原子 ID，格式为 `AH_ATOM_001` |
| knowledge | string | 抽象后的知识点陈述 |
| topics | string[] | 主题标签 |
| skills | string[] | 关联 skill |
| type | string | `principle` / `method` / `checklist` / `diagnosis` / `anti-pattern` / `metric` |
| confidence | string | `high` / `medium` / `low` |
| use_when | string | 适用场景 |
| source_note | string | 来源边界说明 |

如果是从具体材料抽象出来的来源型原子，可以额外增加这些字段：

| 字段 | 类型 | 说明 |
|---|---|---|
| source_type | string | `tweet` / `youtube` / `note` / `ima` |
| source_ref | string | 可公开引用的来源标识；不要写私有文件路径 |
| source_date | string | 来源日期，可为空 |
| extraction_note | string | 提炼说明，不放原文 |

## 使用规则

- 原子库只能作为抽象框架和分析支架。
- 涉及具体原文、出处、书中表述、案例细节时，必须回到 IMA 检索。
- 不要把原子库内容包装成逐字引用。
- 如果原子库和 IMA 检索结果冲突，以 IMA 检索结果为准。
- 输出时要区分“IMA 检索证据”和“框架推断”。
