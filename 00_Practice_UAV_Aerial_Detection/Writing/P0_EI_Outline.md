# P0_EI 写作提纲（现行）

依据：[P0_Two_Paper_Plan_2026-09-22.md](P0_Two_Paper_Plan_2026-09-22.md)；主张与证据全文见 [`../Research_Plan.md`](../Research_Plan.md) §3。

## 主张（终稿措辞，2026-09-27；仅依据 Stage B–F）

- **C1：** 在单一冻结 YOLO11n 权重与 conf 0.25／IoU 0.5 匹配口径下，VisDrone test-dev 上 F1280 比 DensK1 更准（small recall +0.0409，95% CI [0.0355, 0.0462]；precision +0.0681，CI [0.0631, 0.0731]），两者在 GTX 1660 SUPER 上的时延统计上不可区分（逐图 Wilcoxon p = 0.235，均值差 −0.34 ms）。不写"更快"。来源：`P0-BENCH-F-TESTDEV-20260917-01`（`02_paired_stats/data/F_summary.json`）、`P0-BENCH-B-TIMING-20260917-01`。
- **C2：** 选区／覆盖协议只移动召回–精度–时延权衡：VisDrone 上 UnifAll small recall 最高（0.4511，比 F1280 高 0.0507），但时延约 3.3×（112.2 vs 33.7 ms）且精度下降（0.5123 vs 0.6753）；本冻结设置下 SAHI640 在两集上均被 F1280 支配；UAVDT 上排序改为 F1280 > UnifAll > DensK1 > SAHI640 > F640。来源：`P0-BENCH-D-TESTDEV-20260917-01`、`P0-BENCH-E-UAVDT-20260918-FULL`、`P0-BENCH-F-TESTDEV-20260917-01`。
- **适用范围（写入摘要或结论的限定句）：** 时延仅 1660（5060 Ti 另表）；指标为匹配器 precision／small recall，不是 AP；单一冻结权重；配对检验只覆盖 VisDrone test-dev。
- 修订记录：2026-09-27 由"更准且更快／区域分配存在可恢复空间"改为上述措辞。

## 贡献类型（摘要／Intro 口令）

1. 协议族对照实验，不是新检测器／新模块。  
2. 同一冻结权重、同一后处理门槛，只改「怎么推」。  
3. 把 F640／F1280／DensK1／UnifAll／SAHI640 放进同一坐标，用配对统计与跨集结果报清何时增益、何时只是放大分辨率或覆盖。

摘要写「系统比较并量化…」；负结果（跨集排序不稳）写入贡献边界。

## 建议结构

1. **Introduction** — 问题=协议选择（时间／分辨率／切片），不是又涨点。  
2. **Related Work** — 只归「推理时增强／切片评测」（见 `../Literature/` T1–T3）；不进新检测器栏。  
3. **Protocols & Evaluation** — 五协议定义、冻结 SHA、VisDrone／UAVDT 口径、配对统计、1660／5060 Ti 分表。  
4. **Results** — 主表：小目标召回、精度、时延分表、前向次数；配对差图优先于 AP 榜。  
5. **Failure & Boundaries** — 负结果与适用边界。  
6. **Conclusion** — 只写上方 C1／C2。

## 证据指针

| 章节需要 | 路径 |
|---|---|
| 冻结与映射 | `../Experiments/papers/P0_EI/00_freeze/` |
| VisDrone 主精度 | `../Experiments/papers/P0_EI/01_visdrone_main/` |
| 配对统计 | `../Experiments/papers/P0_EI/02_paired_stats/` |
| UAVDT | `../Experiments/papers/P0_EI/03_cross_uavdt/` |
| 1660 时序（5060 Ti 表待补，单列） | `../Experiments/papers/P0_EI/04_timing/` |
| 近邻表／失败例／复现附录／图 1–5 | `../Experiments/papers/P0_EI/05_packaging/` |

## 本篇不做

开训；改检测头；把第二篇的决策切片写进本篇主张；1660 与 5060 Ti 混表；写"F1280 更快"。
