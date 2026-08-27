# N05 开放世界感知

> 状态：未开始｜最近复习：待填写｜对应研究周：见弹性研究周计划

## 1. Why

严格区分未知发现、开放词汇识别与异常检测，建立无泄漏评价；同时认识到通用OWOD和铁路开放集异物检测已有工作，Paper 1不能把“检测未知类别”本身作为创新。

请填写：如果不掌握本模块，Paper 1或后续论文最可能出现什么错误？

## 2. Intuition

不用公式，用不超过200字向同学解释“开放世界感知”是什么。至少给出一个铁路无人机场景。

## 3. Core Concepts

- [ ] Closed-set：用自己的话解释，并写一个反例或失败条件。
- [ ] Open-set：用自己的话解释，并写一个反例或失败条件。
- [ ] Open-vocabulary：用自己的话解释，并写一个反例或失败条件。
- [ ] Open-world：用自己的话解释，并写一个反例或失败条件。
- [ ] Anomaly Detection：用自己的话解释，并写一个反例或失败条件。
- [ ] CLIP共同语义空间：用自己的话解释，并写一个反例或失败条件。
- [ ] Grounding DINO与YOLO-World：用自己的话解释，并写一个反例或失败条件。
- [ ] Unknown score与Known/Unknown轮换：用自己的话解释，并写一个反例或失败条件。

## 4. Minimal Math

必须掌握：相似度、能量/未知分数、AUROC、FPR95、A-OSE与Wilderness Impact的定义条件。

- 公式：
- 符号与单位：
- 公式表达的直觉：
- 适用前提：
- 失效条件：

## 5. Input / Output

输入为图像、已知类别集合和可选文本提示；输出为已知预测、未知候选、未知分数和评价。

请补充输入、输出、形状/单位、必需假设和异常状态。

## 6. Code

生成Known/Unknown划分清单并验证未知类别及增强版本未进入训练集。

- 代码或Notebook位置：
- 环境与版本：
- 最小运行命令：
- 输出证据：

## 7. Railway Example

未知落石、工具、动物或灾害碎片即使无法命名，也可能因侵入轨道而高风险。

请画出或描述数据流，并说明普通场景结论为何不能直接迁移到铁路UAV。

## 8. Paper Connection

Paper 1的H2条件扩展和必要基线。只有`unknownness × clearance violation`相对Unknown-only、Geometry-only和简单融合跨类别轮换稳定改善时，H2才保留。

- 对应论文模块：
- 本模块输出给谁：
- 仍未冻结的接口：

## 9. Classic Papers

仅在核验原文后填写。

| Title | Year | Venue | 解决问题 | 我必须读的章节 | 核验链接 |
|---|---:|---|---|---|---|
| ROSD: Railway intrusion object generalized detection via Open-Set Detection | 2026 | Advanced Engineering Informatics | 铁路场景开放集异物检测直接近邻 | 高：铁路open-set已发表 | https://www.sciencedirect.com/science/article/abs/pii/S1474034625011218 |
| OW-OVD: Unified Open World and Open Vocabulary Object Detection | 2025 | CVPR | 统一开放世界与开放词汇检测 | 中：通用方法基线 | https://openaccess.thecvf.com/content/CVPR2025/html/Xi_OW-OVD_Unified_Open_World_and_Open_Vocabulary_Object_Detection_CVPR_2025_paper.html |

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

- [ ] Open-set、Open-vocabulary、Open-world和异常检测各解决什么？
  - 我的回答：
  - 证据或例子：
- [ ] 对象性与未知性怎样区分？
  - 我的回答：
  - 证据或例子：
- [ ] 随机train/test为何不能支持Open-World主张？
  - 我的回答：
  - 证据或例子：
- [ ] 未知为什么不等于危险，什么clearance条件才使未知度与风险相关？
  - 我的回答：
  - 证据或例子：

新增问题：

## 14. Mini Experiment

构造三组类别轮换并验证哈希无交叉；在小样本上比较Unknown-only、Geometry-only、简单融合和`unknownness × clearance violation`，主要检查误报定义和评价代码，不预设H2成立。

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

- [ ] Open-set、Open-vocabulary、Open-world和异常检测各解决什么？
  - 我的回答：
  - 证据或例子：
- [ ] 对象性与未知性怎样区分？
  - 我的回答：
  - 证据或例子：
- [ ] 随机train/test为何不能支持Open-World主张？
  - 我的回答：
  - 证据或例子：
