# Alex Hormozi Skill 使用说明

这是一组基于 IMA 知识库的 Alex Hormozi workflow skills。ahskill 主入口负责路由，子 skill 负责具体任务，所有 workflow 默认读取同一个 IMA 知识库。

## 默认 IMA 知识库

```text
AlexHormozi 知识库 | 百万美元报价
```

用户不需要每次输入这个知识库名称。只有当用户想使用其他 IMA 知识库时，才需要在提示词里说明。

## 依赖

需要先安装并配置 `ima-skill`。

IMA API Key 获取地址：

```text
https://ima.qq.com/agent-interface
```

如果 IMA 凭证缺失，skill 会提示用户先完成 IMA 配置，不会自动改用非 IMA 资料。

## 技能包

| Skill | 做什么 |
|---|---|
| `$ah` | 主入口。根据用户问题自动路由到合适的 Hormozi workflow。 |
| `$ah-learning-map` | 学习地图。回答先看什么、怎么学、如何把资料变成输出。 |
| `$ah-roadmap` | 商业路线图。把市场、offer、获客、销售、交付、留存、规模化串成 90 天路径。 |
| `$ah-offer` | Offer 设计。设计报价、包装、bonus、guarantee、命名、验证计划。 |
| `$ah-leads` | 获客系统。设计 lead magnet、渠道测试、内容/广告/外联/affiliate 获客。 |
| `$ah-sales` | 销售成交。处理私聊、销售脚本、异议、资格筛选、跟进。 |
| `$ah-pricing` | 定价利润。设计价格梯度、提价测试、利润率、money model。 |
| `$ah-scale` | 规模化运营。诊断系统、交付、留存、LTV、招聘、运营瓶颈。 |
| `$ah-content` | 内容系统。生成内容支柱、选题、hooks、脚本、launch 内容。 |
| `$ah-ima` | 可选 IMA 检索入口。用于显式搜索、阅读、引用或排查 IMA 检索。 |

## 推荐使用方式

普通用户优先用主入口：

```text
$ah 数字产品获客很差，按 Hormozi 框架拆一下。
```

明确知道任务类型时，可以直接调用子 skill：

```text
$ah-learning-map 系统学习 $100M Offers，先看哪些？
$ah-offer 为一个低价知识产品设计更强的 offer。
$ah-leads 产品曝光不少，但咨询很少，设计一个获客测试。
$ah-sales 买家一直问但不下单，设计一套私聊成交路径。
$ah-pricing 低价产品想升级到更高价格，怎么设计价格梯度？
$ah-scale 已经有稳定成交，怎么把交付和复购做起来？
$ah-content 围绕这个 offer 做 30 个短内容选题。
```

## 常见主线

### 学习到实践

```text
ah-learning-map
    ↓
ah-offer
    ↓
ah-leads
```

### 从产品到成交

```text
ah-offer
    ↓
ah-leads
    ↓
ah-sales
```

### 从成交到放大

```text
ah-pricing
    ↓
ah-scale
    ↓
ah-content
```

### 显式 IMA 检索

```text
ah-ima
    ↓
对应 workflow skill
```

## 输出格式

大多数 workflow 都会包含：

```markdown
## IMA 检索摘要
- 知识库：
- 检索词：
- 命中的材料：
- 可用证据：
- 不确定/缺失：

## 核心判断

## Hormozi 框架

## 下一步动作
1.
2.
3.
```

## 分发建议

完整分发包含：

```text
ah/
ah-learning-map/
ah-roadmap/
ah-offer/
ah-leads/
ah-sales/
ah-pricing/
ah-scale/
ah-content/
ah-ima/
```

接收方需要：

1. 安装这些 skills。
2. 安装并配置 `ima-skill`。
3. 已加入ima知识库  `AlexHormozi 知识库 | 百万美元报价`。
4. 使用 `$ah` 或任一子 skill 开始提问。

## 设计原则

- 默认读取 `AlexHormozi 知识库 | 百万美元报价`。
- 只使用 IMA 作为资料检索来源。
- 不暴露 IMA 内部 ID。
- 不伪造引用、标题、日期、收入数字或书中观点。
- 没有实际检索到资料时，必须明确说明。
- 区分「IMA 检索证据」和「框架推断」。
- 不扮演 Alex Hormozi 本人，只做基于资料的分析和应用。

