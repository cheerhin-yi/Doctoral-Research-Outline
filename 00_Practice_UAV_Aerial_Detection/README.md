# 练手论文 P0_EI：无人机航拍小目标检测的推理协议对比

目录名：`00_Practice_UAV_Aerial_Detection`（本目录唯一索引页）。当前事项以 [`../00_Overview/Current_Stage.md`](../00_Overview/Current_Stage.md) 为准；唯一 ACTIVE = P0_EI。

## 文件索引

| 文件／目录 | 用途 |
|---|---|
| [`Research_Plan.md`](Research_Plan.md) | 研究问题、实验设置、**C1／C2 终稿主张与证据**、进度与剩余工作 |
| [`Mainline_A_Current.md`](Mainline_A_Current.md) | 近／中／远边界、资源与 5060 Ti 用途 |
| [`P0_EI_Paper_Overview_and_Experiments.md`](P0_EI_Paper_Overview_and_Experiments.md) | 论文概况与 Stage A–F 全部数字（导读，逐项注明来源文件与 Run ID） |
| [`Completion_Metrics.md`](Completion_Metrics.md) · [`Learning_Check_Baseline.md`](Learning_Check_Baseline.md) | 学习完成指标与检查基线 |
| [`Learning_Notes/`](Learning_Notes/README.md) | 学习笔记与记录模板 |
| [`Literature/`](Literature/README.md) | 文献主题矩阵 T1–T4、阅读清单与笔记 |
| [`Writing/P0_EI_Outline.md`](Writing/P0_EI_Outline.md) | 第一篇写作提纲（含 C1／C2 终稿措辞） |
| [`Writing/P0_Two_Paper_Plan_2026-09-22.md`](Writing/P0_Two_Paper_Plan_2026-09-22.md) | 两篇安排与投稿定位（已采用） |
| [`Experiments/papers/P0_EI/Run_Index.md`](Experiments/papers/P0_EI/Run_Index.md) | P0 证据槽 Run 索引 |
| [`../99_Attachments/查阅/Abbreviation_Glossary.md`](../99_Attachments/查阅/Abbreviation_Glossary.md) | 缩写释义 |

## 实验目录

```text
Experiments/
  diagnose_bt1.py                 评价匹配器（prepare_gt / match_gt / nms / axis_windows）
  P0_Benchmark/stage_{b,d,e,f}/   Stage B/D/E/F 运行脚本（import diagnose_bt1，路径不可移）
  papers/P0_EI/
    Run_Index.md
    00_freeze/          权重 SHA、环境、类别映射、DensK1 定义、config freeze
      provenance/       冻结件的来源记录：权重训练、VisDrone 文件审计、评价语义、DensK1(BTD8) 协议与结果
    01_visdrone_main/   Stage C/D + data/
    02_paired_stats/    Stage F + data/
    03_cross_uavdt/     Stage E + data/
    04_timing/          Stage B（1660）+ data/；5060 Ti 表待补（单列）
    05_packaging/       近邻表 / 失败例 / 复现附录 / figures/（图 1–5 + generate_plots.py）
```

证据槽规则：只收论文要用的报告与汇总表／CSV／JSON；不收 `.npy` 预测、smoke 跑、过程诊断长文；新跑必须带 Run ID 并把 summary／主 CSV 放进对应 `data/`。

## 硬边界（摘要）

- 单目 RGB、无人机视角、已知类别二维小目标；轨道走廊不是方法前提。
- 同一冻结权重，只比较推理协议；不新训、不改网络、不看分改映射。
- 每篇最多两个主张；1660 与 5060 Ti 时序分表。
