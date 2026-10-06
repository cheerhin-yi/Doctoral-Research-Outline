# P0_EI Run Index（终跑）

| Stage | Run ID | 角色 | 数据文件 |
|---|---|---|---|
| A | P0-BENCH-A-ENV-20260917-01 | 冻结 | `00_freeze/*` |
| B | P0-BENCH-B-TIMING-20260917-01 | 1660 计时 | `04_timing/data/` |
| C | P0-BENCH-C-CAL48-20260917-01 | 开发集证据（非主表；cal48） | `01_visdrone_main/data/C_*` |
| D | P0-BENCH-D-TESTDEV-20260917-01 | VisDrone 主精度 | `01_visdrone_main/data/D_*` |
| E | P0-BENCH-E-UAVDT-20260918-FULL | 跨集外推 | `03_cross_uavdt/data/E_*` |
| F | P0-BENCH-F-TESTDEV-20260917-01 | 图级配对 | `02_paired_stats/data/F_*` |
| G | P0-BENCH-G-5060TI-{SMOKE,CAL48,TESTDEV}-20261001-01 | RTX 5060 Ti 16GB 正式时序（**计划中，未跑**；UAVDT 可选；取代从未运行的 `P0-BENCH-G-4090-*-20260920-01`；环境 `F:\Conda\envs\UAV_BT2`，已采用，见 `00_freeze/Environment_Delta_UAV_BT2_vs_UAV_BT1.md`） | 待写 `04_timing/Timing_5060Ti_Table.md`（与 1660 分表） |

Smoke / 失败短跑 / `.npy` 预测不进证据槽（原始输出留在 Git 忽略的 `11_Datasets` 或运行目录）。冻结件的来源记录见 `00_freeze/provenance/`。

注（2026-09-27）：
- `00_freeze/stage_e_config_freeze.json` 内 `run_id` 为 smoke `P0-BENCH-E-UAVDT-20260918-01`（24 图）；全量终跑为 **`P0-BENCH-E-UAVDT-20260918-FULL`**。冻结 JSON 不改。
- 运行代码已从 commit `bad0f8b` 恢复：`Experiments/P0_Benchmark/stage_{b,d,e,f}/run_stage_*.py` 与 `Experiments/diagnose_bt1.py`（SHA 见 `05_packaging/Reproducibility_Appendix.md` §10）。
