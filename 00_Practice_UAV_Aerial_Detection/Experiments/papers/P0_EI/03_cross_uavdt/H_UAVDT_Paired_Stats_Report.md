# Stage H — UAVDT 配对统计（帧级 + 50 序列 cluster bootstrap）

- **Run ID：** `P0-BENCH-H-UAVDT-PAIRED-20261006-01`（2026-10-06 登记；PASS）
- **性质：** CPU-only 再分析；**无新推理、无训练**。输入 = 已冻结的 `03_cross_uavdt/data/E_FULL_per_image_metrics.csv`（Stage E，`P0-BENCH-E-UAVDT-20260918-FULL`，40735 帧 × 5 方法，**GTX 1660 SUPER / UAV_BT1**）。
- **脚本：** `P0_Benchmark/stage_h/run_h_paired_stats.py`（参数化副本；通过 importlib 原样调用冻结的 `stage_f/run_stage_f_paired_stats.py` 中的 `load_by_image / paired / wilcoxon_signed_rank / holm / wilson / bootstrap_pair` 与常量 `PRIMARY / SECONDARY / N_BOOT=10000 / SEED=20260917`；冻结脚本未改动）。
- **运行环境：** UAV_BT2 = Python 3.10.22, numpy 2.2.6, **scipy 1.15.3**（cheerhin, CPU）。
- **数据：** `03_cross_uavdt/data/H_UAVDT_PAIRED_summary.json`、`H_UAVDT_PAIRED_table.csv`；复现核对 `02_paired_stats/data/H_FREPRO_check.json`、`H_FREPRO_summary_UAV_BT2.json`。

## 1. 环境差异与 Stage F 复现核对（mode `check-f`）

| 项 | Stage F 原运行（2026-09-17） | 本次 |
|---|---|---|
| 环境 | UAV_BT1：Python 3.12.14, numpy 2.5.2, **无 scipy** | UAV_BT2：Python 3.10.22, numpy 2.2.6, scipy 1.15.3 |
| 统计实现 | 纯 numpy/math（Wilcoxon 为带 tie / continuity 校正的正态近似；bootstrap 为 `np.random.default_rng(SEED)`） | 同一冻结函数；scipy **未被调用**，仅记录版本 |

用冻结函数在 UAV_BT2 上对 `D_TESTDEV_per_image_metrics.csv` 重算 Stage F 全部输出，与 `F_summary.json` 逐键比较：**0 处不一致，最大相对差 0.0**（逐位一致）。另写的向量化 bootstrap（相同 rng 抽样序列，bincount 加权）与冻结 bootstrap 亦逐位一致（max rel diff 0.0；耗时 2.3 s vs 66.6 s），UAVDT 帧级 bootstrap 使用该向量化版本。
→ **VisDrone Stage F 数字在 UAV_BT2 下完全复现**；scipy 版本差异对 Stage F 无影响。

## 2. UAVDT 结果（Δ = A − B；时延全部为 **GTX 1660 SUPER / UAV_BT1** 一次性计时）

帧级 CI = 冻结 `bootstrap_pair`（逐帧重抽样，B=10000）；序列 CI = 按 50 个序列整体重抽样（B=10000，seed 20260917，比值在重抽样后池化重算）。序列级 Wilcoxon = 冻结 `wilcoxon_signed_rank` 作用于每序列 small recall（M0801 无 small GT，排除 → n=49）；次要对用冻结 `holm` 校正。

| 对 A vs B | Δsmall recall | 帧级 95% CI | **序列 95% CI** | 序列 Wilcoxon p（Holm） | 序列 A优/B优/平 | Δprecision（序列 CI） | Δmean ms 1660（序列 CI） |
|---|---:|---|---|---|---|---|---|
| **F1280 vs DensK1**（主对） | **+0.0257** | [0.0245, 0.0269] | **[0.0100, 0.0403]** | 9.9e-4（主对，不校正） | 37/12/0 | +0.0244 [0.0168, 0.0326] | +0.11 [−0.50, 0.70] |
| F640 vs F1280 | −0.0849 | [−0.0872, −0.0825] | [−0.1203, −0.0468] | 1.4e-6（5.6e-6） | 7/41/1 | +0.0584 [0.0479, 0.0692] | −16.34 [−16.97, −15.70] |
| F1280 vs UnifAll | +0.0105 | [0.0096, 0.0114] | [0.0012, 0.0180] | **0.322（0.322）** | 30/18/1 | +0.0403 [0.0327, 0.0503] | −14.10 [−14.99, −13.20] |
| F1280 vs SAHI640 | +0.0332 | [0.0311, 0.0352] | [0.0039, 0.0732] | 4.0e-4（1.2e-3） | 36/13/0 | +0.0189 [0.0044, 0.0368] | −130.92 [−137.56, −123.98] |
| DensK1 vs UnifAll | −0.0152 | [−0.0158, −0.0146] | [−0.0236, −0.0072] | 4.9e-8（2.4e-7） | 4/40/5 | +0.0159 [0.0106, 0.0221] | −14.21 [−14.70, −13.69] |
| DensK1 vs SAHI640 | +0.0074 | [0.0055, 0.0095] | **[−0.0303, 0.0553]** | 0.017（0.033） | 33/15/1 | −0.0055 [−0.0174, 0.0089] | −131.03 [−137.87, −123.91] |

主对帧级时延 Wilcoxon p = 0.096（1660 上不可区分；序列 CI 亦跨 0）。

## 3. 读法

1. **帧级检验严重高估显著性**：UAVDT 为 50 段视频，帧高度自相关；帧级 p（如主对 3.6e-293）不可作为推断依据。推断以序列 cluster bootstrap / 序列级 Wilcoxon 为准。
2. **主对（F1280 vs DensK1）在序列聚类后仍成立**：small recall +0.026（序列 CI [0.010, 0.040]），precision +0.024（[0.017, 0.033]），37/49 序列 F1280 更优；1660 时延差 +0.11 ms，CI 跨 0（不可区分）。与 VisDrone C1 的精度方向一致。
3. **F1280 vs UnifAll 依赖序列**：池化 Δ 为正（序列 CI [0.0012, 0.018]，下界接近 0），但序列级 Wilcoxon 不显著（p=0.32）；每序列差的均值 −0.0002、中位数 +0.004 —— 池化增益主要来自少数 GT 量大的序列。UnifAll 在 1660 上多花约 14 ms 且 precision 低 0.040。
4. **DensK1 vs SAHI640 未确立**：序列 CI 跨 0，而序列级 Wilcoxon（Holm 0.033）偏向 DensK1，两种口径不一致（序列间异质），按保守读法记为“未确立差异”。
5. 时延列全部来自 1660 / UAV_BT1；本 Run 不涉及 5060 Ti。

## 4. 对 C2（如何选协议）的含义

在 UAVDT（1024×540 视频帧）上，F1280 对 DensK1、SAHI640 的 small recall 与 precision 优势在**序列层面**也成立，且在 1660 上与 DensK1 时延不可区分、比 SAHI640 少约 131 ms；对 UnifAll 则是“精度不低、少约 14 ms（1660）、small recall 优势依赖序列”。选择协议时应以**序列/场景**为统计单元，而非帧；对视频数据，帧级显著性不能作为选协议的依据。
