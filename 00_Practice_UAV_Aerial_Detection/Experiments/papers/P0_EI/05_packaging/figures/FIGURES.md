# P0_EI Packaging Figures

本目录存放近期 P0_EI 对照图（由 Stage D/E/B/F 汇总 JSON **现场再生**，非手工改数）。

## 文件

| 图 | 文件 | 基准数据 |
|---|---|---|
| fig1 VisDrone | `fig1_visdrone_metrics.png` | `01_visdrone_main/data/D_TESTDEV_summary.json` |
| fig2 UAVDT | `fig2_uavdt_metrics.png` | `03_cross_uavdt/data/E_FULL_summary.json` |
| fig3 dual small-recall | `fig3_dual_set_small_recall.png` | 同上 D + E（**禁止 pool**） |
| fig4 1660 timing | `fig4_timing_1660.png` | `04_timing/data/B_TIMING_summary.json` |
| fig5 Stage F deltas | `fig5_stageF_deltas.png` | `02_paired_stats/data/F_summary.json` |

完整对照表见仓库根目录 [`FILE_CATALOG.md`](../../../../../../FILE_CATALOG.md) §4。

## 再生

在本目录执行：

```text
H:\Conda\envs\UAV_BT1\python.exe generate_plots.py
```

脚本读取上级 `P0_EI` 各 stage 的 `*_summary.json`，写出本目录 PNG。勿改硬编码指标；改图先改证据 JSON/报告。