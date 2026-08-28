# Innovation Ledger

以下均为待验证主张或后续接口，不是已证实贡献。当前只允许前置论文A处于`testing`状态。

## I01 前置论文A：飞行条件感知风险校准

- **Status**：testing
- **Primary claim A1**：相对最佳全局校准，条件校准改善独立场景测试集的最差视角可靠性。
- **Supporting claim A2**：在相同危险Recall下减少误报。
- **Mechanism**：原始概率与高度、云台角、目标尺寸、模糊度和归一化轨道位置的轻量条件校准。
- **Strong baselines**：未校准；全局参数校准；非参数等距回归。
- **Required evidence**：NLL/Brier/ECE、worst-group ECE、固定Recall误报、变量消融、scene聚类区间和失败案例。
- **Novelty boundary**：不宣称提出校准算法、多高度检测或物理侵限测量。
- **Fallback**：无稳定收益时降级为跨飞行条件失准诊断与有效观测包络。

## I02 前置论文B：轨道坐标对齐的双视角验证

- **Status**：queued
- **Primary claim B1**：轨道坐标一致性识别错误匹配和跨视角风险冲突。
- **Supporting claim B2**：A的不确定性加权融合降低困难子集漏判。
- **Strong baselines**：首次视角、固定近视角、概率平均、confidence加权。
- **Novelty boundary**：第二视角已经存在；不研究VoI、NBV、航迹或多机分配。
- **Activation gate**：A投稿或达到内部投稿标准并冻结接口。

## I03 Paper 1：开放世界风险感知

- **Status**：paused
- **Reserved contribution**：已知/未知候选、开放世界风险、认知不确定性和轨道风险告警。
- **Boundary**：不得重复I01的封闭集条件校准或I02的固定双视角融合。
- **Activation gate**：A/B完成后重新做最近工作审计和实验计划。

## I04 M1：侵限测量可靠性

- **Status**：blocked
- **Reserved contribution**：将目标、轨道、相机和位姿误差传播为侵限距离区间、侵限概率和测量有效性。
- **Boundary**：不做稠密三维、多时相变化、体积或沉降。
- **Activation gate**：Paper 1开放世界接口稳定。

## I05 M2：风险驱动复检触发

- **Status**：blocked
- **Reserved contribution**：联合Paper 1风险和M1测量不确定性，在时间/能耗成本下决定是否复检。
- **Boundary**：不做候选视点、路径、RL或多机分配。
- **Activation gate**：Paper 1、M1接口和固定复检成本稳定。

## 更新规则

- 每篇论文最多两个主要主张；
- 新实验必须服务某个主张或排除一个反解释；
- 没有证据的内容保持`untested/queued/blocked`；
- 新颖性风险高时优先收缩、降级或删除，不通过增加模块维持故事；
- 每次状态变化记录触发文献或实验ID。
