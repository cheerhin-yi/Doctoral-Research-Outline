# T4：不确定性、校准与实验评价阅读清单

## 本主题要回答

- 检测置信度、未知分数和风险概率有什么区别？
- 哪些指标评价概率质量，哪些指标评价告警决策？
- 校准能否改善人工复核排序，还是只改善ECE？
- 如何按物理场景统计，避免把相邻帧当独立样本？

## 阅读清单

| ID | 论文 | 优先级 | 状态 | 重点阅读 | 笔记 |
|---|---|---|---|---|---|
| T4-01 | Can We Trust You? On Calibration of a Probabilistic Object Detector for Autonomous Driving | SHOULD | TODO | 检测器校准、可靠性指标 | 待核验后创建 |
| T4-02 | Uncertainty-Aware Vision-based Risk Object Identification via Conformal Risk Tube Prediction | SHOULD | TODO | 风险分数、不确定性和安全决策 | 待核验后创建 |
| T4-03 | 场景聚类统计与检测评价方法 | MUST | TODO | 独立单位、置信区间、效应量 | 待检索 |
| T4-04 | [Real-Time Source-Free Object Detection](Real-Time%20Source-Free%20Object%20Detection.pdf) | SHOULD | SCREENED | 无源域适应、域偏移、伪标签与实时约束 | 待创建 |

## 本主题完成门

- [ ] 至少3篇评价/校准核心论文完成精读；
- [ ] 能区分confidence、unknownness、risk和calibration；
- [ ] 冻结Paper 1主要指标与统计单位；
- [ ] 校准若不改变决策价值则降为附录或删除。
