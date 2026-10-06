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
| DensK1 | 密度 Top-1 单片 + 整图融合 | 局部窗 640，步长 512，末窗贴边：每轴起点 `axis_windows(L) = sorted(set(range(0, max(1, L−640+1), 512)) ∪ {max(0, L−640)})`，窗口 = 两轴起点笛卡尔积（每图窗数随尺寸而定，见 §2.1）；整图 F640 粗检 conf≥0.25 的框中心落入最多的窗口为 Top-1（稳定排序，同分取最小索引） | 定义摘录：`../00_freeze/DensK1_Definition.md`。BTD8 的“240 窗”是 cal48 48 张图的窗口**总数**，不是每图窗数 |
| UnifAll | 同网格全覆盖 | F640 整图 + 与 DensK1 同一网格的**全部**窗口，推理后融合 | 覆盖上界 / 选区对照 |
| SAHI640 | SAHI 切片 | slice=640×640，overlap=**0.25/0.25**（步长 480，越界片贴边回退）；其余全部 sahi 默认（见 §2.1） | 工程切片族；网格与 DensK1／UnifAll **不同** |

- [x] 五协议配置（imgsz / crop / overlap / conf / IoU / NMS）

### 2.1 实现细节（读自冻结代码与已装库源码；Run J `P0-BENCH-J-REPRO-20261006-01`，2026-10-06）

**公共（F640／F1280／DensK1／UnifAll；`stage_b/run_stage_b_timing.py`）**

| 项 | 值 |
|---|---|
| 每视图推理 | `model.predict(im, imgsz=…, rect=False, device=0, batch=1, half=False, conf=0.001, iou=0.5, max_det=1000)`（FP32） |
| 整图视图 | F640：imgsz 640；F1280：imgsz 1280；`rect=False` → 正方形 letterbox（640² / 1280²） |
| 窗口视图 | 原图裁 `(x, y, min(W, x+640), min(H, y+640))`，贴到 640×640 画布左上（其余填 114），`imgsz=640, rect=False`；回映时丢弃中心落在画布有效区外的框，裁剪到窗口后平移回原图 |
| finalize（所有协议最后一步，含 SAHI640） | conf ≥ 0.25 → CPU 类内 NMS（IoU > 0.5，稳定排序，最多 500 框；`diagnose_bt1.nms`） |
| DensK1 选窗 | `density_top1`：对 F640 原始输出取 conf ≥ 0.25 的框中心，统计落入各窗（半开区间）的个数，`argsort(-score, kind="stable")[0]` |

每图窗口数（= UnifAll 局部视图数 = SAHI640 切片数，二者在下列尺寸上恰好相同但网格不同）：VisDrone test-dev 1400×788 / 1400×1050 / 1360×765 → 6；1916×1078 / 1920×1080 → 8；960×540 → 2；UAVDT 1024×540 / 960×540 → 2。来源：`../04_timing/data/I_PIXLAT_summary.json` 的 `geometry_by_size`（Run I）。

**SAHI640（`run_sahi640`；sahi 0.11.32 源码核对）**

| 项 | 值 | 来源 |
|---|---|---|
| 模型封装 | `AutoDetectionModel.from_pretrained(model_type="ultralytics", model_path=last.pt, confidence_threshold=0.001, device="cuda:0")`；未传 `image_size` | stage_b L258–263 |
| 每片推理 | sahi 只传 `conf / device / verbose / cfg`，其余用 ultralytics `predict` 默认：`imgsz` = ckpt 训练值 640（`train/args.yaml`），`rect=True`（stride-32 最小填充），**`iou=0.7`、`max_det=300`**，`half=False`，`agnostic_nms=False` | `sahi/models/ultralytics.py::perform_inference`；`ultralytics/engine/model.py` L528；`cfg/default.yaml` |
| 切片 | `get_slice_bboxes(640, 640, overlap 0.25/0.25)`：步长 640−int(0.25×640)=480；越界片右/下贴边（`xmin = max(0, W−640)`），不填充；短边 < 640 时切片取整个短边 | `sahi/slicing.py` |
| 整图标准预测 | `perform_standard_pred=True`（默认），**仅当切片数 > 1** 时执行；同样 rect letterbox 到长边 640 | `sahi/predict.py` L304 |
| 合并 | `postprocess_type="GREEDYNMM"`，`match_metric="IOS"`，`match_threshold=0.5`，`class_agnostic=False`（均为默认） | `get_sliced_prediction` 签名 |
| 输入颜色 | 计时内做 BGR→RGB，再交给 sahi（sahi 内部再转回 BGR 喂 ultralytics） | stage_b L167 |

- 冻结脚本元数据写的 `sahi_postprocess: "sahi_default_NMS"` 是**误称**：实际默认是 GREEDYNMM（贪心合并，IOS 匹配），不是 NMS。冻结文件不改，此处更正。
- SAHI640 的每片推理参数（iou 0.7、max_det 300）与其他四协议（iou 0.5、max_det 1000）不同；这是“按 SAHI 默认使用”的一部分，不是本文调过的设置。

### 2.2 计时边界与预热

| 项 | 值 |
|---|---|
| 边界 | 已解码 BGR 图像（`cv2.imread` 在计时外）→ finalize 后的 CPU 框；`torch.cuda.synchronize()` 前后各一次，`time.perf_counter()` |
| 计时内 | letterbox／画布构建、前向、ultralytics 内部 NMS、GPU→CPU、密度选窗、裁片、回映、合并、finalize；SAHI640 另含 BGR→RGB、sahi 切片与 GREEDYNMM |
| 计时外 | 磁盘读取与解码、窗口坐标列表 `build_windows`、GT 匹配与评价、保存预测、写 CSV |
| Stage B（cal48） | 预热：第一张图 3×(F640 + F1280)；然后 48 图 × 3 次重复，每次重复内方法顺序固定 F640→F1280→DensK1→UnifAll→SAHI640 |
| Stage D／E 及 Run G test-dev | 预热：第一张图 2×F640；每图每方法**一次**（one-shot），方法顺序固定同上 |
| SAHI 模型 | 独立加载同一权重，**无单独预热**；首次 SAHI 调用的初始化开销计入第一张图（对 1610／40735 张图的均值影响可忽略，未单独量化） |
| 数值精度 | FP32，batch 1 |

### 2.3 统计设置（Stage F；Stage H 复用）

| 项 | 值 |
|---|---|
| 单位 | VisDrone：图像（配对）；UAVDT（Stage H）：另加 50 序列 cluster bootstrap |
| Bootstrap | **B = 10000，seed = 20260917**；一个 `np.random.default_rng(SEED)` 按 `ALL_PAIRS` 顺序依次消耗；每次重抽 n 张图（有放回），重算池化比值（Σsmall_tp／Σsmall_gt、Σtp／Σ(tp+fp)、均值 ms）；95% CI = 2.5／97.5 百分位（`np.quantile`） |
| Wilcoxon | 自实现符号秩检验：去掉零差，平均秩，统计量 min(W+, W−)，正态近似 + tie 校正 + 0.5 连续性校正，双侧（`erfc`）；不调用 scipy |
| 多重比较 | 主对 F1280 vs DensK1 不校正；次要对 Holm |
| 胜率 CI | Wilson 95% |
| UAVDT cluster（Stage H） | 按序列重抽 50 个序列，B = 10000，seed 20260917（独立 rng）；序列级 Wilcoxon 排除无 small GT 的序列（M0801，n = 49） |
| 复现 | 冻结函数在 UAV_BT2 下重算 Stage F，与 `F_summary.json` 逐位一致（Run H） |

### 2.4 版本

| 项 | UAV_BT1（冻结；Stage A–F，GTX 1660 SUPER） | UAV_BT2（现用；Run G–J，RTX 5060 Ti 与 CPU 再分析） |
|---|---|---|
| Python | 3.12.14 | 3.10.22 |
| torch / CUDA | 2.7.1+cu126 / 12.6，cuDNN 90701 | 2.7.1+cu128 / 12.8，cuDNN 90701 |
| ultralytics | 8.4.90（pinned zip `ultralytics-07958a7.zip`） | 同一 zip、同一 sha256 |
| opencv / pillow | 5.0.0.93 / 12.3.0 | 5.0.0.93 / 12.3.0 |
| numpy | 2.5.2 | 2.2.6 |
| sahi | Stage A 未装；Stage B–E 运行时版本**无法证明**；09-29 备份为 0.11.32 | 0.11.32（Run G 运行时） |
| scipy | Stage A 未装；09-29 备份 1.18.1（Stage F 不调用 scipy） | 1.15.3 |

完整对照：`../00_freeze/Environment_Delta_UAV_BT2_vs_UAV_BT1.md`。

### 2.5 失败例裁图（可选；Run J）

`failure_crops/`（6 例，`cases.json` 记录选例规则、裁窗坐标与计数）。**来源：Run G 已保存预测（RTX 5060 Ti / UAV_BT2）**，CPU 重新匹配，逐图 small_tp 与 `G_TESTDEV_per_image_metrics.csv` 断言一致；无新推理。绿 = 该方法匹配到的 small GT，红 = 漏检，黄框 = DensK1 所选窗口（由已存 F640 预测按冻结 `density_top1` 重算；所选图 F640 框数 < 500，finalize 截断未触发，故重算精确）。

| 例 | 图像 | 对比 | 整图 small TP / small GT | 观察 |
|---|---|---|---|---|
| 1 | 9999938_00000_d_0000210（1400×788） | F1280 vs DensK1 | 88 vs 47 / 325 | 小目标分散在多个区域，单窗只覆盖其一 |
| 2 | 9999938_00000_d_0000212（1400×788） | F1280 vs DensK1 | 108 vs 69 / 294 | 同上 |
| 3 | 0000073_03155_d_0000004（1920×1080） | F1280 vs DensK1 | 23 vs 38 / 59 | 大图上 F1280 缩放 0.667，所选窗口以原生分辨率覆盖密集人群 |
| 4 | 0000073_01275_d_0000002（1920×1080） | F1280 vs DensK1 | 35 vs 45 / 69 | 同上 |
| 5 | 9999938_00000_d_0000121（1400×788） | UnifAll vs SAHI640 | 62 vs 10 / 176 | 处理像素相同；SAHI640 在切片内清晰可见的行人也大量漏检（机制未验证；候选原因：GREEDYNMM／IOS 合并、每片 iou 0.7／max_det 300 默认） |
| 6 | 9999938_00000_d_0000247（1400×788） | F1280 vs UnifAll | 4 vs 7 / 115 | small GT ≥ 50 的图中三协议最好召回最低的一张：两者都几乎全漏 |

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
| 正式统一时序表 | **RTX 5060 Ti 16GB**（2026-10-01 换卡；取代原计划 4090） | **已跑（2026-10-06，PASS）** → Run G `P0-BENCH-G-5060TI-{SMOKE,CAL48,TESTDEV}-20261001-01` + 配对 `P0-BENCH-G-5060TI-PAIRED-20261006-01`；结果单列 `../04_timing/Timing_5060Ti_Table.md`；环境 `F:\Conda\envs\UAV_BT2`（Python 3.10.22，torch 2.7.1+cu128，ultralytics 8.4.90 同一 pinned zip；见 `00_freeze/Environment_Delta_UAV_BT2_vs_UAV_BT1.md`）；权重／协议／评价器／计时边界／预热不变，冻结 Stage B/D/F 脚本原样调用（入口 `Experiments/P0_Benchmark/stage_g/run_stage_g.py`）；精度与 1660 一致（|Δsmall recall| ≤ 0.014 个百分点）；正文不得用 1660 冒充 5060 Ti |

- [x] 硬件分列（5060 Ti 已跑，单列）

## 7. Run IDs

| Stage | Run ID | Status |
|---|---|---|
| B Timing | `P0-BENCH-B-TIMING-20260917-01` | PASS |
| D VisDrone | `P0-BENCH-D-TESTDEV-20260917-01` | PASS |
| E UAVDT | `P0-BENCH-E-UAVDT-20260918-FULL` | PASS |
| F Paired | `P0-BENCH-F-TESTDEV-20260917-01` | PASS |
| G 5060 Ti | `P0-BENCH-G-5060TI-{SMOKE,CAL48,TESTDEV}-20261001-01` | PASS（2026-10-06） |
| G 5060 Ti 配对 | `P0-BENCH-G-5060TI-PAIRED-20261006-01` | PASS（2026-10-06） |
| H UAVDT 配对统计 | `P0-BENCH-H-UAVDT-PAIRED-20261006-01` | PASS（2026-10-06；CPU） |
| I 像素–时延 | `P0-BENCH-I-PIXLAT-20261006-01` | PASS（2026-10-06；CPU） |
| J 附录补缺 + 失败例 | `P0-BENCH-J-REPRO-20261006-01` | PASS（2026-10-06；CPU） |
| K 密度切片 | `P0-BENCH-K-DENSITY-20261006-01` | PASS（2026-10-06；CPU） |

- [x] Run ID 列表

## 8. Hard bans

- [x] **无重训** / 无改权重  
- [x] **无看分后重映射** / 无改 conf 刷终表  
- [x] **无 Paper 2–7** 内容混入本练习槽成稿  
- [x] 1660 与 5060 Ti **分表**；禁止混机「公平」时序

## 9. 关键证据路径

- Freeze：`../00_freeze/`  
- D：`../01_visdrone_main/` · E：`../03_cross_uavdt/` · F：`../02_paired_stats/` · B：`../04_timing/`  
- 近邻表 / 失败例：同目录 `Neighbor_Protocol_Table.md`、`Failure_Boundary_Cases.md`

## 10. 运行代码（2026-09-27 从 commit `bad0f8b` 恢复）

目录重构（commit `efba65e`，2026-09-23）曾删除以下脚本；现按原路径恢复（仅代码，不含预测/输出）。SHA256 为 git blob 内容（LF）；Windows 工作树因 `core.autocrlf=true` 可能为 CRLF。

| 路径（相对 `00_Practice_UAV_Aerial_Detection/`） | SHA256（blob） | 核对 |
|---|---|---|
| `Experiments/diagnose_bt1.py` | `53bedab8aa7cba7eac915968d761201c6cb4946e585433c3e7c4ccc89a16267d` | = `00_freeze/script_sha256.txt` 登记值 ✓ |
| `Experiments/P0_Benchmark/stage_b/run_stage_b_timing.py` | `f00ac0c35240dd799a78fef96eb53681b4b3f5eee5dea62d7ecc61b1913c9983` | 无冻结登记值可比（Stage A 后编写） |
| `Experiments/P0_Benchmark/stage_d/run_stage_d_oneshot.py` | `ec55719d57f9fccee4da97f24fe1b4dd3534aa3729a9f52e8dadd8d42173ae5a` | = `00_freeze/stage_d_config_freeze.json` 的 `script_sha256` ✓ |
| `Experiments/P0_Benchmark/stage_e/run_stage_e_oneshot.py` | `b02dddfde9cb72c366e948ce8e20e60436cd3818244d27010501aeb1c4fab728` | 无冻结登记值可比（Stage A 后编写） |
| `Experiments/P0_Benchmark/stage_f/run_stage_f_paired_stats.py` | `63ec6ee59f7a633c60b1ad4d8a983fab128f70828cfacb96a99d318896b2abb9` | 无冻结登记值可比（Stage A 后编写） |

- 依赖：`run_stage_{d,e}` import `stage_b/run_stage_b_timing.py`；三者均 import `Experiments/diagnose_bt1.py`（`EXP = parents[2]`，故 `diagnose_bt1.py` 必须留在 `Experiments/` 根）。
- 原运行输出目录 `Experiments/P0_Benchmark/stage_*/<RUN_ID>/`（含 `preds/*.npy`）不在仓库；论文用 summary/CSV 已在各 Stage `data/`。
- **sahi 版本：** 运行时版本未冻结（Stage A 时尚未安装）。2026-09-27 环境中为 `sahi 0.11.32`——仅为事后记录，**不能**证明即运行时版本（open）。
- **更新（2026-10-06，Run J）：** Run G（RTX 5060 Ti / UAV_BT2）运行时 sahi = 0.11.32（已证明）；§2.1 的 SAHI 默认参数据此版本源码核对。1660 上 Stage B–E 的运行时版本仍为 open（UAV_BT1 所在 H: 分区已不挂载，无法回查）。
