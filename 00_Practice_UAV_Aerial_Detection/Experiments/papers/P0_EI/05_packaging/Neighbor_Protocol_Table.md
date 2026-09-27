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
| Selection: DensK1 → UnifAll | **+0.0916** | −0.0948 | +78.1 | 1660 SUPER | 全覆盖切片抬召回，付精度与时延 |
| Slicing vs full-res: SAHI640 → F1280 | **+0.1820** | +0.3166 | −339.5 | 1660 SUPER | 由 SAHI640 换成 F1280：召回↑、精度↑、时延降约一个数量级（即本冻结 SAHI640 相对 F1280 三项均劣） |
| （可选）SAHI640 → UnifAll | +0.2327 | +0.1536 | −261.0 | 1660 SUPER | 同为切片族：由 SAHI640 换成 UnifAll，召回↑、精度↑且更快（本设置） |

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

| Pair（轴）（Δ = 后 − 前） | Δsmall_recall | Δprecision | Δmean_ms | 同机 |
|---|---:|---:|---:|---|
| F640 → F1280 | **+0.0849** | −0.0584 | +16.3 | 1660 SUPER |
| DensK1 → UnifAll | **+0.0152** | −0.0159 | +14.2 | 1660 SUPER |
| SAHI640 → F1280 | +0.0332 | +0.0189 | −130.9 | 1660 SUPER |
| （可选）SAHI640 → UnifAll | +0.0227 | −0.0213 | −116.8 | 1660 SUPER |

基线绝对值：

| Method | Precision | small Recall | mean ms/img |
|---|---:|---:|---:|
| F640 | 0.4302 | 0.7080 | 16.7 |
| F1280 | 0.3719 | 0.7929 | 33.1 |
| DensK1 | 0.3475 | 0.7672 | 33.0 |
| UnifAll | 0.3316 | 0.7824 | 47.2 |
| SAHI640 | 0.3530 | 0.7597 | 164.0 |

## C. 主张支持与边界（终稿措辞，2026-09-27）

**P0-EI-C1**：在单一冻结 YOLO11n 权重与 conf 0.25／IoU 0.5 匹配口径下，VisDrone test-dev 上 F1280 比 DensK1 更准——Stage F 主配对 Δsmall_recall +0.0409，95% CI [0.0355, 0.0462]，Δprecision +0.0681 [0.0631, 0.0731]；两者在 1660 上的时延统计上不可区分（单次时延逐图 Wilcoxon p=0.235，均值差 −0.34 ms；Stage B 均值 33.15 vs 35.34 ms）。不主张"更快"。E 上同向（small recall 0.7929 vs 0.7672，precision 0.3719 vs 0.3475，33.1 vs 33.0 ms；无配对检验）。背景轴：D 上 F640→F1280 小召回 +0.1616 而精度几乎不变（CI 跨 0）；E 上召回升但精度 −0.0584，权衡面依赖数据域。  
**P0-EI-C2**：选区／覆盖协议只移动召回–精度–时延权衡。D 上 UnifAll 小召回最高（0.4511；相对 F1280 +0.0507，相对 DensK1 +0.0916），代价是精度（0.5123 vs F1280 0.6753）与时延（112.2 vs 33.7 ms，≈3.3×；Stage B T=40 ms 超时率 UnifAll 1.000，F1280 0，DensK1 0.021）；E 上 DensK1→UnifAll 仅 +0.0152 且精度 −0.0159。本冻结设置下 SAHI640 在 D、E 上均被 F1280 支配（上表 SAHI640→F1280 两行三项同向改善）。  
**名次不稳作边界**：D 上 small-recall 序 UnifAll > F1280 > DensK1 > F640 > SAHI640；E 上 F1280 > UnifAll > DensK1 > SAHI640 > F640。跨集重排写作主张边界，不写"通用排序"。  
**适用范围**：时延仅 GTX 1660 SUPER；指标为匹配器 precision／small recall（非 AP）；单一冻结权重。主张全文与证据见 `../../../../Research_Plan.md` §3。

## D. 指针

- D 聚合 / 逐图：`../01_visdrone_main/data/D_TESTDEV_summary.json`、`D_TESTDEV_per_image_metrics.csv`  
- E 聚合 / 逐图：`../03_cross_uavdt/data/E_FULL_summary.json`、`E_FULL_per_image_metrics.csv`  
- F 配对：`../02_paired_stats/data/F_summary.json`、`F_bootstrap_deltas.csv`  
- B 1660 计时（cal48）：`../04_timing/data/B_TIMING_summary.json`（F640~18.6 / F1280~33.2 / DensK1~35.3 / UnifAll~96.4 / SAHI640~317 ms）— **勿与 4090 混表**；4090 正式时序 Run G（`P0-BENCH-G-4090-*`）尚未跑，结果将单列于 `../04_timing/Timing_4090_Table.md`。

> 修订记录（2026-09-27）：A/B 两表全部行按「后 − 前」由 `D_TESTDEV_summary.json` / `E_FULL_summary.json` 重算。修正：SAHI640 两行原按「前 − 后」填写（符号反）；D DensK1→UnifAll Δsmall_recall +0.0915→+0.0916（舍入）；E F640→F1280 Δprecision −0.0583→−0.0584、Δmean_ms +16.4→+16.3（舍入）；E SAHI640→UnifAll Δprecision 原 −0.0214 在两种符号约定下均不符，重算为 −0.0213（UnifAll 精度低于 SAHI640）。其余单元与 JSON 一致。同日 §C 改为基于 Stage B–F 的 C1／C2 终稿措辞（C1 去掉"更快"；C2 改为选区／覆盖权衡陈述）。
