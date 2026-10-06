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

Run G 共同条件：环境 `F:\Conda\envs\UAV_BT2`（已采用，见 `00_freeze/Environment_Delta_UAV_BT2_vs_UAV_BT1.md`）；权重／协议／评价器／类别映射不变；冻结的 Stage B/D/F 脚本**原样**调用，参数化入口为 `Experiments/P0_Benchmark/stage_g/run_stage_g.py`（只传 `--run-id`／`--max-images`／`--skip-extract`）。Run ID 日期选择：SMOKE／CAL48／TESTDEV **保留原计划日期 20261001**（与所有已登记文档一致，不改名）；配对检验是本次新增的 Run ID，按登记日 20261006 命名。取代从未运行的 `P0-BENCH-G-4090-*-20260920-01`。UAVDT 时序可选，本轮未跑。结果表：`04_timing/Timing_5060Ti_Table.md`（与 1660 分表）。

Smoke / 失败短跑 / `.npy` 预测不进证据槽（原始输出留在 Git 忽略的 `11_Datasets` 或运行目录）。冻结件的来源记录见 `00_freeze/provenance/`。

注（2026-09-27）：
- `00_freeze/stage_e_config_freeze.json` 内 `run_id` 为 smoke `P0-BENCH-E-UAVDT-20260918-01`（24 图）；全量终跑为 **`P0-BENCH-E-UAVDT-20260918-FULL`**。冻结 JSON 不改。
- 运行代码已从 commit `bad0f8b` 恢复：`Experiments/P0_Benchmark/stage_{b,d,e,f}/run_stage_*.py` 与 `Experiments/diagnose_bt1.py`（SHA 见 `05_packaging/Reproducibility_Appendix.md` §10）。
