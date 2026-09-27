# P0_EI 练手论文：基本情况与实验内容（详细版）

> **生成：** 2026-09-27（Asia/Shanghai）。**性质：** 汇总／导读文档，把已冻结、已 PASS 的证据按"论文视角"串起来；**不新增实验、不改任何冻结配置、不改映射**。  
> **效力：** 不改变 [`../00_Overview/Current_Stage.md`](../00_Overview/Current_Stage.md) 的唯一 ACTIVE = **P0_EI**；与源文件冲突时以源文件（Current_Stage、各 Stage 报告与 `data/*.json`）为准。  
> **数字纪律：** 表中每个数字都取自磁盘上的 summary JSON／CSV／报告，并注明来源文件与 Run ID。标 **「派生」** 的，是本文从已有逐图 CSV 直接求和／相除得到（没有改动任何源文件）。磁盘上找不到的写 **「待补」**，并说明应从哪里来。  
> **路径简写：** `PR/` = `00_Practice_UAV_Aerial_Detection/`；`P0_EI/` = `00_Practice_UAV_Aerial_Detection/Experiments/papers/P0_EI/`。

---

## 一、论文基本情况

### 1.1 题目

| 项 | 内容 | 来源 |
|---|---|---|
| 现有工作题目 | **面向无人机航拍的时间预算约束小目标检测** | `PR/Research_Plan.md` §1、`PR/Mainline_A_Current.md` §3（原文"题目仍可叫"） |
| 目录 README 标题 | 练手论文：无人机航拍时间预算约束小目标检测 | `PR/README.md` |
| 建议英文工作题（**本文建议，未登记，待用户确认**） | *Inference Protocol Matters: An Experimental Evaluation of Resolution and Slicing Protocols for UAV Small-Object Detection with a Frozen Detector* | — |

> 说明：现有中文题目强调"时间预算约束"，但 P0_EI 证据的主线是"**同一冻结权重上比较推理协议**"。成稿前建议把题目与摘要统一到"推理协议对比／实验评估"口径（`PR/Writing/P0_Two_Paper_Plan_2026-09-22.md`：摘要写 *experimental evaluation*，不写 *we propose*）。

### 1.2 论文类型

- **EI 会议对比／协议论文**（experimental evaluation），**不是新检测器、不是新模块**（`PR/Writing/P0_EI_Outline.md`"贡献类型"）。
- 实验全部在同一个冻结 YOLO 权重上进行，**只改"怎么推理"**：输入分辨率、是否切片、切哪些片、怎么合并。

### 1.3 研究问题

原文（`PR/Research_Plan.md` §1，执行效力）：

> 在固定检测器、固定后处理与声明的整帧时间核算下，**整图 640、整图 1280、密度单片与均匀切片**对 VisDrone 小目标的召回、误检和超时率如何比较？失败条件是什么？

P0_EI 证据槽把它落成可执行的问题（`P0_EI/README.md`"主张"）：

> 冻结 VisDrone 训练权重，比较五个推理协议（F640／F1280／DensK1／UnifAll／SAHI640）在航拍小目标上的**召回–精度–代价**；VisDrone 做主评测，UAVDT 做外推；统计单位是**图像**，做配对检验。

其中 SAHI640 是作为"工程切片族"的近邻协议加入的（`P0_EI/00_freeze/Environment_Freeze.md` 五方法表 M5）。

### 1.4 核心主张 C1／C2（按原文登记）

| ID              | 原文主张                                               | 状态                          | 当初依据（历史，默认不重跑）                                                                                         | 来源                                                       |
| --------------- | -------------------------------------------------- | --------------------------- | ------------------------------------------------------------------------------------------------------ | -------------------------------------------------------- |
| **P0-EI-C1**    | 在本项目固定 YOLO11n 与已声明预算口径下，**整图 1280 比当前密度单片更准且更快**。 | PROPOSED（协议／对比主张，非新算法）      | cal48，conf=.25，IoU=.5，2720 个小 GT；F1280 小 TP 1312，27.33／41.44 ms；密度单片 1172，37.36／64.51 ms；GTX1660SUPER。 | `PR/Research_Plan.md` §2.1、`PR/Mainline_A_Current.md` §4 |
| **P0-EI-C2**    | **区域分配存在可恢复空间，但不等于可部署增益**；必须同时报告超时率与选择漏检。          | PROPOSED（协议／对比主张，非新算法）      | BTD1–BTD7、BTD11；逐图用 GT 在 F1280 与最佳单片之间选择，仅净增 33。**禁止**把 GT oracle 或低分修复写成方法精度。                         | 同上                                                       |
| P0-A-C1／P0-A-C2 | 旧区域机制主张                                            | **HOLD**（只作历史追踪，不指导本稿主实验叙事） | —                                                                                                      | `PR/Research_Plan.md` §2.2                               |

> ✅ **口径差异已于 2026-09-27 修正：** `P0_EI/05_packaging/Neighbor_Protocol_Table.md` §C 原来把 C1／C2 写成"分辨率／有效像素轴""选区／覆盖轴"，现已按 Research_Plan 原文对齐，轴的说法保留为括注。C1"更快"一项已在 `Research_Plan.md` §2.1 和 `Mainline_A_Current.md` §4 加了 2026-09-27 核注；**主张原文没改**，是否改写由用户决定。第五节仍按原文逐条核对证据。

### 1.5 贡献点（按 `PR/Writing/P0_EI_Outline.md`，并按已有证据细化）

1. **协议族对照实验**，不是新检测器／新模块。
2. **同一冻结权重、同一后处理门槛，只改推理协议**：F640／F1280／DensK1／UnifAll／SAHI640 放在同一坐标系里比较（VisDrone test-dev 1610 张 + UAVDT 40735 帧，见第三节）。
3. **图级配对统计**（Wilcoxon + bootstrap + Holm + 胜负计数），说清"什么时候是真增益、什么时候只是放大分辨率"（Stage F）。
4. **跨集外推与负结果边界**：两个数据集的排序不稳定这一点，写进贡献边界，而不是藏起来（Stage E 报告 §4）。
5. **可复现包装**：权重 SHA、分前冻结的类别映射、配置冻结、Run ID、失败／边界例、图表再生脚本（`P0_EI/05_packaging/`）。

### 1.6 不做什么（边界／门禁）

来源：`00_Overview/Current_Stage.md`"实验门"、`PR/Research_Plan.md` §1、`P0_EI/05_packaging/Reproducibility_Appendix.md` §8。

- **不训练、不微调、不改网络、不改检测头**；不用注意力／损失／蒸馏／剪枝／新检测头补证据。
- **不看分后改映射**：VisDrone→UAVDT 类别映射在出分前冻结（FROZEN_PRE_RESULTS）；不看分后改 conf 刷终表。
- **新机制一律 HOLD**（P0-A-*）；不创建 BTD13；不开 Paper 2–7；Post-EI 的 A（RailUAV-SOD）／B（Paper1）只是 IDLE／PREP。
- **test-dev 只做一次性终评**，不能用来选策略或选 checkpoint（Stage D `one_shot: true`）。
- **1660 与 4090 时序分表**，禁止合并成一个"公平"时序表。
- 不把 VisDrone 结果写成铁路安全或高原泛化；轨道走廊**不是**本篇的方法前提。
- 不把 GT oracle 选择写成方法精度；不声称"两集通吃的统一排序"。
- 第三方 UAVDT 子集（包括已拒绝的 Kaggle JSON 包）不能当主库。
- 所有精度数字都是**匹配器 precision／small_recall**，**不是**官方 COCO AP、VisDrone 排行榜 AP 或 UAVDT MATLAB AP。

### 1.7 投稿定位与 JCR／EI 口径

| 项 | 口径 | 来源 |
|---|---|---|
| 本篇目标 | **EI 会议**；不承诺录用；不是中科院二区／Trans | `PR/Research_Plan.md` §1、§5 |
| 主跟踪会议 | **ICIP 2027 全文**（目录惯例为 CCF-C，投稿前核对 CCF 第七版）；备选 ACCV／ICPR 全文；不把 CCF-B（ICME／ICASSP）当第一目标；Workshop／短文通常不算目录会议 | `PR/Writing/P0_Two_Paper_Plan_2026-09-22.md` |
| 分区主尺 | 期刊用 **JCR-primary**（Q1–Q4）；会议按投稿时的 CCF 推荐目录；**EI 索引只是描述项**，不替代 CCF／JCR | `00_Overview/Venue_and_Claim_Policy_JCR_2026-09-24.md` §1 |
| 第二篇（另授权） | 统一时间预算下的协议选择 + 一条受限推理切片；出口 **JCR Q2 应用／系统刊**；启动条件是五协议逐图 oracle 上界足够 | `P0_Two_Paper_Plan_2026-09-22.md` |
| 会期 | Mainline §8 要求"选定 2027 年 EI 会期并写入 Current_Stage"——**待补**（Current_Stage 目前未写具体会期／截稿日） | `PR/Mainline_A_Current.md` §8 |

> 注：`Venue_and_Claim_Policy_JCR_2026-09-24.md` 的正文只有 A／B 两篇的 claim×venue 梯子，**没有 P0 专条**。"P0 以 EI 为先"来自 Research_Plan 与两篇安排；该政策文件对 P0 只起到"会议看 CCF、期刊看 JCR"这一总口径的作用。

### 1.8 当前状态（截至 2026-09-27 磁盘扫描）

| 项 | 状态 | 证据 |
|---|---|---|
| 唯一 ACTIVE | **P0_EI**（本文未修改） | `00_Overview/Current_Stage.md` |
| Stage A 冻结 | PASS · `P0-BENCH-A-ENV-20260917-01` | `P0_EI/00_freeze/Environment_Freeze.md` |
| Stage B 1660 计时 | PASS · `P0-BENCH-B-TIMING-20260917-01` | `P0_EI/04_timing/` |
| Stage C cal48 精度（开发证据） | PASS · `P0-BENCH-C-CAL48-20260917-01` | `P0_EI/01_visdrone_main/StageC_Cal48_Dev_Report.md` |
| Stage D VisDrone test-dev | PASS · `P0-BENCH-D-TESTDEV-20260917-01` | `P0_EI/01_visdrone_main/` |
| Stage E UAVDT 外推 | DONE／PASS · `P0-BENCH-E-UAVDT-20260918-FULL` | `P0_EI/03_cross_uavdt/` |
| Stage F 图级配对 | PASS · `P0-BENCH-F-TESTDEV-20260917-01` | `P0_EI/02_paired_stats/` |
| EI 包装（近邻表／失败例／复现附录／图 1–5） | **已填** | `P0_EI/05_packaging/README.md` |
| 4090 正式时序 | **缺**（`Timing_4090_Table.md` pending；Run G 尚未跑） | `P0_EI/05_packaging/Next_Authorized_Runs.md` |
| 稿件正文／PDF | **缺**：`PR/` 下没有 `.tex`／`.pdf`／`.docx`，只有提纲 `PR/Writing/P0_EI_Outline.md` | 本文扫描 |
| 学习侧（Part B 等） | 由用户自己完成；按 `PR/Research_Plan.md` §3，"学习作答不是执行门" | — |

---

## 二、实验设置

### 2.1 冻结模型与权重

| 项 | 值 | 来源 |
|---|---|---|
| 检测器 | YOLO11n（Research_Plan C1 原文"固定 YOLO11n"）；VisDrone 本地训练 BT1，100 轮 | `PR/Research_Plan.md` §2.1、§3 |
| 主权重 | `11_Datasets/processed/VisDrone/BT1/BT1-LOCAL-20260913-01/train/weights/last.pt` | `P0_EI/00_freeze/Environment_Freeze.md` |
| 归档副本 | `11_Datasets/processed/VisDrone/BT1/BTD1-CAL48-20260913-01/baseline_archive/BT1-LOCAL-20260913-01/train/weights/last.pt` | 同上 |
| **SHA256** | **`bc42d54e37acaf1f698af487439dc222fa86fb4498623e8cf954df14e0aa5533`**（两份均 match=True） | `P0_EI/00_freeze/weight_sha_reverify.txt` |
| 大小 | 5457882 bytes | 同上 |
| 运行内复核 | Stage B／D／E 的 summary／protocol 都写入了同一个 SHA；Stage B 脚本在运行前 `assert sha(WEIGHT)==WEIGHT_SHA` | `B_TIMING_protocol.json`、`D_TESTDEV_summary.json`、`E_FULL_summary.json` |

### 2.2 代码与环境

| 项 | 值 | 来源 |
|---|---|---|
| conda 环境 | `H:\Conda\envs\UAV_BT1`（base `E:/miniconda3`），没有重装 | `P0_EI/00_freeze/Environment_Freeze.md` |
| Python | 3.12.14（conda-forge，MSC v.1944 64 bit） | `P0_EI/00_freeze/env_snapshot.txt` |
| torch／torchvision | 2.7.1+cu126／0.22.1+cu126；CUDA 12.6；cuDNN 90701 | 同上 |
| ultralytics | 8.4.90 | 同上 |
| OpenCV／numpy／PIL | 5.0.0／2.5.2／12.3.0 | 同上 |
| OS | Windows-11-10.0.26200-SP0 | 同上 |
| sahi | Stage A 时**未安装**（M5 blocker，已披露），之后安装。本文 2026-09-27 核查环境中是 `sahi-0.11.32.dist-info`。**运行当时的 sahi 版本没有写进冻结件 → 待补**（应补进 `00_freeze/` 的 pip 快照） | `Environment_Freeze.md`；本文核查 |
| Stage D 脚本 SHA／git head | `script_sha256=ec55719d57f9fccee4da97f24fe1b4dd3534aa3729a9f52e8dadd8d42173ae5a`；`git_head=cb406b5c209e6af3007216a949f065837cb6cba4` | `P0_EI/00_freeze/stage_d_config_freeze.json` |
| 运行脚本 | `run_stage_b_timing.py`、`run_stage_d_oneshot.py`、`run_stage_e_oneshot.py`、`run_stage_f_paired_stats.py`、`diagnose_bt1.py`（`prepare_gt`／`match_gt`／`nms`／`axis_windows`） | 见下方说明 |
| 图再生 | `P0_EI/05_packaging/figures/generate_plots.py`（只读四个 summary JSON） | `figures/FIGURES.md` |

> ✅ **复现缺口已于 2026-09-27 补上：** 这些运行脚本在目录重构（commit `efba65e`）时被删除，现已从 commit `bad0f8b` 按原路径恢复：`PR/Experiments/P0_Benchmark/stage_{b,d,e,f}/run_stage_*.py` 和 `PR/Experiments/diagnose_bt1.py`（只有代码）。核对结果：`diagnose_bt1.py` 的 blob SHA256 与 `00_freeze/script_sha256.txt` 的登记值一致；`run_stage_d_oneshot.py` 与 `stage_d_config_freeze.json` 的 `script_sha256` 一致（详见 `05_packaging/Reproducibility_Appendix.md` §10）。`11_Datasets/.../BTD1-CAL48-20260913-01/diagnose_bt1.py` 是更早的版本，和运行时版本**不一致**，不要用它。第 2.5 节的协议细节就是从这些脚本读出来的。

### 2.3 硬件

| 项 | 值 | 来源 |
|---|---|---|
| 精度与流水线计时（B／C／D／E） | **NVIDIA GeForce GTX 1660 SUPER ×1**，6144 MiB，驱动 591.86，功耗上限 125 W，UUID `GPU-43b14c17-…` | `P0_EI/00_freeze/gpu_snapshot.txt` |
| Stage B 峰值显存 | 159038464 bytes（约 151.7 MiB） | `P0_EI/04_timing/data/B_TIMING_summary.json` |
| 正式时序 | **RTX 4090：尚未跑**。Run ID 已登记：`P0-BENCH-G-4090-{SMOKE,CAL48,TESTDEV}-20260920-01`（UAVDT 可选） | `P0_EI/05_packaging/Next_Authorized_Runs.md` |
| 纪律 | 1660 数字只算 pipeline validation；正文时序表只用 4090；**两者不能进同一张表** | `Current_Stage.md`、`Environment_Freeze.md` |

### 2.4 数据集

#### (1) VisDrone2019-DET test-dev（主评测，Stage D）

| 项 | 值 | 来源 |
|---|---|---|
| 来源 | Ultralytics assets 镜像 `VisDrone2019-DET-test-dev.zip`（带图像和标注，本地 GT） | `P0_EI/01_visdrone_main/StageD_Channel_Decision.md` |
| ZIP SHA256 | `b28a94b06dfd9e36ce77ff8155fb82b9d2c030f198a76105933bd56c6ea6a68d` | `D_TESTDEV_summary.json` |
| 图像数 | **1610** | 同上 |
| 类别 | 10 类：pedestrian, people, bicycle, car, van, truck, tricycle, awning-tricycle, bus, motor | `P0_EI/00_freeze/class_mapping_preregister.json` |
| 小目标 GT | **50431** | `D_TESTDEV_summary.json` |
| 有效 GT（全尺寸） | 74707（**派生**：`D_TESTDEV_per_image_metrics.csv` 中 `valid_gt` 求和） | 本文计算 |
| 无小目标图像 | 111 张（派生）→ Stage F 召回检验的 N = 1610 − 111 = **1499**，与 `F_summary.json` 一致 | 本文计算／`F_summary.json` |
| 分辨率（抽样） | 每 20 张抽 1 张，共 81 张：1400×788、1400×1050、1360×765、1916×1078、960×540、1920×1080 | 本文抽样 |
| 注意 | Ultralytics 的 train／test-dev ZIP 可能和原始挑战包不同，只有 val ZIP 的 SHA 和官方校验包一致；只能用于学术／内部基准，不能声称官方挑战排名 | `StageD_Channel_Decision.md` |

#### (2) cal48（开发证据，Stage B／C）

- 清单 `11_Datasets/processed/VisDrone/BT1/full_data_v2/cal48.txt`，SHA256 `b0e27b1dc10d952a927597022a1fe0cfa52714d45a89e4c3f36880c2a4a68e7f`，48 张，**没有重采样**（`Environment_Freeze.md`）。
- 小 GT 2720（`C_cal48_summary.json`）。**不是独立测试集**，会议稿要把它披露为开发证据（`StageC_Cal48_Dev_Report.md`）。

#### (3) UAVDT DET（跨集外推，Stage E）

| 项 | 值 | 来源 |
|---|---|---|
| 数据 | 作者版 UAVDT DET：50 个序列／**40735** 帧／50 个 `*_gt_whole.txt`（布局 PASS） | `P0_EI/03_cross_uavdt/StageE_UAVDT_Report.md` §1 |
| 本机路径 | **`G:\Schloar Data\P0\UAVDT`**（2026-09-27 核实，40735 帧、50 个 gt_whole）。运行时登记的路径是 `G:\Schloar Data\UAVDT\`，冻结的 `stage_e_config_freeze.json` 里仍是这个旧路径，有意不改。Current_Stage 和 Stage E 文档已更新 | `Current_Stage.md`、`StageE_Channel_Decision.md`、`StageE_UAVDT_Report.md` §8 |
| 分辨率（抽样） | 每 1000 帧抽 1 帧，共 41 帧：39 帧 1024×540，2 帧 960×540 | 本文抽样 |
| 评测类别 | 只评车辆可比子集：car／truck／bus | `class_mapping_preregister.json` |
| 小目标 GT | **493861** | `E_FULL_summary.json` |
| 有效 GT（映射后车辆） | 798795（派生：`E_FULL_per_image_metrics.csv` 中 `valid_gt` 求和） | 本文计算 |
| 无小目标帧 | 4649（派生） | 本文计算 |
| ignore | 官方 `*_gt_ignore.txt` **不使用**；不虚构 VisDrone 式 ignore mask（冻结规则） | `StageE_Channel_Decision.md` |

**类别映射（出分前冻结，`registered_at 2026-09-17T15:28:36`，status `FROZEN_PRE_RESULTS`）：**

| VisDrone（YOLO id） | VisDrone 名 | → UAVDT 名 | UAVDT id |
|---:|---|---|---:|
| 3 | car | car | 0 |
| 4 | van | car（显式合并） | 0 |
| 5 | truck | truck | 1 |
| 8 | bus | bus | 2 |
| 0,1,2,6,7,9 | pedestrian, people, bicycle, tricycle, awning-tricycle, motor | **排除**（GT 与预测两侧都不计分） | — |

来源：`P0_EI/00_freeze/class_mapping_preregister.json`、`Class_Mapping_Preregister.md`。修改策略：锁定，直到用户明确重开 Stage E 映射门；**看分后不能改**。

### 2.5 五种推理协议（逐一说明）

> 协议实现细节读自 `bad0f8b` 中的 `run_stage_b_timing.py`（Stage D／E 脚本都 `from run_stage_b_timing import …`，复用同一套函数）和 `diagnose_bt1.py`；定义摘要见 `P0_EI/00_freeze/Environment_Freeze.md`、`DensK1_Definition.md`、`05_packaging/Reproducibility_Appendix.md` §2。

**公共部分（五个协议都一样）：**

- 每个视图（整图或切片）单独前向：`model.predict(imgsz=…, rect=False, device=0, batch=1, half=False, conf=0.001, iou=0.5, max_det=1000)`，也就是 FP32、batch=1。
- **统一终处理 `finalize`：** 先按 `conf ≥ 0.25` 过滤，再做 `diagnose_bt1.nms`，即**稳定排序、按类别独立的 CPU NMS，IoU > 0.5，最多保留 500 个**（BTD5 风格）。
- **切片网格 `axis_windows(size)`：** 窗口 640、步长 512，起点为 `{0, 512, 1024, … ≤ size−640} ∪ {size−640}`（最后一窗贴边）。切片不足 640 时用灰色 114 填充到 640×640；局部预测按中心点落在有效区域内筛选，裁剪后再加回偏移，映射到原图坐标。
- **计时边界：** 从已解码的内存 BGR 图像开始，到最终可评估的检测框为止；前后各做一次 `torch.cuda.synchronize()`。磁盘读取／解码和评估匹配不计时。预热：第一张图各跑 3 次 F640 和 F1280（Stage B 脚本）。

| 协议 | 做法 | 每图前向次数 | 关键参数 |
|---|---|---|---|
| **F640** | 整图，imgsz=640，前向一次 → finalize | 1 | 最快基线 |
| **F1280** | 整图，imgsz=1280，前向一次 → finalize | 1 | C1 的强简单基线；在 UAVDT（长边 1024）上相当于**上采样** |
| **DensK1** | ① 整图 640 前向；② 在切片网格的每个窗口里，统计整图预测中 conf≥0.25 的**框中心数**；③ 取数量最多的窗口（稳定排序，同分取索引最小）；④ 对这 1 片做 640 前向并映射回原图；⑤ 整图 + 单片预测拼接 → finalize | 2（整图 + 1 片） | 定义沿用 BTD8，没有重新定义；DensK1 在 cal48 上的小 TP=1172，与 BTD8 锁定值一致（`StageC_Cal48_Dev_Report.md`） |
| **UnifAll** | 整图 640 前向 + **同一网格的全部窗口**逐片 640 前向 → 全部拼接 → finalize | 1 + N（N 由分辨率决定） | 和 DensK1 同网格，作为"覆盖上界／选区对照"。cal48：33 张 6 窗、13 张 2 窗、2 张 8 窗，共 240 窗（派生：`B_TIMING_timings.csv` 的 `n_windows`，与 BTD8 的 240 窗一致）。按规则推算：VisDrone 抽样分辨率对应 2／6／8 窗；UAVDT 1024×540 对应 **2 窗** |
| **SAHI640** | `sahi.predict.get_sliced_prediction`：slice 640×640，`overlap_height_ratio = overlap_width_ratio = 0.25`；`AutoDetectionModel(model_type="ultralytics", confidence_threshold=0.001, device="cuda:0")`；其余用 sahi 默认参数；输出再过同一个 finalize | 取决于 sahi 切片数（+ 默认的整图标准预测） | 本文核查已装的 sahi 0.11.32，默认 `perform_standard_pred=True`、`postprocess_type="GREEDYNMM"`、`match_metric="IOS"`、`match_threshold=0.5`、按类别处理。脚本元数据记为 `sahi_postprocess: "sahi_default_NMS"`。**运行时版本待补**（见 2.2） |

> 注：SAHI640 的切片网格（重叠 0.25）和 DensK1／UnifAll 的网格（步长 512）**不是同一个网格**，SAHI 内部还有自己的合并（GREEDYNMM／IOS），计时里也包含 BGR→RGB 转换。SAHI640 应理解为"按 SAHI 默认设置使用的工程切片近邻"，不能代表 SAHI 族的最优调参结果（见 `Failure_Boundary_Cases.md` (c)）。

**DensK1 的时间构成（cal48，1660，144 次的平均；派生：`P0_EI/04_timing/data/B_TIMING_timings.csv`）：** 整图检测 17.60 ms、选区 + 局部检测 16.12 ms、合并／NMS 1.61 ms，合计 35.34 ms（与 `B_TIMING_summary.json` 中的 mean 一致）。

### 2.6 评价指标定义

**匹配器：** `diagnose_bt1.prepare_gt + match_gt`（VisDrone 兼容口径，本地 GT）。

1. **有效 GT：** 类别 1–10，w、h > 0，且不落在 ignore 区域。类别 0（ignored regions）的框会生成一张积分图作为 ignore mask。
2. **预测：** 保留 `conf ≥ 0.25`；落在 ignore 区域的预测直接剔除。
3. **匹配：** 按分数从高到低贪心匹配；类别必须一致；IoU ≥ 0.5。优先匹配普通 GT，再匹配 score=0 的 GT（可重复使用，记为 ignored，不算 FP）。重叠相同时取后一个 GT（沿用已核对的 MATLAB 语义）。没匹配上的预测记为 **FP**。
4. **TP／FP** 是把所有图像的计数加起来（pooled）。**precision = TP / (TP + FP)**。
5. **小目标：** GT score > 0，且原图像素面积 **0 < w·h < 1024**。**small_recall = small_tp / small_gt**。匹配是对所有尺寸的框一起做的，small_tp 是被匹配上的小 GT 数。
6. **recall_all**（本文派生）= TP / valid_gt，只作补充。
7. Stage E 先把预测按冻结映射改成 UAVDT 的 3 类，再用同一个匹配器；UAVDT 不使用 ignore。

**⚠ 与 AP 的区别（成稿中必须明确写出）：** 这里只用**单一置信度阈值 0.25**、单一 IoU 0.5 算 precision／recall，**没有**对 PR 曲线积分。所以它**不是** COCO AP、**不是** VisDrone 官方排行榜 AP、**不是** UAVDT 官方 MATLAB AP。Ultralytics 原生 AP ≠ VisDrone 兼容 AP（`Environment_Freeze.md`"Evaluation gates"、`PR/Research_Plan.md` §2.1 口径）。

**时延：** `mean_ms` 是每图平均端到端时延。Stage B 另外报告 median、std、p90／p95／p99、每图 3 次中位数的均值和 p95；**超预算率 `budget_violation_rate[T]`** = "每图 3 次中位数 > T ms"的图像比例，T 取 10／15／20／25／30／40／50／75／100。**40 ms 只是相对参考，不是业务硬期限。**

**统计（Stage F）：** 统计单位是**图像**（N=1610；small_gt=0 的图不计入召回检验，有效 N=1499）。recall_small 用双侧 Wilcoxon 符号秩检验；pooled 指标差值用配对图像重采样 bootstrap（B=10000，seed=20260917）求 95% CI。主比较 **F1280 vs DensK1** 报原始 p；5 个次要比较做 Holm 校正；另报胜负计数（Wilson CI）和 McNemar 检验。

---

## 三、实验内容与结果（Stage A–F）

### Stage A — 冻结（环境／权重／协议定义）

- **目的：** 在跑任何对比之前，锁定权重、数据清单、环境和五个协议的定义，防止事后调参。
- **做法：** 复核权重 SHA，冻结 cal48 清单和环境快照，登记五协议定义、评价门、计时边界和统计单位；不训练，也不跑 Stage B。
- **Run ID：** `P0-BENCH-A-ENV-20260917-01`（2026-09-17）· **A_STATUS: PASS**

| 检查项 | 结果 |
|---|---|
| 权重 SHA 期望＝实际 | **YES**（两份 last.pt，5457882 bytes） |
| cal48 清单 | 48 行／48 图／48 标注，没有重采样；SHA `b0e27b1d…8e7f` |
| git | HEAD `604aeec`（冻结时） |
| GPU | GTX 1660 SUPER（非 4090 → 正式 4090 表在本机被阻塞，已披露） |
| sahi | 缺失 → 当时 M5 被阻塞（后来安装，见 2.2） |
| 评价门／计时边界／统计单位 | 已登记：conf 0.25、IoU 0.5、small<1024；解码图 → 最终框；统计单位＝图像，主对照 F1280 vs DensK1 |

- **结论：** 冻结完成；后续每个 Stage 都在运行时复核同一个 SHA。
- **证据：** `P0_EI/00_freeze/Environment_Freeze.md`、`weight_sha_reverify.txt`、`env_snapshot.txt`、`gpu_snapshot.txt`、`git_snapshot.txt`、`pip_freeze.txt`、`script_sha256.txt`、`DensK1_Definition.md`。

### Stage B — 本地 1660 SUPER 流水线计时

- **目的：** 在同一台机器上，按统一计时边界测量五个协议的端到端时延，用于 pipeline 验证。**这不是正式 4090 表。**
- **做法：** cal48 的 48 张 × 5 个协议 × 3 次 = 每个协议 144 条计时；检查每次输出是否与第 0 次一致（atol=1e-5）；保存 rep0 的预测供 Stage C 使用。
- **Run ID：** `P0-BENCH-B-TIMING-20260917-01` · **PASS**

**表 B-1　时延（ms，GTX 1660 SUPER，cal48，n=144/协议）** — 来源 `P0_EI/04_timing/data/B_TIMING_summary.json`

| 协议 | mean | median | std | p90 | p95 | p99 | 每图中位数均值 | 每图中位数 p95 | 不一致次数 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| F640 | 18.62 | 18.23 | 2.45 | 21.95 | 23.09 | 24.97 | 18.44 | 21.24 | 0 |
| F1280 | 33.15 | 32.88 | 3.74 | 37.53 | 38.73 | 42.31 | 32.78 | 36.79 | 0 |
| DensK1 | 35.34 | 34.63 | 4.47 | 40.16 | 43.20 | 49.69 | 34.82 | 39.46 | 0 |
| UnifAll | 96.42 | 105.79 | 31.54 | 127.49 | 134.92 | 156.46 | 95.14 | 126.08 | 0 |
| SAHI640 | 317.45 | 363.90 | 118.78 | 447.05 | 493.61 | 538.25 | 308.68 | 407.82 | 0 |

**表 B-2　超预算率（每图 3 次中位数 > T 的图像比例）** — 同一来源

| 协议 | T=20 | T=25 | T=30 | T=40 | T=50 | T=75 | T=100 |
|---|---:|---:|---:|---:|---:|---:|---:|
| F640 | 0.125 | 0.021 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| F1280 | 1.000 | 1.000 | 0.792 | 0.000 | 0.000 | 0.000 | 0.000 |
| DensK1 | 1.000 | 1.000 | 0.958 | 0.021 | 0.000 | 0.000 | 0.000 |
| UnifAll | 1.000 | 1.000 | 1.000 | 1.000 | 0.896 | 0.729 | 0.729 |
| SAHI640 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.979 |

- **结论：** 在 1660 上，F1280 与 DensK1 的时延是**同一量级**（均值 33.15 vs 35.34 ms，p95 38.73 vs 43.20 ms）。在 T=40 ms 这个相对参考下，DensK1 有 2.1% 的图像超时，F1280 为 0。UnifAll 约为 F1280 的 3 倍，SAHI640 约为 10 倍。三次重复的输出全部一致。
- **与历史数字的差别：** C1 原始依据中的 1660 数字（F1280 27.33／41.44 ms；DensK1 37.36／64.51 ms，来自 BTD8）和本次 Stage B 的数字不同。两者的计时实现与轮次不同，成稿时应**只引用 Stage B（或 4090）**，BTD8 的数字只作历史说明。
- **证据：** `P0_EI/04_timing/StageB_Timing_Report.md`、`data/B_TIMING_summary.json`、`B_TIMING_timings.csv`、`B_TIMING_protocol.json`；图 4。

### Stage C — cal48 精度（开发证据，非主表）

- **目的：** 用 Stage B rep0 的预测做开发集精度对照，核对 DensK1 实现与历史 BTD8 是否一致。
- **Run ID：** `P0-BENCH-C-CAL48-20260917-01`（`Run_Index.md` 中写作"cal48"）· **PASS**

**表 C-1** — 来源 `P0_EI/01_visdrone_main/data/C_cal48_summary.json`（n=48，小 GT=2720）

| 协议 | TP | FP | Precision | small TP | small Recall |
|---|---:|---:|---:|---:|---:|
| F640 | 1492 | 576 | 0.7215 | 840 | 0.3088 |
| F1280 | 2010 | 839 | 0.7055 | 1312 | 0.4824 |
| DensK1 | 1857 | 1051 | 0.6386 | 1172 | 0.4309 |
| UnifAll | 2110 | 1572 | 0.5731 | 1367 | 0.5026 |
| SAHI640 | 1345 | 1928 | 0.4109 | 749 | 0.2754 |

- **结论：** DensK1 的 small_tp=1172 与 BTD8 锁定值一致（实现核对通过）。F1280 的小召回高于 DensK1（0.482 vs 0.431），与 C1 的历史依据（1312 vs 1172）一致。**cal48 不能称作独立测试集。**
- **证据：** `P0_EI/01_visdrone_main/StageC_Cal48_Dev_Report.md`、`data/C_cal48_metrics.csv`。

### Stage D — VisDrone test-dev 五协议一次性终评（主精度表）

- **目的：** 在完整 test-dev（1610 张）上一次性评测五个协议，作为论文主精度表。
- **做法：** 先冻结配置和评测通道（Case 1 + Case 3：本地镜像 GT + VisDrone 兼容匹配器），再每个协议只预测一次，看分后不调参，意外结果原样保留。逐图指标供 Stage F 使用。
- **Run ID：** `P0-BENCH-D-TESTDEV-20260917-01` · **PASS**（2026-09-17 14:33 完成；wall 1128.1 s）

**表 D-1　VisDrone test-dev（n=1610，conf 0.25，IoU 0.5，小目标 <1024 px²）**  
来源：`P0_EI/01_visdrone_main/data/D_TESTDEV_summary.json`（TP／FP／Precision／small／mean_ms）；median_ms 取自 `P0_EI/02_paired_stats/data/F_summary.json` → `method_aggregates`；recall_all 和 n_dets 为**派生**（`D_TESTDEV_per_image_metrics.csv` 求和）。

| 协议 | TP | FP | Precision | small TP | small GT | **small Recall** | recall_all（派生） | n_dets（派生） | mean ms | median ms |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| F640 | 28346 | 13911 | 0.6708 | 12042 | 50431 | 0.2388 | 0.3794 | 43011 | 17.40 | 17.02 |
| F1280 | 37767 | 18160 | **0.6753** | 20194 | 50431 | 0.4004 | 0.5055 | 58047 | 33.72 | 33.08 |
| DensK1 | 35662 | 23075 | 0.6071 | 18133 | 50431 | 0.3596 | 0.4774 | 60685 | 34.06 | 32.73 |
| UnifAll | 41705 | 39695 | 0.5123 | 22751 | 50431 | **0.4511** | 0.5582 | 84691 | 112.21 | 110.23 |
| SAHI640 | 26086 | 46632 | 0.3587 | 11016 | 50431 | 0.2184 | 0.3492 | 75415 | 373.23 | 375.69 |

- **小召回排序：** UnifAll 0.451 > F1280 0.400 > DensK1 0.360 > F640 0.239 > SAHI640 0.218。
- **结论：** ① 把分辨率从 640 提到 1280，小召回 +0.16，精度基本不变，时延约翻倍。② UnifAll 小召回最高，但精度最低，时延约 112 ms。③ F1280 在高召回的几个协议中精度最高，并且在小召回和精度两项上都优于 DensK1，时延相当。④ 按默认设置运行的 SAHI640 在本设置下召回和精度都最低、最慢（边界见第四节）。
- **口径：** 所有数字都是"VisDrone-compatible evaluator on Ultralytics-mirror test-dev local GT"，**不是官方排行榜 AP**；时延是 1660 上单次运行的值。
- **证据：** `P0_EI/01_visdrone_main/StageD_TestDev_Report.md`、`StageD_Channel_Decision.md`、`data/D_TESTDEV_summary.json`、`D_TESTDEV_per_image_metrics.csv`（8050 行 = 1610 × 5）、`D_TESTDEV_status.json`、`00_freeze/stage_d_config_freeze.json`；图 1、图 3。

### Stage E — UAVDT 跨集外推（类别映射分前冻结）

- **目的：** 检验"协议改变召回–精度–代价权衡"这一粗趋势能否迁移到另一个航拍车辆基准。**不是**争 UAVDT SOTA。
- **做法：** 用同一个冻结 last.pt，不在 UAVDT 上微调。按分前冻结的 VisDrone→UAVDT 映射改写预测类别，然后用同一匹配器评估；不用 ignore。先跑 24 张的 smoke（`P0-BENCH-E-UAVDT-20260918-01`，PASS，约 58 s），再跑全量。不保存预测（`save_preds=false`）。
- **Run ID：** `P0-BENCH-E-UAVDT-20260918-FULL` · **DONE／PASS**（wall 17149.2 s ≈ 4.76 h）

**表 E-1　UAVDT DET FULL（n=40735，车辆 3 类，冻结映射）**  
来源：`P0_EI/03_cross_uavdt/data/E_FULL_summary.json`；median_ms、recall_all 为**派生**（`E_FULL_per_image_metrics.csv`）。

| 协议 | TP | FP | Precision | small TP | small GT | **small Recall** | recall_all（派生） | mean ms | median ms（派生） |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| F640 | 623956 | 826262 | **0.4302** | 349664 | 493861 | 0.7080 | 0.7811 | **16.74** | 16.14 |
| F1280 | 671489 | 1134085 | 0.3719 | 391579 | 493861 | **0.7929** | 0.8406 | 33.08 | 31.46 |
| DensK1 | 658280 | 1236148 | 0.3475 | 378871 | 493861 | 0.7672 | 0.8241 | 32.97 | 32.04 |
| UnifAll | 668237 | 1346758 | 0.3316 | 386393 | 493861 | 0.7824 | 0.8366 | 47.18 | 44.36 |
| SAHI640 | 648364 | 1188553 | 0.3530 | 375203 | 493861 | 0.7597 | 0.8117 | 164.00 | 163.67 |

**表 E-2　与 Stage D 的跨集对照**（来源 `StageE_UAVDT_Report.md` §4）

| 模式 | VisDrone D | UAVDT E | 判读 |
|---|---|---|---|
| F640 小召回最弱（在整图／密度／切片几类中） | 是（SAHI 更低） | 是 | **一致** |
| 提分辨率／切片 → 小召回高于 F640 | 是 | 是 | **一致** |
| 召回升，精度常降 | 是（UnifAll／SAHI 尤其明显） | 是 | **权衡叙事一致** |
| 排名第一的协议 | UnifAll | F1280 | **不完全稳定** |
| SAHI 位置 | 垫底 | 中游 | **对数据集敏感** |

- **结论：** 允许写"推理协议在两个数据集上都会系统性地改变小目标召回–精度–代价"；**不允许**写"存在跨数据集通用的五协议排序"。UAVDT 上 UnifAll 时延只有 47 ms，是因为 1024×540 的帧按网格只切 2 窗（按 2.5 节规则推算）。在 UAVDT 上 F1280 与 DensK1 的**平均**时延几乎相同（33.08 vs 32.97 ms，DensK1 略快）。
- **缺口：** Stage E **没有做图级配对统计**（Stage F 只覆盖 D）。如果需要，可以只用现有的 `E_FULL_per_image_metrics.csv` 补做，不需要新推理（**待授权**）。
- **证据：** `P0_EI/03_cross_uavdt/StageE_UAVDT_Report.md`、`StageE_Channel_Decision.md`、`data/E_FULL_summary.json`、`E_FULL_per_image_metrics.csv`（203675 行 = 40735 × 5）、`E_FULL_status.json`、`00_freeze/stage_e_config_freeze.json`、`class_mapping_preregister.json`；图 2、图 3。

### Stage F — 图级配对统计（基于 Stage D）

- **目的：** 用图像作为统计单位，检验协议之间的差异是否稳定，而不是只比较 pooled 的总数。主比较 F1280 vs DensK1。
- **做法：** 基于 Stage D 的逐图 CSV：recall_small 做 Wilcoxon（去掉 small_gt=0 的图）；pooled 指标差值做 bootstrap（B=10000，seed=20260917）；次要比较做 Holm 校正；另报胜负计数、Wilson CI 和 McNemar。时延用 Stage D 单次运行的 total_ms。
- **Run ID：** `P0-BENCH-F-TESTDEV-20260917-01` · **PASS**（wall 71.45 s）

**表 F-1　主比较：F1280 vs DensK1** — 来源 `P0_EI/02_paired_stats/data/F_summary.json`

| 指标 | 值 |
|---|---|
| 有小 GT 的图像数 N | 1499（非零差 1089） |
| recall_small 逐图差 中位数／均值 | 0.0000／**+0.0345** |
| Wilcoxon（双侧，原始 p） | statistic 182331.5，z = −11.02，**p = 2.997e-28** |
| pooled small recall | F1280 0.4004 vs DensK1 0.3596，**Δ = +0.0409** |
| **Δ small recall 95% bootstrap CI** | **[0.0355, 0.0462]**（**不跨 0**） |
| Δ precision [95% CI] | +0.0681 [0.0631, 0.0731] |
| Δ mean ms [95% CI] | −0.34 [−0.66, −0.01] |
| 时延 Wilcoxon（单次运行 total_ms） | p = **0.235**（不显著）；逐图中位差 **+0.25 ms**（按中位数 F1280 略慢），均值差 −0.34 ms |
| 胜负计数（按 recall_small） | F1280 更好 720／DensK1 更好 369／平 410；Wilson p(F1280 更好) = 0.480 [0.455, 0.506]；McNemar p = 2.79e-26 |

**表 F-2　次要比较：Wilcoxon（recall_small）+ Holm** — 来源 `P0_EI/02_paired_stats/data/F_wilcoxon_recall_small.csv`

| 比较（A vs B） | N | 中位 Δ(A−B) | 均值 Δ | p 原始 | p Holm |
|---|---:|---:|---:|---:|---:|
| F640 vs F1280 | 1499 | −0.1429 | −0.1487 | 5.994e-172 | 2.398e-171 |
| F1280 vs UnifAll | 1499 | −0.0370 | −0.0594 | 2.927e-86 | 2.927e-86 |
| F1280 vs SAHI640 | 1499 | +0.1778 | +0.2029 | 4.060e-183 | 2.030e-182 |
| DensK1 vs UnifAll | 1499 | −0.0667 | −0.0939 | 8.617e-161 | 2.585e-160 |
| DensK1 vs SAHI640 | 1499 | +0.1395 | +0.1683 | 1.590e-155 | 3.180e-155 |

**表 F-3　bootstrap Δ（A − B），95% CI** — 来源 `P0_EI/02_paired_stats/data/F_bootstrap_deltas.csv`

| 比较 | Δ small recall | Δ precision | Δ mean ms |
|---|---|---|---|
| F1280 vs DensK1 | +0.0409 [0.0355, 0.0462] | +0.0681 [0.0631, 0.0731] | −0.3 [−0.7, −0.0] |
| F640 vs F1280 | −0.1616 [−0.1675, −0.1559] | −0.0045 [−0.0110, 0.0018] | −16.3 [−16.6, −16.1] |
| F1280 vs UnifAll | −0.0507 [−0.0551, −0.0464] | +0.1629 [0.1583, 0.1677] | −78.5 [−79.5, −77.5] |
| F1280 vs SAHI640 | +0.1820 [0.1735, 0.1908] | +0.3166 [0.3090, 0.3239] | −339.5 [−343.4, −335.6] |
| DensK1 vs UnifAll | −0.0916 [−0.0966, −0.0866] | +0.0948 [0.0906, 0.0993] | −78.1 [−79.1, −77.2] |
| DensK1 vs SAHI640 | +0.1411 [0.1311, 0.1512] | +0.2484 [0.2411, 0.2555] | −339.2 [−343.1, −335.3] |

**表 F-4　逐图胜负计数（描述性）** — 来源 `StageF_Paired_Stats_Report.md`／`F_summary.json → binary_win_counts`

| 比较 | A 更好 | B 更好 | 平 | Wilson p(A 更好) |
|---|---:|---:|---:|---|
| F1280 vs DensK1 | 720 | 369 | 410 | 0.480 [0.455, 0.506] |
| F640 vs F1280 | 53 | 1161 | 285 | 0.035 [0.027, 0.046] |
| F1280 vs UnifAll | 193 | 899 | 407 | 0.129 [0.113, 0.147] |
| F1280 vs SAHI640 | 1201 | 81 | 217 | 0.801 [0.780, 0.821] |
| DensK1 vs UnifAll | 21 | 1008 | 470 | 0.014 [0.009, 0.021] |
| DensK1 vs SAHI640 | 1122 | 144 | 233 | 0.748 [0.726, 0.770] |

- **结论：** ① 主比较中，F1280 相对 DensK1 的小召回提升是稳定的（CI 不跨 0，p≈3e-28），精度也更高。② 时延上两者**没有显著差异**（p=0.235），均值上 F1280 只快 0.34 ms，中位数上反而慢 0.25 ms，所以"更快"不能作为主张。③ 次要比较经 Holm 校正后全部显著；F640 vs F1280 的精度差 CI [−0.0110, 0.0018] 跨 0，说明提高分辨率基本**不损失精度**。
- **证据：** `P0_EI/02_paired_stats/StageF_Paired_Stats_Report.md`、`data/F_summary.json`、`F_wilcoxon_recall_small.csv`、`F_bootstrap_deltas.csv`、`F_status.json`；图 5。

---

## 四、EI 包装（`P0_EI/05_packaging/`）

### 4.1 近邻协议对照表（`Neighbor_Protocol_Table.md`）

用途：展示"只动一个协议旋钮"时召回–精度–代价怎么变化；**不是**五协议夺冠总表。D、E 分开展示，**禁止混合平均**。

| 轴（前 → 后） | VisDrone D：Δsmall_recall／Δprecision／Δms | UAVDT E：Δsmall_recall／Δprecision／Δms | 判读 |
|---|---|---|---|
| 分辨率：F640 → F1280 | +0.1616／+0.0045／+16.3 | +0.0849／−0.0584／+16.3 | 两集都是召回升；D 上精度基本持平，E 上精度下降 → 权衡面依赖数据域 |
| 选区→全覆盖：DensK1 → UnifAll | +0.0916／−0.0948／+78.1 | +0.0152／−0.0159／+14.2 | 覆盖增加抬高召回，代价是精度和时延；D 上更陡 |
| 工程切片 vs 整图高分：SAHI640 → F1280 | +0.1820／+0.3166／−339.5 | +0.0332／+0.0189／−130.9 | 由 SAHI640 换成 F1280：召回↑、精度↑、时延大幅下降；即本冻结设置下 SAHI640 三项都不如 F1280 |
| 同为切片族：SAHI640 → UnifAll | +0.2327／+0.1536／−261.0 | +0.0227／−0.0213／−116.8 | D：UnifAll 召回和精度都更高，而且更快；E：UnifAll 召回更高、更快，但**精度略低** |

数据来源：D 取自 `D_TESTDEV_summary.json` 与 `F_bootstrap_deltas.csv`（Run `P0-BENCH-D-TESTDEV-20260917-01`／`P0-BENCH-F-TESTDEV-20260917-01`），E 取自 `E_FULL_summary.json`（Run `P0-BENCH-E-UAVDT-20260918-FULL`）。

> ✅ **已于 2026-09-27 修正原表：** `Neighbor_Protocol_Table.md` A、B 两表的所有行都已按"后 − 前"从 summary JSON 重新计算。修正内容：① SAHI640 两行原来按"前 − 后"填写（符号反了）；② 三处舍入：D DensK1→UnifAll 的 Δsmall_recall +0.0915→+0.0916，E F640→F1280 的 Δprecision −0.0583→−0.0584、Δms +16.4→+16.3；③ E SAHI640→UnifAll 的 Δprecision 原值 −0.0214 在两种符号约定下都对不上，重算为 −0.0213（UnifAll 精度低于 SAHI640）。本文初版照抄了原表的三处舍入值，并把 E 的这个精度差误写成 +0.0214，上表已一并更正。

### 4.2 失败／边界例（`Failure_Boundary_Cases.md`）

每例四要素：协议｜Image ID 或检索规则｜现象｜不外推的边界句。ID 都是在 Stage D 冻结 CSV 上按规则检索得到的。

| 例 | 协议 | 代表图像 | 现象（来自原表） | 边界句 |
|---|---|---|---|---|
| (a) 小目标漏检 | F640 ↔ F1280 | `9999996_00000_d_0000028.jpg`（次选 `9999938_00000_d_0000059.jpg`）；规则：small_gt≥10，取 F1280−F640 的 recall_small 最大者 | small_gt=14：F640 small_tp=3（≈0.21）→ F1280 12（≈0.86），Δ≈+0.64 | 低有效分辨率容易丢小目标；**不能**推出"F640 没有部署价值"（它最快） |
| (b) 误检抬升 | UnifAll／SAHI640 vs F1280 | `9999938_00000_d_0000207.jpg`（UnifAll FP=209，SAHI FP=203，F1280 FP=121）；次选 `9999979_00000_d_0000009.jpg` | 在密集或纹理复杂的图上，FP 和 n_dets 明显增加 | 切片抬召回常常要付精度代价；**不能**推出"切片一定更差" |
| (c) 接缝／重复框风险 | SAHI640 vs F1280 | `0000310_03500_d_0000125.jpg`（SAHI n_dets=104 vs F1280=17，prec≈0.08）；次选 `0000265_03000_d_0000007.jpg` | 检测数和 FP 膨胀（用"过检"作代理指标，不是逐框接缝标注） | 讨论接缝时必须披露 overlap 和 NMS 参数；**不能**写成"SAHI 族普遍失败" |
| (d) 映射空洞 | Stage E 映射 | 不需要单图 ID：映射规则本身就是边界 | 行人／非机动车类在 UAVDT DET 中没有对应类别 → 评价上界受映射限制 | 这是合法的跨集边界；**禁止**看分后改映射，也不能把映射外类别的漏检写成协议失败 |

### 4.3 复现附录（`Reproducibility_Appendix.md`）

清单已全部勾选：权重路径 + SHA、五协议配置（imgsz／crop／overlap／conf／IoU／NMS）、映射版本与冻结状态、评价器声明、split 与图像数（D 1610／E 40735／B 48×3／F 1610）、硬件分列（4090 标为 TODO）、Run ID 列表（G 为 NOT YET）、硬禁令。

本文核查后建议补充的复现项及状态（2026-09-27）：① 运行脚本 → **已恢复**（附录 §10）；② sahi 运行时版本 → **open**（无法事后确认；附录 §10 只记录了事后看到的 0.11.32 和默认后处理参数）；③ `stage_e_config_freeze.json` 的 smoke run_id → **已加注**（`Run_Index.md`、Stage E 报告 §8；JSON 未改）；④ UAVDT 路径 → **已更新**（Current_Stage、Stage E 文档）。

### 4.4 图 1–5（`05_packaging/figures/`，由 `generate_plots.py` 从 summary JSON 现场再生）

| 图 | 文件 | 展示内容 | 数据来源 | Run ID |
|---|---|---|---|---|
| 图 1 | `fig1_visdrone_metrics.png` | 左：五协议 Precision 与 small-object recall 分组柱状图；右：单次运行 mean latency 柱状图 | `01_visdrone_main/data/D_TESTDEV_summary.json` | `P0-BENCH-D-TESTDEV-20260917-01` |
| 图 2 | `fig2_uavdt_metrics.png` | 与图 1 相同版式，数据集为 UAVDT DET FULL | `03_cross_uavdt/data/E_FULL_summary.json` | `P0-BENCH-E-UAVDT-20260918-FULL` |
| 图 3 | `fig3_dual_set_small_recall.png` | 两个数据集的小召回并排柱状图（标题注明 do not pool D+E） | D + E 两个 summary | 上面两个 Run ID |
| 图 4 | `fig4_timing_1660.png` | Stage B 每协议的 mean 与 median 时延（标题注明 GTX 1660 SUPER，cal48，3 reps；4090 N/A） | `04_timing/data/B_TIMING_summary.json` | `P0-BENCH-B-TIMING-20260917-01` |
| 图 5 | `fig5_stageF_deltas.png` | 5 个配对的 Δ small recall 横向条形图 + 95% bootstrap CI：F1280−DensK1（主）+0.0409、F1280−F640 +0.1616、UnifAll−DensK1 +0.0916、F1280−UnifAll −0.0507、F1280−SAHI640 +0.1820 | `02_paired_stats/data/F_summary.json → bootstrap_all` | `P0-BENCH-F-TESTDEV-20260917-01` |

完整对照表见根目录 `FILE_CATALOG.md` §4。纪律：要改图，先改证据 JSON 或报告；脚本不能硬编码指标。

---

## 五、主张—证据对照表

| 主张（原文或拆分） | 证据（数字 + 来源） | 强度 | 注意事项／建议措辞 |
|---|---|---|---|
| **C1-a：F1280 比 DensK1 更准** | D：Δsmall recall +0.0409，CI [0.0355, 0.0462]，Wilcoxon p=2.997e-28；Δprecision +0.0681 [0.0631, 0.0731]（`F_summary.json`，F-run）。cal48：1312 vs 1172 小 TP（`C_cal48_summary.json`）。E：small recall 0.793 vs 0.767，precision 0.372 vs 0.347（`E_FULL_summary.json`） | **强**（D，配对统计）／**中**（E，只有 pooled，没有配对检验） | 指标是匹配器 precision／small_recall（conf 0.25 单阈值），不是 AP；cal48 只是开发证据 |
| **C1-b：F1280 比 DensK1 更快** | B（1660 cal48）：mean 33.15 vs 35.34，p95 38.73 vs 43.20；T=40 超时率 0 vs 0.021（`B_TIMING_summary.json`）。D（单次运行）：Δmean −0.34 ms，CI [−0.66, −0.01]，但时延 Wilcoxon p=0.235，逐图中位差 +0.25 ms（`F_summary.json`）。E：mean 33.08 vs 32.97（DensK1 略快） | **弱** | 只有 1660 数据；三个来源方向不一致。**建议改写为："在同量级时延下（1660），F1280 比 DensK1 更准"**；等 4090 正式表出来后再决定是否保留"更快" |
| **C2：区域分配有可恢复空间，但不等于可部署增益；必须同时报告超时率与选择漏检** | 可恢复空间：DensK1→UnifAll 在 D 上 Δsmall recall +0.0916 [0.0866, 0.0966]（`F_bootstrap_deltas.csv`），E 上 +0.0152。代价：D 上 Δprecision −0.0948、Δms +78.1；B 中 T=40 超时率 DensK1 0.021 vs UnifAll 1.000，T=100 时 UnifAll 仍为 0.729（`B_TIMING_summary.json`）。历史：GT oracle 选择仅净增 33（BTD，`Research_Plan.md`，不在 P0_EI data 中） | **中** | "选择漏检"（未选区域中漏掉的目标）在 P0_EI 数据槽中**没有单独的表** → **待补**（可以引用 BTD 历史结果，或基于现有逐图 CSV 做描述性统计；不做新推理）。GT oracle 不能写成方法精度 |
| 分辨率抬小召回（近邻表 C1 的说法） | F640→F1280：D +0.1616 [0.1559, 0.1675]，精度差 CI 跨 0；E +0.0849（精度 −0.0584） | **强**（D）／**中**（E） | 权衡面依赖数据域（E 上精度下降） |
| 边界主张：协议改变权衡，但没有通用排序 | D 排序 UnifAll > F1280 > DensK1 > F640 > SAHI640；E 排序 F1280 > UnifAll > DensK1 > SAHI640 > F640（`StageE_UAVDT_Report.md` §4） | **强**（作为边界） | 写成负结果或边界，不能写成"C1／C2 失败" |
| SAHI640 在本冻结设置下代价效益最差 | D：0.2184／0.3587／373 ms；E：0.760／0.353／164 ms；B：mean 317 ms | **中** | 只适用于 sahi 默认后处理（GREEDYNMM／IOS，含整图标准预测）+ 统一 finalize；不能推广到 SAHI 族 |

---

## 六、局限与待办

### 6.1 4090 正式时序（必须单列）

- 待跑：`P0-BENCH-G-4090-SMOKE-20260920-01` → `…-CAL48-…` → `…-TESTDEV-…`（UAVDT 可选）（`Next_Authorized_Runs.md`）。
- 结果**只写进** `P0_EI/04_timing/` 下独立的 `Timing_4090_Table.md`（目前 pending），**不能和 1660 合并成一行或一张表**。正文时序只用 4090；D／E 精度表保持不变；1660 标注为 pipeline validation。
- 4090 表是 C1-b"更快"能否保留的关键证据。

### 6.2 稿件／PDF

- `PR/` 下目前**没有稿件正文或 PDF**，只有提纲 `PR/Writing/P0_EI_Outline.md`（6 节结构）。
- 会期没有写进 `Current_Stage.md`（Mainline §8 成功标准 1）→ 待补；主跟踪会议为 ICIP 2027 全文，截稿日需核实。
- 文献：`Literature_Matrix.md` 的 9 篇都是 SCREENED，MUST 篇 PDF 待放入各主题的 `pdfs/`；ClusDet 等书目需补 DOI。

### 6.3 可选增强（不引入新算法、不新推理、不训练；都需要按 Current_Stage 纪律另行确认）

1. **Stage E 图级配对统计**：只用现有 `E_FULL_per_image_metrics.csv`，套用 Stage F 的方法（需另登记 Run ID）。
2. **"选择漏检"描述表**：补 C2 的另一半证据（依据 BTD 历史或现有逐图 CSV）。
3. **超预算率曲线图**：从 `B_TIMING_summary.json` 已有的 `budget_violation_rate` 画 T–超时率曲线（4090 出来后另画一张，不叠加）。
4. **recall_all 列和 n_dets 列**：本文已派生，可作补充表。
5. 把 C1 的措辞按第五节建议改写，并统一近邻表和 Research_Plan 对 C1／C2 的说法。

### 6.4 发现的文档不一致及处理状态（2026-09-27 更新）

> 用户已批准修正。下表标出每项是"已修"（附改动的文件）还是"open"（附原因）。所有数值结果都没有改动；冻结的 JSON 都没有改动；ACTIVE 仍为 P0_EI。

| # | 不一致 | 状态 | 改动文件／说明 |
|---|---|---|---|
| 1 | C1／C2 措辞：近邻表 §C 写成"分辨率轴""选区覆盖轴"，与 Research_Plan 原文不一致 | **已修** | `05_packaging/Neighbor_Protocol_Table.md` §C：按 Research_Plan §2.1 原文对齐，轴的说法保留为括注 |
| 2 | C1"更快"不被 1660 上的 B／D／E／F 数据支持；BTD8 的历史数字已被 Stage B 取代 | **已加核注；主张措辞仍 open** | `PR/Research_Plan.md` §2.1、`PR/Mainline_A_Current.md` §4 各加一条 2026-09-27 核注（引用数字和文件）。改写为"时延相当下更准"还是等 4090 表，由用户决定 |
| 3 | 近邻表 SAHI 两行的符号与表头约定相反 | **已修** | `Neighbor_Protocol_Table.md`：A、B 两表全部按"后 − 前"从 JSON 重算；另外修了 3 处舍入和 E SAHI→UnifAll 的 Δprecision（−0.0214→−0.0213）；文末附修订记录 |
| 4 | 失效链接 `Research_Question_Decision_2026-09-16.md`（已于 commit `c97f263` 删除）和 `P0_Benchmark_StageE_UAVDT_Report.md` | **已修** | `00_Overview/Current_Stage.md`（改指 `Mainline_A_Current.md`／`03_cross_uavdt/StageE_UAVDT_Report.md` 并加说明）；同一失效链接也在 `PR/Research_Plan.md`、`PR/Mainline_A_Current.md`、`PR/Stage_Guide.md` 中修了 |
| 5 | Current_Stage 的下一步仍写"EI 包装" | **已修** | `Current_Stage.md`：包装标为 DONE（进度表加一行），下一步改为 ① 4090 时序（单独成表）② 稿件正文；ACTIVE 表没动。同步修了 `Experiments/00_Index.md` 和 `Writing/P0_EI_Outline.md` 中过时的"包装待补" |
| 6 | 运行脚本不在 HEAD 中 | **已修** | 从 `bad0f8b` 恢复 5 个脚本；Stage B／D／E／F 报告末尾各加路径说明；`00_freeze/Environment_Freeze.md` 加 stage_a 路径说明；`Experiments/README.md` 登记例外；`Reproducibility_Appendix.md` §10 列出脚本和 SHA；`FILE_CATALOG.md` §6 加一行 |
| 7 | Run_Index 中 Stage C 写"cal48" | **已修** | `Run_Index.md`：C → `P0-BENCH-C-CAL48-20260917-01`（A 也补为 `P0-BENCH-A-ENV-20260917-01`） |
| 8 | `stage_e_config_freeze.json` 带的是 smoke 的 run_id | **已加注** | `Run_Index.md` 注、`StageE_UAVDT_Report.md` §8；冻结 JSON 有意不改 |
| 9 | UAVDT 路径变了 | **已修** | `Current_Stage.md`、`03_cross_uavdt/StageE_Channel_Decision.md`、`StageE_UAVDT_Report.md` §8（新路径 `G:\Schloar Data\P0\UAVDT`，已核实存在）；冻结 JSON 保留旧路径 |
| 10 | 类别映射 md 第 7、18 行有控制字符 | **已修** | `00_freeze/Class_Mapping_Preregister.md`：只修文本编码，恢复 truck／bus／van 字样，文末加注；映射本身没改 |
| 11 | "双 4090"与"本机只有 1660"的关系没说明 | **已加注** | `PR/Mainline_A_Current.md` §1 |
| 12 | 运行时的 sahi 版本没有冻结 | **open** | 运行时版本已经无法事后确认；`Reproducibility_Appendix.md` §10 只记录了事后看到的 0.11.32，并注明它不是运行时证据 |
| 附 | venue 政策没有 P0 专节 | **已修** | `00_Overview/Venue_and_Claim_Policy_JCR_2026-09-24.md` 新增 §8，只放指向 Research_Plan 和两篇安排的指针，不做新决定 |
| 附 | Current_Stage 登记的 T4 目录 `G:\Schloar Data\P0_T4_Train\` 已不存在 | **已加注** | `Current_Stage.md` |

**仍然 open 的其他发现（不在原来 12 项里，本次没改）：**
- `PR/Research_Plan.md` 的历史段落里还有几个失效链接：`Literature/matrices/Mainline_A_Prior_Work_Comparison.md`、`Experiments/Training_Interface_Audit.md`、`Experiments/Diagnostic_Admission_Review.md`、`Research_Plan_Railway_A0_History.md`。它们都属于 HOLD 的历史叙述，重构时被归档或删除，应该改指哪里需要用户确认。
- `PR/Experiments/README.md` 说归档位于 `_Archive_20260923_PreP0_Cleanup/Experiments/`，但仓库里找不到这个目录，可能在仓库外或已被删除，需要用户确认。

### 6.5 下一步可检查事项（按优先级）

1. ~~修正第 6.4 节中的文档错误~~ 已完成（2026-09-27），只剩 #2 的措辞决定和 #12。
2. 在 4090 机器上按 Run G 登记并跑正式时序 → 写 `Timing_4090_Table.md`（单列）。
3. 按第五节建议统一 C1／C2 措辞，按提纲开始写正文（Intro／Protocols & Evaluation／Results／Failure & Boundaries）。
4. 选定会期并写入 Current_Stage（由用户操作）。
5. 可选：Stage E 配对统计、选择漏检表（只做分析）。

---

## 七、文件索引（关键路径）

| 类别 | 路径 |
|---|---|
| 唯一当前事项 | `00_Overview/Current_Stage.md` |
| 发表／主张政策 | `00_Overview/Venue_and_Claim_Policy_JCR_2026-09-24.md` |
| 练手入口／计划 | `PR/README.md` · `PR/Research_Plan.md` · `PR/Mainline_A_Current.md` · `PR/Stage_Guide.md` |
| 写作 | `PR/Writing/P0_EI_Outline.md` · `PR/Writing/P0_Two_Paper_Plan_2026-09-22.md` |
| 文献 | `PR/Literature/Literature_Matrix.md`（T1 切片／T2 高分高效 SOD／T3 多尺度放大／T4 航拍基准） |
| 证据槽入口 | `P0_EI/README.md` · `P0_EI/Run_Index.md` |
| Stage A 冻结 | `P0_EI/00_freeze/Environment_Freeze.md` · `weight_sha_reverify.txt` · `DensK1_Definition.md` · `class_mapping_preregister.json` · `Class_Mapping_Preregister.md` · `stage_d_config_freeze.json` · `stage_e_config_freeze.json` · `env_snapshot.txt` · `gpu_snapshot.txt` · `git_snapshot.txt` · `pip_freeze.txt` · `script_sha256.txt` |
| Stage B | `P0_EI/04_timing/StageB_Timing_Report.md` · `data/B_TIMING_summary.json` · `B_TIMING_timings.csv` · `B_TIMING_protocol.json` |
| Stage C／D | `P0_EI/01_visdrone_main/StageC_Cal48_Dev_Report.md` · `StageD_TestDev_Report.md` · `StageD_Channel_Decision.md` · `data/C_cal48_summary.json` · `C_cal48_metrics.csv` · `D_TESTDEV_summary.json` · `D_TESTDEV_per_image_metrics.csv` · `D_TESTDEV_status.json` |
| Stage E | `P0_EI/03_cross_uavdt/StageE_UAVDT_Report.md` · `StageE_Channel_Decision.md` · `data/E_FULL_summary.json` · `E_FULL_per_image_metrics.csv` · `E_FULL_status.json` |
| Stage F | `P0_EI/02_paired_stats/StageF_Paired_Stats_Report.md` · `data/F_summary.json` · `F_wilcoxon_recall_small.csv` · `F_bootstrap_deltas.csv` · `F_status.json` |
| 包装 | `P0_EI/05_packaging/README.md` · `Neighbor_Protocol_Table.md` · `Failure_Boundary_Cases.md` · `Reproducibility_Appendix.md` · `Next_Authorized_Runs.md` |
| 图 | `P0_EI/05_packaging/figures/fig1_visdrone_metrics.png` … `fig5_stageF_deltas.png` · `FIGURES.md` · `generate_plots.py` |
| 图↔数据总表 | `FILE_CATALOG.md` §4 |
| 运行脚本（历史 commit） | `git show bad0f8b:00_Practice_UAV_Aerial_Detection/Experiments/P0_Benchmark/stage_{b,d,e,f}/run_stage_*.py`；`…/Experiments/diagnose_bt1.py` |
| 冻结权重 | `11_Datasets/processed/VisDrone/BT1/BT1-LOCAL-20260913-01/train/weights/last.pt`（SHA `bc42d54e…5533`） |
