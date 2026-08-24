# Paper 7：通信—感知约束下多无人机协同应急决策

## 核心科学问题

在通信受限、感知不确定和灾害动态变化下，谁去哪里、看什么、传什么和执行什么？

## 候选创新

- 异构Search/Verification/Relay/RF角色（待文献与实验核验）
- Communication + Risk + Uncertainty + Task联合状态（待文献与实验核验）
- MAPPO/GNN/层次规划候选（待文献与实验核验）

## 输入

位置、电量、信道、传感器、风险、不确定性、任务和动态通信图。

## 输出

move/inspect/sense/transmit/relay/return联合决策。

## 前置依赖与启动门槛

Paper 3–6形成稳定模块；N13–N15完成；评价环境能够报告风险降低、任务、时延、能量和通信成本。

## 当前明确延后

本16周不构造MARL环境或比较PPO与路径算法。

## 待办

- [ ] 在真正启动前联网核验最新Closest Work与Novelty Risk。
- [ ] 冻结问题、主张和最小证据后再设计实验。
- [ ] 检查与前后论文接口，避免形成孤立课题。
