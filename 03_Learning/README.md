# 学习框架指南

**当前项目**：前置论文A——飞行条件感知风险校准  
**当前周**：第1周——文献证据与研究边界  
**投入上限**：每周8–10小时，至少一天完全休息

本目录不是需要依次学完的课程列表。每个模块只有在当前研究问题触发时才学习；没有启动的模块不是欠账。

## 1. 当前学习目标

前置论文A只需要建立两条能力链：

1. 判断检测confidence在不同飞行条件下是否可靠；
2. 用无泄漏、可复现的实验验证条件校准是否改善最差视角和危险筛查。

因此当前核心是N07和N08。检测、轨道和风险知识只补到能完成校准输入与评价；开放世界、三维测量、通信、优化、强化学习和主动视点全部延后。

## 2. 模块状态

| 模块 | 在最新研究链中的职责 | 状态 | 何时使用 |
|---|---|---|---|
| [N07 不确定性与校准](N07_Uncertainty_and_Calibration.md) | A的核心方法和指标；B的视角权重 | **ACTIVE / MUST** | 第1–12周 |
| [N08 科研实验与评价](N08_Research_Experiment_and_Evaluation.md) | scene级划分、主张—证据、统计和复现 | **ACTIVE / MUST** | 第1–20周 |
| [N02 目标检测核心](N02_Object_Detection_Core.md) | 读取冻结检测输出、confidence、Recall和误报 | LIMITED | 第2–6周按需 |
| [N01 PyTorch科研能力](N01_PyTorch_for_Research.md) | 运行校准脚本、固定种子和保存结果 | LIMITED | 第2–7周按需 |
| [N04 铁路几何](N04_Railway_Geometry.md) | A的归一化位置；B的固定双视角坐标 | LIMITED | 第2–18周按需 |
| [N06 风险推理](N06_Risk_Reasoning.md) | A的封闭集危险定义和错误成本 | LIMITED | 第2、8周按需 |
| [N03 铁路场景解析](N03_Railway_Scene_Parsing.md) | 缺少轨道ROI时提供最低成本输入 | CONDITIONAL | 数据确实缺失时 |
| [N05 开放世界感知](N05_Open_World_Perception.md) | Paper 1未知候选 | PAUSED | A/B完成后 |
| [N09 无线通信](N09_Wireless_Communication_for_AI.md) | Paper 3/4/7通信基础 | PAUSED | Paper 3启动前 |
| [N10 优化](N10_Optimization_Core.md) | M2及Paper 3–7的决策形式化 | PAUSED | 出现明确变量/目标/约束后 |
| [N11 语义通信](N11_Task_Oriented_Semantic_Communication.md) | Paper 3 | PAUSED | N09完成且Paper 3模型冻结后 |
| [N12 ISAC](N12_ISAC_Core.md) | Paper 4 | PAUSED | Paper 3通信模型可用后 |
| [N13 单智能体RL](N13_RL_for_UAV_Communication.md) | Paper 4/6/7候选方法 | PAUSED / OPTIONAL | 规则和优化基线不足时 |
| [N14 MARL](N14_MARL_for_Multi_UAV.md) | Paper 7候选方法 | PAUSED / OPTIONAL | Paper 3–6模块稳定后 |
| [N15 GNN](N15_GNN_for_UAV_Networks.md) | Paper 7动态图候选方法 | PAUSED / OPTIONAL | 动态图不可替代时 |
| [N16 主动感知](N16_Active_Perception.md) | Paper 6视点、航迹和执行 | PAUSED | M2完成是否复检接口后 |

## 3. 前置论文A学习顺序

### 第1周：N07＋N08

只学习：

- confidence、probability、risk、calibration的区别；
- NLL、Brier、ECE和可靠性图回答什么问题；
- 全局平均为何会掩盖最差飞行条件；
- scene级划分为何不同于随机帧划分；
- 主张、基线、成功标准和失败解释如何对应。

交付物：20篇证据矩阵、3张论文卡片、一页A—Paper 1—M1重叠图。

### 第2周：N07＋N08，必要时N01

只学习：

- 手算NLL、Brier和ECE；
- 温度缩放的输入、参数、校准集和测试集；
- 逻辑校准与等距回归的适用条件；
- 场景聚类Bootstrap；
- 复现实验的种子、配置和输出记录。

交付物：指标手算、温度缩放小复现、字段与划分冻结、A-E01至A-E06运行顺序。

### 第3–10周：按实验缺口学习

- N01：只在不会运行或调试校准脚本时使用；
- N02：只在不理解冻结检测输出或分层指标时使用；
- N03：只在没有轨道ROI/边界输入时使用；
- N04：只实现归一化轨道相对位置和有效性；
- N06：只定义危险标签、固定Recall和误报成本；
- N07/N08持续用于方法、消融、统计和失败分析。

### 第11–12周：写作回查

只回查论文中真正出现的概念、公式、指标和实验，不新开学习模块。

### 第13–20周：前置论文B

激活N04、N07、N08中与固定双视角对齐、一致性、冲突和不确定性加权融合直接相关的部分。仍不激活N05、N10、N13、N14、N16。

## 4. 每个模块的使用方法

打开模块前先回答：

- 当前周哪项任务需要它？
- 只需要其中哪几个概念？
- 结束时留下什么证据？
- 哪些内容属于后续论文，必须停止？

学习输出只能是以下一种或多种：

- 用自己的话写出的概念解释；
- 一次公式或指标手算；
- 一个小型可重复练习；
- 一张论文卡片；
- 一个已登记的实验设计或结果。

不以课程时长、视频数量或填满整篇笔记作为完成标准。

## 5. 当前明确删除的学习内容

前置论文A/B二十周内不学习或实现：

- 开放集、开放词汇、OWOD和未知目标模型；
- YOLO结构创新、RT-DETR对照和大规模检测器调参；
- 物理侵限距离、完整相机模型、RTK/GCP误差传播；
- SfM、MVS、SLAM、点云和多时相三维；
- 正式VoI、强化学习、NBV、航迹和避障；
- 多无人机分配、无线通信、语义通信、ISAC和GNN。

这些内容不是永久删除，而是从当前学习计划删除，只有对应启动门槛满足后才重新建立学习任务。

## 6. 学习完成门

一项当前学习任务只有同时满足以下条件才算完成：

1. 能闭卷解释概念和适用前提；
2. 有公式检查、代码输出、文献卡片或实验文件；
3. 能指出它服务A1还是A2；
4. 能说明至少一个失效条件；
5. 没有提前占用Paper 1、M1、M2、Paper 2或Paper 6的创新范围。

## 7. 当前第一步

现在只打开：

1. [N07 不确定性与校准](N07_Uncertainty_and_Calibration.md)；
2. [N08 科研实验与评价](N08_Research_Experiment_and_Evaluation.md)；
3. [前置论文文献矩阵](../00_Project/PrePaper_Literature_and_Venue_Matrix.md)。

其他学习模块暂时关闭。
