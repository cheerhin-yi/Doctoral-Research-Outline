# P0_EI 写作提纲（现行）

依据：[P0_Two_Paper_Plan_2026-09-22.md](P0_Two_Paper_Plan_2026-09-22.md)。  
旧机制／区域头提纲已归档，不作为执行依据。

## 贡献类型（摘要／Intro 口令）

1. 协议族对照实验，不是新检测器／新模块。  
2. 同一冻结权重、同一后处理门槛，只改「怎么推」。  
3. 把 F640／F1280／DensK1／UnifAll／SAHI640 放进同一坐标，用跨集配对统计报清何时增益、何时只是放大分辨率。

摘要写「系统比较并量化…」；负结果（排序不稳、仅数据集内）写入贡献边界。

## 建议结构

1. **Introduction** — 问题=协议选择（时间／分辨率／切片），不是又涨点。  
2. **Related Work** — 只归「推理时增强／切片评测」（见 `../Literature/` T1–T3）；不进新检测器栏。  
3. **Protocols & Evaluation** — 五协议定义、冻结 SHA、VisDrone／UAVDT 口径、配对统计、1660／4090 分表。  
4. **Results** — 主表：小目标召回、精度、时延分表、前向次数；配对差图优先于 AP 榜。  
5. **Failure & Boundaries** — 负结果与适用边界。  
6. **Conclusion** — 两项以内、证据支持的句子。

## 证据指针

| 章节需要 | 路径 |
|---|---|
| 冻结与映射 | `../Experiments/papers/P0_EI/00_freeze/` |
| VisDrone 主精度 | `../Experiments/papers/P0_EI/01_visdrone_main/` |
| 配对统计 | `../Experiments/papers/P0_EI/02_paired_stats/` |
| UAVDT | `../Experiments/papers/P0_EI/03_cross_uavdt/` |
| 1660 时序 | `../Experiments/papers/P0_EI/04_timing/` |
| 近邻表／失败例／复现（待补） | `../Experiments/papers/P0_EI/05_packaging/` |

## 本篇不做

开训；改检测头；把第二篇的决策切片写进本篇主张；1660 与 4090 混表。
