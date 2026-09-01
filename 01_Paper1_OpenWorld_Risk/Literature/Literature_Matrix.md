# Paper 1文献矩阵

本矩阵只保存“索引＋证据＋与Paper 1的关系”。详细阅读过程写入对应主题目录中的单篇笔记。

## 1. 主题与状态

| 主题 | 内容 | 对应主张 |
|---|---|---|
| T1 | 铁路UAV、YOLO、小目标和实时检测 | C1已知检测基础 |
| T2 | open-set、open-vocabulary、open-world和未知候选 | C1未知路径 |
| T3 | 轨道区域、侵界关系和风险告警 | C2 |
| T4 | 不确定性、校准、告警预算和实验评价 | C1/C2支撑 |

状态：`TODO`未核验；`SCREENED`已核验元数据/摘要；`READING`精读中；`DONE`笔记和矩阵均完成；`EXCLUDED`已记录排除理由。

## 2. 核心论文索引

| ID | 主题 | 年份 | 论文 | 状态 | 优先级 | 单篇笔记 |
|---|---|---:|---|---|---|---|
| T1-01 | T1/T3 | 2023 | UAV imagery based potential safety hazard evaluation for high-speed railroad using Real-time instance segmentation | SCREENED | MUST | 待创建于T1；T3引用同一笔记 |
| T1-04 | T1 | 2025 | CSEANet: Cross-Stage Enhanced Aggregation Network for Detecting Surface Bolt Defects in Railway Steel Truss Bridges | SCREENED | MUST | 待创建 |
| T2-01 | T2 | 2026 | ROSD: Railway intrusion object generalized detection via Open-Set Detection | SCREENED | MUST | 待创建 |
| T2-02 | T2 | 2021 | Towards Open World Object Detection | SCREENED | MUST | 待创建 |
| T2-03 | T2 | 2025 | OW-OVD: Unified Open World and Open Vocabulary Object Detection | SCREENED | MUST | 待创建 |
| T2-05 | T2 | 2025 | YOLOE: Real-Time Seeing Anything | SCREENED | MUST | 待创建 |
| T2-06 | T2 | 2025 | YOLO-IOD: Towards Real-Time Incremental Object Detection | SCREENED | SHOULD | 待创建 |
| T2-07 | T2 | 2026 | NegAS: Negative Label Guided Attention and Scoring for Out-of-Distribution Object Detection with Vision-Language Models | SCREENED | MUST | 待创建 |
| T3-02 | T3 | 2025 | Railway Intrusion Risk Quantification with Track Semantic Segmentation and Spatiotemporal Features | SCREENED | MUST | 待创建 |
| T3-03 | T3 | 2026 | Spatial Relation Reasoning Based on Keypoints for Railway Intrusion Detection and Risk Assessment | SCREENED | MUST | 待创建 |
| T4-01 | T4 | 2019 | Can We Trust You? On Calibration of a Probabilistic Object Detector for Autonomous Driving | TODO | SHOULD | 元数据待核验 |
| T4-02 | T4 | 2026 | Uncertainty-Aware Vision-based Risk Object Identification via Conformal Risk Tube Prediction | TODO | SHOULD | 元数据待核验 |
| T4-04 | T4 | 2026 | Real-Time Source-Free Object Detection | SCREENED | SHOULD | 待创建 |

## 3. 证据与新颖性矩阵

| ID | 已覆盖的问题/方法 | 需要从原文提取的证据 | 对Paper 1的约束或用途 | 对C1/C2关系 | 冲突等级 |
|---|---|---|---|---|---|
| T1-01 | UAV铁路图像、轨道/危险物解析、距离和危险等级 | 数据、split、检测/分割指标、实时性、危险规则 | “UAV＋轨道距离＋危险分级”不能单独作为创新；可作为系统基线 | C1基础；挑战C2新颖性 | 高 |
| T1-04 | UAV铁路桥螺栓小目标检测、跨阶段聚合与滑窗增强 | 数据、目标尺度、结构变量、消融、速度 | 约束铁路UAV已知检测和结构改动的新颖性 | C1已知检测基础 | 中/高 |
| T2-01 | 铁路场景开放集异物检测 | Known/Unknown协议、基线、未知指标、误报和泛化 | “铁路未知目标检测”不能单独作为创新，C1必须证明新的任务价值 | 直接挑战C1 | 高 |
| T2-02 | 通用开放世界目标检测定义与协议 | 任务定义、A-OSE/Wilderness Impact、增量设置 | Paper 1必须准确使用open-world术语 | 支撑C1评价 | 中 |
| T2-03 | 统一开放世界与开放词汇检测 | 预训练、提示、数据、现代基线与指标 | 开放词汇预训练知识必须公平报告 | C1强基线候选 | 中 |
| T2-05 | 实时开放词汇、提示式检测和分割 | 预训练、提示类型、零样本协议、速度 | 可作为现代实时开放词汇强基线；不能与无预训练方法直接横比 | C1强基线候选 | 高 |
| T2-06 | 实时增量目标检测与持续学习 | 任务序列、旧类遗忘、数据保留和指标 | 用于明确“增量检测”不等于“未知检测” | C1术语与协议边界 | 中 |
| T2-07 | 负标签引导的VLM OOD目标评分 | 负提示构造、未知分数、OOD协议、误报 | 直接候选未知路径；需验证铁路域和告警预算下价值 | 直接挑战/支撑C1 | 高 |
| T3-02 | 轨道分割、标准轨距、横向距离和风险量化 | 数据、几何公式、误差、风险指标 | 轨距/中心距离风险已有直接工作 | 直接挑战C2 | 高 |
| T3-03 | 轨道边界关键点、横向距离和风险等级 | 关键点、距离、风险标签、场景结果 | 轨道相对几何和风险分级不能重复宣称 | 直接挑战C2 | 高 |
| T4-01 | 概率检测器校准 | 校准位置、ECE/Brier/NLL、数据划分 | 校准只能是可靠性工具，不能默认作为创新 | 支撑评价 | 中 |
| T4-02 | 风险分数与不确定性用于安全决策 | 风险定义、覆盖/校准、下游决策收益 | 风险不确定性已有近邻；必须证明铁路告警增量 | 挑战C2支撑方法 | 中/高待核验 |
| T4-04 | 无源实时目标检测域适应 | 目标域假设、伪标签、速度和域偏移结果 | 作为域偏移背景，不能替代开放世界未知评价 | C1/T4稳健性支撑 | 低/中 |

## 4. 与主张的证据链

### C1：已知＋未知双路径提高危险召回

| 链条 | 当前状态 | 需要补什么 |
|---|---|---|
| 最近工作 | T2-01直接近邻；T2-02/T2-03通用强基线 | 精读协议和真实缺口 |
| 尚存缺口 | 待确认是否缺少“固定告警预算下的铁路危险召回” | 检索告警预算/复核负担工作 |
| 拟采用方法 | YOLO已知检测＋一个未知候选强基线 | 阶段2后冻结 |
| 最低证据 | 两组Unknown轮换、Known性能、Unknown Recall、FPR和告警预算曲线 | 从近邻论文提取同类指标 |

### C2：轨道上下文提高未知危险告警价值

| 链条 | 当前状态 | 需要补什么 |
|---|---|---|
| 最近工作 | T1-01、T3-02、T3-03已覆盖距离/边界/风险 | 精读其风险标签和评价方式 |
| 尚存缺口 | 待确认是否缺少“未知候选＋轨道上下文＋告警排序” | 检索组合近邻和风险排序工作 |
| 拟采用方法 | 最简单track-zone/boundary规则或最小融合 | 不预设复杂网络 |
| 最低证据 | 固定高风险Recall下降低告警数，或固定预算提高命中 | 提取近邻可比指标 |

## 5. 当前缺口清单

- [ ] T1补足铁路UAV小目标检测和YOLO强基线；
- [ ] T2补足铁路开放词汇、开放集与异常候选最近工作；
- [ ] T3补足未知候选和轨道风险联合筛查；
- [ ] T4补足告警预算、复核排序和场景聚类统计；
- [ ] 至少15篇直接相关论文完成核验，其中最近三年不少于10篇；
- [ ] 所有MUST论文建立单篇笔记并回链；
- [ ] C1/C2若找不到真实缺口，修改或删除后才能进入数据阶段。

## 6. 原文入口

| ID | 原文链接 | 元数据核验 |
|---|---|---|
| T1-01 | https://www.sciencedirect.com/science/article/pii/S1474034622002774 | 投稿前复核 |
| T1-04 | [仓库PDF](01_Railway_UAV_Detection/CSEANet%20-%20Cross-Stage%20Enhanced%20Aggregation%20Network%20for%20Detecting%20Surface%20Bolt%20Defects%20in%20Railway%20Steel%20Truss%20Bridges.pdf) | 已初筛；正式元数据待精读核验 |
| T2-01 | https://www.sciencedirect.com/science/article/abs/pii/S1474034625011218 | 投稿前复核 |
| T2-02 | https://openaccess.thecvf.com/content/CVPR2021/html/Joseph_Towards_Open_World_Object_Detection_CVPR_2021_paper.html | 已初步核验 |
| T2-03 | https://openaccess.thecvf.com/content/CVPR2025/html/Xi_OW-OVD_Unified_Open_World_and_Open_Vocabulary_Object_Detection_CVPR_2025_paper.html | 投稿前复核 |
| T2-05 | [仓库PDF](02_Open_World_Detection/YOLOE%20-%20Real-Time%20Seeing%20Anything.pdf) | 已初筛；正式元数据待精读核验 |
| T2-06 | [仓库PDF](02_Open_World_Detection/YOLO-IOD%20-%20Towards%20Real-Time%20Incremental%20Object%20Detection.pdf) | 已初筛；正式元数据待精读核验 |
| T2-07 | [仓库PDF](02_Open_World_Detection/NegAS%20-%20Negative%20Label%20Guided%20Attention%20and%20Scoring%20for%20Out-of-Distribution%20Object%20Detection%20with%20Vision-Language%20Models.pdf) | 已初筛；正式元数据待精读核验 |
| T3-02 | https://pmc.ncbi.nlm.nih.gov/articles/PMC12431379/ | 投稿前复核 |
| T3-03 | https://www.mdpi.com/2076-3417/16/6/3026 | 投稿前复核 |
| T4-01 | https://arxiv.org/abs/1909.12358 | 待核验正式版本 |
| T4-02 | https://arxiv.org/abs/2603.23919 | 待核验 |
| T4-04 | [仓库PDF](04_Uncertainty_and_Evaluation/Real-Time%20Source-Free%20Object%20Detection.pdf) | 已初筛；正式元数据待精读核验 |
