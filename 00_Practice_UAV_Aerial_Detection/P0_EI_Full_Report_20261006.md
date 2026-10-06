# P0_EI 练手论文完整报告：背景、故事线、实验构成与全部结果

> **生成：** 2026-10-06（Asia/Shanghai）。**读者：** 你本人，作为学习者，从零了解这篇练手论文：为什么做、怎么做、做了什么、得到什么。  
> **与导读的关系：** [`P0_EI_Paper_Overview_and_Experiments.md`](P0_EI_Paper_Overview_and_Experiments.md)（下称“导读”，2026-09-27）是**查数手册**，按论文章节列出 Stage A–G 的全部表格。本报告是它的**叙事伴读**：讲背景和时间线，解释每个术语，并补上 2026-10-06 新做的 Run H／I／J／K。数字两边一致；有冲突时以源文件（各 Stage 报告与 `data/*.json`／`*.csv`）为准。  
> **效力：** 纯文档，不新增实验，不改冻结件，不改变 [`../00_Overview/Current_Stage.md`](../00_Overview/Current_Stage.md) 的唯一 ACTIVE = **P0_EI**。  
> **数字纪律：** 每个数字都注明来源文件与 Run ID。仓库里找不到的写 **待补**。来自仓库外（Git 忽略的 `11_Datasets/`、G 盘）的写明“仓库外”。  
> **路径简写：** `PR/` = `00_Practice_UAV_Aerial_Detection/`（本文件所在目录）；`P0_EI/` = `PR/Experiments/papers/P0_EI/`；`BENCH/` = `PR/Experiments/P0_Benchmark/`。  
> **GPU 纪律：** GTX 1660 SUPER（环境 UAV_BT1）与 RTX 5060 Ti（环境 UAV_BT2）的时延**从不合进同一张表或同一列**。需要并排时，每列都写明 GPU 和环境。“更快”一律带 GPU 名称。

**建议阅读顺序：** §1（为什么做）→ §2（主张）→ §3.4（五种协议）和 §3.5（匹配器）→ §4（故事线）→ §5（结果）→ §6（怎么读、怎么选）→ §7（局限）。§10 术语表随时查。

---

## 目录

1. 背景与动机  
2. 研究问题与主张 C1／C2  
3. 实验设置（权重、数据、五协议、匹配器、统计、硬件）  
4. 故事线：Stage 0 与 A–K 按时间顺序  
5. 全部结果表  
6. 结果解读与“怎么选协议”  
7. 局限与效度威胁  
8. 复现指引（文件地图、脚本、冻结件）  
9. 距离投稿还差什么  
10. 术语表与 Run ID 表  

---

## 1. 背景与动机

### 1.1 这篇论文在博士计划里的位置

- **博士总体方向：** 铁路无人机巡检。七篇主论文依次是危险感知 → 三维灾害量化 → 通信受限风险共享 → 通感资源分配 → 多模态风险理解 → 主动复检 → 多无人机联合决策（`PROJECT_CONTEXT.md` §2，`00_Overview/Seven_Paper_Roadmap.md`）。
- **P0 是“练手论文”：** 在 Paper 1 之前单独做，**不计入七篇主论文**（`PROJECT_CONTEXT.md` §2）。目录名 `00_Practice_UAV_Aerial_Detection` 里的 Practice 就是这个意思。
- **它的三个用途**（`00_Overview/SWJTU_Info_College_Degree_Credit_Note_2026-09-28.md` §5）：“**练手 + 占坑 + 第二篇引用基线**”。
  - 练手：完整走一遍实验冻结、评测、统计、写作的流程。
  - 占坑：先把“推理协议对比”这个实证结果发出来。
  - 引用基线：后续第二篇（方法文）要把这篇会议版当作初步实证来引用（`PR/Writing/P0_Two_Paper_Plan_2026-09-22.md`）。
- **现在的状态：** 全项目唯一 ACTIVE 事项就是 P0_EI。Post-EI 的 A（RailUAV-SOD，`08_RailUAV_SOD/`）和 B（Paper1 开放世界风险，`01_Paper1_OpenWorld_Risk/`）只是 IDLE／PREP 预备包；Paper 2–7 都是 PAUSED（`00_Overview/Current_Stage.md`“Post-EI 预备包登记”）。

### 1.2 为什么 “EI 先行”

- **先发一篇小而稳的会议稿。** 研究计划写明本篇目标是 **EI 会议**，不承诺录用（`PR/Research_Plan.md` §1）。
- **会议选择：** 首投 **IJCNN 2027**（截稿 2027-01-31），落选转投 **ICIP 2027**（截稿 2027-03-31）（2026-10-06 定；均为 CCF-C，投稿前要按 CCF 第七版核对），备选 ACCV／ICPR 全文；不把 CCF-B（ICME／ICASSP）当第一目标；Workshop／短文通常不算目录会议（`PR/Writing/P0_Two_Paper_Plan_2026-09-22.md`）。
- **分区口径：** 期刊看 **JCR**（Q1–Q4），会议看投稿时的 **CCF 推荐目录**；“被 EI 收录”只是描述项，不能代替 CCF／JCR（`00_Overview/Venue_and_Claim_Policy_JCR_2026-09-24.md` §1）。该政策文件正文只有 A／B 两篇的梯子，**没有 P0 专条**（导读 §1.7 注）。
- **2026-10-06 投稿出口（用户决定）：** 练手不计学位分，CCF-C 优先：首投 **IJCNN 2027**（截稿 2027-01-31，≤6 页 IEEE 双栏）；落选转投 **ICIP 2027**（截稿 2027-03-31，CCF 第七版仍为 C 类）。见 `00_Overview/Current_Stage.md`「Venue / 学位分」。

### 1.3 学位分：为什么这篇“不计分”也要做

来源：`00_Overview/SWJTU_Info_College_Degree_Credit_Note_2026-09-28.md`（依据学院 2021 细则和学校 2023 期刊目录；最终以分委员会书面解释为准）。

| 事实 | 内容 |
|---|---|
| 学术型博士正常评阅 | 创新成果分 **≥ 30**，至少两篇论文，其中至少一篇第一作者 SCI 期刊 |
| CCF-C 会议（ICIP、ACCV、ICPR 等） | 表上 6 分，但学术博士**不计分** |
| 普通 EI 会议 | **0 分**，也不能顶替“一篇 SCI 期刊” |
| 最小闭环 | 两篇本人一作 SCI 一区或二区（每篇 15 分）= 30 分 |

所以 P0 的价值**不在学位分**。它是练手、占坑，并给第二篇（目标 JCR Q2 应用／系统刊）当引用基线。学位最小闭环仍是“两篇能计分的 SCI 期刊（建议二区）”。

### 1.4 研究主题怎么来的（一句话版）

最早想做一个**新的区域选择机制**（只在图里最密的局部用高分辨率重看一次，以省时间）。实验发现，**直接把整图放大到 1280 再推理一次（F1280）**比这个机制更准，时延也不差。新机制因此搁置（HOLD），论文改成**“同一个冻结检测器上，几种推理协议的系统对比”**。详细经过见 §4 的 Stage 0。

---

## 2. 研究问题与主张 C1／C2

### 2.1 研究问题

> 在同一冻结检测器、同一后处理门槛下，只改变推理协议（输入分辨率／是否切片／切哪些片），航拍小目标的召回、精度与端到端时延如何权衡？何时增益只是来自分辨率或覆盖范围？  
> —— `PR/Research_Plan.md` §1

几个术语先解释：

- **冻结检测器（frozen detector）：** 权重训练好以后不再改动。整个实验只用一个权重文件，用 SHA256 指纹核对，保证每一步用的是同一份。
- **推理协议（inference protocol）：** 同一个模型，“怎么把图喂进去、怎么把结果拼回来”的规则。例如整图缩到多大、要不要切成小块、切哪几块、怎么合并重复框。
- **小目标（small object）：** 本项目定义为原图像素面积 $0 < w\cdot h < 1024$ 的目标，即面积小于 $32\times 32$ 像素。
- **召回（recall）／精度（precision）：** 召回 = 真目标里被找到的比例；精度 = 报出的框里正确的比例。精确定义见 §3.5。
- **端到端时延（end-to-end latency）：** 从“图像已在内存里”到“拿到最终框”所花的时间，单位 ms。边界见 §3.4.6。

### 2.2 主张 C1（终稿措辞，C1 时延部分 2026-10-06 改为分 GPU）

> **P0-EI-C1：** 在单一冻结 YOLO11n 权重与 conf 0.25／IoU 0.5 匹配口径下，VisDrone test-dev 上 F1280 比 DensK1 **更准**：small recall +0.0409（图级 bootstrap 95% CI [0.0355, 0.0462]），precision +0.0681（CI [0.0631, 0.0731]）。时延分 GPU 表述：在 **GTX 1660 SUPER（UAV_BT1）** 上两者时延**统计上不可区分**（逐图 Wilcoxon p = 0.235，均值差 −0.34 ms）；在 **RTX 5060 Ti（UAV_BT2）** 上 **F1280 更快**（均值差 −14.01 ms，95% CI [−14.22, −13.80]，p≈3.6e-264，1607／1610 张图更快；`P0-BENCH-G-5060TI-PAIRED-20261006-01`）。时延排序取决于 CPU／流水线：5060 Ti 运行中 GPU 平均利用率约 11%，CPU 为 Ryzen 5 5600G（Windows“平衡”电源计划），耗时未分解；不写不带 GPU 名称的“更快”。  
> —— `PR/Research_Plan.md` §3（状态 SUPPORTED，Stage B/D/F/G）

用大白话说：**整图放大到 1280 推理一次，比“整图 640 + 最密的一块局部”更准。** 时延谁快取决于机器：在 1660 上两者打平；在 5060 Ti 上 F1280 明显更快。

### 2.3 主张 C2

> **P0-EI-C2：** 选区／覆盖协议只移动召回–精度–时延权衡，没有跨数据集通用的最优协议：VisDrone 上 UnifAll small recall 最高（0.4511，比 F1280 高 0.0507），但时延约 3.3×（112.2 vs 33.7 ms）且精度下降（0.5123 vs 0.6753）；本冻结设置下 SAHI640 在两集上均被 F1280 支配；UAVDT 上排序改为 F1280 > UnifAll > DensK1 > SAHI640 > F640。  
> —— `PR/Research_Plan.md` §3、导读 §1.4

大白话：**多切几块能多找到一些小目标，但要付出精度和时间。没有哪种协议在两个数据集上都是第一。** 按默认设置使用的 SAHI 在本设置下三项（召回、精度、时延）都输给 F1280。“支配（dominated）”就是指这种“每一项都不如”。

### 2.4 C1 措辞的三次变化

| 时间 | 措辞 | 依据 | 来源 |
|---|---|---|---|
| 2026-09-14 | “F1280 比实际单片**更准且更快**” | BTD9（cal48，48 张开发图）：F1280 1312 个小 TP，27.33／41.44 ms（均值／p95）；DensK1 1172 个，37.36／64.51 ms | `PROJECT_CONTEXT.md` §6 表 |
| 2026-09-27 | “**时延统计不可区分下**更准” | Stage F（test-dev 1610 张，1660）：时延逐图 Wilcoxon p = 0.235，均值差只有 −0.34 ms，中位差反而 +0.25 ms | `PR/Research_Plan.md` §3.4；`P0_EI/02_paired_stats/data/F_summary.json` |
| 2026-10-06 | **分 GPU：**1660 不可区分；5060 Ti 上 F1280 更快 | Run G 配对检验：均值差 −14.01 ms，1607／1610 张更快 | `PR/Research_Plan.md` §3.4；`P0_EI/04_timing/data/G_PAIRED_summary.json`；commit `bb617f0` |

教训：BTD8 的计时实现和轮次跟 Stage B 不同，成稿**只引用 Stage B／D／F 和 Run G 的数字**，BTD8 的数字只作历史说明（导读 Stage B 节）。

### 2.5 刻意**不**主张的东西

来源：`PR/Research_Plan.md` §1、§3.3、§6；`00_Overview/Current_Stage.md`“实验门”；导读 §1.6。

1. **不是新检测器、不是新模块。** 摘要写 *experimental evaluation*，不写 *we propose*。
2. **不说“F1280 更快”而不带 GPU 名称。** 1660 上只写“统计上不可区分”。
3. **不说存在跨数据集通用的五协议排序。**
4. **不说结果对所有检测器成立。** 只有一个权重（YOLO11n，seed 0）。
5. **不把匹配器指标说成 AP。** 不是 COCO AP，不是 VisDrone 排行榜 AP，也不是 UAVDT 官方 MATLAB AP。
6. **不说 SAHI 族普遍不行。** 只说“按 sahi 默认设置使用”时被 F1280 支配。
7. **不把 VisDrone 结果写成铁路安全或高原泛化结论。**
8. **不把 GT oracle（用真值挑最好结果）写成方法精度。**
9. 旧区域机制主张 **P0-A-C1／C2 保持 HOLD**，不指导本稿。

---

## 3. 实验设置

### 3.1 冻结权重：BT1 YOLO11n，100 轮

| 项 | 值 | 来源 |
|---|---|---|
| 模型 | YOLO11n（Ultralytics，P3–P5 三个检测尺度），COCO 预训练初始化后适配 VisDrone 十类；**没有**改 backbone、loss 或加模块 | `PROJECT_CONTEXT.md` §5 |
| 训练 | VisDrone train 6471 张，cal48 监控，seed 0，imgsz 640，batch 4，FP32，SGD，100 轮；GTX 1660 SUPER 6 GiB；环境 `H:/Conda/envs/UAV_BT1`；Ultralytics 8.4.90（提交 `07958a70…`），torch 2.7.1+cu126 | `P0_EI/00_freeze/provenance/BT1_100_Epoch_Archive.md` |
| Run ID | `BT1-LOCAL-20260912-01`（第 1–3 轮）→ `…-20260912-02`（第 4 轮）→ `BT1-LOCAL-20260913-01`（第 5–100 轮，PASS） | 同上 |
| 墙钟 | 1121.17 + 378.20 + 52463.16 s，合计约 14.99 小时（含系统等待，不是 GPU 计费小时） | 同上 |
| 选模规则 | 固定取**第 100 轮** EMA `last.pt`，不按 cal48 最佳值挑 | 同上；`PROJECT_CONTEXT.md` §5 |
| 权重路径 | `11_Datasets/processed/VisDrone/BT1/BT1-LOCAL-20260913-01/train/weights/last.pt`（仓库外，Git 忽略） | `P0_EI/00_freeze/Environment_Freeze.md` |
| **SHA256** | **`bc42d54e37acaf1f698af487439dc222fa86fb4498623e8cf954df14e0aa5533`**，5457882 bytes，主权重与归档副本两份都一致 | `P0_EI/00_freeze/weight_sha_reverify.txt` |
| 归档包 | `BT1_100epochs_evidence.zip`，46,344,126 bytes，SHA256 `9419bf3c…cad21b0`（同一块本机磁盘，不是异地备份） | `BT1_100_Epoch_Archive.md` |
| 第 100 轮原生监控值（cal48） | Precision 0.46533，Recall 0.34912，mAP50 0.34101，mAP50–95 0.18591 | 同上 |

> **SHA256 指纹：** 对文件内容算出的 64 位十六进制串。文件改动哪怕一个字节，指纹都会完全不同。每个 Stage 运行前都断言权重 SHA 等于上表的值（`B_TIMING_protocol.json`、`D_TESTDEV_summary.json`、`E_FULL_summary.json`；Run G 由冻结脚本和启动器双重断言）。  
> **注意：** 上表的 mAP50 是 Ultralytics 自带验证器在 cal48 上的值，**不能**和本项目匹配器的 precision／small recall 直接比较（`BT1_100_Epoch_Archive.md`）。

### 3.2 数据集

#### 3.2.1 VisDrone2019-DET test-dev（主评测）

| 项 | 值 | 来源 |
|---|---|---|
| 来源 | Ultralytics assets 镜像 `VisDrone2019-DET-test-dev.zip`（官方 Google Drive 的 train／test-dev 返回 *Quota exceeded*，故用镜像） | `P0_EI/00_freeze/provenance/A0-05_VisDrone_File_Audit.md`；`P0_EI/01_visdrone_main/StageD_Channel_Decision.md` |
| ZIP SHA256 | `b28a94b0…a6ea6a68d` | `P0_EI/01_visdrone_main/data/D_TESTDEV_summary.json` |
| 图像数 | **1610** | 同上 |
| 尺寸分布 | 1400×788: 933，1400×1050: 274，1360×765: 167，1916×1078: 151，960×540: 49，1920×1080: 36 | `P0_EI/04_timing/Pixel_Latency_Table.md` §1（Run I） |
| 十类 | pedestrian, people, bicycle, car, van, truck, tricycle, awning-tricycle, bus, motor | `P0_EI/00_freeze/class_mapping_preregister.json` |
| 小目标 GT | **50431** | `D_TESTDEV_summary.json` |
| 有效 GT（全尺寸） | 74707（派生：逐图 CSV `valid_gt` 求和） | 导读 §2.4 |
| 无小目标的图 | 111 张 → 召回检验的 N = 1610 − 111 = **1499** | 导读 §2.4；`F_summary.json` |
| 口径限制 | Ultralytics 的 train／test-dev ZIP 与作者原包的逐字节身份 Unknown（只有 val ZIP 与官方一致）；只能做学术／内部基准，不能声称官方挑战排名 | `StageD_Channel_Decision.md`；`PROJECT_CONTEXT.md` §4 |

> **test-dev：** VisDrone 公开了标注的测试划分。本项目把它当作**只用一次**的终评集（one-shot），不能拿来挑协议或挑权重（Stage D `one_shot: true`）。

#### 3.2.2 cal48（开发集，不是测试集）

- 从 VisDrone val 按 SHA256(`diag-v1:` + 文件名) 排序取前 48 张；清单 SHA256 `b0e27b1d…8e7f`（`PROJECT_CONTEXT.md` §4；`P0_EI/00_freeze/Environment_Freeze.md`）。
- 小 GT 2720，全尺寸有效 GT 3619（`PROJECT_CONTEXT.md` §4）。
- 它在训练时被用作监控，又在 BTD 诊断中反复使用，所以**只算开发证据**，论文里必须这样披露（`P0_EI/01_visdrone_main/StageC_Cal48_Dev_Report.md`）。

#### 3.2.3 UAVDT DET（跨数据集外推）

| 项 | 值 | 来源 |
|---|---|---|
| 版本 | 作者版 UAV-benchmark-M（帧）+ UAV-benchmark-MOTD_v1.0（标注工具包）；**50 个序列／40735 帧／50 个 `*_gt_whole.txt`**，布局 PASS | `P0_EI/03_cross_uavdt/StageE_UAVDT_Report.md` §1；`StageE_Channel_Decision.md` |
| 压缩包（仓库外） | `UAV-benchmark-M.zip` 6,809,272,793 bytes（时间戳 2026-09-17 17:09）；`UAV-benchmark-MOTD_v1.0.zip` 245,719,325 bytes（2026-09-17 16:50） | 本机 `G:\Schloar Data\P0\dataset\UAVDT\` 目录列表（2026-10-06 查看） |
| 尺寸分布 | 1024×540: 38829 帧，960×540: 1906 帧 | `Pixel_Latency_Table.md` §1（Run I） |
| 评测类别 | 只评车辆：car／truck／bus | `class_mapping_preregister.json` |
| 小目标 GT | **493861** | `P0_EI/03_cross_uavdt/data/E_FULL_summary.json` |
| 有效 GT（映射后车辆） | 798795（派生） | 导读 §2.4 |
| 无小目标帧 | 4649（派生） | 导读 §2.4；`K_Density_Slices_Report.md` §4 |
| ignore | 官方 `*_gt_ignore.txt` **不用**，也不虚构 VisDrone 式 ignore 区域（冻结规则） | `StageE_Channel_Decision.md` |
| 属性文件 | 场景／高度／视角属性包（`M_attr`）**不在盘上** | `P0_EI/06_density_slices/K_Density_Slices_Report.md` §6 |

**路径漂移（同一份数据，三处写法）：** 冻结的 `stage_e_config_freeze.json` 和 Stage E 脚本写 `G:\Schloar Data\UAVDT\`（运行时路径，冻结件有意不改）；`Current_Stage.md` 写 `G:\Schloar Data\P0\UAVDT\`（2026-09-27 核实）；**当前实际位置**是 `G:\Schloar Data\P0\dataset\UAVDT\`（2026-10-06 核实，解压目录时间戳 2026-10-04 21:13；`K_Density_Slices_Report.md` §6）。重跑 Stage E 必须用参数化副本并登记新 Run ID。

**类别映射（看到分数之前冻结）：** 登记时间 `2026-09-17T15:28:36`，状态 `FROZEN_PRE_RESULTS`（`P0_EI/00_freeze/class_mapping_preregister.json`、`Class_Mapping_Preregister.md`）。

| VisDrone（YOLO id） | VisDrone 名 | → UAVDT 名 | UAVDT id |
|---:|---|---|---:|
| 3 | car | car | 0 |
| 4 | van | car（显式合并） | 0 |
| 5 | truck | truck | 1 |
| 8 | bus | bus | 2 |
| 0,1,2,6,7,9 | pedestrian, people, bicycle, tricycle, awning-tricycle, motor | **排除**（GT 与预测两侧都不计分） | — |

> **为什么要“分前冻结”：** 如果先看到分数再决定 van 算不算 car，就可能（哪怕无意）挑出对某个协议有利的映射。先登记、后出分，是防止事后调参的标准做法。

### 3.3 一张图看懂五种协议

> [!example]- 图：五种推理协议在一张 1400×788 图上的视图
> ![[p0fr_protocols.svg|700]]

（图源：`PR/assets/P0_EI_Full_Report_20261006/p0fr_protocols.svg`；几何来自 `P0_EI/04_timing/data/I_PIXLAT_summary.json` 的 `geometry_by_size`（Run I）和 `P0_EI/05_packaging/Reproducibility_Appendix.md` §2.1（Run J）。）

### 3.4 五种推理协议（逐一详解）

实现读自冻结脚本 `BENCH/stage_b/run_stage_b_timing.py`（Stage D／E 都从这里 import 同一套函数）和 `PR/Experiments/diagnose_bt1.py`；细节已整理进 `Reproducibility_Appendix.md` §2.1–2.2（Run J，2026-10-06）。

#### 3.4.1 公共部分（F640／F1280／DensK1／UnifAll）

- **每个视图单独前向：** `model.predict(imgsz=…, rect=False, device=0, batch=1, half=False, conf=0.001, iou=0.5, max_det=1000)`，即 FP32、batch 1。
  - `rect=False`：输入一律是**正方形**（640×640 或 1280×1280），不足部分用灰边填充（letterbox）。
  - `conf=0.001`：每个视图先保留几乎所有候选框，真正的阈值在最后统一过滤。
- **统一终处理 finalize（五个协议最后都过这一步，含 SAHI640）：** 先保留 $\text{conf}\ge 0.25$ 的框，再做**按类别独立的 CPU NMS**（IoU > 0.5，稳定排序，最多保留 500 个；`diagnose_bt1.nms`）。
  > **NMS（非极大值抑制）：** 同一个目标常被预测出好几个重叠的框。NMS 按分数从高到低，删掉与已保留框重叠（IoU）超过阈值的框。  
  > **IoU（交并比）：** 两个框交集面积 ÷ 并集面积，0 表示不重叠，1 表示完全重合。
- **窗口网格 `axis_windows`（DensK1 和 UnifAll 共用）：** 窗口 640×640，步长 512，最后一窗贴边。每个坐标轴的起点集合为
  $$S(L)=\{0,512,1024,\dots\le L-640\}\cup\{\max(0,L-640)\}$$
  窗口是 x 起点与 y 起点的笛卡尔积。窗口贴到 640×640 画布左上角，空余处填灰值 114。局部预测只保留中心落在画布有效区域内的框，裁剪后平移回原图坐标（`Reproducibility_Appendix.md` §2.1）。
- **每图窗口数：** VisDrone 1400×788／1400×1050／1360×765 → **6 窗**；1916×1078／1920×1080 → **8 窗**；960×540 → **2 窗**；UAVDT 1024×540／960×540 → **2 窗**（`Reproducibility_Appendix.md` §2.1，来自 Run I `geometry_by_size`）。

#### 3.4.2 F640 与 F1280（整图）

- **F640：** 整图 letterbox 到 640×640，前向 1 次 → finalize。最快的基线。1400×788 图上的缩放系数 $640/1400\approx 0.457$ 。
- **F1280：** 整图 letterbox 到 1280×1280，前向 1 次 → finalize。C1 里的“强简单基线”。1400×788 上缩放约 0.914；UAVDT 1024×540 上缩放 $1280/1024=1.25$ ，即**放大**（上采样）。
- **平均局部缩放**（Run I，`Pixel_Latency_Table.md` §2–3）：VisDrone F640 0.451、F1280 0.901；UAVDT F640 0.627、F1280 1.254。窗口类协议恒为 1.0（原生像素）。

#### 3.4.3 DensK1（密度 Top-1 单片）

步骤（`P0_EI/00_freeze/DensK1_Definition.md`；`Reproducibility_Appendix.md` §2.1）：

1. 整图 640 前向（就是 F640）。
2. 取 F640 原始输出中 $\text{conf}\ge 0.25$ 的框，统计**框中心**落在每个窗口里的个数（半开区间）。
3. 取个数最多的窗口；同分时取索引最小的（`argsort(-score, kind="stable")[0]`）。
4. 对这 1 个窗口做 640 前向，映射回原图。
5. 整图预测 + 单片预测拼接 → finalize。

- 每图 **2 次前向**。名字里的 K1 指“只选 1 片”（K = 1）。
- 定义沿用 BTD8，**没有重新定义**。实现核对：Stage C 中 DensK1 在 cal48 上的小 TP = 1172，与 BTD8 锁定值一致（`StageC_Cal48_Dev_Report.md`）。

#### 3.4.4 UnifAll（同网格全覆盖）

- 整图 640 前向 + **同一网格的全部窗口**逐片 640 前向 → 全部拼接 → finalize。
- 每图 $1+N$ 次前向， $N$ 是窗口数（VisDrone 平均 7.11 次，UAVDT 3 次；`Pixel_Latency_Table.md`）。
- 角色：**覆盖上界／选区对照**。它告诉我们“如果每块都看，召回能到多少”，DensK1 与它的差就是“只挑一块”丢掉的部分。

#### 3.4.5 SAHI640（工程切片近邻）

> **SAHI（Slicing Aided Hyper Inference）：** 一个流行的开源切片推理库（ICIP 2022，`PR/Literature/Literature_Matrix.md` T1-01），把大图切成重叠小块分别检测，再合并结果。本项目把它当作“工程上最常用的切片做法”的代表。

调用：`sahi.predict.get_sliced_prediction`，sahi 0.11.32（Run G 运行时版本；Stage B–E 当时的版本无法事后证明，见 §7）。细节读自代码（`Reproducibility_Appendix.md` §2.1，Run J）：

| 项 | 值 |
|---|---|
| 模型封装 | `AutoDetectionModel.from_pretrained(model_type="ultralytics", confidence_threshold=0.001, device="cuda:0")`，未传 `image_size` |
| 每片推理 | 用 ultralytics `predict` 默认值：`imgsz` = 权重训练值 640，`rect=True`（最小填充），**`iou=0.7`、`max_det=300`** |
| 切片 | 640×640，重叠率 0.25／0.25 → 步长 $640-\lfloor 0.25\times 640\rfloor=480$ ；越界切片贴边回退，不填充 |
| 整图标准预测 | `perform_standard_pred=True`（默认），**仅当切片数 > 1 时**执行 |
| 合并 | **`GREEDYNMM`**，匹配度量 **`IOS`**，阈值 0.5，按类别（均为默认） |
| 最后 | 再过统一 finalize（conf ≥ 0.25 → NMS 0.5 → 500） |

**GREEDYNMM／IOS 的发现（Run J）：** 冻结脚本元数据写的是 `sahi_postprocess: "sahi_default_NMS"`。读源码后确认这是**误称**：实际默认是 GREEDYNMM（贪心合并），匹配用 IOS，不是 NMS。冻结文件不改，在附录里更正（`Reproducibility_Appendix.md` §2.1）。

> **GREEDYNMM（Greedy Non-Maximum Merging）：** 和 NMS 相似，但重叠框不是被删掉，而是被**合并**成一个更大的框。  
> **IOS（Intersection over Smaller）：** 交集面积 ÷ 两框中较小者的面积。小框被大框包住时 IOS 接近 1，比 IoU 更容易判为“重叠”。

两点要记住：

- SAHI640 的网格（步长 480）和 DensK1／UnifAll 的网格（步长 512）**不是同一个**。不过在本数据的几种尺寸上，切片数与 UnifAll 的窗口数恰好相同（例如 1400×788 都是 6 块；`Reproducibility_Appendix.md` §2.1）。
- SAHI640 每片的 `iou 0.7／max_det 300` 与其他四协议的 `iou 0.5／max_det 1000` 不同。这是“按 SAHI 默认使用”的一部分，**不是本项目调过的设置**，也是 SAHI 结果偏低的候选原因之一（未验证）。

#### 3.4.6 计时边界与预热

来源：`Reproducibility_Appendix.md` §2.2。

| 项 | 值 |
|---|---|
| 起点 → 终点 | 已解码的内存 BGR 图像 → finalize 后的 CPU 框；前后各一次 `torch.cuda.synchronize()`，`time.perf_counter()` |
| 计时内 | letterbox／画布构建、前向、ultralytics 内部 NMS、GPU→CPU、密度选窗、裁片、回映、合并、finalize；SAHI640 另含 BGR→RGB、sahi 切片与 GREEDYNMM |
| 计时外 | 磁盘读取与解码、窗口坐标列表、GT 匹配与评价、保存预测、写 CSV |
| Stage B（cal48） | 预热：第一张图 3×(F640 + F1280)；之后 48 图 × 3 次重复；方法顺序固定 F640→F1280→DensK1→UnifAll→SAHI640 |
| Stage D／E 与 Run G test-dev | 预热：第一张图 2×F640；之后每图每方法**只测一次**（one-shot） |
| SAHI 模型 | 独立加载同一权重，无单独预热；首次初始化开销计入第一张图（未单独量化） |

> **CUDA synchronize：** GPU 是异步执行的，CPU 发完命令就返回。不加同步，计时会只量到“发命令”的时间，而不是 GPU 真正算完的时间。

### 3.5 匹配器（matcher）：本项目怎么判对错，以及为什么不是 AP

匹配器是 `diagnose_bt1.prepare_gt + match_gt`（VisDrone 兼容口径；语义核对见 `P0_EI/00_freeze/provenance/A0-07_Evaluator_Semantics_Check.md`）。规则（导读 §2.6）：

1. **有效 GT：** 类别 1–10， $w,h>0$ ，且不落在 ignore 区域。VisDrone 类别 0（ignored regions）用来生成 ignore 掩码。
2. **预测：** 保留 $\text{conf}\ge 0.25$ ；落在 ignore 区域的预测直接剔除。
3. **匹配：** 按分数从高到低贪心匹配，类别必须一致， $\text{IoU}\ge 0.5$ 。没匹配上的预测记为 FP（误检）。
4. **计数方式：** 所有图像的 TP／FP 加总后再算比值（pooled，池化）。
5. **小目标：** GT 面积 $0<w\cdot h<1024$ 。匹配对所有尺寸一起做；small_tp 是被匹配上的小 GT 个数。

公式：

$$\text{precision}=\frac{TP}{TP+FP},\qquad \text{small recall}=\frac{TP_{s}}{GT_{s}},\qquad \text{recall\_all}=\frac{TP}{GT_{\text{valid}}}$$

其中 $TP_s$ 是被匹配上的小 GT 数， $GT_s$ 是小 GT 总数。recall_all 是导读派生的补充指标。

**为什么不是 AP：**

- **AP（Average Precision）** 是把置信度阈值从高到低扫一遍，画出“精度–召回曲线”，再求曲线下面积。COCO AP 还会在多个 IoU 阈值上平均。
- 本项目只在**一个工作点**（conf 0.25、IoU 0.5）上算 precision 和 recall，相当于曲线上的**一个点**，没有积分。
- 这样做的好处：它对应部署时真正会用的阈值，五个协议在同一个阈值下直接可比。
- 代价：数字**不能**和论文里常见的 AP 榜单比较。成稿必须写清楚这一点（导读 §2.6；`PR/Research_Plan.md` §3.3）。
- UAVDT：先按冻结映射把预测改成 3 类，再用同一匹配器；不用 ignore（`StageE_Channel_Decision.md`）。

### 3.6 统计方法

#### 3.6.1 为什么要“逐图配对”

两个协议跑的是**同一批图**。图和图之间难度差别很大（有的图 300 个小目标，有的 0 个）。逐图比较“同一张图上 A 比 B 好多少”，可以消掉图像难度这个噪声。统计单位是**图像**（Stage F；N = 1610，召回检验去掉无小 GT 的图后 N = 1499）。

#### 3.6.2 Wilcoxon 符号秩检验

- **问题：** 逐图差值 $d_i=A_i-B_i$ 的“中心”是不是 0？
- **做法：** 去掉 $d_i=0$ 的图，把 $|d_i|$ 排名次（并列取平均名次）。正差的名次和记 $W^+$ ，负差的记 $W^-$ 。若 A、B 无差别，二者应差不多大。
- **本项目实现：** 自写函数，统计量 $\min(W^+,W^-)$ ，用正态近似，含并列（tie）校正和 0.5 连续性校正，双侧检验，不调用 scipy（`Reproducibility_Appendix.md` §2.3）。
- **p 值：** 如果真实无差别，看到这么极端（或更极端）结果的概率。p 很小说明“无差别”不太可信。**p 不表示差别有多大**；N 很大时，很小的差别也会给出极小的 p。

#### 3.6.3 Bootstrap 置信区间

- **问题：** 池化指标（如总 small recall）之差有多不确定？
- **做法：** 从 N 张图中**有放回地**抽 N 张，组成一份“新测试集”，重新算差值 Δ。重复 $B=10000$ 次，取第 2.5 和第 97.5 百分位作为 **95% 置信区间（CI）**。
- **读法：** CI 不含 0 → 差值方向稳定；CI 跨 0 → 方向不确定。
- **本项目设置：** $B=10000$ ，seed 20260917，一个随机数发生器按固定的比较对顺序依次使用；百分位法（`Reproducibility_Appendix.md` §2.3）。

#### 3.6.4 Cluster（序列）bootstrap

UAVDT 的 40735 帧来自 50 段视频。同一段视频相邻帧几乎一样，**不是独立样本**。逐帧 bootstrap 会把“40735 个独立证据”算进去，严重低估不确定性。**Cluster bootstrap** 改为按**序列**整体有放回抽样（每次抽 50 个序列），抽中的序列的所有帧一起进入，再重算池化比值（Run H，`H_UAVDT_Paired_Stats_Report.md`）。Run K 的 UAVDT 密度分箱也用这一方法。

#### 3.6.5 Holm 多重比较校正

同时做多次检验，总有一些会“碰巧显著”。Holm 法：把 $m$ 个 p 值从小到大排序为 $p_{(1)}\le\dots\le p_{(m)}$ ，第 $i$ 个乘以 $(m-i+1)$ ，再保证单调不减：

$$p^{\text{Holm}}_{(i)}=\max_{j\le i}\ \min\bigl(1,\,(m-j+1)\,p_{(j)}\bigr)$$

本项目：主对 **F1280 vs DensK1** 报原始 p，不校正；5 个次要对做 Holm 校正（Stage F；Run H 同）。

#### 3.6.6 胜负计数、Wilson 区间与 McNemar

- **胜负计数：** 逐图数“A 更好／B 更好／打平”的张数，是描述性统计。
- **Wilson 区间：** 比例（如“A 更好的比例”）的 95% 置信区间，小样本或比例接近 0／1 时比简单的“正态近似”更可靠。
- **McNemar 检验：** 针对配对二分类结果（每张图 A 胜或 B 胜）的检验（Stage F 报告）。

### 3.7 硬件与环境

| 项 | GTX 1660 SUPER／**UAV_BT1**（冻结） | RTX 5060 Ti 16GB／**UAV_BT2**（现用） |
|---|---|---|
| 用于 | BT1 训练；Stage A–F 全部精度与时延（2026-09-12 至 09-18） | Run G 正式时序（2026-10-06）；Run H–K 的 CPU 再分析也在此环境 |
| GPU 细节 | 6144 MiB，驱动 591.86，功耗上限 125 W，UUID `GPU-43b14c17-…`（`P0_EI/00_freeze/gpu_snapshot.txt`） | 16311 MiB，驱动 591.86，sm_120，功耗上限 180 W，UUID `GPU-1d6d4cde-…`（`Timing_5060Ti_Table.md` §1） |
| CPU／电源计划 | 冻结件未记录 → **待补** | AMD Ryzen 5 5600G（6C／12T）；Windows“平衡”计划（同上） |
| Python | 3.12.14 | 3.10.22 |
| torch／CUDA／cuDNN | 2.7.1+cu126／12.6／90701 | 2.7.1+cu128／12.8／90701 |
| ultralytics | 8.4.90（pinned zip `ultralytics-07958a7.zip`） | 同一 zip、同一 sha256 |
| numpy | 2.5.2 | 2.2.6 |
| opencv／pillow | 5.0.0.93／12.3.0 | 5.0.0.93／12.3.0 |
| sahi | Stage A 时未装；Stage B–E 运行时版本**无法证明**；09-29 备份为 0.11.32 | 0.11.32 |
| scipy | Stage A 未装；09-29 备份 1.18.1（Stage F 不调用 scipy） | 1.15.3 |
| 环境位置 | `H:\Conda\envs\UAV_BT1`，**2026-10-04 换盘后 H: 分区不再挂载，环境已不存在**；可按 `.temp/conda-backup/` 中 2026-09-29 的导出重建（未入库） | `F:\Conda\envs\UAV_BT2`，2026-10-06 采用 |

来源：`P0_EI/05_packaging/Reproducibility_Appendix.md` §2.4；`P0_EI/00_freeze/Environment_Delta_UAV_BT2_vs_UAV_BT1.md`；`env_snapshot.txt`；`env_snapshot_UAV_BT2_20261006.txt`。

**环境变了，结果还算数吗？** 两个核对给出肯定回答：

- **精度：** Run G 在 5060 Ti／UAV_BT2 上重跑 test-dev，各方法 $\lvert\Delta\text{small recall}\rvert\le 0.014$ 个百分点，F1280 − DensK1 为 0.04089（1660：0.04087）（`Timing_5060Ti_Table.md` §5）。
- **统计：** Run H 在 UAV_BT2 下用冻结函数重算 Stage F，与 `F_summary.json` **逐位一致**（0 处不一致；`H_UAVDT_Paired_Stats_Report.md` §1）。

---

## 4. 故事线：Stage 0 与 A–K 按时间顺序

> [!example]- 图：P0_EI 时间线
> ![[p0fr_timeline.svg|720]]

（图源：`PR/assets/P0_EI_Full_Report_20261006/p0fr_timeline.svg`。仓库 Git 历史从 2026-09-27 的 commit `fd1f3c4` 开始可见，更早的事件依据 `PROJECT_CONTEXT.md`、各冻结件与 provenance 记录。）

### Stage 0（2026-09-10 至 09-16）：从“新机制”到“协议对比”

**目标：** 在 VisDrone 上训练一个普通基线，然后论证一个“局部高分辨率计算分配”的新机制。

**0-a 准备（09-10 至 09-12）**

- 09-10 转向主线 A，接受“VisDrone 优先、弱化铁路前提”；UAV-RSOD 退出关键路径（`PROJECT_CONTEXT.md` §2）。
- A0-05 VisDrone 文件审计（09-10 启动，09-11 完成）：官方 Google Drive 的 train／test-dev 返回 *Quota exceeded*，改用 Ultralytics 公开镜像；8629 张图全部可解码、标注对应（`A0-05_VisDrone_File_Audit.md`；`PROJECT_CONTEXT.md` §4）。
- A0-07 评价语义核对：Python 构造 24/24 与 Octave 原版有限交叉 24/24，差异 0（`PROJECT_CONTEXT.md` §4）。
- 09-12 批准受限普通基线。**云端受阻：**Kaggle 手机验证未完成，Colab 在安装前 Python 版本检查失败 → 改在本机 1660 SUPER 上训练（`PROJECT_CONTEXT.md` §2、“平台／数据准备阻塞”）。

**0-b BT1 训练（09-12 至 09-13）**

- `BT1-SMOKE-20260912-01`：4 张图 1 轮冒烟，148.75 s，PASS（权重不作基线）。
- 三段接续训练 100 轮，约 14.99 h，归档 PASS（§3.1；`BT1_100_Epoch_Archive.md`）。

**0-c BT 诊断阶段 BTD1–BTD12（09-13 至 09-14，另有书面审查）**

全部在 cal48（及 diag500）上做，属**开发证据**（`PROJECT_CONTEXT.md` §6 表）。

| Run | 做了什么 | 关键数字 | 结论 |
|---|---|---|---|
| BTD1-CAL48-20260913-01 | 全图漏检能否被局部窗口恢复 | 2720 个小 GT 中 558 个全图漏检可被局部恢复；弱响应候选恢复 336，P3-only 338，密度 429 | 弱响应 v0.1 转 HOLD |
| BTD2／BTD3 | 密度遗漏分析；去重密度 | BTD3：小 TP 1259 → 1282，区间跨 0 | 不能称稳定增益 |
| BTD4-DIAG500 | 在 diag500 上实测两规则 | 净 +273 小 TP；均值约 90 ms，相对 61 ms 参考超限约 90% | **预算失败** |
| BTD5-NMS | 公共 NMS 等价加速 | 合并约 27 ms → 6–7 ms | 工程加速，不算创新 |
| BTD6-PIPELINE | 新 NMS 后整帧复测 | 均值约 51.2 ms；40 ms 参考超限约 99% | 预算仍失败 |
| BTD7-RESIDUAL-01／02 | 残差与条件收益 | 01 因 NumPy int64 的 JSON 序列化失败中断，02 接续完成；GT 最佳第二片仅净 +26 | 不支持“第二片重排”作为创新 |
| **BTD8-SINGLE-20260914-01** | **密度单片 K1（即后来的 DensK1）** | cal48 小 TP 1172（GT 最佳单片 1223）；37.36／64.51 ms，40 ms 超限 20.83% | 尾部预算未通过 |
| **BTD9-F1280-20260914-01** | **复用 BTD8 预测比较整图 1280** | F1280 小 TP 1312，27.33／41.44 ms | **F1280 比单片更准且更快 → 区域机制 HOLD** |
| BTD10、BTD12 | 书面审查（无 Run ID） | — | 未形成新创新；BTD12 DISMISSED |
| BTD11-ERROR | 缓存错误分解 | 1408 个小 FN、839 个 FP 分解完成 | 低分空间不等于可部署收益 |

**转折点：** BTD9 发现，最朴素的“整图放大到 1280”超过了当时的 GT 最佳单片上界（1312 > 1223）。09-14 的“强简单基线与近邻审查”促使机制暂缓。**09-16 采用决定：P0 不再追求独立新机制，近程只写 EI 对比／协议稿（P0-EI-C1／C2）；P0-A-C1／C2 保持 HOLD；不创建 BTD13**（`PROJECT_CONTEXT.md` 开头与 §2）。

### Stage A（2026-09-17）：冻结

- **目标：** 跑任何对比之前，先锁定权重、数据清单、环境、五协议定义、评价门、计时边界和统计单位，防止事后调参。
- **Run ID：** `P0-BENCH-A-ENV-20260917-01` · **PASS**（`P0_EI/00_freeze/Environment_Freeze.md`）。
- **结果：** 权重 SHA 两份一致；cal48 48 行无重采样；git HEAD `604aeec`（冻结时）；GPU 是 1660 SUPER（当时计划的正式 4090 表“在本机被阻塞”，已披露）；**sahi 未安装**（SAHI640 当时被阻塞，后来安装）。
- **遗留：** `Environment_Freeze.md` 第 108 行写 “candidate grid yields 240 windows”，容易被误读为每图 240 窗；见 Stage J 的更正。

### Stage B（Run ID 日期 2026-09-17）：1660 流水线计时

- **目标：** 统一计时边界，测五协议端到端时延。只算**流水线验证**，不是正式时序表。
- **做法：** cal48 48 张 × 5 协议 × 3 次 = 每协议 144 条；检查每次输出与第 0 次一致（atol 1e-5）；保存第 0 次预测给 Stage C。
- **Run ID：** `P0-BENCH-B-TIMING-20260917-01` · **PASS**。
- **关键数字：** 均值 F640 18.62／F1280 33.15／DensK1 35.34／UnifAll 96.42／SAHI640 317.45 ms；三次输出全部一致（§5.4 表 B-1）。
- **决定：** 成稿只引用 Stage B（或 5060 Ti）的计时，BTD8 计时只作历史。

### Stage C（2026-09-17）：cal48 精度（开发证据）

- **目标：** 用 Stage B 第 0 次预测核对 DensK1 实现是否与 BTD8 一致。
- **Run ID：** `P0-BENCH-C-CAL48-20260917-01` · **PASS**。
- **结果：** DensK1 小 TP = **1172**，与 BTD8 锁定值一致；F1280 0.4824 > DensK1 0.4309（§5.5 表 C-1）。

### Stage D（2026-09-17）：VisDrone test-dev 一次性终评（主精度表）

- **目标：** 在完整 test-dev 上每个协议只预测一次，作为论文主精度表。
- **做法：** 先冻结配置和评测通道（本地镜像 GT + VisDrone 兼容匹配器），再预测；看分后不调参，意外结果原样保留。
- **Run ID：** `P0-BENCH-D-TESTDEV-20260917-01` · **PASS**，2026-09-17 14:33 完成，墙钟 1128.1 s（`D_TESTDEV_status.json`）。
- **结果：** small recall UnifAll 0.4511 > F1280 0.4004 > DensK1 0.3596 > F640 0.2388 > SAHI640 0.2184（§5.1）。

### Stage F（Run ID 日期 2026-09-17）：图级配对统计

- **目标：** 以图像为单位，检验差异是否稳定。
- **Run ID：** `P0-BENCH-F-TESTDEV-20260917-01` · **PASS**，墙钟 71.45 s。
- **结果：** 主对 Δsmall recall +0.0409 [0.0355, 0.0462]，p = 2.997e-28；**时延 p = 0.235**（不显著）。这一结果在 09-27 让 C1 从“更快”改为“不可区分”（§2.4、§5.3）。

### 插曲 1（2026-09-17）：UAVDT 下载波折

Stage E 需要 UAVDT。下面的过程记录都在 **仓库外** 的 `11_Datasets/raw/UAVDT/`（Git 忽略），2026-10-06 查看：

1. **15:28** 冻结 VisDrone→UAVDT 类别映射（`class_mapping_preregister.json`，仓库内）。
2. **15:30 作者 Google Drive：** 脚本 `_download_uavdt.py` 用 gdown 拉三个包（Benchmark-M、DET/MOT toolkit、Attributes）。第一次因 gdown 不认 `fuzzy` 参数失败（`download_manifest.json`）；重试后 Drive 返回 *“Too many users have viewed or downloaded this file recently”*（`download_console.log`、`curl_toolkit.log`）。
3. **15:31 Zenodo 第三方重传（备选）：** record 10.5281/zenodo.14575517，`UAVDT.zip` 4,026,830,525 bytes，MD5 `19f318b1…182b`（`zenodo_record_meta.json`）。curl 速度约 50 KB/s，预计约 22 小时，最终 `curl: (18) end of response with 3990250161 bytes missing`，只下到 36,580,364 bytes（`curl_zenodo.log`；`zenodo_UAVDT.zip` 文件大小）。
4. **15:38 改走百度网盘：** “User chose Baidu Yunpan path on 2026-09-17”。作者页提取码：Benchmark-M `uwn8`，DET/MOT toolkit `ilxx`，Attributes `t9d3`（可选）（`BAIDU_HANDOFF.md`）。同时写了选包指南：拒绝 Benchmark-S（单目标跟踪）、Kaggle 小子集、类别重映射不明的 YOLO 版本（`UAVDT_Package_Selection_Guide.md`）。
5. **16:50／17:09** 两个包落盘（MOTD 245,719,325 bytes；M 6,809,272,793 bytes；G 盘目录时间戳）。**Attributes 包没有下载**，这就是 Run K 无法做场景／高度／视角切片的原因。
6. 第三方 Kaggle UAVDT JSON 包被**拒绝作主库**（`Current_Stage.md` 实验门）；拒绝的具体日期 **待补**。

### 插曲 2（2026-09-17 至 09-18）：T4／Kaggle 重训轨（已撤回）

记录在 **仓库外** 的 `G:\Schloar Data\P0\dataset\P0_T4_Train\`：

- **09-17：** 用户选了 **B（真训练）**：在 Kaggle 免费 T4 上按 BT-1 固定配方从 COCO `yolo11n.pt` 重训 VisDrone，打算替换冻结权重后重测五协议（`logs/B1_recipe_lock_20260917.md`，19:15；`update_stage_b.py`，17:28）。
- **Kaggle Version #1 失败：** venv／ensurepip 错误，约 21.6 s，**没有产生任何新权重**（`revert_infer_20260918.py` 写入的 Current_Stage 文本）。
- **09-18：** 用户撤回授权，回到“冻结 `last.pt`、只做推理对比”。本地冻结权重复核：SHA 一致，`LastWriteTime` 2026-09-13 14:41:20（同上）。
- 仓库内的结论：`00_Overview/Current_Stage.md`：“T4／Kaggle 训练轨已于 2026-09-18 撤回，未产生任何新权重；本地冻结权重未被改写。”

### Stage E（2026-09-18）：UAVDT 跨集外推

- **目标：** 检验“协议改变召回–精度–代价”的粗趋势能否迁移到另一个航拍车辆基准。不是争 UAVDT SOTA。
- **做法：** 同一冻结 `last.pt`，不在 UAVDT 上微调；按冻结映射改写预测类别，用同一匹配器；不保存预测（`save_preds=false`）。
- **闸门：** 2026-09-18 `E_STATUS: READY`；冒烟 `P0-BENCH-E-UAVDT-20260918-01`，24 张图，约 58 s，PASS（`StageE_Channel_Decision.md`）。
- **Run ID：** `P0-BENCH-E-UAVDT-20260918-FULL` · **PASS**，墙钟 17149.2 s（约 4.76 h；`E_FULL_status.json`）。冻结 JSON 里的 `run_id` 是冒烟值，以 FULL 为准（`Run_Index.md` 注）。
- **结果：** 排序变成 F1280 0.7929 > UnifAll 0.7824 > DensK1 0.7672 > SAHI640 0.7597 > F640 0.7080（§5.2）。这成为 C2“没有通用排序”的依据。

### 整理期（2026-09-20 至 09-29）

- **09-20 周报：** “4090 的测时协议和 Run 号写好了，机器上还没跑”；计划“1660 和 4090 准备分两张表”（`99_Attachments/周报记录/2026/9月/余传灏-2026.09.20周报.md`）。登记的 Run ID 是 `P0-BENCH-G-4090-*-20260920-01`，**从未运行**（`Run_Index.md`）。
- **09-27：** 仓库大整理（commit `fd1f3c4` 导读、`b8871f9` 文档一致性、`64ab335` 基于结果的主张）：
  - 运行脚本在目录重构 `efba65e` 时被删，从 `bad0f8b` 恢复，SHA 与冻结登记一致（`Reproducibility_Appendix.md` §10）；
  - C1 改为“时延统计不可区分下更准”；
  - 旧 BTD 叙述退出主张；
  - 旧练手目录删除，冻结件来源记录移入 `00_freeze/provenance/`。
- **09-28／29：** 学位分备忘入库（commit `4369f59`）。

### Stage G（2026-10-01 改计划，10-06 运行）：RTX 5060 Ti 正式时序

- **10-01：** 本机 GPU 换为 RTX 5060 Ti 16GB；正式时序 Run G 由 4090 改为 5060 Ti（commit `e761abd`，“planned timing GPU 4090 -> RTX 5060 Ti 16GB (Run G, not run)”）。为什么 4090 没有落实，仓库内**没有书面记录（待补）**。
- **10-04：** 换盘后 **H: 分区不再挂载**，冻结环境 UAV_BT1 不复存在（`Environment_Delta_UAV_BT2_vs_UAV_BT1.md`）。图 1–5 也是在这个环境里生成的（`FIGURES.md`）。
- **10-06 16:15：** 采用新环境 UAV_BT2，写环境快照与差异表（commit `e4f6375`）。
- **10-06 16:23–16:53：** Run G 四个闸门（`Timing_5060Ti_Table.md` §1–2；commit `7049a8d`）：

| Run ID | 内容 | 结果 |
|---|---|---|
| `P0-BENCH-G-5060TI-SMOKE-20261001-01` | 2 张 cal48 + 3 张 test-dev，只验链路 | PASS（不进表） |
| `P0-BENCH-G-5060TI-CAL48-20261001-01` | 冻结 Stage B 脚本，48 × 5 × 3 | PASS；240 个（图, 方法）对中 22 对差 1–2 个框 |
| `P0-BENCH-G-5060TI-TESTDEV-20261001-01` | 冻结 Stage D 脚本，1610 × 5 | PASS；墙钟 1406 s； $\lvert\Delta\text{small recall}\rvert\le 0.014$ 个百分点 |
| `P0-BENCH-G-5060TI-PAIRED-20261006-01` | 冻结 Stage F 统计函数，配对时延 | PASS；F1280 比 DensK1 快，逐图中位差 −13.32 ms |

- Run ID 日期说明：前三个保留原计划日期 20261001（已登记文档一致，不改名）；PAIRED 是新增的，按登记日 20261006（`Run_Index.md`）。
- **10-06 17:42：** 按用户决定把 C1 时延改为分 GPU 表述（commit `bb617f0`；`dcf1ad4` 同步 Innovation_Ledger 与缩写表）。

### Stage H（2026-10-06）：UAVDT 配对统计

- **目标：** 补上 Stage E 缺的配对统计，并处理视频帧自相关。
- **Run ID：** `P0-BENCH-H-UAVDT-PAIRED-20261006-01` · **PASS**（commit `c3a4990`）。CPU-only，无推理。
- **做法：** 用 importlib 原样调用冻结 Stage F 函数，输入 `E_FULL_per_image_metrics.csv`；另加 50 序列 cluster bootstrap 和序列级 Wilcoxon（M0801 无小 GT，排除，n = 49）。
- **附带核对：** UAV_BT2 下重算 Stage F，**逐位一致**；向量化 bootstrap 与冻结版逐位一致（2.3 s vs 66.6 s）。
- **关键发现：** 帧级 p 严重高估显著性（主对帧级 p = 3.6e-293）。按序列聚类后主对仍成立：Δsmall recall +0.0257，序列 CI [0.0100, 0.0403]（§5.6）。

### Stage I（2026-10-06）：像素–时延归一化

- **目标：** 把“多处理像素”的效应和“协议本身”的效应分开。
- **Run ID：** `P0-BENCH-I-PIXLAT-20261006-01` · **PASS**（commit `d9db2db`）。CPU-only，只数像素。
- **关键发现：** VisDrone 上 UnifAll 与 SAHI640 都是 7.11 次前向、内容像素都是 2.742 Mpx，small recall 却是 0.451 vs 0.218；**时延主要由前向次数决定**（§5.8）。

### Stage J（2026-10-06）：复现附录补缺 + 失败例裁图

- **Run ID：** `P0-BENCH-J-REPRO-20261006-01` · **PASS**（commit `8f79fda`）。CPU-only。
- **做了什么：**
  - 从代码读出 SAHI 实际设置，发现 **GREEDYNMM／IOS** 误称；
  - 写清 DensK1 精确网格、每视图 conf、计时边界与预热、版本表、bootstrap 设置；
  - 用 Run G 已存预测画了 6 张失败例裁图。
- **“240 窗”更正：** BTD8 与 `Environment_Freeze.md` 中的“240 windows”是 cal48 **48 张图的窗口总数**（33 张 6 窗 + 13 张 2 窗 + 2 张 8 窗 = 240；导读 §2.5 派生自 `B_TIMING_timings.csv`），**不是每图窗数**。每图窗数是 2／6／8（`Reproducibility_Appendix.md` §2 表与 §2.1）。

### Stage K（2026-10-06）：密度属性切片

- **Run ID：** `P0-BENCH-K-DENSITY-20261006-01` · **PASS**（commit `3b1a77f`）。CPU-only。
- **做法：** 按每图 valid_gt 和 small_gt 的五分位分箱（**五分位**：把数值从小到大分成人数大致相等的 5 组）；VisDrone 用图像 bootstrap，UAVDT 用序列 cluster bootstrap；1660 与 5060 Ti 时延分列。
- **关键发现：** VisDrone 每个箱 UnifAll 最佳、F1280 − DensK1 都显著为正；UAVDT 最稀疏箱 F1280 与 DensK1 打平，valid_gt ≥ 10 起 F1280 最佳；**DensK1 从未在任何箱最佳**（§5.9）。
- **没做的：** UAVDT 场景／高度／视角切片（属性文件不在盘上）；目标尺度切片（按用户指示不做）。

---

## 5. 全部结果表

> 时延列一律注明 GPU 与环境。Stage B–F 与 Stage H／K 中 UAVDT 的时延来自 **GTX 1660 SUPER／UAV_BT1**；Run G 来自 **RTX 5060 Ti／UAV_BT2**。

### 5.1 VisDrone test-dev 五协议（Stage D；时延 = 1660 SUPER／UAV_BT1 单次运行）

来源：`P0_EI/01_visdrone_main/data/D_TESTDEV_summary.json`（`P0-BENCH-D-TESTDEV-20260917-01`）；median 来自 `P0_EI/02_paired_stats/data/F_summary.json` → `method_aggregates`；recall_all、n_dets 为导读派生。n = 1610，conf 0.25，IoU 0.5，小目标 < 1024 px²。

| 协议 | TP | FP | Precision | small TP | **small recall** | recall_all | n_dets | mean ms（1660） | median ms（1660） |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| F640 | 28346 | 13911 | 0.6708 | 12042 | 0.2388 | 0.3794 | 43011 | 17.40 | 17.02 |
| F1280 | 37767 | 18160 | **0.6753** | 20194 | 0.4004 | 0.5055 | 58047 | 33.72 | 33.08 |
| DensK1 | 35662 | 23075 | 0.6071 | 18133 | 0.3596 | 0.4774 | 60685 | 34.06 | 32.73 |
| UnifAll | 41705 | 39695 | 0.5123 | 22751 | **0.4511** | 0.5582 | 84691 | 112.21 | 110.23 |
| SAHI640 | 26086 | 46632 | 0.3587 | 11016 | 0.2184 | 0.3492 | 75415 | 373.23 | 375.69 |

> [!example]- 图 1：VisDrone 五协议精度、召回与 1660 时延
> ![[fig1_visdrone_metrics.png|680]]

（`P0_EI/05_packaging/figures/fig1_visdrone_metrics.png`，数据 `D_TESTDEV_summary.json`）

### 5.2 UAVDT 五协议（Stage E；时延 = 1660 SUPER／UAV_BT1 单次运行）

来源：`P0_EI/03_cross_uavdt/data/E_FULL_summary.json`（`P0-BENCH-E-UAVDT-20260918-FULL`）；median、recall_all 为导读派生。n = 40735，车辆 3 类，冻结映射。

| 协议 | TP | FP | Precision | small TP | **small recall** | recall_all | mean ms（1660） | median ms（1660） |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| F640 | 623956 | 826262 | **0.4302** | 349664 | 0.7080 | 0.7811 | **16.74** | 16.14 |
| F1280 | 671489 | 1134085 | 0.3719 | 391579 | **0.7929** | 0.8406 | 33.08 | 31.46 |
| DensK1 | 658280 | 1236148 | 0.3475 | 378871 | 0.7672 | 0.8241 | 32.97 | 32.04 |
| UnifAll | 668237 | 1346758 | 0.3316 | 386393 | 0.7824 | 0.8366 | 47.18 | 44.36 |
| SAHI640 | 648364 | 1188553 | 0.3530 | 375203 | 0.7597 | 0.8117 | 164.00 | 163.67 |

跨集对照（`StageE_UAVDT_Report.md` §4）：

| 模式 | VisDrone（D） | UAVDT（E） | 判读 |
|---|---|---|---|
| F640 小召回最弱（整图／密度／切片几类中） | 是（SAHI 更低） | 是 | 一致 |
| 提分辨率／切片 → 小召回高于 F640 | 是 | 是 | 一致 |
| 召回升，精度常降 | 是 | 是 | 权衡叙事一致 |
| 第一名 | UnifAll | F1280 | **不稳定** |
| SAHI 位置 | 垫底 | 中游 | 对数据集敏感 |

> [!example]- 图 2：UAVDT 五协议；图 3：两集小召回并排（禁止合并平均）
> ![[fig2_uavdt_metrics.png|680]]
> ![[fig3_dual_set_small_recall.png|560]]

### 5.3 Stage F 配对统计（VisDrone test-dev；时延 = 1660 SUPER／UAV_BT1）

来源：`P0_EI/02_paired_stats/data/F_summary.json`、`F_wilcoxon_recall_small.csv`、`F_bootstrap_deltas.csv`（`P0-BENCH-F-TESTDEV-20260917-01`）。

**表 F-1 主对 F1280 vs DensK1**

| 指标 | 值 |
|---|---|
| 有小 GT 的图 N | 1499（非零差 1089） |
| 逐图 Δrecall_small 中位数／均值 | 0.0000／+0.0345 |
| Wilcoxon（双侧，原始 p） | 统计量 182331.5，z = −11.02，**p = 2.997e-28** |
| 池化 small recall | 0.4004 vs 0.3596，**Δ = +0.0409**，95% CI **[0.0355, 0.0462]** |
| Δprecision | +0.0681 [0.0631, 0.0731] |
| Δmean ms（1660） | −0.34 [−0.66, −0.01] |
| 时延逐图 Wilcoxon（1660） | **p = 0.235**；逐图中位差 +0.25 ms |
| 胜负（按 recall_small） | F1280 更好 720／DensK1 更好 369／平 410；Wilson p(F1280 更好) = 0.480 [0.455, 0.506]；McNemar p = 2.79e-26 |

**表 F-2 bootstrap Δ（A − B），95% CI；Holm 校正后的 Wilcoxon p**

| 比较 | Δsmall recall | Δprecision | Δmean ms（1660） | Wilcoxon p（Holm） |
|---|---|---|---|---|
| F1280 vs DensK1（主） | +0.0409 [0.0355, 0.0462] | +0.0681 [0.0631, 0.0731] | −0.3 [−0.7, −0.0] | 2.997e-28（原始） |
| F640 vs F1280 | −0.1616 [−0.1675, −0.1559] | −0.0045 [−0.0110, 0.0018] | −16.3 [−16.6, −16.1] | 2.398e-171 |
| F1280 vs UnifAll | −0.0507 [−0.0551, −0.0464] | +0.1629 [0.1583, 0.1677] | −78.5 [−79.5, −77.5] | 2.927e-86 |
| F1280 vs SAHI640 | +0.1820 [0.1735, 0.1908] | +0.3166 [0.3090, 0.3239] | −339.5 [−343.4, −335.6] | 2.030e-182 |
| DensK1 vs UnifAll | −0.0916 [−0.0966, −0.0866] | +0.0948 [0.0906, 0.0993] | −78.1 [−79.1, −77.2] | 2.585e-160 |
| DensK1 vs SAHI640 | +0.1411 [0.1311, 0.1512] | +0.2484 [0.2411, 0.2555] | −339.2 [−343.1, −335.3] | 3.180e-155 |

**表 F-3 逐图胜负计数（描述性）**

| 比较 | A 更好 | B 更好 | 平 | Wilson p(A 更好) |
|---|---:|---:|---:|---|
| F1280 vs DensK1 | 720 | 369 | 410 | 0.480 [0.455, 0.506] |
| F640 vs F1280 | 53 | 1161 | 285 | 0.035 [0.027, 0.046] |
| F1280 vs UnifAll | 193 | 899 | 407 | 0.129 [0.113, 0.147] |
| F1280 vs SAHI640 | 1201 | 81 | 217 | 0.801 [0.780, 0.821] |
| DensK1 vs UnifAll | 21 | 1008 | 470 | 0.014 [0.009, 0.021] |
| DensK1 vs SAHI640 | 1122 | 144 | 233 | 0.748 [0.726, 0.770] |

> [!example]- 图 5：Stage F 配对 Δsmall recall 与 95% CI
> ![[fig5_stageF_deltas.png|640]]

近邻单轴对照（`P0_EI/05_packaging/Neighbor_Protocol_Table.md`；D 与 E 分开，禁止混合平均；时延均为 1660）：

| 轴（前 → 后） | VisDrone：Δsr／Δprec／Δms | UAVDT：Δsr／Δprec／Δms |
|---|---|---|
| 分辨率：F640 → F1280 | +0.1616／+0.0045／+16.3 | +0.0849／−0.0584／+16.3 |
| 选区→全覆盖：DensK1 → UnifAll | +0.0916／−0.0948／+78.1 | +0.0152／−0.0159／+14.2 |
| 工程切片→整图高分：SAHI640 → F1280 | +0.1820／+0.3166／−339.5 | +0.0332／+0.0189／−130.9 |
| 同为切片族：SAHI640 → UnifAll | +0.2327／+0.1536／−261.0 | +0.0227／−0.0213／−116.8 |

### 5.4 时延表：1660 SUPER 与 5060 Ti 分表

**表 B-1 GTX 1660 SUPER／UAV_BT1，cal48，n = 144／协议**（`P0_EI/04_timing/data/B_TIMING_summary.json`，`P0-BENCH-B-TIMING-20260917-01`）

| 协议 | mean | median | std | p90 | p95 | p99 | 每图中位数均值 | 每图中位数 p95 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| F640 | 18.62 | 18.23 | 2.45 | 21.95 | 23.09 | 24.97 | 18.44 | 21.24 |
| F1280 | 33.15 | 32.88 | 3.74 | 37.53 | 38.73 | 42.31 | 32.78 | 36.79 |
| DensK1 | 35.34 | 34.63 | 4.47 | 40.16 | 43.20 | 49.69 | 34.82 | 39.46 |
| UnifAll | 96.42 | 105.79 | 31.54 | 127.49 | 134.92 | 156.46 | 95.14 | 126.08 |
| SAHI640 | 317.45 | 363.90 | 118.78 | 447.05 | 493.61 | 538.25 | 308.68 | 407.82 |

DensK1 时间构成（1660，cal48，144 次平均；导读派生自 `B_TIMING_timings.csv`）：整图 17.60 + 选区与局部检测 16.12 + 合并／NMS 1.61 = 35.34 ms。

> **p90／p95／p99：** 90%／95%／99% 的样本时延不超过这个值，反映“慢的时候有多慢”（尾部时延）。  
> **超预算率** `budget_violation_rate[T]`：每图 3 次中位数 > T ms 的图像比例。T = 40 ms 只是相对参考，不是业务硬期限（导读 §2.6）。

**表 B-2 1660 超预算率（cal48）**

| 协议 | T=20 | T=25 | T=30 | T=40 | T=50 | T=75 | T=100 |
|---|---:|---:|---:|---:|---:|---:|---:|
| F640 | 0.125 | 0.021 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| F1280 | 1.000 | 1.000 | 0.792 | 0.000 | 0.000 | 0.000 | 0.000 |
| DensK1 | 1.000 | 1.000 | 0.958 | 0.021 | 0.000 | 0.000 | 0.000 |
| UnifAll | 1.000 | 1.000 | 1.000 | 1.000 | 0.896 | 0.729 | 0.729 |
| SAHI640 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.979 |

> [!example]- 图 4：1660 SUPER 时延（Stage B）
> ![[fig4_timing_1660.png|600]]

**表 G-1 RTX 5060 Ti／UAV_BT2，cal48，n = 144／协议**（`P0_EI/04_timing/data/G_CAL48_summary.json`，`P0-BENCH-G-5060TI-CAL48-20261001-01`）

| 协议 | mean | median | p90 | p95 | p99 | std |
|---|---:|---:|---:|---:|---:|---:|
| F640 | 19.91 | 19.11 | 22.65 | 24.82 | 30.30 | 2.72 |
| F1280 | 27.43 | 26.57 | 30.55 | 33.43 | 45.67 | 4.20 |
| DensK1 | 40.12 | 39.22 | 44.74 | 47.10 | 53.06 | 4.17 |
| UnifAll | 114.48 | 126.95 | 148.14 | 158.63 | 185.21 | 36.93 |
| SAHI640 | 427.50 | 466.90 | 618.29 | 642.03 | 724.33 | 160.53 |

**表 G-3 RTX 5060 Ti／UAV_BT2，test-dev 1610 图，one-shot**（`G_TESTDEV_per_image_metrics.csv`、`G_TIMING_stats.json`，`P0-BENCH-G-5060TI-TESTDEV-20261001-01`）

| 协议 | mean | median | p90 | p95 | p99 | std | 相对 F640 |
|---|---:|---:|---:|---:|---:|---:|---:|
| F640 | 19.85 | 18.68 | 24.01 | 26.68 | 32.51 | 3.18 | 1.00× |
| F1280 | 26.25 | 25.03 | 31.15 | 34.49 | 40.61 | 3.77 | 1.32× |
| DensK1 | 40.26 | 38.35 | 47.31 | 51.75 | 58.61 | 5.24 | 2.03× |
| UnifAll | 136.59 | 131.44 | 166.04 | 175.83 | 194.64 | 23.03 | 6.88× |
| SAHI640 | 507.10 | 498.16 | 646.22 | 691.71 | 787.28 | 110.25 | 25.55× |

运行中 GPU 监测（2 s 采样）：cal48 利用率均值 10.7%（最大 55%），test-dev 均值 11.4%（最大 75%）；峰值显存 209082368 bytes（约 199.4 MiB）（`Timing_5060Ti_Table.md` §1、§3）。

> [!example]- 图 4b：RTX 5060 Ti 时延（Run G，单列）
> ![[fig4b_timing_5060ti.png|600]]

### 5.5 cal48 精度（Stage C，开发证据，非主表）

来源：`P0_EI/01_visdrone_main/data/C_cal48_summary.json`（`P0-BENCH-C-CAL48-20260917-01`），n = 48，小 GT 2720。

| 协议 | TP | FP | Precision | small TP | small recall |
|---|---:|---:|---:|---:|---:|
| F640 | 1492 | 576 | 0.7215 | 840 | 0.3088 |
| F1280 | 2010 | 839 | 0.7055 | 1312 | 0.4824 |
| DensK1 | 1857 | 1051 | 0.6386 | 1172 | 0.4309 |
| UnifAll | 2110 | 1572 | 0.5731 | 1367 | 0.5026 |
| SAHI640 | 1345 | 1928 | 0.4109 | 749 | 0.2754 |

### 5.6 配对时延：F1280 vs DensK1，两块 GPU 并排（每列标明 GPU 与环境）

来源：`Timing_5060Ti_Table.md` §4（表 G-5）、§6。

| 主对 F1280 vs DensK1（test-dev，图级） | **GTX 1660 SUPER／UAV_BT1**（`P0-BENCH-F-TESTDEV-20260917-01`） | **RTX 5060 Ti／UAV_BT2**（`P0-BENCH-G-5060TI-PAIRED-20261006-01`） |
|---|---:|---:|
| 逐图中位差 (ms) | +0.25 | −13.32 |
| 均值差 (ms) | −0.34 | −14.01 |
| 均值差 95% CI | [−0.66, −0.01] | [−14.22, −13.80] |
| Wilcoxon p | 0.235 | 3.6e-264 |
| F1280 更快的图像比例 | 47.3% | 99.8%（1607／1610） |

Run G 其他配对（5060 Ti／UAV_BT2，N = 1610，均值差 [95% CI]）：F640 vs F1280 −6.40 [−6.57, −6.23]；F1280 vs UnifAll −110.34 [−111.44, −109.28]；F1280 vs SAHI640 −480.85 [−486.16, −475.42]；DensK1 vs UnifAll −96.33 [−97.38, −95.27]；DensK1 vs SAHI640 −466.84 [−472.22, −461.52]（表 G-5）。p 值在 N = 1610、几乎全部同号时已到正态近似的极端尾部，只说明“方向一致且极显著”，不要当精确值引用。

**观察（只描述，未做归因实验）：** 换到 5060 Ti 后只有 F1280 变快（cal48 33.15 → 27.43 ms），其余四个协议均值反而更高。GPU 平均利用率只有约 11%，提示这条流水线主要受**主机端开销**限制（Python／Ultralytics 预处理与后处理、CPU 端 NMS、SAHI 合并），而不是 GPU 算力。单次 640 前向（含前后处理）约 19 ms，1280 前向约 27 ms，所以“一次 1280”比“两次 640 + 合并”便宜（`Timing_5060Ti_Table.md` §6）。

### 5.7 UAVDT 配对统计与逐序列结果（Run H；时延 = 1660 SUPER／UAV_BT1）

来源：`P0_EI/03_cross_uavdt/H_UAVDT_Paired_Stats_Report.md`、`data/H_UAVDT_PAIRED_summary.json`、`H_UAVDT_PAIRED_table.csv`（`P0-BENCH-H-UAVDT-PAIRED-20261006-01`）。

| 对 A vs B | Δsmall recall | 帧级 95% CI | **序列 95% CI** | 序列 Wilcoxon p（Holm） | 序列 A优／B优／平 | Δprecision（序列 CI） | Δmean ms 1660（序列 CI） |
|---|---:|---|---|---|---|---|---|
| **F1280 vs DensK1**（主） | **+0.0257** | [0.0245, 0.0269] | **[0.0100, 0.0403]** | 9.9e-4（不校正） | 37／12／0 | +0.0244 [0.0168, 0.0326] | +0.11 [−0.50, 0.70] |
| F640 vs F1280 | −0.0849 | [−0.0872, −0.0825] | [−0.1203, −0.0468] | 1.4e-6（5.6e-6） | 7／41／1 | +0.0584 [0.0479, 0.0692] | −16.34 [−16.97, −15.70] |
| F1280 vs UnifAll | +0.0105 | [0.0096, 0.0114] | [0.0012, 0.0180] | **0.322（0.322）** | 30／18／1 | +0.0403 [0.0327, 0.0503] | −14.10 [−14.99, −13.20] |
| F1280 vs SAHI640 | +0.0332 | [0.0311, 0.0352] | [0.0039, 0.0732] | 4.0e-4（1.2e-3） | 36／13／0 | +0.0189 [0.0044, 0.0368] | −130.92 [−137.56, −123.98] |
| DensK1 vs UnifAll | −0.0152 | [−0.0158, −0.0146] | [−0.0236, −0.0072] | 4.9e-8（2.4e-7） | 4／40／5 | +0.0159 [0.0106, 0.0221] | −14.21 [−14.70, −13.69] |
| DensK1 vs SAHI640 | +0.0074 | [0.0055, 0.0095] | **[−0.0303, 0.0553]** | 0.017（0.033） | 33／15／1 | −0.0055 [−0.0174, 0.0089] | −131.03 [−137.87, −123.91] |

- 主对帧级时延 Wilcoxon p = 0.096（1660 上不可区分）；帧级召回 p = 3.6e-293，因自相关而**不可作推断依据**。
- **F1280 vs UnifAll 依赖序列：** 池化 Δ 为正，但序列级不显著；每序列差的均值 −0.0002、中位数 +0.004，池化增益主要来自少数 GT 量大的序列。
- **DensK1 vs SAHI640 未确立：** 序列 CI 跨 0，而序列 Wilcoxon（Holm 0.033）偏向 DensK1，两口径不一致，按保守读法记为“未确立差异”。
- 逐序列明细：`H_UAVDT_PAIRED_table.csv`；50 个序列逐一列出的序列表本报告不重复。

### 5.8 像素–时延归一化（Run I）

来源：`P0_EI/04_timing/Pixel_Latency_Table.md`、`data/I_PIXLAT_summary.json`、`I_PIXLAT_table.csv`（`P0-BENCH-I-PIXLAT-20261006-01`）。

- **输入 Mpx：** 每图送进网络的像素总数（百万像素），含 letterbox 填充。
- **内容 Mpx：** 只计图像内容。
- **边际 Δrecall／增加 Mpx：** 相对 F640，每多处理 1 Mpx 能换来多少 small recall：
  $$\frac{R_s(\text{协议})-R_s(\text{F640})}{\text{Mpx}(\text{协议})-\text{Mpx}(\text{F640})}$$

**VisDrone test-dev（n = 1610；精度来自 Stage D）**

| 协议 | 前向次数／图 | 输入 Mpx | 内容 Mpx | 局部缩放 | small recall | 边际 Δrecall／Mpx | ms／输入 Mpx：1660／UAV_BT1 | ms／输入 Mpx：5060 Ti／UAV_BT2 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| F640 | 1.00 | 0.410 | 0.243 | 0.451 | 0.2388 | — | 42.5 | 48.5 |
| F1280 | 1.00 | 1.638 | 0.974 | 0.901 | 0.4004 | 0.132 | 20.6 | 16.0 |
| DensK1 | 2.00 | 0.819 | 0.651 | 1.000 | 0.3596 | **0.295** | 41.6 | 49.1 |
| UnifAll | 7.11 | 2.912 | 2.742 | 1.000 | 0.4511 | 0.085 | 38.5 | 46.9 |
| SAHI640 | 7.11 | 2.755 | 2.742 | 1.000 | 0.2184 | −0.009 | 135.5 | 184.0 |

**UAVDT（n = 40735；只有 1660 时延）**

| 协议 | 前向次数／图 | 输入 Mpx | 内容 Mpx | 局部缩放 | small recall | 边际 Δrecall／Mpx | ms／输入 Mpx：1660／UAV_BT1 |
|---|---:|---:|---:|---:|---:|---:|---:|
| F640 | 1.00 | 0.410 | 0.217 | 0.627 | 0.7080 | — | 40.9 |
| F1280 | 1.00 | 1.638 | 0.867 | 1.254 | 0.7929 | 0.069 | 20.2 |
| DensK1 | 2.00 | 0.819 | 0.563 | 1.000 | 0.7672 | **0.144** | 40.2 |
| UnifAll | 3.00 | 1.229 | 0.908 | 1.000 | 0.7824 | 0.091 | 38.4 |
| SAHI640 | 3.00 | 0.923 | 0.908 | 1.000 | 0.7597 | 0.101 | 177.8 |

三条结论（`Pixel_Latency_Table.md` §4）：

1. **同样的像素，协议不同，结果差很远：** UnifAll 与 SAHI640 内容像素相同，VisDrone small recall 0.451 vs 0.218。
2. **像素效率 DensK1 最高**，但绝对 recall 不如 F1280／UnifAll。
3. **时延由前向次数决定，不由像素数决定：** 单次前向的 F1280 每 Mpx 最便宜；多次前向的 DensK1／UnifAll 约 38–49 ms／Mpx（两块 GPU 都如此）。

### 5.9 密度切片（Run K）

来源：`P0_EI/06_density_slices/K_Density_Slices_Report.md`、`data/K_DENSITY_summary.json`、`K_DENSITY_slices.csv`、`K_DENSITY_pairs.csv`（`P0-BENCH-K-DENSITY-20261006-01`）。

**VisDrone，按 valid_gt 分箱（Δms 两列分别标明 GPU）**

| 箱 | 图数 | F1280 sr | DensK1 sr | UnifAll sr | F1280−DensK1 Δsr [95% CI] | Δms 1660／UAV_BT1 | Δms 5060 Ti／UAV_BT2 |
|---|---:|---:|---:|---:|---|---:|---:|
| [1,18] | 352 | 0.515 | 0.480 | 0.563 | +0.0347 [+0.0130, +0.0570] | −1.20 | −13.60 |
| [19,29] | 296 | 0.436 | 0.414 | 0.496 | +0.0218 [+0.0074, +0.0364] | −0.72 | −13.99 |
| [30,43] | 330 | 0.485 | 0.448 | 0.543 | +0.0365 [+0.0249, +0.0484] | −0.29 | −14.15 |
| [44,63] | 313 | 0.424 | 0.386 | 0.480 | +0.0381 [+0.0272, +0.0490] | −0.21 | −14.14 |
| [64,446] | 319 | 0.357 | 0.311 | 0.403 | +0.0460 [+0.0380, +0.0539] | +0.78 | −14.21 |

（Δms = F1280 − DensK1 均值差；负值表示 F1280 在该 GPU 上更快。）按 small_gt 分箱时，F1280 − DensK1 在五个非零箱依次为 +0.030／+0.037／+0.027／+0.043／+0.045，CI 都不含 0；1660 上最密箱 Δms +0.95（K 报告 §2）。

**UAVDT，按 valid_gt 分箱（序列 cluster CI；时延仅 1660）**

| 箱 | 帧数 | 序列数 | F1280 sr | DensK1 sr | UnifAll sr | 最佳 | F1280−DensK1 Δsr [95% CI] |
|---|---:|---:|---:|---:|---:|---|---|
| [1,9] | 9522 | 25 | 0.797 | 0.798 | **0.812** | UnifAll | −0.0009 [−0.0270, +0.0271] |
| [10,13] | 8062 | 31 | **0.851** | 0.833 | 0.846 | F1280 | +0.0183 [+0.0014, +0.0402] |
| [14,18] | 7216 | 32 | **0.893** | 0.875 | 0.880 | F1280 | +0.0181 [+0.0096, +0.0280] |
| [19,27] | 8013 | 27 | **0.914** | 0.889 | 0.899 | F1280 | +0.0258 [+0.0092, +0.0480] |
| [28,107] | 7596 | 19 | **0.727** | 0.695 | 0.714 | F1280 | +0.0318 [+0.0032, +0.0511] |

（valid_gt = 0 的 326 帧来自 2 个序列，无有效 GT，不比较。）

要点：VisDrone 10 个非零箱里 UnifAll 全部最佳；UAVDT 排序随密度翻转；**DensK1 从未在任何箱最佳**；最密箱所有协议都明显变差，密度本身是主要难度来源（K 报告 §5）。

### 5.10 失败与边界例

**按规则检索的四类边界例**（`P0_EI/05_packaging/Failure_Boundary_Cases.md`；Stage D 冻结 CSV）：

| 例 | 协议 | 代表图像 | 现象 | 不外推的边界句 |
|---|---|---|---|---|
| (a) 小目标漏检 | F640 ↔ F1280 | `9999996_00000_d_0000028.jpg` | small_gt = 14：F640 small_tp 3 → F1280 12 | 不能推出“F640 没有部署价值”（它最快） |
| (b) 误检抬升 | UnifAll／SAHI640 vs F1280 | `9999938_00000_d_0000207.jpg` | FP：UnifAll 209，SAHI 203，F1280 121 | 不能推出“切片一定更差” |
| (c) 接缝／重复框风险 | SAHI640 vs F1280 | `0000310_03500_d_0000125.jpg` | SAHI n_dets 104 vs F1280 17，prec ≈ 0.08 | 必须披露 overlap 与合并参数；不能写成“SAHI 族普遍失败” |
| (d) 映射空洞 | Stage E | 映射规则本身 | 行人／非机动车类在 UAVDT DET 无对应 | 合法的跨集边界；禁止看分后改映射 |

**六张失败例裁图**（Run J；来源为 Run G 已存预测，RTX 5060 Ti／UAV_BT2；逐图 small_tp 已与 `G_TESTDEV_per_image_metrics.csv` 断言一致；绿 = 匹配到的小 GT，红 = 漏检，黄框 = DensK1 所选窗口）。来源：`P0_EI/05_packaging/failure_crops/cases.json`、`Reproducibility_Appendix.md` §2.5。

| 例 | 图像 | 对比 | small TP／small GT | 观察 |
|---|---|---|---|---|
| 1 | 9999938_00000_d_0000210（1400×788） | F1280 vs DensK1 | 88 vs 47／325 | 小目标分散在多个区域，单窗只覆盖其一 |
| 2 | 9999938_00000_d_0000212（1400×788） | F1280 vs DensK1 | 108 vs 69／294 | 同上 |
| 3 | 0000073_03155_d_0000004（1920×1080） | F1280 vs DensK1 | 23 vs 38／59 | 大图上 F1280 缩放 0.667，所选窗口以原生分辨率覆盖密集人群 |
| 4 | 0000073_01275_d_0000002（1920×1080） | F1280 vs DensK1 | 35 vs 45／69 | 同上 |
| 5 | 9999938_00000_d_0000121（1400×788） | UnifAll vs SAHI640 | 62 vs 10／176 | 像素相同；SAHI640 大量漏检（机制未验证；候选原因：GREEDYNMM／IOS、每片 iou 0.7／max_det 300） |
| 6 | 9999938_00000_d_0000247（1400×788） | F1280 vs UnifAll | 4 vs 7／115 | small GT ≥ 50 的图中三协议最好召回最低的一张 |

> [!example]- 裁图 1／3：F1280 赢（分散目标）与 DensK1 赢（大图密集人群）
> ![[case1_F1280_wins_9999938_00000_d_0000210.jpg|640]]
> ![[case3_DensK1_wins_0000073_03155_d_0000004.jpg|640]]

> [!example]- 裁图 5／6：同像素下 SAHI640 漏检；三协议都几乎全漏
> ![[case5_SAHI640_loses_same_pixels_9999938_00000_d_0000121.jpg|640]]
> ![[case6_all_miss_9999938_00000_d_0000247.jpg|640]]

其余两张：`case2_F1280_wins_9999938_00000_d_0000212.jpg`、`case4_DensK1_wins_0000073_01275_d_0000002.jpg`（同目录）。

---

## 6. 结果解读与“怎么选协议”

### 6.1 主线结论（大白话）

1. **分辨率是第一杠杆。** 从 F640 到 F1280，VisDrone small recall +0.1616，精度差 CI [−0.0110, 0.0018] 跨 0，基本不损失精度（表 F-2）。UAVDT 上 +0.0849，但精度降 0.0584（近邻表）。
2. **“只挑一块看”（DensK1）不如“整图放大”（F1280）。** 两个数据集、序列层面、几乎所有密度箱都如此（§5.3、§5.7、§5.9）。原因可以从失败例 1–2 直观看到：小目标分散时，一块 640 窗只覆盖其中一处。DensK1 只在大图（1920×1080，F1280 缩放仅 0.667）上的密集局部赢（例 3–4）。
3. **“全看一遍”（UnifAll）召回最高，但要付代价。** VisDrone 上比 F1280 高 0.0507，精度低 0.1629，1660 上时延约 3.3×（§5.3）。UAVDT 上这一优势变弱且依赖序列（§5.7）。
4. **按默认设置用 SAHI，在本设置下三项都输给 F1280。** 与 UnifAll 处理同样的像素，召回却差 0.23（VisDrone），说明问题出在**协议细节**（合并方式、每片推理参数），不是像素不够（§5.8）。
5. **时延结论随机器变。** 在本项目的 YOLO11n 规模上，每次前向的固定开销（预处理、调用、同步、CPU 端合并）占主导，所以“一次大前向”通常比“多次小前向”便宜。1660 上 F1280 与 DensK1 打平；5060 Ti 上 F1280 每图快约 14 ms（§5.6）。
6. **跨数据集排序不稳。** VisDrone 第一是 UnifAll，UAVDT 第一是 F1280。一个可能的解释是**局部缩放**：F1280 在 VisDrone 上缩放约 0.90（略低于原生），在 UAVDT 上约 1.25（放大），窗口类协议恒为 1.0。这只是假设，未做因果检验；验证需要按目标尺度切片（`Pixel_Latency_Table.md` §4）。

### 6.2 怎么选协议（基于本项目证据的操作指南）

下面的建议只适用于“单一冻结 YOLO11n + 本项目匹配器 + 本项目两块 GPU”的条件。

| 你的约束 | 建议 | 依据 |
|---|---|---|
| 时延受限、只能做一次前向 | **F1280**（单次前向 + 更大输入），而不是多次 640 前向 | §5.6、§5.8：前向次数决定时延 |
| 要最高 small recall，能承受精度下降与 3–7 倍时延 | **UnifAll** | VisDrone 各密度箱、UAVDT 最稀疏帧（§5.9） |
| 显存或像素预算受限 | DensK1 的单位像素回报最高（VisDrone 0.295／Mpx），但绝对召回不如 F1280 | §5.8 |
| 图像很大（如 1920×1080）、目标集中在一处 | DensK1 可能赢（例 3–4），但没有任何密度箱整体占优 | §5.9、§5.10 |
| 打算直接用 SAHI 默认设置 | 本设置下不推荐；若要用，先核对合并方式（GREEDYNMM／IOS）与每片 `iou`／`max_det`，并在自己的数据上重新评测（本项目未调参） | §3.4.5、§5.8 |
| 数据是视频 | 用**序列／场景**作统计单位，帧级显著性不能作为选协议依据 | §5.7 |
| 要在新 GPU 上部署 | **在目标硬件上重新测**时延，不要搬用本表的“谁快” | §5.6 |
| 目标比训练时更小（如 UAVDT 1024 宽的帧） | 适度上采样（F1280 在 UAVDT 上缩放 1.25）有益 | §5.2、§5.8 |

---

## 7. 局限与效度威胁

**内部效度（结论在本设置内是否可靠）**

1. **单一权重、单一 seed。** 只有 YOLO11n seed 0。结论不能外推到其他检测器、规模或训练种子（`PR/Research_Plan.md` §3.3）。
2. **SAHI640 的每片参数与其他协议不同**（iou 0.7／max_det 300 vs 0.5／1000），且合并为 GREEDYNMM。它代表“默认用法”，不代表 SAHI 调好后的上限（`Reproducibility_Appendix.md` §2.1）。
3. **DensK1 的定义来自 BTD8，而 BTD8 是在 cal48 上开发的。** cal48 也用于训练监控，所以 Stage C 只是开发证据。Stage D test-dev 是一次性终评，可以抵消大部分这种风险。
4. **1660 上 Stage D／E 的时延是单次测量。** Stage B 有 3 次重复，但只覆盖 48 张图。
5. **时延没有分解。** 5060 Ti 上 GPU 平均利用率约 11%，时延主要受主机端开销支配；CPU 是 Ryzen 5 5600G，电源计划为“平衡”。1660 运行时的 CPU／电源计划未记录（待补）。前向、NMS、Python 开销各占多少，**没有测量**。
6. **环境漂移。** UAV_BT1 已随 H: 盘丢失。Stage B–E 当时的 sahi 版本无法证明。UAV_BT2 的 numpy、Python、CUDA 都与冻结环境不同。缓解：Run G 精度差 ≤ 0.014 个百分点；Run H 逐位复现 Stage F。
7. **5060 Ti 与 1660 的时延不能互比。** GPU、torch／CUDA、numpy 都不同（`Timing_5060Ti_Table.md` §6）。

**构念效度（指标是否量到想量的东西）**

8. **匹配器指标不是 AP。** 单一 conf 0.25、IoU 0.5 的工作点，不能与 AP 榜单比较。
9. **“小目标”是面积 < 1024 px² 的单一切点。** 按更细的目标尺度切片（如 < 8²、8²–16²、16²–32²）没有做。
10. **超预算率的 T 只是相对参考**，不是任何真实系统的硬期限。

**外部效度（能否推广）**

11. **两个数据集都是航拍，但只有两个。** UAVDT 只评车辆 3 类；行人／非机动车类被映射排除（边界例 d）。UAVDT 不用 ignore 文件。
12. **VisDrone test-dev 来自 Ultralytics 镜像**，与作者原包的逐字节身份 Unknown；不能声称官方排名。train 与 test-dev 之间有 34 对近重复候选和共享场景线索，来源组 Unknown（`PROJECT_CONTEXT.md` §4）。
13. **UAVDT 帧高度自相关。** 帧级 p 值不可用；推断以序列聚类为准（Run H）。
14. **UAVDT 没有场景／高度／视角切片**（属性包没下载），也没有 5060 Ti 时延（可选，未跑）。

**统计结论效度**

15. **N 很大时 p 值极小**（如 3.6e-264），只说明方向一致，不说明差别大。应看效应量和 CI。
16. **密度分箱的切点是事后按五分位定的**，属描述性分析；各箱的多个比较未做多重比较校正（K 报告未提及校正）。
17. **DensK1 vs SAHI640（UAVDT）两种口径不一致**，记为“未确立”（Run H）。

**记录与可追溯性**

18. 仓库 Git 历史从 2026-09-27 开始可见；09-27 前的过程依据 provenance 文件和 `PROJECT_CONTEXT.md`。UAVDT 下载与 T4 轨的过程记录在**仓库外**（`11_Datasets/raw/UAVDT/`、`G:\Schloar Data\P0\dataset\P0_T4_Train\`）。
19. 冻结 JSON 中有已知不一致（Stage E 的 `run_id` 是冒烟值；UAVDT 路径是旧路径；“240 windows”易误读；`protocol.json` 的 `hardware_role` 仍写 4090），都已在附录或 `Run_Index.md` 注明，冻结件不改。

---

## 8. 复现指引

### 8.1 文件地图

| 想找什么 | 去哪里 |
|---|---|
| 当前唯一事项 | `00_Overview/Current_Stage.md` |
| 主张全文与证据 | `PR/Research_Plan.md` §3 |
| 查数手册（导读） | `PR/P0_EI_Paper_Overview_and_Experiments.md` |
| Run 索引（A–K） | `P0_EI/Run_Index.md` |
| 冻结件 | `P0_EI/00_freeze/`：`Environment_Freeze.md`、`weight_sha_reverify.txt`、`DensK1_Definition.md`、`class_mapping_preregister.json`、`Class_Mapping_Preregister.md`、`stage_d_config_freeze.json`、`stage_e_config_freeze.json`、`env_snapshot*.txt`、`pip_freeze*.txt`、`gpu_snapshot.txt`、`script_sha256.txt`、`Environment_Delta_UAV_BT2_vs_UAV_BT1.md` |
| 冻结件来源记录 | `P0_EI/00_freeze/provenance/`：BT1 100 轮归档、A0-05 VisDrone 审计、A0-07 评价语义、标签转换核对、BTD8 协议与结果 |
| VisDrone 主精度（C／D） | `P0_EI/01_visdrone_main/`（报告 + `data/C_*`、`data/D_*`） |
| 配对统计（F） | `P0_EI/02_paired_stats/`（报告 + `data/F_*`；Run H 复现 `data/H_FREPRO_*`） |
| UAVDT（E／H） | `P0_EI/03_cross_uavdt/`（`StageE_UAVDT_Report.md`、`H_UAVDT_Paired_Stats_Report.md` + `data/E_*`、`data/H_*`） |
| 时延（B／G／I） | `P0_EI/04_timing/`（`StageB_Timing_Report.md`、`Timing_5060Ti_Table.md`、`Pixel_Latency_Table.md` + `data/B_*`、`data/G_*`、`data/I_*`） |
| 包装（近邻表、失败例、复现附录、图、裁图） | `P0_EI/05_packaging/` |
| 密度切片（K） | `P0_EI/06_density_slices/` |
| 本报告的示意图 | `PR/assets/P0_EI_Full_Report_20261006/`（SVG + 生成脚本） |

### 8.2 脚本

| 脚本 | 作用 | 状态 |
|---|---|---|
| `PR/Experiments/diagnose_bt1.py` | 匹配器（`prepare_gt`／`match_gt`）、`nms`、`axis_windows` | 冻结，勿改 |
| `BENCH/stage_b/run_stage_b_timing.py` | 五协议实现 + Stage B 计时 | 冻结（git blob `5ae22d60`） |
| `BENCH/stage_d/run_stage_d_oneshot.py` | Stage D test-dev 一次性终评 | 冻结（`6bf296a0`；SHA 与 `stage_d_config_freeze.json` 一致） |
| `BENCH/stage_e/run_stage_e_oneshot.py` | Stage E UAVDT | 冻结（数据路径为旧路径） |
| `BENCH/stage_f/run_stage_f_paired_stats.py` | Stage F 统计函数 | 冻结 |
| `BENCH/stage_g/run_stage_g.py` 等 | Run G 参数化入口（只传 `--run-id`／`--max-images`／`--skip-extract`）、精度一致性、配对时延、汇总 | 新增 |
| `BENCH/stage_h/run_h_paired_stats.py` | Run H（importlib 调冻结 Stage F） | 新增 |
| `BENCH/stage_i/run_i_pixlat.py` | Run I 像素几何 | 新增 |
| `BENCH/stage_j/run_j_failure_crops.py` | Run J 裁图 | 新增 |
| `BENCH/stage_k/run_k_density.py` | Run K 分箱 | 新增 |
| `P0_EI/05_packaging/figures/generate_plots.py`、`generate_fig4b_timing_5060ti.py` | 由 summary JSON 再生图 | 改图先改证据，不硬编码 |

冻结脚本的 SHA 与恢复记录见 `Reproducibility_Appendix.md` §10。新环境用 `F:\Conda\envs\UAV_BT2\python.exe`。

### 8.3 不在仓库里的东西

- 权重、原始数据、预测 `.npy`、运行目录：`11_Datasets/` 与 `BENCH/stage_*/<Run ID>/`（Git 忽略）。
- Run G 的 test-dev 预测：`BENCH/stage_d/P0-BENCH-G-5060TI-TESTDEV-20261001-01/preds/`（1610 × 5 = 8050 个 `.npy`；Run J 与可选的目标尺度切片都依赖它）。
- Stage D（1660）与 Stage E 的预测**没有保存**。
- UAVDT 数据：`G:\Schloar Data\P0\dataset\UAVDT\`。

---

## 9. 距离投稿还差什么

| # | 事项 | 必需／可选 | 现状 | 说明 |
|---|---|---|---|---|
| 1 | **稿件正文** | **必需** | 未开始（`Current_Stage.md` 进度表）；`PR/` 下没有 `.tex`／`.pdf`／`.docx` | 按 `PR/Writing/P0_EI_Outline.md` 六节：Introduction／Related Work／Protocols & Evaluation／Results／Failure & Boundaries／Conclusion；主张只用 C1／C2 终稿措辞 |
| 2 | **选定出口（会议或期刊）与截稿日，并写入 Current_Stage** | **必需** | 已定（2026-10-06）：首投 IJCNN 2027（截稿 2027-01-31）；落选转投 ICIP 2027（截稿 2027-03-31）；已写入 `Current_Stage.md` | 出口决定篇幅（IJCNN ≤6 页；ICIP 2026 版为 5+1 页，装不下全部结果）和第二篇的引用安排 |
| 3 | **题目统一** | **必需** | 现有中文题强调“时间预算约束”；导读建议的英文工作题未登记，待你确认 | 摘要写 experimental evaluation |
| 4 | **文献** | **必需** | `PR/Literature/Literature_Matrix.md` 9 篇都是 SCREENED；MUST 篇 PDF 待放入各主题 `pdfs/`；ClusDet 等需补 DOI | Related Work 只归“推理时增强／切片评测” |
| 5 | 正文时延表的选择与披露 | **必需** | 两张表都已就绪（1660 Stage B／D；5060 Ti Run G） | 分表呈现，C1 时延按 GPU 分写 |
| 6 | 把 Run H–K 纳入正文或附录 | 建议（可选） | 已 PASS，有报告 | H 可放进 UAVDT 结果；I／K 适合放讨论或补充材料 |
| 7 | **目标尺度切片** | 可选 | 未做（按用户指示） | VisDrone 可用 Run G 已存预测 CPU 完成，无需推理；UAVDT 需重新推理 40735 帧 × 5 协议（Stage E 在 1660 上墙钟 17149 s），并用参数化副本修正数据路径、登记新 Run ID（K 报告 §6） |
| 8 | **时延分解** | 可选 | 未做 | 需要新的计时运行（属推理），须另行授权并登记 Run ID；可回答“主机端开销占多少” |
| 9 | UAVDT 在 5060 Ti 上的时延 | 可选 | 未跑 | `Run_Index.md`“UAVDT 时序可选” |
| 10 | UAVDT 场景／高度／视角切片 | 可选 | 属性文件不在盘上 | 需要另外获取 Attributes 包（百度提取码 `t9d3`，`BAIDU_HANDOFF.md`，仓库外）；序列级，CPU 即可 |
| 11 | 超预算率曲线图 | 可选 | 未画 | 从 `B_TIMING_summary.json`／Run G 已有数据画，1660 与 5060 Ti 各一张，不叠加 |
| 12 | 用 UAV_BT2 重生成图 1–5 | 可选 | 图 1–5 由已丢失的 UAV_BT1 生成 | matplotlib 版本不同，样式可能细微变化，数值不变（`FIGURES.md`） |
| 13 | 第二篇启动条件：五协议逐图 oracle 上界 | 第二篇事项，非本篇必需 | 未算 | 用已有逐图 CSV 即可（`P0_Two_Paper_Plan_2026-09-22.md`）；须另行授权 |

---

## 10. 术语表与 Run ID 表

### 10.1 术语表

| 术语 | 解释 |
|---|---|
| P0／P0_EI | 练手论文的代号；EI 指目标是 EI 会议 |
| C1／C2 | 本文两条主张（§2） |
| P0-A-C1／C2 | 旧区域机制的两条候选主张，HOLD |
| 冻结（frozen） | 权重、配置、映射在出分前锁定，之后不改 |
| SHA256 | 文件内容指纹，用来证明用的是同一个文件 |
| YOLO11n | Ultralytics 的 YOLO 第 11 版 nano（最小）模型 |
| BT1 | 本项目的普通 YOLO11n 基线训练（100 轮） |
| BTD1–BTD12 | BT1 之后的诊断系列（09-13 至 09-14），开发证据 |
| VisDrone test-dev | VisDrone2019-DET 的公开测试划分，1610 张，本项目一次性终评 |
| cal48 | 从 VisDrone val 固定取的 48 张开发图 |
| diag500 | VisDrone val 其余 500 张，BTD4／6 用过 |
| UAVDT | 无人机车辆检测与跟踪基准；本项目用 DET 部分 50 序列 40735 帧 |
| 类别映射 | VisDrone 10 类 → UAVDT 3 类（car／truck／bus），分前冻结 |
| 推理协议 | 同一模型“怎么喂图、怎么拼结果”的规则 |
| F640 | 整图 letterbox 到 640×640，前向 1 次 |
| F1280 | 整图 letterbox 到 1280×1280，前向 1 次 |
| DensK1 | F640 + 粗检框中心最多的 1 个 640 窗（K = 1），前向 2 次 |
| UnifAll | F640 + 网格全部 640 窗（步长 512），覆盖上界 |
| SAHI／SAHI640 | 开源切片推理库；本项目按默认设置、640 切片、重叠 0.25 使用 |
| letterbox | 等比缩放后用灰边填成目标尺寸 |
| 窗口／切片（window／slice） | 从原图裁出的局部块 |
| 局部缩放 | 最高分辨率那一路相对原图的缩放系数（1.0 = 原生像素） |
| 前向（forward pass） | 模型对一张输入跑一次 |
| finalize | 五协议共同的终处理：conf ≥ 0.25 → 类内 NMS 0.5 → 最多 500 框 |
| conf | 置信度分数 |
| NMS | 非极大值抑制，删除重叠的重复框 |
| GREEDYNMM | 贪心合并重叠框（sahi 默认），合并而非删除 |
| IoU | 交并比 |
| IOS | 交集 ÷ 较小框面积 |
| max_det | 每次推理最多保留的框数 |
| 匹配器（matcher） | 本项目判定 TP／FP 的程序（`diagnose_bt1.prepare_gt + match_gt`） |
| TP／FP／FN | 正确检出／误检／漏检 |
| 有效 GT（valid_gt） | 计入评价的真值框 |
| ignore 区域 | VisDrone 标注的“不评价”区域 |
| 小目标（small） | 面积 $0<w\cdot h<1024$ px² |
| small recall | $TP_s/GT_s$ |
| precision | $TP/(TP+FP)$ |
| recall_all | $TP/GT_{\text{valid}}$ （派生补充指标） |
| AP | PR 曲线下面积，本项目**不报** |
| 池化（pooled） | 先把所有图的计数加总再算比值 |
| 端到端时延 | 已解码图像 → 最终框的时间 |
| p90／p95／p99 | 时延分位数（尾部） |
| 超预算率 | 时延超过参考 T 的图像比例 |
| one-shot | 每图每方法只跑一次 |
| 预热（warm-up） | 正式计时前先跑几次，排除初始化开销 |
| 配对（paired） | 两协议在同一张图上比较 |
| Wilcoxon 符号秩检验 | 检验配对差值中心是否为 0 的非参数检验 |
| bootstrap | 有放回重抽样估计不确定性 |
| 95% CI | 95% 置信区间 |
| cluster（序列）bootstrap | 按序列整体重抽样，处理视频帧自相关 |
| Holm 校正 | 多重比较时调整 p 值的方法 |
| Wilson 区间 | 比例的置信区间 |
| McNemar 检验 | 配对二分类结果的检验 |
| 自相关 | 相邻样本高度相似，不是独立证据 |
| 支配（dominated） | 每项指标都不如另一方 |
| 边际 Δrecall／Mpx | 每多处理 1 百万像素换来的 small recall |
| 五分位分箱 | 按数值大小分成数量大致相等的 5 组 |
| UAV_BT1／UAV_BT2 | 冻结环境（已丢失）／现用环境 |
| GTX 1660 SUPER／RTX 5060 Ti | 两块 GPU；时延分表 |
| JCR／CCF | 期刊分区（Q1–Q4）／中国计算机学会推荐目录 |
| HOLD／IDLE／PREP／PAUSED／ACTIVE | 暂缓／空闲／预备／暂停／唯一执行中 |
| 待补 | 仓库中找不到依据的项 |

### 10.2 Run ID 表

| Run ID | 内容 | 日期（Run ID 名义／实际） | 状态 |
|---|---|---|---|
| `BT1-SMOKE-20260912-01` | BT1 冒烟（4 图 1 轮） | 09-12 | PASS（不作基线） |
| `BT1-LOCAL-20260912-01`／`-02`／`BT1-LOCAL-20260913-01` | BT1 训练 1–3／4／5–100 轮 | 09-12 至 09-13 | PASS |
| `BTD1-…` 至 `BTD11-…` | 诊断系列（见 §4 Stage 0） | 09-13 至 09-14 | 开发证据 |
| `P0-BENCH-A-ENV-20260917-01` | Stage A 冻结 | 09-17 | PASS |
| `P0-BENCH-B-TIMING-20260917-01` | Stage B 1660 计时（cal48） | 09-17 | PASS |
| `P0-BENCH-C-CAL48-20260917-01` | Stage C cal48 精度 | 09-17 | PASS |
| `P0-BENCH-D-TESTDEV-20260917-01` | Stage D test-dev 一次性终评 | 09-17（14:33 完成） | PASS |
| `P0-BENCH-F-TESTDEV-20260917-01` | Stage F 图级配对统计 | 09-17 | PASS |
| `P0-BENCH-E-UAVDT-20260918-01` | Stage E 冒烟（24 图） | 09-18 | PASS |
| `P0-BENCH-E-UAVDT-20260918-FULL` | Stage E UAVDT 全量 | 09-18 | PASS |
| `P0-BENCH-G-4090-*-20260920-01` | 原计划 4090 时序 | 09-20 登记 | **从未运行**，被 Run G 取代 |
| `P0-BENCH-G-5060TI-SMOKE-20261001-01` | 5060 Ti 冒烟 | 名义 10-01／实际 10-06 | PASS（不进表） |
| `P0-BENCH-G-5060TI-CAL48-20261001-01` | 5060 Ti cal48 计时 | 名义 10-01／实际 10-06 | PASS |
| `P0-BENCH-G-5060TI-TESTDEV-20261001-01` | 5060 Ti test-dev 计时 | 名义 10-01／实际 10-06 | PASS |
| `P0-BENCH-G-5060TI-PAIRED-20261006-01` | 5060 Ti 配对时延 | 10-06 | PASS |
| `P0-BENCH-H-UAVDT-PAIRED-20261006-01` | UAVDT 配对 + 序列 cluster | 10-06 | PASS |
| `P0-BENCH-I-PIXLAT-20261006-01` | 像素–时延归一化 | 10-06 | PASS |
| `P0-BENCH-J-REPRO-20261006-01` | 复现附录补缺 + 失败例裁图 | 10-06 | PASS |
| `P0-BENCH-K-DENSITY-20261006-01` | 密度属性切片 | 10-06 | PASS |

---

*本报告的示意图源文件与生成脚本：`PR/assets/P0_EI_Full_Report_20261006/`。修改任何数字前，先改对应证据文件或报告，再同步本报告与导读。*
