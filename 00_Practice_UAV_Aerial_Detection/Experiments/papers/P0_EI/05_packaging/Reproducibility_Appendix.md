# Reproducibility_Appendix — 可复现附录（勾选清单）

> 填自 `../00_freeze/` 与 Stage D/E/F/B 冻结产物。本篇为**冻结 VisDrone YOLO 权重上的推理协议比较**，非新检测器论文。

## 1. 权重

| 项 | 值 |
|---|---|
| Path | `11_Datasets/processed/VisDrone/BT1/BT1-LOCAL-20260913-01/train/weights/last.pt` |
| SHA256 | `bc42d54e37acaf1f698af487439dc222fa86fb4498623e8cf954df14e0aa5533` |
| 来源冻结 | `../00_freeze/Environment_Freeze.md`、`weight_sha_reverify.txt` |

- [x] 权重路径 + SHA256

## 2. 五协议定义（短）

公共评价门：conf=**0.25**，匹配 IoU=**0.5**，batch=1；small：原图像素 0<w×h<1024。  
NMS：BTD5 风格 CPU NMS，类间独立，IoU>0.5，max500（DensK1/UnifAll 融合路径沿用；整图路径为协议内后处理）。

| ID | 协议 | imgsz / crop / overlap | 备注 |
|---|---|---|---|
| F640 | 整图 | imgsz=640；无切片 | 最快基线 |
| F1280 | 整图 | imgsz=1280；无切片 | C1 强简单基线 |
| DensK1 | 密度 Top-1 单片 + 整图融合 | 局部窗 640；候选网格同 BTD8（240 窗量级）；粗检 conf≥0.25 选密度中心最多窗；overlap/步长沿 BTD8（窗 640 / 步长 512） | 定义摘录：`../00_freeze/DensK1_Definition.md` |
| UnifAll | 同网格全覆盖 | 与 DensK1 同窗网格，**全部**窗口推理后融合 | 覆盖上界 / 选区对照 |
| SAHI640 | SAHI 切片 | slice=640，overlap=**0.25** | 工程切片族；本机曾需安装 sahi |

- [x] 五协议配置（imgsz / crop / overlap / conf / IoU / NMS）

## 3. 类映射（Stage E）

版本：`../00_freeze/class_mapping_preregister.json` · status **FROZEN_PRE_RESULTS** · 文档 `Class_Mapping_Preregister.md`  
- 纳入：car→car，van→car，truck→truck，bus→bus  
- 排除：pedestrian / people / bicycle / tricycle / awning-tricycle / motor  
- 规则：见分前冻结；**禁止**看分后改映射

- [x] VisDrone→UAVDT 映射版本 / 冻结状态

## 4. 评价器

- VisDrone-compatible matcher：`diagnose_bt1.prepare_gt + match_gt`（本地 mirror GT）  
- **不是**官方 VisDrone 排行榜 AP  
- Stage E：**不是**官方 UAVDT MATLAB AP（趋势检验；ignore mask 按冻结规则不虚构）

- [x] 评价器声明

## 5. Splits

| Stage | Split | n |
|---|---|---:|
| D | VisDrone test-dev（Ultralytics-mirror local GT） | 1610 |
| E | UAVDT DET FULL（作者布局 DET） | 40735 |
| B | cal48 计时 | 48 × 3 reps |
| F | 在 D 逐图上配对 | 1610 images |

- [x] Split 与图像数

## 6. 硬件分列（硬纪律）

| 用途 | GPU | 状态 |
|---|---|---|
| D/E 精度 + B 流水线时序 | **GTX 1660 SUPER** | 已跑（本附录数字） |
| 正式统一时序表 | **RTX 4090** | **尚未跑** → 见 `Next_Authorized_Runs.md`；正文不得用 1660 冒充 4090；`Timing_4090_Table.md` 保持 pending |

- [x] 硬件分列（4090 标 TODO）

## 7. Run IDs

| Stage | Run ID | Status |
|---|---|---|
| B Timing | `P0-BENCH-B-TIMING-20260917-01` | PASS |
| D VisDrone | `P0-BENCH-D-TESTDEV-20260917-01` | PASS |
| E UAVDT | `P0-BENCH-E-UAVDT-20260918-FULL` | PASS |
| F Paired | `P0-BENCH-F-TESTDEV-20260917-01` | PASS |
| G 4090 | `P0-BENCH-G-4090-*`（见 Next_Authorized） | **NOT YET** |

- [x] Run ID 列表

## 8. Hard bans

- [x] **无重训** / 无改权重  
- [x] **无看分后重映射** / 无改 conf 刷终表  
- [x] **无 Paper 2–7** 内容混入本练习槽成稿  
- [x] 1660 与 4090 **分表**；禁止混机「公平」时序

## 9. 关键证据路径

- Freeze：`../00_freeze/`  
- D：`../01_visdrone_main/` · E：`../03_cross_uavdt/` · F：`../02_paired_stats/` · B：`../04_timing/`  
- 近邻表 / 失败例：同目录 `Neighbor_Protocol_Table.md`、`Failure_Boundary_Cases.md`
