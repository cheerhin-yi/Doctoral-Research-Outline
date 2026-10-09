# 练手论文研究计划：P0_EI（冻结检测器上的推理协议对比）

更新：2026-09-27（Asia/Shanghai）。当前事项与授权以 [`../00_Overview/Current_Stage.md`](../00_Overview/Current_Stage.md) 为准；唯一 ACTIVE = **P0_EI**。  
本页只写当前实际实验内容与结果主张；旧版 A0 铁路路线、训练接口审计、诊断准入、BTD1–BTD12 过程叙述已移除（见 Git 历史）。

## 1. 研究问题与边界

**问题：** 在同一冻结检测器、同一后处理门槛下，只改变推理协议（输入分辨率／是否切片／切哪些片），航拍小目标的召回、精度与端到端时延如何权衡？何时增益只是来自分辨率或覆盖范围？

- 工作题目：面向无人机航拍的时间预算约束小目标检测（成稿拟改为"推理协议对比／experimental evaluation"口径）。
- 论文类型：EI 会议对比／协议稿，**不是新检测器、不是新模块**；摘要写 experimental evaluation，不写 we propose。
- 边界：单目 RGB、无人机视角、已知类别二维小目标；轨道走廊不是方法前提；不把 VisDrone 结果写成铁路安全或高原泛化。
- 每篇最多两项主张；禁止用注意力／损失／蒸馏／剪枝／新检测头补证据；旧区域机制主张 P0-A-C1／C2 保持 **HOLD**。
- 目标：首投 **IJCNN 2027**（截稿 2027-01-31）；落选转投 **ICIP 2027**（截稿 2027-03-31）；不承诺录用。

## 2. 实验设置（已冻结）

| 项 | 内容 | 来源 |
|---|---|---|
| 检测器／权重 | YOLO11n，VisDrone train 本地训练 100 轮（BT1）；`11_Datasets/processed/VisDrone/BT1/BT1-LOCAL-20260913-01/train/weights/last.pt`，SHA256 `bc42d54e37acaf1f698af487439dc222fa86fb4498623e8cf954df14e0aa5533` | `Experiments/papers/P0_EI/00_freeze/Environment_Freeze.md`、`weight_sha_reverify.txt`、`00_freeze/provenance/BT1_100_Epoch_Archive.md` |
| 五协议 | F640（整图 640）／F1280（整图 1280）／DensK1（整图 640 + 密度最高单片）／UnifAll（整图 640 + 同网格全部 640 窗口）／SAHI640（sahi 默认切片） | `00_freeze/Environment_Freeze.md`、`00_freeze/DensK1_Definition.md` |
| 评价口径 | 本项目 VisDrone 兼容匹配器（`diagnose_bt1.prepare_gt`／`match_gt`）；conf=0.25、IoU=0.5；报告 precision 与 small recall（small：原图 0<w·h<1024）；**不是 AP** | `00_freeze/Environment_Freeze.md`、`00_freeze/provenance/A0-07_Evaluator_Semantics_Check.md` |
| 数据 | VisDrone2019-DET test-dev（Ultralytics 镜像本地 GT，1610 图）主评测；cal48 开发集；UAVDT DET（40735 帧，VisDrone→UAVDT 映射分前冻结）跨集 | `01_visdrone_main/StageD_Channel_Decision.md`、`00_freeze/class_mapping_preregister.json` |
| 硬件 | Stage A–F 在 GTX 1660 SUPER 上完成；Run G 正式时序在 RTX 5060 Ti 16GB（环境 UAV_BT2）上完成（2026-10-06），单列 | `00_freeze/gpu_snapshot.txt`；`04_timing/Timing_5060Ti_Table.md` |
| 代码 | `Experiments/P0_Benchmark/stage_{b,d,e,f}/run_stage_*.py`、`Experiments/diagnose_bt1.py`（SHA 见复现附录 §10） | `Experiments/papers/P0_EI/05_packaging/Reproducibility_Appendix.md` |

## 3. 会议主张（终稿措辞，2026-09-27；依据 Stage B–F；C1 时延部分 2026-10-06 按 Run G 改为分 GPU 表述）

| ID | 主张 | 状态 |
|---|---|---|
| **P0-EI-C1** | 在单一冻结 YOLO11n 权重与 conf 0.25／IoU 0.5 匹配口径下，VisDrone test-dev 上 F1280 比 DensK1 **更准**：small recall +0.0409（图级 bootstrap 95% CI [0.0355, 0.0462]），precision +0.0681（CI [0.0631, 0.0731]）。时延分 GPU 表述：在 **GTX 1660 SUPER（UAV_BT1）** 上两者时延**统计上不可区分**（逐图 Wilcoxon p = 0.235，均值差 −0.34 ms）；在 **RTX 5060 Ti（UAV_BT2）** 上 **F1280 更快**（均值差 −14.01 ms，95% CI [−14.22, −13.80]，p≈3.6e-264，1607／1610 张图更快；`P0-BENCH-G-5060TI-PAIRED-20261006-01`）。时延排序取决于 CPU／流水线：5060 Ti 运行中 GPU 平均利用率约 11%，CPU 为 Ryzen 5 5600G（Windows“平衡”电源计划），耗时未分解；不写不带 GPU 名称的“更快”。 | SUPPORTED（Stage B/D/F/G） |
| **P0-EI-C2** | 选区／覆盖协议只移动召回–精度–时延权衡，没有跨数据集通用的最优协议：VisDrone 上全覆盖切片 UnifAll small recall 最高，但时延约 3.3×、精度下降；本冻结设置下 SAHI640 被 F1280 支配；UAVDT 上排序改变（F1280 居首）。 | SUPPORTED（Stage B/D/E/F） |

### 3.1 C1 证据

- **精度（Stage F，`P0-BENCH-F-TESTDEV-20260917-01`，`Experiments/papers/P0_EI/02_paired_stats/data/F_summary.json` → `primary_bootstrap`／`primary_wilcoxon_recall_small`）：** F1280 − DensK1：Δsmall recall +0.0409 [0.0355, 0.0462]；逐图 Wilcoxon p = 3.0e-28（N = 1499 张含小 GT 图）；Δprecision +0.0681 [0.0631, 0.0731]。聚合值（Stage D，`P0-BENCH-D-TESTDEV-20260917-01`，`01_visdrone_main/data/D_TESTDEV_summary.json`）：small recall 0.4004 vs 0.3596，precision 0.6753 vs 0.6071。
- **时延（1660）：** Stage F 单次时延逐图 Wilcoxon p = 0.235，逐图中位差 +0.25 ms（F1280 略慢），均值差 −0.34 ms（bootstrap CI [−0.66, −0.01]，约为均值的 1%）；Stage B（`P0-BENCH-B-TIMING-20260917-01`，cal48 48 图 × 3 次，`04_timing/data/B_TIMING_summary.json`）均值 33.15 vs 35.34 ms、p95 38.73 vs 43.20 ms。1660 上的结论只写"时延相当／不可区分"。
- **时延（RTX 5060 Ti，UAV_BT2）：** Run G 配对检验（`P0-BENCH-G-5060TI-PAIRED-20261006-01`，冻结 Stage F 统计函数，`04_timing/data/G_PAIRED_summary.json`）F1280 − DensK1 均值差 −14.01 ms（bootstrap 95% CI [−14.22, −13.80]），逐图中位差 −13.32 ms，Wilcoxon p≈3.6e-264，1607／1610 张图 F1280 更快；Run G test-dev 均值 26.25 vs 40.26 ms，cal48（3 次）27.43 vs 40.12 ms（`04_timing/Timing_5060Ti_Table.md`）。精度与 1660 冻结记录一致（|Δsmall recall| ≤ 0.014 个百分点）。
- **时延排序依赖 CPU／流水线：** 5060 Ti 运行中 GPU 平均利用率约 11%，CPU 为 Ryzen 5 5600G（Windows“平衡”电源计划），耗时未分解（单次 640 前向约 19 ms、1280 前向约 27 ms 仅为观察）。任何“更快”都必须带 GPU 名称。
- **跨集同向（描述性，无配对检验）：** Stage E（`P0-BENCH-E-UAVDT-20260918-FULL`，`03_cross_uavdt/data/E_FULL_summary.json`）small recall 0.7929 vs 0.7672，precision 0.3719 vs 0.3475，均值 33.1 vs 33.0 ms。

### 3.2 C2 证据

- **UnifAll（VisDrone，Stage D/F）：** small recall 0.4511，为五协议最高；相对 F1280 Δsmall recall +0.0507 [0.0464, 0.0551]、Δprecision −0.1629（0.5123 vs 0.6753）、单次均值 112.2 vs 33.7 ms（≈3.3×）；相对 DensK1 Δsmall recall +0.0916 [0.0866, 0.0966]、Δprecision −0.0948。Stage B：UnifAll 均值 96.4 ms，T = 40 ms 相对参考下超时率 1.00（F1280 0，DensK1 0.021）。来源 `F_summary.json` → `bootstrap_all`、`B_TIMING_summary.json`。
- **SAHI640 被 F1280 支配（本冻结设置：sahi 默认后处理 + 统一 finalize）：** VisDrone small recall 0.2184 vs 0.4004、precision 0.3587 vs 0.6753、373.2 vs 33.7 ms（F1280 − SAHI640：+0.1820 [0.1735, 0.1908]／+0.3166）；UAVDT 0.7597 vs 0.7929、0.3530 vs 0.3719、164.0 vs 33.1 ms。
- **跨集排序（small recall）：** VisDrone UnifAll 0.451 > F1280 0.400 > DensK1 0.360 > F640 0.239 > SAHI640 0.218；UAVDT F1280 0.793 > UnifAll 0.782 > DensK1 0.767 > SAHI640 0.760 > F640 0.708。UAVDT 上 UnifAll 时延比降为 1.43×（47.2 vs 33.1 ms）。跨集重排写作主张边界，不写"通用排序"。
- 近邻单轴差分见 `Experiments/papers/P0_EI/05_packaging/Neighbor_Protocol_Table.md`。

### 3.3 适用范围（成稿必须披露）

1. **硬件：** Stage B–F 时延来自 GTX 1660 SUPER（UAV_BT1；Stage B 为 3 次重复计时，Stage D/E 为单次运行计时）；Run G 时延来自 RTX 5060 Ti 16GB（UAV_BT2；2026-10-06），单独成表（`04_timing/Timing_5060Ti_Table.md`），不与 1660 合并。C1 时延结论随 GPU 不同：1660 上不可区分，5060 Ti 上 F1280 更快；排序依赖 CPU／流水线（GPU 利用率约 11%，Ryzen 5 5600G，Windows“平衡”电源计划，未分解）。
2. **指标：** 本项目匹配器的 precision／small recall（单一 conf 0.25、IoU 0.5），**不是** COCO／VisDrone 排行榜 AP，也不是 UAVDT 官方 MATLAB 评测；test-dev 为 Ultralytics 镜像本地 GT。
3. **模型：** 单一冻结权重（YOLO11n，seed 0），未跨检测器、权重或训练种子；不能外推为"对所有检测器成立"。
4. **统计：** 配对检验只覆盖 VisDrone test-dev（Stage F）；UAVDT 只有聚合值；cal48 为开发证据；不含选择漏检表或 GT oracle 数字。

### 3.4 修订记录

- 2026-09-27：C1 由"更准且更快"改为"时延统计不可区分下更准"；C2 由"区域分配存在可恢复空间……必须同时报告超时率与选择漏检"改为仅依据 Stage B–F 的选区／覆盖权衡陈述；旧 BTD8／BTD1–BTD11 依据退出主张（Git 历史保留）。
- 2026-10-06（用户决定）：C1 时延部分改为分 GPU 表述（1660 SUPER 不可区分；RTX 5060 Ti 上 F1280 更快），并注明时延排序依赖 CPU／流水线；C1 精度部分不变。

## 4. 实验进度

| Stage | Run ID | 状态 | 证据目录（`Experiments/papers/P0_EI/`） |
|---|---|---|---|
| A 冻结 | `P0-BENCH-A-ENV-20260917-01` | PASS | `00_freeze/` |
| B 1660 计时 | `P0-BENCH-B-TIMING-20260917-01` | PASS | `04_timing/` |
| C cal48 精度（开发） | `P0-BENCH-C-CAL48-20260917-01` | PASS | `01_visdrone_main/` |
| D VisDrone test-dev | `P0-BENCH-D-TESTDEV-20260917-01` | PASS | `01_visdrone_main/` |
| E UAVDT 跨集 | `P0-BENCH-E-UAVDT-20260918-FULL` | PASS | `03_cross_uavdt/` |
| F 图级配对统计 | `P0-BENCH-F-TESTDEV-20260917-01` | PASS | `02_paired_stats/` |
| EI 包装 | — | DONE（近邻表、失败／边界例、复现附录、图 1–5） | `05_packaging/` |
| G 5060 Ti 正式时序 | `P0-BENCH-G-5060TI-{SMOKE,CAL48,TESTDEV}-20261001-01`；配对 `P0-BENCH-G-5060TI-PAIRED-20261006-01`（UAVDT 可选，未跑） | PASS（2026-10-06） | `04_timing/Timing_5060Ti_Table.md` |
| 稿件正文 | — | 未开始 | `Writing/P0_EI_Outline.md` |

## 5. 剩余工作

1. **5060 Ti 正式时序（Run G）：** **已完成（2026-10-06）**，SMOKE／CAL48／TESTDEV／PAIRED 全部 PASS，环境 `F:\Conda\envs\UAV_BT2`，权重／协议／评价器不变；结果单列 `Experiments/papers/P0_EI/04_timing/Timing_5060Ti_Table.md`。精度与 1660 一致（可忽略差异）；5060 Ti 配对检验显示 F1280 比 DensK1 显著更快（逐图中位差 −13.32 ms，p≈3.6e-264），而 1660 上不可区分（p = 0.235）。C1 已于 2026-10-06 按用户决定改为分 GPU 表述（见 §3）；“更准”部分不变。
2. **稿件正文：** 按 `Writing/P0_EI_Outline.md` 起草；导读与全部数字见 [`P0_EI_Paper_Overview_and_Experiments.md`](P0_EI_Paper_Overview_and_Experiments.md)。
3. 会期已定（2026-10-06）：首投 IJCNN 2027（2027-01-31），落选转投 ICIP 2027（2027-03-31）。

## 6. 禁止事项

新训练／微调；改 backbone、loss、检测头；看分后改类别映射或 conf；重复使用 test-dev 选策略；1660 与 5060 Ti 混表；把 VisDrone 结果写成铁路或高原结论；开 Paper 2–7。

> AI生成
