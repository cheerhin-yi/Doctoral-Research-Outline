# P0_EI Run Index（终跑）

| Stage | Run ID | 角色 | 数据文件 |
|---|---|---|---|
| A | P0-BENCH-A-ENV-20260917-01 | 冻结 | `00_freeze/*` |
| B | P0-BENCH-B-TIMING-20260917-01 | 1660 计时 | `04_timing/data/` |
| C | P0-BENCH-C-CAL48-20260917-01 | 开发集证据（非主表；cal48） | `01_visdrone_main/data/C_*` |
| D | P0-BENCH-D-TESTDEV-20260917-01 | VisDrone 主精度 | `01_visdrone_main/data/D_*` |
| E | P0-BENCH-E-UAVDT-20260918-FULL | 跨集外推 | `03_cross_uavdt/data/E_*` |
| F | P0-BENCH-F-TESTDEV-20260917-01 | 图级配对 | `02_paired_stats/data/F_*` |
| G-SMOKE | P0-BENCH-G-5060TI-SMOKE-20261001-01 | RTX 5060 Ti 16GB 冒烟（2 张 cal48 走 Stage B + 3 张 test-dev 走 Stage D；只验 GPU／权重 SHA／五方法／计时链路；不进证据表）— 已登记 2026-10-06；**PASS**（16:23–16:25） | `04_timing/data/G_logs/P0-BENCH-G-5060TI-SMOKE-20261001-01/`（只放日志与冒烟输出） |
| G-CAL48 | P0-BENCH-G-5060TI-CAL48-20261001-01 | RTX 5060 Ti 16GB cal48 计时（冻结 Stage B 脚本，48 图 × 5 方法 × 3 次）+ 与 1660 cal48 的精度一致性闸门 — 已登记 2026-10-06；**PASS**（16:25–16:27；240 对中 22 对差 1–2 框，|Δsmall_tp| ≤ 1，可忽略） | `04_timing/data/G_CAL48_*`；日志 `G_logs/` |
| G-TESTDEV | P0-BENCH-G-5060TI-TESTDEV-20261001-01 | RTX 5060 Ti 16GB test-dev 全量计时（冻结 Stage D 脚本，1610 图 × 5 方法，one-shot）— 已登记 2026-10-06；**PASS**（16:28–16:51，墙钟 1406 s；|Δsmall recall| ≤ 0.014 个百分点） | `04_timing/data/G_TESTDEV_*`；日志 `G_logs/` |
| G-PAIRED | P0-BENCH-G-5060TI-PAIRED-20261006-01 | 5060 Ti 图级配对时延检验（冻结 Stage F 统计函数；主对 F1280 vs DensK1）— 新增 Run ID，已登记 2026-10-06；**PASS**（F1280 更快：逐图中位差 −13.32 ms，p≈3.6e-264） | `04_timing/data/G_PAIRED_*` |
| H | P0-BENCH-H-UAVDT-PAIRED-20261006-01 | UAVDT 图级配对统计（冻结 Stage F 函数的参数化调用，`E_FULL_per_image_metrics.csv`）＋ 50 序列 cluster bootstrap；附 VisDrone Stage F 在 UAV_BT2 下的复现核对；CPU only，无推理；UAV_BT2 — **PASS**（Stage F 逐位复现；主对序列 CI [0.010, 0.040]） | `03_cross_uavdt/H_UAVDT_Paired_Stats_Report.md`；`03_cross_uavdt/data/H_*`；`02_paired_stats/data/H_FREPRO_*` |
| I | P0-BENCH-I-PIXLAT-20261006-01 | 像素–时延归一化表：每图网络输入像素（冻结 Stage B 几何 + sahi 0.11.32 切片 + ultralytics LetterBox）× 已有 D/E（1660）与 G（5060 Ti）时延分列；CPU only，无推理 — **PASS**（同像素的 UnifAll vs SAHI640 recall 0.451 vs 0.218；时延主要由前向次数决定） | `04_timing/Pixel_Latency_Table.md`；`04_timing/data/I_*` |
| J | P0-BENCH-J-REPRO-20261006-01 | 可复现附录补缺（SAHI 设置读自代码、DensK1 精确网格、每视图 conf、计时边界与预热、版本、bootstrap seed/B）＋ 可选失败例裁图（复用 Run G 已存预测，RTX 5060 Ti／UAV_BT2；CPU only，无推理） — **PASS**（附录 §2.1–2.5；SAHI 实际合并为 GREEDYNMM/IOS，元数据“NMS”为误称；6 例裁图） | `05_packaging/Reproducibility_Appendix.md`；`05_packaging/failure_crops/` |
| K | P0-BENCH-K-DENSITY-20261006-01 | 密度属性切片：按 valid_gt／small_gt 五分位分箱（VisDrone Stage D，时延 1660 与 5060 Ti 分列；UAVDT Stage E，序列 cluster bootstrap）；UAVDT 场景/高度/视角属性文件不在盘上 → 不做；目标尺度切片不做（需逐目标匹配）；CPU only，无推理 — **PASS**（VisDrone 各箱 F1280−DensK1 +0.030～+0.046，均显著；UAVDT 最稀疏箱打平，valid_gt≥10 起 F1280 最佳） | `06_density_slices/K_Density_Slices_Report.md`；`06_density_slices/data/K_*` |

Run G 共同条件：环境 `F:\Conda\envs\UAV_BT2`（已采用，见 `00_freeze/Environment_Delta_UAV_BT2_vs_UAV_BT1.md`）；权重／协议／评价器／类别映射不变；冻结的 Stage B/D/F 脚本**原样**调用，参数化入口为 `Experiments/P0_Benchmark/stage_g/run_stage_g.py`（只传 `--run-id`／`--max-images`／`--skip-extract`）。Run ID 日期选择：SMOKE／CAL48／TESTDEV **保留原计划日期 20261001**（与所有已登记文档一致，不改名）；配对检验是本次新增的 Run ID，按登记日 20261006 命名。取代从未运行的 `P0-BENCH-G-4090-*-20260920-01`。UAVDT 时序可选，本轮未跑。结果表：`04_timing/Timing_5060Ti_Table.md`（与 1660 分表）。

Smoke / 失败短跑 / `.npy` 预测不进证据槽（原始输出留在 Git 忽略的 `11_Datasets` 或运行目录）。冻结件的来源记录见 `00_freeze/provenance/`。

注（2026-09-27）：
- `00_freeze/stage_e_config_freeze.json` 内 `run_id` 为 smoke `P0-BENCH-E-UAVDT-20260918-01`（24 图）；全量终跑为 **`P0-BENCH-E-UAVDT-20260918-FULL`**。冻结 JSON 不改。
- 运行代码已从 commit `bad0f8b` 恢复：`Experiments/P0_Benchmark/stage_{b,d,e,f}/run_stage_*.py` 与 `Experiments/diagnose_bt1.py`（SHA 见 `05_packaging/Reproducibility_Appendix.md` §10）。
