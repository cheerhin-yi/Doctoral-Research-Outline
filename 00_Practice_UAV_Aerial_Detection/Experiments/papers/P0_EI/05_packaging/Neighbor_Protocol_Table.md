# Neighbor_Protocol_Table — 近邻协议对照（单一轴差分）

> 用途：展示「只动一个协议旋钮」时的召回–精度–代价移动；**不是**五方法夺冠总表。  
> 权重冻结 VisDrone YOLO `last.pt`；推理协议比较。GPU 同机：GTX 1660 SUPER。  
> 数据：`../01_visdrone_main/data/`、`../03_cross_uavdt/data/`、`../02_paired_stats/data/`；计时参考 `../04_timing/`（1660 流水线，勿与 4090 混表）。

## A. VisDrone test-dev（Stage D）

Run: `P0-BENCH-D-TESTDEV-20260917-01` PASS · n=1610 · conf=0.25 · IoU=0.5 · small=0<area<1024  
Weight SHA256: `bc42d54e37acaf1f698af487439dc222fa86fb4498623e8cf954df14e0aa5533`

| Pair（轴） | Δsmall_recall | Δprecision | Δmean_ms | 同机 | 读法（后 − 前） |
|---|---:|---:|---:|---|---|
| Resolution: F640 → F1280 | **+0.1616** | +0.0045 | +16.3 | 1660 SUPER | 抬有效分辨率 → 小目标召回明显升；精度几乎持平；时延约翻倍 |
| Selection: DensK1 → UnifAll | **+0.0915** | −0.0948 | +78.1 | 1660 SUPER | 全覆盖切片抬召回，付精度与时延 |
| Slicing vs full-res: SAHI640 → F1280 | **−0.1820**（SAHI−F1280）| −0.3166 | +339.5 | 1660 SUPER | 本冻结 SAHI640 相对 F1280：召回更低、精度更低、时延高一个数量级 |
| （可选）SAHI640 → UnifAll | −0.2327 | −0.1536 | +261.0 | 1660 SUPER | 同为切片族：UnifAll 召回更高且更快（本设置） |

基线绝对值（便于核对，非排名表）：

| Method | Precision | small Recall | mean ms/img |
|---|---:|---:|---:|
| F640 | 0.6708 | 0.2388 | 17.4 |
| F1280 | 0.6753 | 0.4004 | 33.7 |
| DensK1 | 0.6071 | 0.3596 | 34.1 |
| UnifAll | 0.5123 | 0.4511 | 112.2 |
| SAHI640 | 0.3587 | 0.2184 | 373.2 |

### 主配对（Stage F，图级；仍在 D 上）

Run: `P0-BENCH-F-TESTDEV-20260917-01` · primary: **F1280 vs DensK1**  
- Δsmall_recall (F1280−DensK1) ≈ **+0.0409**；95% bootstrap CI **不跨 0**（见 `../02_paired_stats/data/F_summary.json`）  
- 方向核对（聚合）：F640→F1280 召回升；DensK1→UnifAll 召回升、精度降。

## B. UAVDT DET FULL（Stage E）— 分面，禁止与 D 混平均

Run: `P0-BENCH-E-UAVDT-20260918-FULL` PASS · n=40735 · 冻结 VisDrone→UAVDT 映射 · **非**官方 UAVDT MATLAB AP（趋势检验）

| Pair（轴） | Δsmall_recall | Δprecision | Δmean_ms | 同机 |
|---|---:|---:|---:|---|
| F640 → F1280 | **+0.0849** | −0.0583 | +16.4 | 1660 SUPER |
| DensK1 → UnifAll | **+0.0152** | −0.0159 | +14.2 | 1660 SUPER |
| SAHI640 → F1280 | −0.0332 | −0.0189 | +130.9 | 1660 SUPER |
| （可选）SAHI640 → UnifAll | −0.0227 | −0.0214 | +116.8 | 1660 SUPER |

基线绝对值：

| Method | Precision | small Recall | mean ms/img |
|---|---:|---:|---:|
| F640 | 0.4302 | 0.7080 | 16.7 |
| F1280 | 0.3719 | 0.7929 | 33.1 |
| DensK1 | 0.3475 | 0.7672 | 33.0 |
| UnifAll | 0.3316 | 0.7824 | 47.2 |
| SAHI640 | 0.3530 | 0.7597 | 164.0 |

## C. 主张支持与边界（短）

**C1（分辨率/有效像素）**：D 上 F640→F1280 小召回 +0.16 而精度几乎不变，支持「抬有效分辨率改变小目标召回–代价权衡」；E 上同向召回升但精度下降，说明权衡面依赖域。  
**C2（选区/覆盖）**：DensK1→UnifAll 在 D/E 均为召回升、精度降（D 上更陡），支持「覆盖↑常抬召回并付精度/时延」；不支持「某一选区协议通论最优」。  
**名次不稳作边界**：D 上 small-recall 粗序 UnifAll > F1280 > DensK1；E 上 F1280 > UnifAll > DensK1。跨集名次重排是**主张边界**（协议改权衡 ≠ 找两集通吃第一名），不是 C1/C2 失败。

## D. 指针

- D 聚合 / 逐图：`../01_visdrone_main/data/D_TESTDEV_summary.json`、`D_TESTDEV_per_image_metrics.csv`  
- E 聚合 / 逐图：`../03_cross_uavdt/data/E_FULL_summary.json`、`E_FULL_per_image_metrics.csv`  
- F 配对：`../02_paired_stats/data/F_summary.json`、`F_bootstrap_deltas.csv`  
- B 1660 计时（cal48）：`../04_timing/data/B_TIMING_summary.json`（F640~18.6 / F1280~33.2 / DensK1~35.3 / UnifAll~96.4 / SAHI640~317 ms）— **勿与 4090 混表**；4090 见 `Next_Authorized_Runs.md`（尚未跑）。
