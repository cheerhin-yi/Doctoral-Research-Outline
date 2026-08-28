# Paper 1最近工作与新颖性审计（2026-08-27）

## 1. 审计目的与边界

本文件回答：Paper 1原候选主张中，哪些组成已经发表，哪些只能作为待证伪实验假设。它是截至2026-08-27的第一轮公开文献核查，不等于系统综述、专利自由实施检索或“绝对无人做过”的证明。正式投稿前必须更新检索。

**状态说明（2026-08-28）**：Paper 1当前暂停，待前置论文A/B完成后重新审计。本文件只保存既有新颖性边界，不能作为当前学习或实验计划。A不得重复普通校准或距离风险，Paper 1未来不得重复A的封闭集条件校准和B的固定双视角融合。

## 2. 审计结论

- 轨道中心线/边界作为空间参照、目标到轨道距离、标准轨距换算和距离风险分级均已有铁路研究，不能单独作为创新。
- UAV铁路危险物检测、轨道解析和危险等级评估已有直接工作。
- 铁路开放集/未见类别异物检测已有直接工作；通用开放世界检测更早已形成研究方向。
- 风险概率校准和不确定性感知风险识别已有跨领域工作；Temperature Scaling、ECE和Brier不能作为方法创新。
- Paper 1可争取的最小空间是：用匹配物理场景严格比较多种空间表示，验证局部轨道宽度归一化侵界量在UAV跨高度、分辨率和轻度视角变化下是否呈现新的、可重复的稳定性finding。

## 3. 最接近工作

| ID | 工作 | 已覆盖内容 | 对Paper 1的约束 | 核验链接 |
|---|---|---|---|---|
| PA01 | Wu et al., *UAV imagery based potential safety hazard evaluation for high-speed railroad using Real-time instance segmentation*, 2023 | UAV铁路图像、轨道与危险物解析、目标到轨道距离、危险等级评价 | “UAV+轨道距离+危险分级”已发表 | https://www.sciencedirect.com/science/article/pii/S1474034622002774 |
| PA02 | *Railway Intrusion Risk Quantification with Track Semantic Segmentation and Spatiotemporal Features*, 2025 | 轨道语义分割、标准轨距空间参照、目标到轨道中心横向距离、风险量化 | 轨距/中心距离转风险已发表 | https://pmc.ncbi.nlm.nih.gov/articles/PMC12431379/ |
| PA03 | Ning et al., *Spatial Relation Reasoning Based on Keypoints for Railway Intrusion Detection and Risk Assessment*, 2026 | 目标底部关键点相对轨道边界、横向距离、运动状态、九级风险 | 轨道相对几何和风险分级已发表 | https://www.mdpi.com/2076-3417/16/6/3026 |
| PA04 | *CMF-Net: A Novel Deep Learning Framework for High-Precision and Robust Detection of Foreign Objects on Railway Tracks*, 2026 | 轨道中心线Mask、像素到中心线欧氏距离、高斯距离衰减空间先验 | 中心线距离场本身非创新 | https://www.mdpi.com/2227-7080/14/6/322 |
| PA05 | Bai et al., *ROSD: Railway intrusion object generalized detection via Open-Set Detection*, 2026 | 铁路场景开放集异物检测和未见类别泛化 | 铁路unknown/open-set检测本身非创新 | https://www.sciencedirect.com/science/article/abs/pii/S1474034625011218 |
| PA06 | Joseph et al., *Towards Open World Object Detection*, CVPR 2021 | 建立Open World Object Detection问题 | 通用OWOD不是本项目创新 | https://openaccess.thecvf.com/content/CVPR2021/html/Joseph_Towards_Open_World_Object_Detection_CVPR_2021_paper.html |
| PA07 | Fu and Chen, *Uncertainty-Aware Vision-based Risk Object Identification via Conformal Risk Tube Prediction*, 2026 | calibrated risk scores、risk uncertainty、下游安全决策 | 风险校准/不确定性本身非创新 | https://arxiv.org/abs/2603.23919 |

## 4. 当前角色：支撑风险告警的几何假设

### G1：可选几何消融

在同一物理侵界关系、不同UAV高度/分辨率/轻度视角扰动下，局部轨道宽度归一化横向侵界量相较raw pixel distance及现有铁路空间表示具有更低波动，并能更稳定地预测高风险事件。

必须比较：raw pixel、centerline distance、track-boundary/keypoint zone、standard-gauge metric distance、local-width normalization；标定可用时加入Homography/BEV。

### G2：未知候选与侵界关系的可选分析

未知度单独使用可能造成大量误报；`unknownness × clearance violation`只有在跨held-out category轮换稳定优于Unknown-only、Geometry-only和简单融合时才保留。

### G3：辅助可靠性实验

对high-risk event probability校准可能改善独立测试集上的Brier/NLL/ECE或top-k review hit rate。校准方法本身不列为贡献。

## 5. 停止/继续规则

- G1只优于raw pixel但不优于metric、boundary或BEV：降为基线复现，不称核心创新。
- G1只在普通图像缩放成立：只能声称缩放不变性，不声称跨飞行高度鲁棒性。
- G1在真值轨道几何成立、预测几何失败：报告误差传播，不隐藏上游瓶颈。
- G1没有稳定信号：删除归一化消融，采用最简单可靠的track-zone/boundary告警；Paper 1的YOLO主线继续。
- G2/G3没有跨split或复检增量：删除或放入附录，不能用工程完整性冒充创新。

## 6. 投稿前仍需完成

- 在Web of Science、Scopus、IEEE Xplore、ScienceDirect、Google Scholar及可用中文数据库重复检索并保存检索式和筛选流程。
- 补查专利、学位论文、预印本和2026年在线优先论文。
- 为每条拟写贡献制作“最近工作—相同点—不同点—证据”四列表。
- 由导师或领域研究者复核最近工作是否遗漏；任何“首次”表述须有单独证据，不默认使用。
