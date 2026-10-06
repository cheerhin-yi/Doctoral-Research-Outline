# P0_EI Research Story（科研叙事主文档）

> [!info] 分工与规则（先读）
> - **助手预填事实：** §0、§3 的修订记录、§4、§5、§7、§9 由助手（Grok Bot）于 2026-10-06 预填。每条都写了来源路径或 Run ID；仓库里查不到的值写 **待补**。
> - **你写理解：** §1、§2、§3（假设正文）、§6、§8（§8.1 只给了句式）、§10 留空，由你用自己的话写。每节下有一行灰色提示，只指出证据在哪里，不给答案。
> - **之后的审阅：** 你写完后，助手只用批注审阅（例如在段后加 `%% 审阅：… %%` 或单独的批注块），**不改你的原文**。
> - **路径简写：** `PR/` = `00_Practice_UAV_Aerial_Detection/`；`P0_EI/` = `PR/Experiments/papers/P0_EI/`；`BENCH/` = `PR/Experiments/P0_Benchmark/`。“Full Report”= `PR/P0_EI_Full_Report_20261006.md`。
> - **模板来源：** `99_Attachments/事件/Doctoral-Research-Outline_科研叙事与论文草稿模板.md`。按约定改了三处：§3 改为回顾性假设并加修订记录；§5 改为 Run 链接表；§8.1 改为实证对比句式，§8.5 改名为“Evaluation Design / 评测设计”。
> - **GPU 纪律：** GTX 1660 SUPER（UAV_BT1）与 RTX 5060 Ti（UAV_BT2）的时延不合表、不合列；“更快”必须带 GPU 名称。

> 用途：每篇论文从 IDEA 开始长期维护的科研主文档。
>
> 核心原则：**先记录问题 → 提出假设 → 设计证据 → 执行实验 → 解释结果 →
> 冻结科学叙事 → 再写正式论文。**
>
> 适用范围：博士论文、SCI/EI论文、会议论文、实验性研究和方法论文。
>
> 重要规则： 1. 实验前记录假设，不允许看到结果后任意修改假设。 2.
> 原始结果只记录事实，不在结果表里"包装"结论。 3.
> 每个主要结论必须能够追溯到具体实验、数据或文献。 4.
> 明确区分"观察到的现象""合理解释""已经被证据证明的结论"。 5.
> 正式论文写作前必须完成 Research Story Freeze。 6.
> 不因为预设期刊分区而反向制造实验结论。 7.
> 所有数字、统计量、硬件、数据集、模型版本必须可追溯。

------------------------------------------------------------------------

# 0. Project Metadata

-   Paper ID：P0_EI（`00_Overview/Current_Stage.md`，唯一 ACTIVE 事项）
-   暂定题目：**待补**。现有中文工作题为“面向无人机航拍的时间预算约束小目标检测（成稿拟改为‘推理协议对比／experimental evaluation’口径）”（`PR/Research_Plan.md` §1）；英文工作题未登记（Full Report §9 第 3 项）。
-   项目：练手论文 P0，在 Paper 1 之前单独做，不计入七篇主论文（Full Report §1.1，引 `PROJECT_CONTEXT.md` §2）
-   研究方向：冻结检测器上的推理协议对比，无人机航拍小目标（`PR/Research_Plan.md` 标题与 §1）
-   论文类型：`实证`（`PR/Research_Plan.md` §1：“不是新检测器、不是新模块；摘要写 experimental evaluation，不写 we propose”）
-   当前阶段：Stage A–F、Run G、Run H–K 全部 PASS；稿件正文未开始（`00_Overview/Current_Stage.md`“进度”表）
-   目标期刊/会议：**IJCNN 2027**（IEEE，常规论文 ≤6 页双栏；2027-06-14～18）；落选后转投 **ICIP 2027**（5+1 页，截稿 2027-03-31）（`PR/Writing/Venue_Survey_20261006.md` §7.4 短名单与推荐、[C19]／[C20]；2026-10-06 用户决定，commit `02cab84`）。注：`Current_Stage.md` 与 `Research_Plan.md` 仍写“主跟踪 ICIP 2027”，尚未同步。
-   目标投稿时间：2027-01-31（IJCNN 2027 常规论文截稿；通知 2027-03-15；终稿 2027-04-12）（`Venue_Survey_20261006.md` [C20]）。是否双盲、截止时区 **待补**（同文件 §7.5）。
-   负责人：余传灏（`99_Attachments/周报记录/2026/9月/余传灏-2026.09.20周报.md` 文件名）
-   Git commit：写入本文件时仓库 HEAD 为 `02cab84`（2026-10-06，venue survey s7）；本文件自身的提交见 `git log -- PR/Writing/P0_EI_Research_Story.md`。冻结时 HEAD `604aeec`（Stage A，Full Report §4）。
-   数据版本：
    -   VisDrone2019-DET test-dev：Ultralytics assets 镜像 `VisDrone2019-DET-test-dev.zip`，SHA256 `b28a94b06dfd9e36ce77ff8155fb82b9d2c030f198a76105933bd56c6ea6a68d`，1610 张（`P0_EI/01_visdrone_main/data/D_TESTDEV_summary.json`）；与作者原包的逐字节身份 Unknown（`P0_EI/01_visdrone_main/StageD_Channel_Decision.md`）
    -   cal48（开发集，非测试集）：清单 SHA256 `b0e27b1dc10d952a927597022a1fe0cfa52714d45a89e4c3f36880c2a4a68e7f`（`P0_EI/00_freeze/Environment_Freeze.md`）
    -   UAVDT DET：作者版 UAV-benchmark-M + UAV-benchmark-MOTD_v1.0，50 序列／40735 帧（`P0_EI/03_cross_uavdt/StageE_UAVDT_Report.md` §1）
    -   VisDrone→UAVDT 类别映射：`FROZEN_PRE_RESULTS`，登记 `2026-09-17T15:28:36`（`P0_EI/00_freeze/class_mapping_preregister.json`）
-   权重版本：BT1 YOLO11n 第 100 轮 EMA `last.pt`（Run `BT1-LOCAL-20260913-01`），SHA256 `bc42d54e37acaf1f698af487439dc222fa86fb4498623e8cf954df14e0aa5533`，5457882 bytes（`P0_EI/00_freeze/weight_sha_reverify.txt`；`P0_EI/00_freeze/provenance/BT1_100_Epoch_Archive.md`）
-   最后更新时间：2026-10-06（Asia/Shanghai）

------------------------------------------------------------------------

# 1. Research Problem｜研究问题卡片

<span style="color:gray">提示：证据在 `PR/Research_Plan.md` §1（研究问题与边界）、Full Report §1–§2、`PR/Writing/P0_Two_Paper_Plan_2026-09-22.md`；问题边界可对照 Full Report §2.5（刻意不主张的内容）。</span>

## 1.1 研究领域

> 我研究的是：

## 1.2 实际应用场景

> 场景是什么？谁使用？受到什么约束？

## 1.3 当前问题

-   问题1：
-   问题2：
-   问题3：

## 1.4 我真正想解决的问题

> 用一句话描述，避免"提高精度"这种过于宽泛的表述。

## 1.5 为什么值得研究？

### 科学价值

### 工程价值

### 实际应用价值

## 1.6 问题边界

明确本论文**研究什么、不研究什么**：

-   研究：
-   不研究：
-   暂不研究：

## 1.7 初步研究问题 RQ

### RQ1

### RQ2

### RQ3

------------------------------------------------------------------------

# 2. Existing Work & Research Gap｜已有研究与缺口

<span style="color:gray">提示：文献在 `PR/Literature/`：`Literature_Matrix.md`（§5 为 2026-10-06 新增 22 篇与“建议优先读”）、各主题 `Reading_List.md` 的事实表、`P0_C1C2.md`（已下全文的可用／不可用句子）；近邻协议数字对照见 `P0_EI/05_packaging/Neighbor_Protocol_Table.md`。</span>

## 2.1 现有方法分类

### 方法A

-   核心思想：
-   优点：
-   局限：
-   代表工作：

### 方法B

-   核心思想：
-   优点：
-   局限：
-   代表工作：

### 方法C

-   核心思想：
-   优点：
-   局限：
-   代表工作：

## 2.2 现有研究解决了什么？

## 2.3 现有研究没有解决什么？

## 2.4 Research Gap

## 2.5 Closest Prior Work

> 当前与本文最接近的工作：

-   Paper：
-   年份：
-   核心方法：
-   数据集：
-   检测器/模型：
-   主要结果：
-   与本文最相似之处：
-   本文必须解决的差异：

## 2.6 Novelty Boundary

> 本文真正可能的新颖性是什么？

> 哪些内容**不能**声称为创新？

------------------------------------------------------------------------

# 3. Research Hypotheses｜回顾性假设（实验已完成后补写，保留修改记录）

> 原则：实验前填写。结果出来后只能根据新证据修正，并保留修改记录。
>
> **本篇说明：** P0 的实验（Stage A–K）已经完成，本节是**回顾性补写**。请写清楚哪些是当时（实验前）的预期、哪些是事后补写；不要按结果倒推假设。

## 3.0 修订记录（Revision History）

下表只记录 C1 措辞变化的**事实**（助手预填，来源见各行）；“修改理由”一列留给你写。

| 版本 | 日期 | C1 措辞 | 触发证据（数字照抄来源） | 来源 | 修改理由（用户填） |
|---|---|---|---|---|---|
| v1 | 2026-09-14 | “F1280 比实际单片**更准且更快**” | BTD9（cal48，48 张开发图）：F1280 1312 个小 TP，27.33／41.44 ms（均值／p95）；DensK1 1172 个，37.36／64.51 ms | `PROJECT_CONTEXT.md` §6 表（经 Full Report §2.4） |  |
| v2 | 2026-09-27 | “**时延统计不可区分下**更准”（indistinguishable on 1660） | Stage F（test-dev 1610 张，GTX 1660 SUPER）：时延逐图 Wilcoxon p = 0.235，均值差 −0.34 ms，中位差 +0.25 ms | `PR/Research_Plan.md` §3.4；`P0_EI/02_paired_stats/data/F_summary.json`；`P0-BENCH-F-TESTDEV-20260917-01` |  |
| v3 | 2026-10-06 | **分 GPU：** GTX 1660 SUPER（UAV_BT1）上统计上不可区分；RTX 5060 Ti（UAV_BT2）上 F1280 更快 | Run G 配对检验：均值差 −14.01 ms，95% CI [−14.22, −13.80]，p≈3.6e-264，1607／1610 张更快 | `PR/Research_Plan.md` §3.4；`P0_EI/04_timing/data/G_PAIRED_summary.json`；`P0-BENCH-G-5060TI-PAIRED-20261006-01`；commit `bb617f0` |  |

现行 C1／C2 全文：`PR/Research_Plan.md` §3（Full Report §2.2–2.3 照录）。

## H1

<span style="color:gray">提示：回顾性写法：先写实验前你当时的预期（可参考 §3.0 v1 及 `PR/Writing/P0_Two_Paper_Plan_2026-09-22.md`），再写事后补充；不要按结果倒推。</span>


### 假设

### 为什么认为成立

### 验证实验

### 支持H1需要看到什么

### 如果H1不成立意味着什么

------------------------------------------------------------------------

## H2

### 假设

### 为什么认为成立

### 验证实验

### 支持H2需要看到什么

### 如果H2不成立意味着什么

------------------------------------------------------------------------

## H3

### 假设

### 为什么认为成立

### 验证实验

### 支持H3需要看到什么

### 如果H3不成立意味着什么

------------------------------------------------------------------------

# 4. Experiment Design｜实验设计卡

> 本节只记已冻结、已执行的设计事实（助手预填）。“对应 RQ／假设”与“预期结果”留给你在 §1.7、§3 写完后回填。

## 4.1 实验目的

> 本实验回答：“在同一冻结检测器、同一后处理门槛下，只改变推理协议（输入分辨率／是否切片／切哪些片），航拍小目标的召回、精度与端到端时延如何权衡？何时增益只是来自分辨率或覆盖范围？”（原文照录，`PR/Research_Plan.md` §1）

## 4.2 对应研究问题

-   RQ：（待你在 §1.7 写出 RQ 后回填）

## 4.3 对应假设

-   H：（待你在 §3 写出假设后回填）

## 4.4 自变量

-   推理协议，5 个水平：F640／F1280／DensK1／UnifAll／SAHI640（定义见 §4.7；`P0_EI/00_freeze/Environment_Freeze.md`、`P0_EI/00_freeze/DensK1_Definition.md`）
-   数据集：VisDrone2019-DET test-dev（主评测）／UAVDT DET（跨集外推）（`PR/Research_Plan.md` §2）
-   时延测量平台（只作分列，不作合并比较）：GTX 1660 SUPER／UAV_BT1；RTX 5060 Ti／UAV_BT2（Full Report §3.7）

## 4.5 因变量

-   precision = TP／(TP+FP)（池化）
-   small recall = 匹配上的小 GT 数／小 GT 总数；小目标 = 原图面积 0 < w·h < 1024 px²
-   recall_all = TP／有效 GT（导读派生的补充指标）
-   端到端时延（ms）：已解码内存 BGR 图 → finalize 后的 CPU 框，前后各一次 `torch.cuda.synchronize()`（`P0_EI/05_packaging/Reproducibility_Appendix.md` §2.2）
-   派生量（Run I）：每图前向次数、输入／内容 Mpx、边际 Δrecall／Mpx、ms／输入 Mpx（`P0_EI/04_timing/Pixel_Latency_Table.md`）

来源：Full Report §3.5（匹配器）、§3.4.6（计时边界）。

## 4.6 控制变量

-   模型：YOLO11n（Ultralytics，P3–P5 三尺度），未改 backbone／loss／模块（Full Report §3.1，引 `PROJECT_CONTEXT.md` §5）
-   权重：单一冻结 `last.pt`，SHA256 `bc42d54e…0aa5533`（全文见 §0）；每个 Stage 运行前断言 SHA（`B_TIMING_protocol.json`、`D_TESTDEV_summary.json`、`E_FULL_summary.json`）
-   数据集：VisDrone test-dev 1610 张（小 GT 50431）；UAVDT 40735 帧（只评 car／truck／bus，小 GT 493861）（`D_TESTDEV_summary.json`、`E_FULL_summary.json`）
-   数据划分：test-dev 只用一次（Stage D `one_shot: true`）；cal48 只算开发证据（`P0_EI/01_visdrone_main/StageC_Cal48_Dev_Report.md`）
-   输入尺寸：F640／F1280 整图 letterbox 到 640×640／1280×1280（`rect=False`）；DensK1／UnifAll 窗口 640×640、步长 512、末窗贴边；SAHI640 切片 640×640、重叠 0.25（步长 480）、每片 `rect=True`（`Reproducibility_Appendix.md` §2.1）
-   Confidence：每视图前向 `conf=0.001`；统一终处理 finalize 保留 conf ≥ 0.25；匹配器只用 conf ≥ 0.25 的预测（Full Report §3.4.1、§3.5）
-   IoU：finalize 为按类别 CPU NMS，IoU > 0.5，最多 500 框；匹配器 IoU ≥ 0.5；SAHI640 每片 ultralytics 默认 `iou=0.7`、`max_det=300`，合并 GREEDYNMM／IOS 0.5（Full Report §3.4.1、§3.4.5）
-   Hardware：见下表
-   Software：见下表
-   其他：FP32、batch 1（`half=False`）；五协议共用同一 finalize；UAVDT 预测按冻结映射改写类别，不用 ignore 文件（`P0_EI/03_cross_uavdt/StageE_Channel_Decision.md`）

**硬件与软件（两套环境分列，来源：`Reproducibility_Appendix.md` §2.4；`P0_EI/00_freeze/Environment_Delta_UAV_BT2_vs_UAV_BT1.md`；`env_snapshot.txt`；`env_snapshot_UAV_BT2_20261006.txt`；Full Report §3.7）**

| 项 | GTX 1660 SUPER／**UAV_BT1**（冻结） | RTX 5060 Ti 16GB／**UAV_BT2**（现用） |
|---|---|---|
| 用于 | BT1 训练；Stage A–F 全部精度与时延 | Run G 正式时序；Run H–K 的 CPU 再分析 |
| GPU | 6144 MiB，驱动 591.86，功耗上限 125 W | 16311 MiB，驱动 591.86，sm_120，功耗上限 180 W |
| CPU／电源计划 | **待补**（冻结件未记录） | AMD Ryzen 5 5600G（6C／12T）；Windows“平衡” |
| Python | 3.12.14 | 3.10.22 |
| torch／CUDA／cuDNN | 2.7.1+cu126／12.6／90701 | 2.7.1+cu128／12.8／90701 |
| ultralytics | 8.4.90（pinned zip `ultralytics-07958a7.zip`） | 同一 zip、同一 sha256 |
| numpy | 2.5.2 | 2.2.6 |
| opencv／pillow | 5.0.0.93／12.3.0 | 5.0.0.93／12.3.0 |
| sahi | Stage B–E 运行时版本无法证明；09-29 备份为 0.11.32 | 0.11.32 |
| 环境位置 | `H:\Conda\envs\UAV_BT1`，2026-10-04 换盘后已不存在 | `F:\Conda\envs\UAV_BT2` |

## 4.7 Baselines

| Method | Resolution | Slicing | Detector | Purpose |
|---|---|---|---|---|
| F640 | 整图 letterbox 640×640 | 无；每图 1 次前向 | 冻结 YOLO11n | 最快的整图基线 |
| F1280 | 整图 letterbox 1280×1280 | 无；每图 1 次前向 | 同上 | C1 的“强简单基线” |
| DensK1 | 整图 640 + 1 个 640×640 原生像素窗 | 网格 640／步长 512；按 F640 中 conf ≥ 0.25 框中心计数选 Top-1 窗；每图 2 次前向 | 同上 | 选区（只看一块）；定义沿用 BTD8 |
| UnifAll | 整图 640 + 同网格全部 640×640 窗 | 全覆盖；每图 1+N 次前向（VisDrone 平均 7.11，UAVDT 3） | 同上 | 覆盖上界／选区对照 |
| SAHI640 | 640×640 切片，每片 `rect=True` | sahi 0.11.32 `get_sliced_prediction` 默认：重叠 0.25、整图标准预测（切片数 > 1 时）、GREEDYNMM／IOS 0.5 | 同上 | 工程切片近邻（按默认设置使用，未调参） |

来源：Full Report §3.4.2–3.4.5；`Reproducibility_Appendix.md` §2.1（Run J）；`P0_EI/04_timing/Pixel_Latency_Table.md`（前向次数，Run I）。

## 4.8 指标

> **口径声明：** 本项目用的是 conf 0.25／IoU 0.5 单工作点的匹配器（`diagnose_bt1.prepare_gt + match_gt`，VisDrone 兼容口径），报 precision 与 small recall。**它不是 AP**：不是 COCO AP，不是 VisDrone 排行榜 AP，也不是 UAVDT 官方 MATLAB AP（`PR/Research_Plan.md` §2–§3.3；Full Report §3.5；`P0_EI/00_freeze/provenance/A0-07_Evaluator_Semantics_Check.md`）。

### Accuracy

-   mAP：未使用（匹配器不是 AP）
-   AP50：未使用
-   AP75：未使用
-   AP-Small：未使用；以 small recall 代替（面积 < 1024 px²）
-   Recall：small recall（主指标）；recall_all（派生补充）
-   Precision：pooled precision（conf ≥ 0.25，IoU ≥ 0.5）
-   F1：未报告

### Efficiency

-   Latency：端到端 mean（ms），按 GPU 分表
-   p50：median（Stage B、Stage D／F、Run G 均报）
-   p95：报（Stage B 表 B-1；Run G 表 G-1／G-3）
-   p99：报（同上）；另报 p90
-   FPS：未报告（统一用 ms）
-   Memory：RTX 5060 Ti 运行峰值显存 209082368 bytes（约 199.4 MiB）（`P0_EI/04_timing/Timing_5060Ti_Table.md` §1、§3）；1660 **待补**
-   Power：未测量
-   Budget violation：Stage B（1660，cal48）报每图 3 次中位数 > T 的比例，T = 20／25／30／40／50／75／100 ms；T = 40 ms 只是相对参考，不是业务硬期限（`P0_EI/04_timing/data/B_TIMING_summary.json`；Full Report §5.4）

### Statistics

-   Statistical unit：VisDrone 为图像（N = 1610；召回检验去掉无小 GT 的 111 张后 N = 1499）；UAVDT 为序列（50 个；序列级 Wilcoxon 排除无小 GT 的 M0801，n = 49）（`F_summary.json`；`P0_EI/03_cross_uavdt/H_UAVDT_Paired_Stats_Report.md`）
-   Test：Wilcoxon 符号秩检验（自写，统计量 min(W+, W−)，正态近似，含 tie 校正与 0.5 连续性校正，双侧，不调用 scipy）；另报胜负计数、Wilson 区间、McNemar（`Reproducibility_Appendix.md` §2.3；`P0_EI/02_paired_stats/StageF_Paired_Stats_Report.md`）
-   Bootstrap：图像级有放回重抽样，B = 10000，seed 20260917，百分位法；UAVDT 另做 50 序列 cluster bootstrap（Run H；Run K 的 UAVDT 分箱同法）
-   Confidence interval：95%
-   Multiple-comparison correction：主对 F1280 vs DensK1 报原始 p；5 个次要对做 Holm 校正（Stage F；Run H 同）。Run K 分箱比较未做多重比较校正（Full Report §7 第 16 条）

## 4.9 预期结果

<span style="color:gray">提示：本篇实验已完成，这里若要写，请标明是“回顾性”的；可对照 §3.0 修订记录。</span>

### 如果H1成立

### 如果H1不成立

### 可能出现的替代解释

------------------------------------------------------------------------

# 5. Experiment Log｜实验日志

> 按约定不复制日志正文，只列 Run A–K 的链接表。权威索引：[`P0_EI/Run_Index.md`](../Experiments/papers/P0_EI/Run_Index.md)。路径相对 `P0_EI/`。

## Experiment ID

| Stage | Run ID | 目的 | 状态 | 报告 | 数据 |
|---|---|---|---|---|---|
| A | `P0-BENCH-A-ENV-20260917-01` | 冻结权重、数据清单、环境、五协议定义、评价门、计时边界 | **PASS** | `00_freeze/Environment_Freeze.md` | `00_freeze/*` |
| B | `P0-BENCH-B-TIMING-20260917-01` | GTX 1660 SUPER 流水线计时（cal48，48 × 5 × 3） | **PASS** | `04_timing/StageB_Timing_Report.md` | `04_timing/data/B_*` |
| C | `P0-BENCH-C-CAL48-20260917-01` | cal48 精度（开发证据，非主表） | **PASS** | `01_visdrone_main/StageC_Cal48_Dev_Report.md` | `01_visdrone_main/data/C_*` |
| D | `P0-BENCH-D-TESTDEV-20260917-01` | VisDrone test-dev 一次性终评（主精度表） | **PASS** | `01_visdrone_main/StageD_TestDev_Report.md` | `01_visdrone_main/data/D_*` |
| E | `P0-BENCH-E-UAVDT-20260918-FULL` | UAVDT 跨集外推（冻结 JSON 内 `run_id` 为冒烟值 `…-01`，以 FULL 为准） | **PASS** | `03_cross_uavdt/StageE_UAVDT_Report.md` | `03_cross_uavdt/data/E_*` |
| F | `P0-BENCH-F-TESTDEV-20260917-01` | VisDrone 图级配对统计 | **PASS** | `02_paired_stats/StageF_Paired_Stats_Report.md` | `02_paired_stats/data/F_*` |
| G-SMOKE | `P0-BENCH-G-5060TI-SMOKE-20261001-01` | RTX 5060 Ti 链路冒烟（不进证据表） | **PASS** | `04_timing/Timing_5060Ti_Table.md` | `04_timing/data/G_logs/P0-BENCH-G-5060TI-SMOKE-20261001-01/` |
| G-CAL48 | `P0-BENCH-G-5060TI-CAL48-20261001-01` | 5060 Ti cal48 计时 + 与 1660 的精度一致性闸门 | **PASS** | `04_timing/Timing_5060Ti_Table.md` | `04_timing/data/G_CAL48_*` |
| G-TESTDEV | `P0-BENCH-G-5060TI-TESTDEV-20261001-01` | 5060 Ti test-dev 全量计时（1610 × 5，one-shot） | **PASS** | `04_timing/Timing_5060Ti_Table.md` | `04_timing/data/G_TESTDEV_*`、`G_TIMING_stats.json` |
| G-PAIRED | `P0-BENCH-G-5060TI-PAIRED-20261006-01` | 5060 Ti 图级配对时延检验（主对 F1280 vs DensK1） | **PASS** | `04_timing/Timing_5060Ti_Table.md` §4 | `04_timing/data/G_PAIRED_*` |
| H | `P0-BENCH-H-UAVDT-PAIRED-20261006-01` | UAVDT 图级配对 + 50 序列 cluster bootstrap；Stage F 在 UAV_BT2 下复现核对（CPU only） | **PASS** | `03_cross_uavdt/H_UAVDT_Paired_Stats_Report.md` | `03_cross_uavdt/data/H_*`；`02_paired_stats/data/H_FREPRO_*` |
| I | `P0-BENCH-I-PIXLAT-20261006-01` | 像素–时延归一化（CPU only） | **PASS** | `04_timing/Pixel_Latency_Table.md` | `04_timing/data/I_*` |
| J | `P0-BENCH-J-REPRO-20261006-01` | 复现附录补缺 + 6 例失败裁图（复用 Run G 预测，CPU only） | **PASS** | `05_packaging/Reproducibility_Appendix.md` | `05_packaging/failure_crops/` |
| K | `P0-BENCH-K-DENSITY-20261006-01` | 密度属性切片（valid_gt／small_gt 五分位，CPU only） | **PASS** | `06_density_slices/K_Density_Slices_Report.md` | `06_density_slices/data/K_*` |

来源：`P0_EI/Run_Index.md`；`00_Overview/Current_Stage.md`“进度”表。脚本：`BENCH/stage_{b,d,e,f,g,h,i,j,k}/`（Full Report §8.2）。

## 原始结果

不在此复制；见上表各报告，汇总见 Full Report §5（数字以源文件 `data/*.json`／`*.csv` 为准）。

## 客观观察

<span style="color:gray">提示：如要写观察，请只写事实；可从 Full Report §5 各表抄数并注明 Run ID。</span>

1.  
2.  
3.  

## 异常

已登记、冻结件不改的已知不一致（Full Report §7 第 19 条；`P0_EI/Run_Index.md` 注）：

-   `00_freeze/stage_e_config_freeze.json` 的 `run_id` 是冒烟值 `P0-BENCH-E-UAVDT-20260918-01`；全量终跑为 `P0-BENCH-E-UAVDT-20260918-FULL`。
-   UAVDT 路径三处写法不同；当前实际位置 `G:\Schloar Data\P0\dataset\UAVDT\`（Full Report §3.2.3）。
-   冻结元数据 `sahi_postprocess: "sahi_default_NMS"` 为误称，实际为 GREEDYNMM／IOS（Run J，`Reproducibility_Appendix.md` §2.1）。
-   `Environment_Freeze.md` 的“240 windows”是 cal48 48 张图的窗口总数，不是每图窗数（Run J）。
-   `protocol.json` 的 `hardware_role` 仍写 4090（Full Report §7 第 19 条）。
-   `Run_Index.md` 中 Run K 摘要写“VisDrone 各箱 F1280−DensK1 +0.030～+0.046”；`K_Density_Slices_Report.md` §1 按 valid_gt 为 +0.0218～+0.0460，§2 按 small_gt 为 +0.0265～+0.0449。两处表述 **待核**（本文 §7 用 K 报告原表数字）。

## 失败实验

-   实验：T4／Kaggle 重训轨（2026-09-17 授权，09-18 撤回）
-   失败原因：Kaggle Version #1 venv／ensurepip 错误，约 21.6 s，未产生任何新权重
-   是否影响论文：否；本地冻结权重 SHA 复核一致（Full Report §4 插曲 2；`00_Overview/Current_Stage.md`）
-   是否需要重跑：否（授权已撤回）

-   实验：UAVDT 下载（作者 Google Drive／Zenodo 重传）
-   失败原因：Drive 配额限制；Zenodo 下载中断（仅 36,580,364 bytes）；改走百度网盘后成功
-   是否影响论文：Attributes 包未下载，Run K 无法做场景／高度／视角切片（Full Report §4 插曲 1）
-   是否需要重跑：可选（Full Report §9 第 10 项）

-   实验：`P0-BENCH-G-4090-*-20260920-01`
-   失败原因：从未运行，已由 5060 Ti 的 Run G 取代；4090 未落实的原因仓库内无书面记录（**待补**）（`P0_EI/Run_Index.md`；Full Report §4 Stage G）
-   是否影响论文：否
-   是否需要重跑：否

------------------------------------------------------------------------

# 6. Result Interpretation｜结果解释卡

<span style="color:gray">提示：结果在 Full Report §5（全部结果表）与 §6（解读，供对照，不要照抄）；局限在 Full Report §7；各 Run 报告见 §5 链接表。</span>

## 6.1 最重要的结果

## 6.2 结果说明什么？

## 6.3 为什么可能出现？

## 6.4 其他可能解释

1.  
2.  
3.  

## 6.5 如何排除其他解释？

## 6.6 当前证据能支持什么？

## 6.7 当前证据不能支持什么？

## 6.8 是否存在反例？

## 6.9 是否需要新增实验？

-   [ ] 不需要
-   [ ] 必须
-   [ ] 建议

原因：

------------------------------------------------------------------------

# 7. Evidence Matrix｜证据矩阵

> 数字照抄仓库文档（来源列出）。**Strength 由助手按以下规则预填，待你确认：** Strong = 正确统计单位上的配对检验，95% CI 不含 0；Medium = 描述性结果、单次测量、事后分箱或部分口径不显著；Weak = 两种口径结论不一致或 CI 跨 0。

| Claim | Evidence | Experiment | Dataset | Statistic | Strength | Status |
|---|---|---|---|---|---|---|
| C1（精度） | F1280 vs DensK1：small recall 0.4004 vs 0.3596，Δ = +0.0409；Δprecision +0.0681 [0.0631, 0.0731]；胜负 720／369／410 | `P0-BENCH-D-TESTDEV-20260917-01`；`P0-BENCH-F-TESTDEV-20260917-01` | VisDrone test-dev（N = 1499 有小 GT） | 图级 bootstrap 95% CI [0.0355, 0.0462]；Wilcoxon p = 2.997e-28（原始，主对） | Strong | SUPPORTED（`Research_Plan.md` §3） |
| C1（精度，跨集） | F1280 vs DensK1：Δsmall recall +0.0257；Δprecision +0.0244（序列 CI [0.0168, 0.0326]）；序列胜负 37／12／0 | `P0-BENCH-H-UAVDT-PAIRED-20261006-01` | UAVDT（50 序列） | 序列 cluster CI [0.0100, 0.0403]；序列 Wilcoxon p = 9.9e-4 | Strong | 支持 C1 精度方向（`H_UAVDT_Paired_Stats_Report.md`） |
| C1（时延，1660） | 均值差 −0.34 ms；逐图中位差 +0.25 ms；F1280 更快的图占 47.3% | `P0-BENCH-F-TESTDEV-20260917-01` | VisDrone test-dev，GTX 1660 SUPER／UAV_BT1（每图单次测量） | 均值差 CI [−0.66, −0.01]；逐图 Wilcoxon p = 0.235 | Medium | SUPPORTED，措辞为“统计上不可区分” |
| C1（时延，5060 Ti） | 均值差 −14.01 ms；逐图中位差 −13.32 ms；1607／1610 张 F1280 更快；GPU 平均利用率约 11% | `P0-BENCH-G-5060TI-PAIRED-20261006-01` | VisDrone test-dev，RTX 5060 Ti／UAV_BT2 | 均值差 95% CI [−14.22, −13.80]；p≈3.6e-264（正态近似极端尾部，只说明方向一致） | Strong（仅限该机器；排序依赖 CPU／流水线） | SUPPORTED |
| C1（时延，UAVDT，1660） | Δmean ms +0.11 | `P0-BENCH-H-UAVDT-PAIRED-20261006-01` | UAVDT，GTX 1660 SUPER／UAV_BT1 | 序列 CI [−0.50, 0.70]；帧级 Wilcoxon p = 0.096 | Medium | 与“1660 上不可区分”一致 |
| C2（覆盖换召回） | UnifAll small recall 0.4511 vs F1280 0.4004（F1280 − UnifAll = −0.0507）；precision 0.5123 vs 0.6753（Δ +0.1629）；mean 112.21 vs 33.72 ms（1660，约 3.3×） | Stage D／F | VisDrone test-dev | Δsr CI [−0.0551, −0.0464]；Δprec CI [0.1583, 0.1677]；Holm p = 2.927e-86 | Strong | SUPPORTED |
| C2（SAHI640 被支配） | F1280 − SAHI640：VisDrone Δsr +0.1820、Δprec +0.3166、Δms −339.5（1660）；UAVDT Δsr +0.0332、Δprec +0.0189、Δms −130.92（1660） | Stage D／F；Run H | VisDrone test-dev；UAVDT | VisDrone Δsr CI [0.1735, 0.1908]，Holm p = 2.030e-182；UAVDT 序列 CI [0.0039, 0.0732]，Δprec 序列 CI [0.0044, 0.0368] | Strong（限 sahi 默认设置） | SUPPORTED |
| C2（无通用排序） | VisDrone：UnifAll 0.4511 > F1280 0.4004 > DensK1 0.3596 > F640 0.2388 > SAHI640 0.2184；UAVDT：F1280 0.7929 > UnifAll 0.7824 > DensK1 0.7672 > SAHI640 0.7597 > F640 0.7080 | `P0-BENCH-D-TESTDEV-20260917-01`；`P0-BENCH-E-UAVDT-20260918-FULL`；Run H | 两集分列（禁止合并平均） | 池化描述；UAVDT F1280 vs UnifAll 序列 CI [0.0012, 0.0180]，但序列 Wilcoxon p = 0.322 | Medium | SUPPORTED（`StageE_UAVDT_Report.md` §4） |
| H 发现 1：帧级显著性高估 | UAVDT 主对帧级 Wilcoxon p = 3.6e-293；按序列聚类后 CI [0.0100, 0.0403] | Run H | UAVDT | 帧级 vs 序列 cluster | —（统计单位核对） | 记录在案 |
| H 发现 2：DensK1 vs SAHI640（UAVDT）未确立 | Δsr +0.0074 | Run H | UAVDT | 序列 CI [−0.0303, 0.0553]；序列 Wilcoxon Holm p = 0.033（两口径不一致） | Weak | 记为“未确立差异” |
| H 发现 3：Stage F 复现 | UAV_BT2 下重算 Stage F 与 `F_summary.json` 逐位一致（0 处不一致）；Run G 精度 abs(Δsmall recall) ≤ 0.014 个百分点 | Run H；Run G | VisDrone test-dev | 逐位比对 | —（复现核对） | PASS |
| I 发现：同像素不同协议 | UnifAll 与 SAHI640 同为 7.11 次前向、内容 2.742 Mpx，small recall 0.451 vs 0.218；DensK1 边际 Δrecall／Mpx 0.295（VisDrone）、0.144（UAVDT）最高；ms／输入 Mpx：F1280 20.6（1660）／16.0（5060 Ti），DensK1 41.6／49.1，UnifAll 38.5／46.9 | `P0-BENCH-I-PIXLAT-20261006-01` | VisDrone test-dev；UAVDT | 描述性（未做因果检验） | Medium | 记录在案（`Pixel_Latency_Table.md` §4） |
| J 发现：SAHI 实际设置 | sahi 默认合并为 GREEDYNMM、度量 IOS、阈值 0.5；每片 `iou=0.7`、`max_det=300`；6 例失败裁图（如例 5：UnifAll 62 vs SAHI640 10／176 small GT） | `P0-BENCH-J-REPRO-20261006-01` | VisDrone test-dev（Run G 预测，5060 Ti） | 代码读取 + 逐例断言 | —（事实核对；SAHI 漏检机制未验证） | PASS |
| K 发现：密度切片 | VisDrone 按 valid_gt 五箱 F1280−DensK1：+0.0347／+0.0218／+0.0365／+0.0381／+0.0460，CI 均不含 0；10 个非零箱 UnifAll 均最佳；UAVDT 最稀疏箱 [1,9] −0.0009 [−0.0270, +0.0271]，valid_gt ≥ 10 起 F1280 最佳；DensK1 从未在任何箱最佳 | `P0-BENCH-K-DENSITY-20261006-01` | VisDrone test-dev（图像 bootstrap）；UAVDT（序列 cluster） | 箱内 bootstrap B = 10000；未做多重比较校正 | Medium（事后五分位分箱） | 记录在案（`K_Density_Slices_Report.md` §1、§3、§5） |

来源汇总：Full Report §2.2–2.3、§5.1–5.9；`P0_EI/02_paired_stats/data/F_summary.json`；`P0_EI/04_timing/Timing_5060Ti_Table.md` §4–§6；`P0_EI/03_cross_uavdt/H_UAVDT_Paired_Stats_Report.md`；`P0_EI/04_timing/Pixel_Latency_Table.md`；`P0_EI/05_packaging/Reproducibility_Appendix.md`；`P0_EI/06_density_slices/K_Density_Slices_Report.md`。

> 每个论文核心结论必须有对应证据。

------------------------------------------------------------------------

# 8. Final Scientific Story｜最终科学叙事

<span style="color:gray">提示：主张原文在 `PR/Research_Plan.md` §3（C1／C2）；证据见本文 §7；不应声称的内容见 Full Report §2.5；局限见 Full Report §7。§8.1 只保留了句式。</span>

> **只有完成核心实验后填写。**

## 8.1 一句话故事

> **实证对比句式（只给句式，未填写）：** Under a unified frozen detector and evaluation protocol, we compare [protocols] on [datasets] and find that [finding A] under [condition B], whereas [finding C].

中文句式：在统一的冻结检测器与评测协议下，我们在［数据集］上比较［协议］，发现在［条件 B］下［发现 A］，而［发现 C］。

中文：

## 8.2 Problem

## 8.3 Gap

## 8.4 Key Insight

## 8.5 Evaluation Design / 评测设计

## 8.6 Evidence

## 8.7 Main Findings

1.  
2.  
3.  

## 8.8 Contributions

1.  
2.  
3.  

## 8.9 Limitations

1.  
2.  
3.  

## 8.10 不应声称的结论

1.  
2.  
3.  

------------------------------------------------------------------------

# 9. Figure & Table Story｜图表叙事

> 只列仓库里已有的图表与数据源（事实）；“回答哪个 RQ／支持哪个 Claim”是助手的**建议，待用户确认**。RQ 尚未在 §1.7 定义，先按 C1／C2 与 H–K 发现标注。IJCNN 限 6 页，最终选哪几张由你决定。

## Figure 1

-   图名：VisDrone 五协议精度、召回与 1660 时延
-   文件：`P0_EI/05_packaging/figures/fig1_visdrone_metrics.png`
-   目的：并列展示五协议在 VisDrone test-dev 上的 precision、small recall 与 1660 均值时延；数据 `P0_EI/01_visdrone_main/data/D_TESTDEV_summary.json`（Stage D）
-   回答哪个RQ：建议：协议–精度–时延权衡类 RQ（待用户确认）
-   支持哪个Claim：建议：C2（覆盖换召回）；C1 精度部分（待用户确认）

## Figure 2

-   图名：UAVDT 五协议
-   文件：`P0_EI/05_packaging/figures/fig2_uavdt_metrics.png`
-   目的：五协议在 UAVDT 上的指标；数据 `P0_EI/03_cross_uavdt/data/E_FULL_summary.json`（Stage E）
-   回答哪个RQ：建议：跨数据集外推类 RQ（待用户确认）
-   支持哪个Claim：建议：C2（无通用排序）（待用户确认）

## Figure 3

-   图名：两集 small recall 并排（禁止合并平均）
-   文件：`P0_EI/05_packaging/figures/fig3_dual_set_small_recall.png`
-   目的：把 D 与 E 的 small recall 并排；数据同 fig1／fig2
-   回答哪个RQ：建议：跨数据集外推类 RQ（待用户确认）
-   支持哪个Claim：建议：C2（排序随数据集改变）（待用户确认）

## Figure 4

-   图名：GTX 1660 SUPER 时延（Stage B，cal48）
-   文件：`P0_EI/05_packaging/figures/fig4_timing_1660.png`
-   目的：1660／UAV_BT1 上五协议时延分布；数据 `P0_EI/04_timing/data/B_TIMING_summary.json`
-   回答哪个RQ：建议：时延／硬件依赖类 RQ（待用户确认）
-   支持哪个Claim：建议：C1 时延（1660 部分）（待用户确认）

## Figure 4b

-   图名：RTX 5060 Ti 时延（Run G，单列）
-   文件：`P0_EI/05_packaging/figures/fig4b_timing_5060ti.png`
-   目的：5060 Ti／UAV_BT2 上五协议时延，单独成图、不覆盖 fig4；数据 `P0_EI/04_timing/data/G_TIMING_stats.json`
-   回答哪个RQ：建议：时延／硬件依赖类 RQ（待用户确认）
-   支持哪个Claim：建议：C1 时延（5060 Ti 部分）（待用户确认）

## Figure 5

-   图名：Stage F 配对 Δsmall recall 与 95% CI
-   文件：`P0_EI/05_packaging/figures/fig5_stageF_deltas.png`
-   目的：六个比较对的配对差与 CI；数据 `P0_EI/02_paired_stats/data/F_summary.json`
-   回答哪个RQ：建议：协议–精度权衡类 RQ（待用户确认）
-   支持哪个Claim：建议：C1 精度；C2（待用户确认）

## Figure 6（失败例裁图，6 张）

-   图名：失败与边界例裁图（Run J）
-   文件：`P0_EI/05_packaging/failure_crops/case1_F1280_wins_9999938_00000_d_0000210.jpg`、`case2_F1280_wins_9999938_00000_d_0000212.jpg`、`case3_DensK1_wins_0000073_03155_d_0000004.jpg`、`case4_DensK1_wins_0000073_01275_d_0000002.jpg`、`case5_SAHI640_loses_same_pixels_9999938_00000_d_0000121.jpg`、`case6_all_miss_9999938_00000_d_0000247.jpg`；元数据 `cases.json`
-   目的：例 1–2 F1280 赢（小目标分散）；例 3–4 DensK1 赢（1920×1080 大图密集人群）；例 5 同像素下 SAHI640 漏检；例 6 三协议都几乎全漏（Full Report §5.10）。来源为 Run G 已存预测（5060 Ti／UAV_BT2）
-   回答哪个RQ：建议：失败场景／边界类 RQ（待用户确认）
-   支持哪个Claim：建议：C1 的边界（DensK1 赢的情形）、J 发现（SAHI 设置）（待用户确认）

## Table 1

-   表名：VisDrone test-dev 五协议主表（Stage D）
-   文件：`P0_EI/01_visdrone_main/data/D_TESTDEV_summary.json`；排版参考 Full Report §5.1
-   目的：TP／FP／precision／small TP／small recall／1660 时延
-   回答哪个RQ：建议：协议–精度–时延权衡类 RQ（待用户确认）
-   支持哪个Claim：建议：C1、C2（待用户确认）

## Table 2

-   表名：UAVDT 五协议表（Stage E）+ 序列配对（Run H）
-   文件：`P0_EI/03_cross_uavdt/data/E_FULL_summary.json`；`P0_EI/03_cross_uavdt/data/H_UAVDT_PAIRED_summary.json`
-   目的：跨集指标与序列级 CI
-   回答哪个RQ：建议：跨数据集外推类 RQ（待用户确认）
-   支持哪个Claim：建议：C2；C1 精度跨集（待用户确认）

## Table 3

-   表名：配对时延 F1280 vs DensK1，两块 GPU 分列
-   文件：`P0_EI/04_timing/Timing_5060Ti_Table.md` §4（表 G-5）；`P0_EI/02_paired_stats/data/F_summary.json`
-   目的：同一主对在 1660 与 5060 Ti 上的时延差（每列标明 GPU 与环境）
-   回答哪个RQ：建议：时延／硬件依赖类 RQ（待用户确认）
-   支持哪个Claim：建议：C1 时延（待用户确认）

## Table 4

-   表名：像素–时延归一化（Run I）
-   文件：`P0_EI/04_timing/Pixel_Latency_Table.md`；`P0_EI/04_timing/data/I_PIXLAT_table.csv`
-   目的：前向次数、输入／内容 Mpx、边际 Δrecall／Mpx、ms／Mpx
-   回答哪个RQ：建议：“增益是否只来自像素”类 RQ（待用户确认）
-   支持哪个Claim：建议：I 发现；C2（待用户确认）

## Table 5

-   表名：密度切片（Run K）
-   文件：`P0_EI/06_density_slices/K_Density_Slices_Report.md`；`P0_EI/06_density_slices/data/K_DENSITY_pairs.csv`
-   目的：按 valid_gt／small_gt 五分位的协议对比
-   回答哪个RQ：建议：失败场景／条件依赖类 RQ（待用户确认）
-   支持哪个Claim：建议：K 发现；C1 精度的稳健性（待用户确认）

## Table 6

-   表名：近邻单轴对照（分辨率／选区→全覆盖／工程切片→整图高分／同为切片族）
-   文件：`P0_EI/05_packaging/Neighbor_Protocol_Table.md`
-   目的：D 与 E 分开的单轴 Δsr／Δprec／Δms（1660）
-   回答哪个RQ：建议：协议–精度–时延权衡类 RQ（待用户确认）
-   支持哪个Claim：建议：C2（待用户确认）

> 每张图/表必须回答一个明确问题，禁止"为了看起来丰富"而堆图表。

------------------------------------------------------------------------

# 10. Reviewer Attack Test｜审稿人攻击测试

<span style="color:gray">提示：可用证据：Q3 跨数据集 → Stage E、Run H；Q4 单一检测器 → Full Report §7 第 1 条；Q5 计算量 → Run I（`Pixel_Latency_Table.md`）；Q6 调参 → Stage A 冻结与 test-dev one-shot；Q7 换硬件 → Run G 与 Stage F 分列（`Timing_5060Ti_Table.md` §6）；Q9 失败场景 → `P0_EI/05_packaging/Failure_Boundary_Cases.md`、Run J 裁图、Run K。</span>

## Q1 为什么一定需要这个方法？

回答：

证据：

## Q2 与最接近工作相比创新在哪里？

回答：

证据：

## Q3 是否只在一个数据集有效？

回答：

证据：

## Q4 是否只对某一个检测器有效？

回答：

证据：

## Q5 提升是否来自更多计算量？

回答：

证据：

## Q6 是否因为参数调得更好？

回答：

证据：

## Q7 换硬件还成立吗？

回答：

证据：

## Q8 真实部署有没有价值？

回答：

证据：

## Q9 失败场景是什么？

回答：

## Q10 删除某个模块后论文是否仍然成立？

回答：

------------------------------------------------------------------------

# 11. Story Freeze｜叙事冻结

在进入正式论文写作前必须完成：

-   [ ] Research Problem 已冻结
-   [ ] Research Gap 已冻结
-   [ ] Closest Prior Work 已确认
-   [ ] Hypotheses 已确认
-   [ ] 核心实验已完成
-   [ ] 关键结果已复核
-   [ ] 统计方法已确认
-   [ ] Evidence Matrix 已完成
-   [ ] Figure/Table Story 已完成
-   [ ] Reviewer Attack 已完成
-   [ ] Limitations 已明确
-   [ ] 不允许再为了"让故事更漂亮"篡改实验解释

**Story Freeze Date：**

**冻结版本：**

------------------------------------------------------------------------

# 12. Submission Readiness

-   [ ] 事实审计通过
-   [ ] 数字一致
-   [ ] 图表与正文一致
-   [ ] 引用完整
-   [ ] 参考文献可追溯
-   [ ] 方法可复现
-   [ ] 代码版本冻结
-   [ ] 数据版本冻结
-   [ ] 权重版本冻结
-   [ ] 统计正确
-   [ ] 没有过度声称
-   [ ] Reviewer Attack 已处理
-   [ ] 目标期刊格式完成
