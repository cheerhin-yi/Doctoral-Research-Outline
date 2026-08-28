# N06 风险推理

> 状态：LIMITED｜最近复习：待填写｜当前用途：前置论文A定义封闭集危险事件和错误成本

**当前范围（2026-08-28）**：只定义六类已知障碍的危险标签、固定危险召回率、误报率和漏判成本。不学习未知性风险、多模态融合、序数网络或复杂风险推理。

## 1. Why

学习如何定义和验证铁路高风险事件，而不是默认“语义+几何+未知性”拼接就是创新。重点识别类别捷径、侵界条件、错误成本以及最近工作已经覆盖的距离风险分级。

请填写：如果不掌握本模块，Paper 1或后续论文最可能出现什么错误？

## 2. Intuition

不用公式，用不超过200字向同学解释“风险推理”是什么。至少给出一个铁路无人机场景。

## 3. Core Concepts

- [ ] 对象分类与风险分类：用自己的话解释，并写一个反例或失败条件。
- [ ] 特征融合：用自己的话解释，并写一个反例或失败条件。
- [ ] 概率与序数分类：用自己的话解释，并写一个反例或失败条件。
- [ ] 上下文关系：用自己的话解释，并写一个反例或失败条件。
- [ ] 风险标签协议：用自己的话解释，并写一个反例或失败条件。
- [ ] 类别不平衡与Macro-F1：用自己的话解释，并写一个反例或失败条件。
- [ ] 错误成本：用自己的话解释，并写一个反例或失败条件。

## 4. Minimal Math

必须掌握：P(Risk|Semantic,Geometry,Unknownness,Context)与序数损失的基本形式。

- 公式：
- 符号与单位：
- 公式表达的直觉：
- 适用前提：
- 失效条件：

## 5. Input / Output

输入为语义/未知分数、铁路几何和上下文；输出为风险等级或概率及解释字段。

请补充输入、输出、形状/单位、必需假设和异常状态。

## 6. Code

实现Semantic only、Geometry only和融合基线，统一输出混淆矩阵。

- 代码或Notebook位置：
- 环境与版本：
- 最小运行命令：
- 输出证据：

## 7. Railway Example

同一石块在轨外20米与钢轨之间对应完全不同风险。

请画出或描述数据流，并说明普通场景结论为何不能直接迁移到铁路UAV。

## 8. Paper Connection

前置论文A只使用最小风险映射评价校准是否在固定危险召回率下降低误报。Paper 1恢复后再扩展到未知候选和轨道上下文风险，不在A中构造风险网络。

- 对应论文模块：
- 本模块输出给谁：
- 仍未冻结的接口：

## 9. Classic Papers

仅在核验原文后填写。

| Title | Year | Venue | 解决问题 | 我必须读的章节 | 核验链接 |
|---|---:|---|---|---|---|
| UAV imagery based potential safety hazard evaluation for high-speed railroad using Real-time instance segmentation | 2023 | Advanced Engineering Informatics | UAV铁路危险物距离分级 | 高：UAV+距离风险已发表 | https://www.sciencedirect.com/science/article/pii/S1474034622002774 |
| Spatial Relation Reasoning Based on Keypoints for Railway Intrusion Detection and Risk Assessment | 2026 | Applied Sciences | 轨道关系、运动状态与九级风险 | 高：空间风险推理已有直接工作 | https://www.mdpi.com/2076-3417/16/6/3026 |

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

- [ ] 风险标签的证据依据是什么？
  - 我的回答：
  - 证据或例子：
- [ ] Unknown对象为何仍可判断风险？
  - 我的回答：
  - 证据或例子：
- [ ] 怎样避免风险模型只记住对象类别？
  - 我的回答：
  - 证据或例子：

新增问题：

## 14. Mini Experiment

固定检测预测与风险定义，比较未校准和校准后的危险筛查，在相同危险Recall下报告误报率。轨道上下文、未知候选和复杂风险融合实验留给Paper 1。

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

- [ ] 风险标签的证据依据是什么？
  - 我的回答：
  - 证据或例子：
- [ ] Unknown对象为何仍可判断风险？
  - 我的回答：
  - 证据或例子：
- [ ] 怎样避免风险模型只记住对象类别？
  - 我的回答：
  - 证据或例子：
