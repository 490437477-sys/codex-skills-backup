---
name: temu-backend-keywords
description: "TEMU 后台搜索词与商品标签优化。覆盖 TEMU 卖家中心「商品描述」「搜索词」「类目属性」字段的填法、多语言（英 / 德 / 法 / 西 / 日 / 韩 / 葡）本地化、去重排序、字符限制利用、TEMU 搜索 A9-like 算法适配。当用户询问 TEMU 后台关键词、TEMU 搜索词、TEMU 商品标签、TEMU listing 后台词、TEMU SEO、TEMU 搜索优化、TEMU 多语言后台词、TEMU 字符限制、temu backend keywords、temu search terms、temu listing SEO 时使用。"
metadata: {"category":"temu","emoji":"馃徑"}
---

# TEMU Backend Keywords 馃徑

为 TEMU 卖家中心的后台字段（商品描述 / 搜索词 / 类目属性）生成最大化搜索曝光的关键词集合，适配多语言市场与 TEMU 搜索算法。

## Capabilities

- **多语言后台词生成**：英 / 德 / 法 / 西 / 日 / 韩 / 葡 七语种本地化关键词
- **去重排序**：与前台标题、主图文案、属性字段不重复的高价值词优先
- **字符限制利用**：每个字段按 TEMU 字符上限填满（中文 30、英文 250 等）
- **算法适配**：模拟 TEMU 搜索 A9-like 排序（标题权重 > 后台词 > 类目）
- **拼写变体覆盖**：美 / 英拼写、单复数、词形变化、连字符 / 空格变体

## When to Use

- 用户新链接上架，需要填全后台字段以获得搜索曝光
- 用户链接有曝光但自然单量低，需要排查后台词是否覆盖搜索盲区
- 用户进入新站点，需要做后台词本地化翻译
- 用户做季节性活动，需要在后台词加节日 / 节庆相关长尾词

## TEMU 后台字段速查

| 字段 | 字符上限（中 / 英） | 是否计入搜索权重 | 是否对买家可见 |
|---|---|---|---|
| 商品标题 | 60 / 120 | 高 | 是 |
| 商品描述 | 500 / 1000 | 中 | 是（详情页） |
| 搜索词（后台） | 30 / 250 | 高 | 否 |
| 类目属性 | 按类目固定项 | 中 | 是（参数表） |
| 卖点短句 | 30 / 60 | 中 | 是（详情页顶部） |
| SKU 变体名 | 20 / 50 | 低 | 是（下拉选项） |

> **重点**：搜索词字段（search terms / 后台关键词）是 TEMU 不直接展示但参与搜索匹配的核心字段，必须独立优化。

## Workflow

### Step 1 — 输入清单

向用户收集：

- 商品链接或 SPU 信息
- 目标站点（决定后台词语言）
- 现标题、现描述、现后台词（如有）
- 类目与属性字段当前填写

### Step 2 — 关键词池构建

调用 `temu-keyword-research` 或 `web_search` 抓：

- 类目核心词 + 长尾变体
- 用途词（gym / kitchen / travel 等场景）
- 受众词（women / men / kids / pet 等）
- 材质 / 颜色 / 尺寸词
- 节日 / 节庆关联词（black friday / christmas / mothers day）

### Step 3 — 去重排序

按优先级分桶：

1. 标题未覆盖的高搜索量词（必入后台）
2. 描述未提及但搜索频繁的词
3. 类目属性未勾选但相关的词
4. 拼写变体（美 / 英、连字符、词形）
5. 长尾低竞争词（补量）

### Step 4 — 多语言翻译

按目标站点翻译，使用本地化母语者词频习惯：

- DE：复合名词拆词、用逗号分隔
- FR：注意阴阳单复数、避免英语借词滥用
- JP：平假名 / 外来语 / 汉字三轨并行
- KR：英文音译 + 韩文混排
- ES / PT：注意拉美 / 巴西变体

### Step 5 — 字符填满与排版

按上限填满，按算法权重排序（高优先在前）：

```
搜索词（英）示例：
wireless earbuds, bluetooth headphones, sport earphones, gym workout earbuds,
ipx7 waterproof, noise cancelling, long battery, tws earphones,
auriculares inalambricos, ecouteur sans fil, kabellose ohrhorer
```

注意：

- 用空格 / 逗号分隔，TEMU 不强制单种分隔符
- 不重复堆词（重复不增加权重）
- 不放品牌词（除非自家品牌）
- 不放 ASIN / SKU / 价格词

### Step 6 — 监控与轮换

上线后第 7 / 30 / 60 天回看搜索词报告，把高曝光低转化的词移出后台，加入新长尾词。

## Output

| 字段 | 内容示例 |
|---|---|
| 搜索词（英文） | bluetooth speaker waterproof shower |
| 商品描述补充 | 120 词含 3-5 个长尾词 |
| 卖点短句 3 条 | 每条 60 字符含 1 个核心词 |
| 多语言版本 | DE / FR / ES / JP 各一套 |
| 字符利用率 | 100% |
| 去重确认 | 与前台零重复 |

## Quick Mode

只回答「这个 TEMU 链接后台词怎么填」时，输出 3 行：

1. 搜索词字段（按优先级 30 / 250 字符填满）
2. 商品描述补充关键词清单（5-8 个长尾词）
3. 多语言版本（目标站语言）

注意：TEMU 后台词字符上限与字段命名会随版本变化，上传前用 `web_search` 校准最新卖家中心文档。
