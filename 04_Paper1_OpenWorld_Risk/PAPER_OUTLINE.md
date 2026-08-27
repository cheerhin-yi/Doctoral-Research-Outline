# Paper 1论文提纲

## Abstract

问题、方法主张、数据/协议、经冻结表格支持的关键结果、边界。没有结果前只保留结构，不填写数字。

## 1. Introduction

铁路UAV成像高度/分辨率/视角变化 → 像素距离不稳定问题 → 已有轨道中心/边界、轨距和距离风险方法 → 尚缺的公平跨条件表示比较 → H1及其可证伪条件 → H2/H3仅作为有证据时保留的扩展。

## 2. Related Work

Railway UAV Hazard Evaluation；Track-Relative/Metric/BEV Geometry；Railway Open-Set Detection；Risk Probability and Calibration。必须用“已有能力—剩余缺口—本研究不重复什么”组织，而不是罗列模块。

## 3. Problem Formulation

定义同一物理侵界关系、成像条件、pixel/centerline/boundary/metric-gauge/local-width-normalized/BEV表示、稳定性、风险事件和评价条件；未知性与校准作为条件变量。

## 4. Method

Experimental Framework；Railway Scene Parsing；Compared Spatial Representations；Controlled Imaging-Condition Protocol；Risk Predictor。Unknown-Conditioned Scoring和Calibration仅在H2/H3通过创新门时保留；不把通用模块包装成新架构。

## 5. Experiments

Dataset/Scene Audit；Matched-Scene Imaging Conditions；Spatial Representation Baselines；Stability Metrics；Risk Results；Segmentation-Error Propagation；Known/Unknown Conditional Analysis；Calibration/Review Ranking；Robustness；Failure Analysis。

## 6. Discussion and Limitations

数据规模、地域、风险标注、未知类别定义、分割依赖、相机几何近似和部署边界。

## 7. Conclusion

只总结H1–H3实际获得的证据。若只有H1成立，只报告空间表示比较finding；若H1不成立，明确报告边界并停止将H2/H3包装为完整系统贡献。
