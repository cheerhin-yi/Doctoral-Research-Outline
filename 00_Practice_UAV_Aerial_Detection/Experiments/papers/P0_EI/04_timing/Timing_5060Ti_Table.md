# Timing — RTX 5060 Ti 16GB（Run G，正式时序表）

> **单列表。** 本页只放 RTX 5060 Ti + `F:\Conda\envs\UAV_BT2` 的数字；GTX 1660 SUPER + UAV_BT1 的数字在 `StageB_Timing_Report.md`／`data/B_TIMING_*`，两者**不合并成同一张表或同一列**。文末 §6 的“仅供参考”并排节逐列标明 GPU 与环境。

## 1. 运行与条件

| 项 | 值 |
|---|---|
| Run ID | `P0-BENCH-G-5060TI-SMOKE-20261001-01`（冒烟，不进表）；`P0-BENCH-G-5060TI-CAL48-20261001-01`；`P0-BENCH-G-5060TI-TESTDEV-20261001-01`；`P0-BENCH-G-5060TI-PAIRED-20261006-01`（配对时延检验，新增） |
| Run ID 日期 | SMOKE／CAL48／TESTDEV 保留原计划日期 20261001（与已登记文档一致）；PAIRED 为本次新增，按登记日 20261006 |
| 运行时间 | 2026-10-06 16:23–16:53（Asia/Shanghai） |
| GPU | NVIDIA GeForce RTX 5060 Ti，16311 MiB，UUID `GPU-1d6d4cde-f073-217b-3867-015abdbd5478`，驱动 591.86，sm_120，功耗上限 180 W |
| CPU／电源计划 | AMD Ryzen 5 5600G（6C／12T）；Windows“平衡”计划（未改系统设置） |
| 环境 | `F:\Conda\envs\UAV_BT2`：Python 3.10.22，torch 2.7.1+cu128，cuDNN 90701，ultralytics 8.4.90（冻结同一 pinned zip），sahi 0.11.32，numpy 2.2.6，OpenCV 5.0.0，scipy 1.15.3（见 `../00_freeze/Environment_Delta_UAV_BT2_vs_UAV_BT1.md`） |
| 权重 | `BT1-LOCAL-20260913-01/train/weights/last.pt`，SHA256 `bc42d54e…0aa5533`（每次运行前由冻结脚本与启动器双重断言） |
| 代码 | 冻结脚本**原样调用**：`stage_b/run_stage_b_timing.py`（git blob `5ae22d60`）、`stage_d/run_stage_d_oneshot.py`（`6bf296a0`）、`diagnose_bt1.py`（`c739849a`）；参数化入口 `Experiments/P0_Benchmark/stage_g/run_stage_g.py` 只传 `--run-id`／`--max-images`／`--skip-extract` |
| 协议 | 与 1660 完全相同：conf_keep 0.25，NMS IoU 0.5，max_det 500；640 窗口 stride 512；SAHI 640／overlap 0.25／conf 0.001／默认后处理 |
| 计时边界 | 已解码图像 → 最终可评测检测框，含 `cuda.synchronize`，不含磁盘 I/O（同 `Reproducibility_Appendix.md`） |
| 预热 | CAL48：首图 3×(F640+F1280)（Stage B 默认）；TESTDEV：首图 2×F640（Stage D 默认） |
| 运行前 GPU 负载 | `nvidia-smi`：利用率 0%，无其他 python／计算进程（仅桌面图形进程，显存约 3.0–3.3 GiB 被桌面占用） |
| 运行中 GPU 监测（2 s 采样） | CAL48：利用率均值 10.7%（最大 55%），SM 时钟中位 2145 MHz；TESTDEV：利用率均值 11.4%（最大 75%），SM 时钟中位 1931 MHz，最高 42 °C |

## 2. 闸门

| 闸门 | 结果 | 依据 |
|---|---|---|
| SMOKE | **PASS** | GPU＝RTX 5060 Ti（cap 12.0）检测到；权重 SHA 与冻结锁一致；Stage B 2 张 cal48 × 5 方法 × 3 次、Stage D 3 张 test-dev × 5 方法均跑通，`summary.json`／`timings.csv`／`per_image_metrics.csv` 正常写出；3 张 test-dev 的 n_dets／tp／fp／small_tp 与 1660 Stage D 逐行一致 |
| CAL48 精度一致性 | **PASS（差异可忽略）** | 240 个（图, 方法）对中 22 对有 ±1–2 个框的差异；各方法 small_tp 总差 ≤ 1／2720（≤ 0.04 个百分点），见 §5 |
| TESTDEV | **PASS** | 1610 张 × 5 方法全部完成（墙钟 1406 s）；精度一致性：8050 对中 497 对有差异，各方法 small_tp 总差 ≤ 7／50431（≤ 0.014 个百分点），见 §5 |

## 3. 表 G-1　cal48 时延（RTX 5060 Ti，UAV_BT2；48 图 × 3 次 = n=144／方法）

来源 `data/G_CAL48_summary.json`（冻结 Stage B 脚本直接输出）；派生比值见 `data/G_TIMING_stats.json`。指标定义与 1660 表 B-1 相同。

| 方法 | mean (ms) | median (ms) | p90 | p95 | p99 | std | 相对 F640 耗时（mean 比） | speedup vs F640（F640 mean ÷ 方法 mean） |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| F640 | 19.91 | 19.11 | 22.65 | 24.82 | 30.30 | 2.72 | 1.00× | 1.000 |
| F1280 | 27.43 | 26.57 | 30.55 | 33.43 | 45.67 | 4.20 | 1.38× | 0.726 |
| DensK1 | 40.12 | 39.22 | 44.74 | 47.10 | 53.06 | 4.17 | 2.02× | 0.496 |
| UnifAll | 114.48 | 126.95 | 148.14 | 158.63 | 185.21 | 36.93 | 5.75× | 0.174 |
| SAHI640 | 427.50 | 466.90 | 618.29 | 642.03 | 724.33 | 160.53 | 21.47× | 0.047 |

| 方法 | 每图中位数均值 | 每图中位数 p95 | 三次输出不一致 |
|---|---:|---:|---:|
| F640 | 19.28 | 22.14 | 0 |
| F1280 | 26.85 | 30.10 | 0 |
| DensK1 | 39.71 | 44.26 | 0 |
| UnifAll | 112.83 | 153.89 | 0 |
| SAHI640 | 410.33 | 582.62 | 0 |

峰值显存（torch）：209082368 bytes（约 199.4 MiB）。

**表 G-2　cal48 超预算率（每图 3 次中位数 > T 的图像比例）**

| 方法 | T=20 | T=25 | T=30 | T=40 | T=50 | T=75 | T=100 |
|---|---:|---:|---:|---:|---:|---:|---:|
| F640 | 0.229 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| F1280 | 1.000 | 0.771 | 0.104 | 0.000 | 0.000 | 0.000 | 0.000 |
| DensK1 | 1.000 | 1.000 | 1.000 | 0.417 | 0.000 | 0.000 | 0.000 |
| UnifAll | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.729 | 0.729 |
| SAHI640 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

## 4. 表 G-3　VisDrone test-dev 时延（RTX 5060 Ti，UAV_BT2；1610 图，one-shot）

来源 `data/G_TESTDEV_per_image_metrics.csv`（冻结 Stage D 脚本输出）；统计见 `data/G_TIMING_stats.json`。每图 1 次测量，指标定义同 Stage B（std 为 ddof=1，分位数为 `np.percentile`）。

| 方法 | mean (ms) | median (ms) | p90 | p95 | p99 | std | 相对 F640 耗时（mean 比） | speedup vs F640 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| F640 | 19.85 | 18.68 | 24.01 | 26.68 | 32.51 | 3.18 | 1.00× | 1.000 |
| F1280 | 26.25 | 25.03 | 31.15 | 34.49 | 40.61 | 3.77 | 1.32× | 0.756 |
| DensK1 | 40.26 | 38.35 | 47.31 | 51.75 | 58.61 | 5.24 | 2.03× | 0.493 |
| UnifAll | 136.59 | 131.44 | 166.04 | 175.83 | 194.64 | 23.03 | 6.88× | 0.145 |
| SAHI640 | 507.10 | 498.16 | 646.22 | 691.71 | 787.28 | 110.25 | 25.55× | 0.039 |

**表 G-4　test-dev 超预算率（单次时延 > T 的图像比例）**

| 方法 | T=20 | T=25 | T=30 | T=40 | T=50 | T=75 | T=100 |
|---|---:|---:|---:|---:|---:|---:|---:|
| F640 | 0.303 | 0.076 | 0.022 | 0.000 | 0.000 | 0.000 | 0.000 |
| F1280 | 1.000 | 0.504 | 0.134 | 0.013 | 0.000 | 0.000 | 0.000 |
| DensK1 | 1.000 | 1.000 | 1.000 | 0.358 | 0.064 | 0.001 | 0.000 |
| UnifAll | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.971 | 0.970 |
| SAHI640 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

**表 G-5　图级配对时延检验（`P0-BENCH-G-5060TI-PAIRED-20261006-01`；冻结 Stage F 统计函数原样调用；N=1610；差值＝左 − 右）**

来源 `data/G_PAIRED_summary.json`、`data/G_PAIRED_wilcoxon_latency.csv`。Wilcoxon 为正态近似（含并列与连续性校正），bootstrap B=10000、seed 20260917，次要对做 Holm 校正，与 Stage F 相同。

| 对 | 逐图中位差 (ms) | 均值差 (ms) | bootstrap 95% CI（均值差） | Wilcoxon z | p | p（Holm） |
|---|---:|---:|---|---:|---:|---:|
| F1280 vs DensK1（主对） | -13.32 | -14.01 | [-14.22, -13.80] | -34.72 | 3.61e-264 | — |
| F640 vs F1280 | -6.10 | -6.40 | [-6.57, -6.23] | -33.82 | 1.02e-250 | 1.02e-250 |
| F1280 vs UnifAll | -105.58 | -110.34 | [-111.44, -109.28] | -34.75 | 1.19e-264 | 5.93e-264 |
| F1280 vs SAHI640 | -471.45 | -480.85 | [-486.16, -475.42] | -34.75 | 1.19e-264 | 5.93e-264 |
| DensK1 vs UnifAll | -92.35 | -96.33 | [-97.38, -95.27] | -34.75 | 1.19e-264 | 5.93e-264 |
| DensK1 vs SAHI640 | -458.40 | -466.84 | [-472.22, -461.52] | -34.75 | 1.19e-264 | 5.93e-264 |

- **主对 F1280 vs DensK1：** 在 5060 Ti 上 F1280 在 1607／1610 张图（99.8%）上比 DensK1 快，逐图中位差 −13.32 ms，均值差 −14.01 ms（CI [−14.22, −13.80]），p ≈ 3.6×10⁻²⁶⁴。**1660 上“两者时延统计上不可区分”（p = 0.235）的结论在 5060 Ti／UAV_BT2 上不成立**：这里 F1280 显著更快。
- 以上 p 值在 N=1610、几乎全部同号时已到正态近似的极端尾部，只说明“方向一致且极显著”，不要当精确值引用。

## 5. 精度一致性（与 1660 冻结记录逐图对比）

脚本 `Experiments/P0_Benchmark/stage_g/eval_g_accuracy.py`（调用冻结 `run_stage_d_oneshot.eval_one` → `diagnose_bt1.prepare_gt + match_gt`）。CAL48 参照 `../01_visdrone_main/data/C_cal48_metrics.csv`（Stage C＝1660 Stage B rep0 预测）与 `data/B_TIMING_timings.csv` 的 rep0 n_dets；TESTDEV 参照 `../01_visdrone_main/data/D_TESTDEV_per_image_metrics.csv`。

| 方法 | cal48 有差异的图 | cal48 Δ(n_dets／tp／fp／small_tp) | test-dev 有差异的图 | test-dev Δ(n_dets／tp／fp／small_tp) | test-dev small recall 5060 Ti ／ 1660 |
|---|---:|---|---:|---|---|
| F640 | 4／48 | -2／-1／-1／-1 | 49／1610 | -1／+0／-1／-2 | 0.2387／0.2388 |
| F1280 | 2／48 | +1／+1／+0／+1 | 71／1610 | -4／+1／-8／+1 | 0.4004／0.4004 |
| DensK1 | 5／48 | +0／+1／-2／+1 | 74／1610 | +2／+0／+2／+0 | 0.3596／0.3596 |
| UnifAll | 6／48 | -1／-1／-1／-1 | 147／1610 | -5／-10／+3／-7 | 0.4510／0.4511 |
| SAHI640 | 5／48 | +1／+0／+2／+0 | 156／1610 | +9／+0／+7／+4 | 0.2185／0.2184 |

- small_gt、valid_gt、ignored 完全一致（cal48 2720，test-dev 50431）；差异只是个别图上置信度贴近 0.25 阈值或 NMS 并列的框多／少 1–2 个。
- **差异量级：** cal48 各方法 |Δsmall_tp| ≤ 1（≤ 0.04 个百分点），test-dev 各方法 |Δsmall_tp| ≤ 7／50431（≤ 0.014 个百分点），|Δtp| ≤ 10／41705。F1280 − DensK1 的 test-dev Δsmall recall 为 0.04089（1660：0.04087）。判定为**可忽略**，C1-a 精度结论与 Stage D／F 不受影响。
- **可能原因：** 不同 GPU 架构（sm_120 vs sm_75）与 CUDA 12.8／cuDNN 9.7 的卷积核选择导致浮点舍入不同（torch 2.7.1+cu128 vs 冻结 UAV_BT1）；numpy 2.2.6 与 OpenCV 5.0 在 CPU 端 NMS／预处理上的细微数值差异也可能有贡献。未逐框归因。
- 明细：`data/G_CAL48_accuracy_consistency.json`、`data/G_CAL48_accuracy_diff_rows.csv`、`data/G_CAL48_metrics_5060ti.csv`、`data/G_TESTDEV_accuracy_consistency.json`、`data/G_TESTDEV_accuracy_diff_rows.csv`。

## 6. 仅供参考：与 1660 并排（不同 GPU、不同环境，不可当作同机公平对比）

左列：**GTX 1660 SUPER + `H:\Conda\envs\UAV_BT1`**（冻结环境，2026-09-17）；右列：**RTX 5060 Ti + `F:\Conda\envs\UAV_BT2`**（2026-10-06）。权重、协议、脚本、评价器相同；GPU、torch／CUDA、numpy、OpenCV 不同。

| 方法 | cal48 mean：1660／UAV_BT1 | cal48 mean：5060 Ti／UAV_BT2 | test-dev mean：1660／UAV_BT1 | test-dev mean：5060 Ti／UAV_BT2 | test-dev median：1660／UAV_BT1 | test-dev median：5060 Ti／UAV_BT2 |
|---|---:|---:|---:|---:|---:|---:|
| F640 | 18.62 | 19.91 | 17.40 | 19.85 | 17.02 | 18.68 |
| F1280 | 33.15 | 27.43 | 33.72 | 26.25 | 33.08 | 25.03 |
| DensK1 | 35.34 | 40.12 | 34.06 | 40.26 | 32.73 | 38.35 |
| UnifAll | 96.42 | 114.48 | 112.21 | 136.59 | 110.23 | 131.44 |
| SAHI640 | 317.45 | 427.50 | 373.23 | 507.10 | 375.69 | 498.16 |

| 主对 F1280 vs DensK1（test-dev，图级） | 1660／UAV_BT1（`P0-BENCH-F-TESTDEV-20260917-01`） | 5060 Ti／UAV_BT2（`P0-BENCH-G-5060TI-PAIRED-20261006-01`） |
|---|---:|---:|
| 逐图中位差 (ms) | +0.25 | -13.32 |
| 均值差 (ms) | -0.34 | -14.01 |
| Wilcoxon p | 0.235 | 3.6e-264 |
| F1280 更快的图像比例 | 47.3% | 99.8% |

**观察（只描述，未做归因实验）：** 换到 5060 Ti 后只有 F1280 变快（cal48 33.15 → 27.43 ms），F640、DensK1、UnifAll、SAHI640 的均值反而更高（cal48 +7%～+35%，test-dev +14%～+36%）。运行中 GPU 平均利用率只有约 11%，提示这条流水线在本机主要受主机端（Python／Ultralytics 预处理与后处理、CPU 端 NMS、SAHI 合并）开销限制，而不是 GPU 算力：单次 640 前向（含前后处理）在 5060 Ti 上约 19 ms（DensK1 的 global 19.58／local 18.87 ms；1660 为 17.60／16.12 ms），而 1280 前向只要约 27 ms。因此“一次 1280 前向”比“两次 640 前向 + 合并”（DensK1）便宜，1660 上两者相当的局面在 5060 Ti 上不再成立。环境差异（torch 2.7.1／CUDA 12.8、numpy 2.x、OpenCV 5.0）对主机端开销的影响未单独测量。

## 7. 文件

- 数据：`data/G_CAL48_summary.json`、`G_CAL48_timings.csv`、`G_CAL48_protocol.json`、`G_TESTDEV_summary.json`、`G_TESTDEV_per_image_metrics.csv`、`G_PAIRED_summary.json`、`G_PAIRED_wilcoxon_latency.csv`、`G_TIMING_stats.json`、精度一致性文件（§5）。
- 配置与日志：`data/G_logs/<Run ID>/`（启动器 `config.json`＝环境／GPU／SHA／命令行；`result.json`；`gpu_monitor.csv`；`run.log.gz`＝子进程完整输出；Stage D `progress.log`）。冒烟结果只在 `G_logs/P0-BENCH-G-5060TI-SMOKE-20261001-01/`，不进表。
- 预测 `.npy` 与运行目录留在本机 `Experiments/P0_Benchmark/stage_{b,d,g}/<Run ID>/`（不入库）。
- 脚本：`Experiments/P0_Benchmark/stage_g/run_stage_g.py`、`eval_g_accuracy.py`、`run_g_paired_latency.py`、`summarize_g_timing.py`；图 `../05_packaging/figures/fig4b_timing_5060ti.png`（`generate_fig4b_timing_5060ti.py`；1660 的 `fig4_timing_1660.png` 未改）。
- 冻结的 `protocol.json` 中 `hardware_role` 字段仍是旧字符串“formal 4090 table later”（冻结脚本内置，未改）；本表即该“正式表”，硬件为 RTX 5060 Ti。
