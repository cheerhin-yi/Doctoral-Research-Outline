# P0_EI Run Index（终跑）

| Stage | Run ID | 角色 | 数据文件 |
|---|---|---|---|
| A | env freeze | 冻结 | `00_freeze/*` |
| B | P0-BENCH-B-TIMING-20260917-01 | 1660 计时 | `04_timing/data/` |
| C | cal48 | 开发集证据（非主表） | `01_visdrone_main/data/C_*` |
| D | P0-BENCH-D-TESTDEV-20260917-01 | VisDrone 主精度 | `01_visdrone_main/data/D_*` |
| E | P0-BENCH-E-UAVDT-20260918-FULL | 跨集外推 | `03_cross_uavdt/data/E_*` |
| F | P0-BENCH-F-TESTDEV-20260917-01 | 图级配对 | `02_paired_stats/data/F_*` |

Smoke / 失败短跑 / `.npy` 预测未迁入论文槽（仅存 Archive 或已丢弃策略见 Experiments README）。
