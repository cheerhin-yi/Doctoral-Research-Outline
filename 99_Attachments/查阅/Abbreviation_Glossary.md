# 项目缩写与代号映射

更新日期：2026-09-17（增补 Literature 文件名级映射）。  
本文件解释仓库中常见代号，**不是**进度表。当前唯一事项以 [`00_Overview/Current_Stage.md`](Current_Stage.md) 为准。  
实验运行细节以 [`00_Practice_UAV_Aerial_Detection/Experiments/Experiment_Tracker.md`](../00_Practice_UAV_Aerial_Detection/Experiments/Experiment_Tracker.md) 为准。

阅读约定：
- **BT** = Baseline Training（基线训练）
- **BTD** = Baseline／机制 **Diagnosis**（基线诊断；不是新训练编号）
- **P0** = 练手论文（Practice），不计入七篇主论文
- 同一概念只保留下表主写法；括号内为文件名里偶见的别称

---

## 1. 论文与目录编号

| 代号／目录 | 含义 |
|---|---|
| Paper 1 … Paper 7 | 七篇主论文（开放世界风险 → … → 多机决策） |
| 练手文／Practice／P0 | Paper 1 前的独立练习论文，不计入七篇 |
| `00_Overview` | 总指南、当前阶段、文献注册、创新台账 |
| `00_Practice_UAV_Aerial_Detection` | **当前**练手文工作目录（合并后） |
| `…/Experiments/` | 练手文实验脚本、协议、结果报告（默认只读） |
| `00_PrePaper_Lightweight_Detection` | 历史：轻量共享头（LSM-Head）方案，已归档 |
| `00_Startup_Railway_UAV_Detection` | 历史：主线 A 启动目录名，已归档合并 |
| `01_Paper1_…` … `07_Paper7_…` | 各主论文目录；2–7 现为 PAUSED |
| `90_English_Learning` | 英语支持线（并行，不改科研主张） |
| `99_Attachments` | 附件、指南、归档、本缩写表 |
| `11_Datasets` | 数据与权重（多被 gitignore） |

---

## 2. 学习关卡与旧「S」编号

| 代号 | 含义 |
|---|---|
| **L0–L4** | 2026-09-16 起的掌握关卡，见 `Completion_Metrics.md` |
| **S0-01** | 旧称：YOLO 完整检测链个人验收。现并入 **L0**。表示个人掌握，不是实验授权门 |
| EL-01 | 英语模块：YOLO 检测链术语（见 `90_English_Learning`） |

---

## 3. 主线 A／阶段「A」编号

| 代号 | 含义 |
|---|---|
| **主线 A** | 练手文技术主线：时间预算约束下的航拍小目标检测 |
| **A0** | 可行性／受限开发探索阶段（近邻、数据审计、受限基线与诊断） |
| A1–A5 | 原阶段门：必要知识→基线诊断→单机制→正式实验→写作。**现况：** A0 对独立新机制 HOLD；A2–A4 未开放；A5 仅对本 EI 稿有限开放 |
| **A0-01 … A0-09** | A0 下书面／数据任务编号（多在 `Experiments/` 文件名里） |
| A0-01 | 铁路版计划／UAV-RSOD 等首批核验相关交付 |
| A0-02 | UAV-RSOD 数据缺口补证 |
| A0-03 | 作者数据询问信草稿 |
| A0-04 | VisDrone 优先对象确认与入口预审（文件可能未单独落盘） |
| A0-05 | VisDrone 文件级审计 |
| A0-06 | 评测与数据用途草案 |
| A0-07 | 评价器语义／构造样例核验 |
| A0-08 | 可行性决策 |
| A0-09 | 单机制候选差异与否决审查 |

---

## 4. 主张与问题代号「P／C／RQ」

| 代号 | 含义 | 状态（2026-09-16） |
|---|---|---|
| **P0-EI-C1** | 固定 YOLO11n 与已声明预算口径下，整图 1280 比当前密度单片更准且更快（协议／对比，非新算法） | PROPOSED（近程 EI 稿） |
| **P0-EI-C2** | 区域分配存在可恢复空间 ≠ 可部署增益；须同时报告超时率与选择漏检 | PROPOSED（近程 EI 稿） |
| **P0-A-C1** | 同整帧预算下，区域／局部高分辨率分配能否优于整图、升分辨率、均匀切片或简单选区？ | HOLD（历史机制主张） |
| **P0-A-C2** | 能否控制选区引入的漏检，并满足声明的整帧预算协议？ | HOLD（历史机制主张） |
| P0-C0-1／P0-C0-2 | 更早 LSM-Head 练手主张 | 历史，已退出执行 |
| P1-C1／P1-C2 | Paper 1 两项主张 | PAUSED |
| RQ-BTD12-1 | BTD12 审查的唯一候选：尺度条件 DFL 分布统计重评分 | DISMISSED |

---

## 5. `Experiments/` 核心：BT／BTD／数据切片／对照

### 5.1 怎么读文件名

| 文件名模式 | 含义 |
|---|---|
| `BT1_*.md` / `run_bt1.py` | 基线训练 BT1 相关协议、结果、脚本 |
| `BTD{n}_*_Protocol.md` | 第 n 次诊断的**协议**（先写清再跑） |
| `BTD{n}_*_Result.md` / `*_Analysis.md` | 第 n 次诊断的**结果／分析** |
| `A0-0x_*.md` | A0 阶段书面／数据任务，不是模型训练 |
| `verify_*.py` / `check_*.py` | 校核脚本，不等于新实验创新 |
| `*_Audit.md` | 数据、标签、权重、接口等审计 |

### 5.2 BT1：基线训练

| 代号 | 含义 |
|---|---|
| **BT1** | Baseline Training 1：受限条件下的普通 **YOLO11n** 基线训练包装／运行（不是新网络） |
| BT1-SMOKE-… | 冒烟 Run：只验证训练／保存／重载链路，**不能**当正式基线精度 |
| BT1-LOCAL-… | 本机分段／续训 Run ID（如完成 100 轮的那条链） |
| `last.pt`／EMA | 约定使用的训练末轮（或 EMA）权重 |
| baseline_eligible | 某次运行是否允许当作正式基线证据（冒烟一般为 false） |

### 5.3 BTD1–BTD12：诊断任务（逐号）

**BTD = 在固定 BT1 权重上做的诊断／对照，默认不改网络、不新训。**  
证据多在 `cal48`／`diag500` 等**开发集**上，会议稿必须披露。

| 代号 | 一句话 | 典型文件 |
|---|---|---|
| **BTD1** | cal48 上可恢复漏检诊断（跨层／局部池等启发式，v0.1 后 HOLD） | `BT1_Cal48_Miss_Diagnosis.md` 等 |
| **BTD2** | 密度选区残差归因（未覆盖／覆盖未检出／融合变化） | `BTD2_Density_Miss_*` |
| **BTD3** | 简单「去重密度」相对原密度的缓存对照 | `BTD3_Dedup_Density_Result.md` |
| **BTD4** | 两简单规则在 **diag500** 上配对验证＋实测耗时 | `BTD4_Diag500_*` |
| **BTD5** | 公共 **NMS** 实现等价性与 CPU 耗时（工程加速 ≠ 创新） | `BTD5_NMS_*` |
| **BTD6** | 换用新 NMS 后的**完整流水线**复测与预算校核 | `BTD6_Pipeline_*` |
| **BTD7** | 去重后残差＋「条件再检」新增价值（含一次归档失败续接） | `BTD7_*` |
| **BTD8** | **单片**预算与选择上界（密度 K1 vs 参考计时等） | `BTD8_Single_Crop_*` |
| **BTD9** | **整图 F1280** 强简单基线缓存效果（常优于当时密度单片） | `BTD9_F1280_*` |
| **BTD10** | **书面**研究问题重审（无新模型运行） | `Research_Question_Reassessment_BTD10.md` |
| **BTD11** | F1280 错误结构（FN／FP、低分修复空间等，诊断≠方法增益） | `BTD11_Error_Structure_*` |
| **BTD12** | **书面**单机制否决：尺度条件 DFL 重评分 DISMISSED | `Literature/BTD12_*` |
| **BTD13** | **不存在／禁止擅自创建**（当前决定：不自动开新诊断号） | — |

### 5.4 数据切片与输入对照

| 代号                     | 含义                                      | 注意                  |
| ---------------------- | --------------------------------------- | ------------------- |
| **cal48**（文件中或作 cal48） | 从 val 按固定规则取出的 **48** 张，用于监控／反复开发诊断     | **不是**独立最终测试集       |
| **diag500**（或 diag500） | val 中其余约 **500** 张，用于规则验证／测速            | 同属开发证据              |
| train／val／test-dev     | VisDrone 官方划分语义下的集合                     | test-dev 未授权前不作调参集  |
| **F640**／**F1280**     | 整图输入边长约 640／1280 的强简单对照（F = full image） | F1280 是强基线，不是「新方法」  |
| 密度单片／K1                | 按密度等启发式选 **1** 个局部窗再检                   | 与均匀切片、整图对照区分        |
| 均匀切片                   | 按规则网格切片（EI 问题里的对照之一）                    | 本阶段整理已有证据，不默认新跑     |
| 小目标／small GT           | 本项目常用：原图像素面积 \(0 < w\times h < 1024\)   | 与 COCO small 定义可能不同 |
| ignore                 | 评测忽略区；训练时删正标签 **≠** 正确 ignore 监督        | 见标签适配审计             |

### 5.5 指标与计时（Experiments 报告里常出现）

| 词 | 含义 |
|---|---|
| TP／FP／FN | 真阳性／假阳性／假阴性（报告须写清「小目标」还是全尺寸） |
| Recall／Precision | 召回／精确率 |
| mAP／AP50／AP50–95 | 平均精度；**原生 Ultralytics AP ≠ VisDrone 官方兼容 AP** |
| conf／IoU | 置信度阈值／匹配或 NMS 的交并比阈值 |
| mean／p95 | 耗时均值／95 分位 |
| 超时率 | 超过声明参考时限（如曾用 40 ms）的帧比例；**40 ms 是相对参考，不是业务硬期限** |
| GT oracle／GT 最佳 | 用真值事后选窗或修复，只界定上界 | **禁止写成可部署方法精度** |
| Run ID | 一次运行的唯一编号（见 Tracker 表） | 新跑必须先登记 |

### 5.6 硬件口径

| 词 | 含义 |
|---|---|
| GTX1660SUPER | BT1／多数 BTD 测速时的本机 GPU |
| 双 4090 | **当前**可用服务器；若补测速须**单独列表**，禁止与 1660 混表 |

---

## 6. 文献与状态词

| 代号 | 含义 |
|---|---|
| W-0001 … W-0014 | 全局 Work ID；**完整题名与审计卡路径见 §10.2** |
| PASS（审计） | 文献身份／证据审计通过，**不等于**你已精读 DONE |
| SCREENED | 已过初筛／审计用途明确，本人精读未完成 |
| HOLD | 暂停／未成立／暂不推进 |
| DISMISSED | 书面否决；**不一定**等于已实测无效 |
| BLOCKED | 因门禁未开不可执行 |
| READY／RUNNING／DONE／FAILED | 实验 Tracker 运行状态 |
| PROPOSED | 主张已提出、作当前写作依据，尚未被会议／实验最终钉死 |
| PAUSED | 主线论文方向暂停 |
| DONE | 该任务／运行已完成（仍须看是否含学习验收） |

---

## 7. 方法与数据简称

| 词 | 含义 |
|---|---|
| YOLO11n | Ultralytics YOLO11 nano；本项目 BT1 固定检测器 |
| LSM-Head | Lightweight Shared 检测头方案；历史候选 |
| VisDrone | 航拍检测基准（Experiments 脚本／报告主用此写法；个别总述写作 VisDrone 时以数据包名为准） |
| UAV-RSOD | 铁路场景相关公开数据候选（历史路径，多处 HOLD） |
| SAHI／QueryDet／ESOD／MRU-YOLO 等 | 近邻方法名，见 Literature 矩阵 |
| DFL／GFLV2 | 分布焦点损失及其近邻（BTD12 相关） |
| NMS | Non-Maximum Suppression 非极大值抑制 |
| EMA | Exponential Moving Average 权重 |

---

## 8. 近程 EI 相关（2026-09-16 决定）

| 词 | 含义 |
|---|---|
| EI 稿 | 练手文会议稿目标（2027 会期待选）；不是中科院二区／Trans 承诺 |
| 协议／对比主张 | P0-EI-C1／C2：比固定设置下的输入与选区策略，不宣布新检测算法 |
| Mainline_A_Current | 近中远与口径的当前执行页 |

---

## 9. 如何更新本表

1. 新代号先写进本文件，再在 `Current_Stage`、协议或 Tracker 里使用。  
2. 新增 **BTD** 号必须同时：登记 Tracker、写 Protocol、更新本表第 5.3 节。  
3. 新增 **`W-xxxx_Audit`／`A0-*Review`／`BTDn_*Review`／`*_HOLD_Review`／`*_Candidate_Review`** 时，必须同步更新 **§10**（短称、完整题名或审查用途、路径）；聊天或笔记里首次使用该短称前也要先入库。  
4. 避免并行两套缩写（例如不要同时用 BTD／Diag 指同一诊断）。本仓库诊断统一写 **BTD**。  
5. 数字以对应 `*_Result.md`／Tracker／审计卡正文为准；本表只解释名字，不替代原始报告。

---

## 10. Literature 文件名级代号（审计卡／书面审查）

**纪律：** 凡仓库里出现 `W-xxxx_Audit`、`A0-09_*Review`、`BTD12_*Review` 这类文件名缩写／短称，**必须**在本表登记「短称 → 完整题名／用途 → 路径」。只写 W-0007 或 BTD12 而不写全称，不算完成。

路径根：`00_Practice_UAV_Aerial_Detection/Literature/`（下分 `audits/`、`reviews/`、`matrices/`）。

### 10.1 命名模式

| 文件名模式 | 完整含义 |
|---|---|
| `W-xxxx_Audit.md` | **Work 审计卡**：对注册表工作 `W-xxxx` 的身份／版本／近邻冲突书面审计；`PASS`≠精读 `DONE` |
| `A0-0x_*.md`（Experiments）或 `A0-09_*Review.md`（Literature） | **A0 阶段书面任务／候选审查**；A0-09 专指单机制候选差异与否决审查 |
| `BTDn_*_Protocol/Result/Analysis.md` | 第 n 次 **BTD** 诊断的协议／结果／分析（见 §5.3） |
| `BTD12_*Candidate*Review.md` | **BTD12 书面候选审查**（可无模型运行）；结论常为 `DISMISSED` |
| `*_HOLD_Review.md` | 对某线索的 **HOLD** 书面说明（未赋 Work ID 或暂不推进） |
| `*_Candidate_Review.md` | 机制／评分候选的可证伪边界与停止条件书面审查 |
| `Literature_Matrix.md` | 练手文文献矩阵（阅读优先级、证据摘要、创新关系） |
| `Mainline_A_Prior_Work_Comparison.md` | 主线 A 近邻对照表 |
| `Search_Log.md` | 检索式与筛选日志 |

### 10.2 `W-xxxx_Audit` → 对应工作（完整信息）

| 短称／文件 | Work ID | 常用短名 | 完整题名（审计卡登记） | 路径 |
|---|---|---|---|---|
| `W-0001_Audit` | W-0001 | UAV-RSOD／铁路分割检测数据 | An unmanned aerial vehicle captured dataset for railroad segmentation and obstacle detection | `Literature/audits/W-0001_Audit.md` |
| `W-0002_Audit` | W-0002 | SAHI | Slicing Aided Hyper Inference and Fine-tuning for Small Object Detection | `Literature/audits/W-0002_Audit.md` |
| `W-0003_Audit` | W-0003 | QueryDet | QueryDet: Cascaded Sparse Query for Accelerating High-Resolution Small Object Detection | `Literature/audits/W-0003_Audit.md` |
| `W-0004_Audit` | W-0004 | ESOD | ESOD: Efficient Small Object Detection on High-Resolution Images | `Literature/audits/W-0004_Audit.md` |
| `W-0005_Audit` | W-0005 | ROI-Gated SAHI | ROI-Gated SAHI: Content-Adaptive Slicing-Based Inference for Efficient Object Detection | `Literature/audits/W-0005_Audit.md` |
| `W-0006_Audit` | W-0006 | RVGC-YOLO | Integrated Visual Sensing and Efficient Deep Learning for UAV-Based Track Foreign Object Detection | `Literature/audits/W-0006_Audit.md` |
| `W-0007_Audit` | W-0007 | MRU-YOLO | MRU-YOLO（边际效用引导的选择性局部回看；审计卡以方法短称为题） | `Literature/audits/W-0007_Audit.md` |
| `W-0008_Audit` | W-0008 | DZN | Dynamic Zoom-in Network for Fast Object Detection in Large Images | `Literature/audits/W-0008_Audit.md` |
| `W-0009_Audit` | W-0009 | AutoFocus | AutoFocus: Efficient Multi-Scale Inference | `Literature/audits/W-0009_Audit.md` |
| `W-0010_Audit` | W-0010 | TIDE | TIDE: A General Toolbox for Identifying Object Detection Errors | `Literature/audits/W-0010_Audit.md` |
| `W-0011_Audit` | W-0011 | NWD | A Normalized Gaussian Wasserstein Distance for Tiny Object Detection | `Literature/audits/W-0011_Audit.md` |
| `W-0012_Audit` | W-0012 | Adaptive NMS | Adaptive NMS: Refining Pedestrian Detection in a Crowd | `Literature/audits/W-0012_Audit.md` |
| `W-0013_Audit` | W-0013 | GFLV2 | Generalized Focal Loss V2: Learning Reliable Localization Quality Estimation for Dense Object Detection | `Literature/audits/W-0013_Audit.md` |
| `W-0014_Audit` | W-0014 | Multivariate Conf. Calib. | Multivariate Confidence Calibration for Object Detection | `Literature/audits/W-0014_Audit.md` |

### 10.3 书面审查文件（完整信息）

| 短称／文件 | 完整含义 | 结论摘要（以正文为准） | 路径 |
|---|---|---|---|
| `A0-09_Candidate_Review`／A0-09 | A0-09：单机制候选差异与否决审查（熵／成本归一等定向检索后的候选处置） | 旧候选路线书面否决边界保留；细节见正文 | `Literature/reviews/A0-09_Candidate_Review.md` |
| `BTD12_Low_Score_Candidate_Review`／BTD12 审查 | BTD12：尺度条件 DFL 分布统计重评分候选的书面审查 | 候选 **DISMISSED**（近邻已覆盖核心关系；非实测失败） | `Literature/reviews/BTD12_Low_Score_Candidate_Review.md` |
| `ViCrop_Det_HOLD_Review`／ViCrop-Det | ViCrop-Det 线索 HOLD 审查（内部信号免训练裁剪近邻） | **HOLD**；未赋 Work ID、未当 PASS 正文 | `Literature/reviews/ViCrop_Det_HOLD_Review.md` |
| `Weak_Response_Candidate_Review`／弱响应候选 | 跨层／跨尺度弱响应选区评分候选的可证伪边界审查 | 曾 **PROPOSED**，后弱响应 v0.1 转 **HOLD**；以正文与实验诊断为准 | `Literature/reviews/Weak_Response_Candidate_Review.md` |
