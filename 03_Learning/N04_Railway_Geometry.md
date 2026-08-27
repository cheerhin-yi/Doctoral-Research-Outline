# N04 铁路几何

> 状态：未开始｜最近复习：待填写｜对应研究周：见弹性研究周计划

## 1. Why

理解并公平比较像素、中心线、轨道边界、标准轨距物理距离、局部宽度归一化和BEV等铁路空间表示。中心线和归一化几何已有先例，本模块学习目标不是“发明坐标”，而是判断每种表示的前提、稳定性和误差来源。

请填写：如果不掌握本模块，Paper 1或后续论文最可能出现什么错误？

## 2. Intuition

不用公式，用不超过200字向同学解释“铁路几何”是什么。至少给出一个铁路无人机场景。

## 3. Core Concepts

- [ ] 图像坐标与铁路坐标：用自己的话解释，并写一个反例或失败条件。
- [ ] 纵向与横向位置：用自己的话解释，并写一个反例或失败条件。
- [ ] 归一化横向距离：用自己的话解释，并写一个反例或失败条件。
- [ ] 方向、重叠和相对尺度：用自己的话解释，并写一个反例或失败条件。
- [ ] 内外参、透视与Homography最小知识：用自己的话解释，并写一个反例或失败条件。
- [ ] 几何不确定性：用自己的话解释，并写一个反例或失败条件。

## 4. Minimal Math

必须掌握：`d_norm=(x_object-c(y))/w(y)`、标准轨距换算、坐标投影和误差传播。能推导该比值在局部相似缩放/平移下消去尺度项，同时明确这不能证明其对任意透视、弯道、道岔或分割误差保持不变。

- 公式：
- 符号与单位：
- 公式表达的直觉：
- 适用前提：
- 失效条件：

## 5. Input / Output

输入为目标框/Mask和铁路Mask/中心线；输出为纵向位置、归一化横向偏移、重叠、相对尺度与有效性标记。

请补充输入、输出、形状/单位、必需假设和异常状态。

## 6. Code

实现raw pixel、centerline、track-boundary、metric-gauge和local-width-normalized表示并生成对比图；相机标定可用时再加入Homography/BEV。

- 代码或Notebook位置：
- 环境与版本：
- 最小运行命令：
- 输出证据：

## 7. Railway Example

优先比较同一障碍物、同一物理侵界位置在不同真实/可信高度、分辨率和轻度视角下的表示；普通图像缩放只能验证缩放性质，不能代替无人机高度变化。

请画出或描述数据流，并说明普通场景结论为何不能直接迁移到铁路UAV。

## 8. Paper Connection

Paper 1核心假设H1与空间表示比较协议；向Paper 2输出经实验证据选择的空间表示，而不是预设归一化方案胜出。

- 对应论文模块：
- 本模块输出给谁：
- 仍未冻结的接口：

## 9. Classic Papers

仅在核验原文后填写。

| Title | Year | Venue | 解决问题 | 我必须读的章节 | 核验链接 |
|---|---:|---|---|---|---|
| Railway Intrusion Risk Quantification with Track Semantic Segmentation and Spatiotemporal Features | 2025 | Sensors | 使用标准轨距和轨道中心横向距离量化风险 | 高：轨距/中心距离已发表 | https://pmc.ncbi.nlm.nih.gov/articles/PMC12431379/ |
| Spatial Relation Reasoning Based on Keypoints for Railway Intrusion Detection and Risk Assessment | 2026 | Applied Sciences | 使用轨道边界、关键点和横向距离分级风险 | 高：轨道相对风险已发表 | https://www.mdpi.com/2076-3417/16/6/3026 |

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

- [ ] 铁路宽度如何定义且何时不可见？
  - 我的回答：
  - 证据或例子：
- [ ] 中心线误差会怎样传导到风险判断？
  - 我的回答：
  - 证据或例子：
- [ ] 何时必须升级到相机标定或世界坐标？
  - 我的回答：
  - 证据或例子：
- [ ] 为什么“数学上缩放不变”不等于“真实UAV跨高度稳定”？
  - 我的回答：
  - 证据或例子：

新增问题：

## 14. Mini Experiment

先用解析推导和合成相似变换做sanity check，再在匹配物理场景中比较raw pixel、centerline、boundary、metric-gauge、local-width normalization及可用BEV。分开报告真值轨道几何和预测轨道几何，防止分割误差混入表示比较。

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

- [ ] 铁路宽度如何定义且何时不可见？
  - 我的回答：
  - 证据或例子：
- [ ] 中心线误差会怎样传导到风险判断？
  - 我的回答：
  - 证据或例子：
- [ ] 何时必须升级到相机标定或世界坐标？
  - 我的回答：
  - 证据或例子：
