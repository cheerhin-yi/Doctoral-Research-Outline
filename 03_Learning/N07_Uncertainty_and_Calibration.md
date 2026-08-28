# N07 不确定性与校准

> 状态：ACTIVE / MUST｜最近复习：待填写｜对应阶段：前置论文A第1–12周

**当前范围（2026-08-28）**：这是前置论文A的核心学习模块。必须掌握全局与条件校准、独立校准集、最差视角评价、NLL/Brier/ECE、可靠性图，以及温度缩放、逻辑校准和等距回归。深度集成、贝叶斯网络和开放世界认知不确定性延后。

## 1. Why

避免把检测confidence误当作风险概率，并检验高度、云台角、目标像素尺寸、模糊度和轨道相对位置能否解释条件失准。校准算法本身不是创新；前置论文A的候选贡献是飞行条件感知的风险校准问题、紧凑实现和最差视角证据。

请填写：如果不掌握本模块，Paper 1或后续论文最可能出现什么错误？

## 2. Intuition

不用公式，用不超过200字向同学解释“不确定性与校准”是什么。至少给出一个铁路无人机场景。

## 3. Core Concepts

- [ ] Predictive uncertainty：用自己的话解释，并写一个反例或失败条件。
- [ ] Aleatoric与Epistemic区别：用自己的话解释，并写一个反例或失败条件。
- [ ] Entropy：用自己的话解释，并写一个反例或失败条件。
- [ ] Calibration：用自己的话解释，并写一个反例或失败条件。
- [ ] Temperature Scaling：用自己的话解释，并写一个反例或失败条件。
- [ ] NLL、ECE与Brier Score：用自己的话解释，并写一个反例或失败条件。
- [ ] Reliability Diagram：用自己的话解释，并写一个反例或失败条件。
- [ ] 全局校准与条件/分组校准：说明平均改善为何可能掩盖最差视角失效。
- [ ] Calibration/Test隔离：说明为什么测试集不能拟合校准参数或选择阈值。
- [ ] 分布外失效：用自己的话解释，并写一个反例或失败条件。

## 4. Minimal Math

必须掌握：NLL、Brier Score、ECE分箱、温度缩放、最差组ECE及其适用前提。熵和开放世界认知不确定性当前只需知道边界。

- 公式：
- 符号与单位：
- 公式表达的直觉：
- 适用前提：
- 失效条件：

## 5. Input / Output

输入为未校准logits/概率与真实标签；输出为校准参数、校准概率和可靠性指标。

请补充输入、输出、形状/单位、必需假设和异常状态。

## 6. Code

实现Temperature Scaling、ECE、Brier和Reliability Diagram。

- 代码或Notebook位置：
- 环境与版本：
- 最小运行命令：
- 输出证据：

## 7. Railway Example

高风险且高不确定的疑似滑坡应触发复核，而非直接作确定结论。

请画出或描述数据流，并说明普通场景结论为何不能直接迁移到铁路UAV。

## 8. Paper Connection

前置论文A的核心模块：比较未校准、全局校准和条件校准，并输出`calibrated_risk`、`view_uncertainty`和`observation_valid`。Paper 1未来接收该可靠性经验，但必须另有开放世界贡献。

- 对应论文模块：
- 本模块输出给谁：
- 仍未冻结的接口：

## 9. Classic Papers

仅在核验原文后填写。

| Title | Year | Venue | 解决问题 | 我必须读的章节 | 核验链接 |
|---|---:|---|---|---|---|
| Uncertainty-Aware Vision-based Risk Object Identification via Conformal Risk Tube Prediction | 2026 | arXiv | calibrated risk score、risk uncertainty和下游安全决策 | 高：风险校准/不确定性已覆盖 | https://arxiv.org/abs/2603.23919 |
| Can We Trust You? On Calibration of a Probabilistic Object Detector for Autonomous Driving | 2019 | arXiv | 安全场景概率检测器校准 | 中：校准基础近邻 | https://arxiv.org/abs/1909.12358 |

## 10. Recent Papers

范围为2024年至当前；标题、年份、出处和链接全部核验后再移除“待核验”。

| Title | Year | Venue | 与本项目关系 | 新颖性冲突 | 核验链接 |
|---|---:|---|---|---|---|
| 待核验 |  |  |  |  |  |
| 待核验 |  |  |  |  |  |

## 11. My Understanding

- 我现在能独立解释的是：
- 我最容易混淆的是：
- 与上次相比，我改变的理解是：
- 不看资料写出的三句话总结：

## 12. Failure / Limitation

- 数据失效条件：
- 模型/方法失效条件：
- 指标可能误导的情况：
- 铁路部署限制：

## 13. Open Questions

- [ ] 置信度、风险概率和校准后可信度有何区别？
  - 我的回答：
  - 证据或例子：
- [ ] 为什么温度只能在验证集拟合？
  - 我的回答：
  - 证据或例子：
- [ ] ECE下降但任务召回下降意味着什么？
  - 我的回答：
  - 证据或例子：

新增问题：

## 14. Mini Experiment

先在小表上手算NLL/Brier/ECE并复现温度缩放；正式实验比较未校准、全局温度缩放、逻辑校准、等距回归和条件校准，报告总体及最差视角指标。只有随机性影响核心结论时才运行3个种子。

- Hypothesis：
- Independent Variable：
- Control：
- Baseline：
- Dataset/Split：
- Metrics：
- Success Criterion：
- Failure Interpretation：
- 代码、配置和结果位置：

## 复习卡片

| 卡片 | 正面问题 | 背面答案 | D1 | D3 | D7 | D14 |
|---|---|---|---|---|---|---|
| 1 | 本模块最核心概念是什么？ | 待填写 | ☐ | ☐ | ☐ | ☐ |
| 2 | 最小公式及其前提是什么？ | 待填写 | ☐ | ☐ | ☐ | ☐ |
| 3 | 它如何服务铁路无人机论文？ | 待填写 | ☐ | ☐ | ☐ | ☐ |

## 自测

- [ ] 置信度、风险概率和校准后可信度有何区别？
  - 我的回答：
  - 证据或例子：
- [ ] 为什么温度只能在验证集拟合？
  - 我的回答：
  - 证据或例子：
- [ ] ECE下降但任务召回下降意味着什么？
  - 我的回答：
  - 证据或例子：
