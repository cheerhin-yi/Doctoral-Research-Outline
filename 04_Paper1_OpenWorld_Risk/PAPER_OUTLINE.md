# Paper 1论文提纲

## Abstract

问题、方法主张、数据/协议、经冻结表格支持的关键结果、边界。没有结果前只保留结构，不填写数字。

## 1. Introduction

铁路UAV巡检需求 → YOLO实时检测优势 → 小目标、远距离和开放类别盲区 → 仅检测类别不足以形成风险告警 → RQ1–RQ4及贡献边界。

## 2. Related Work

YOLO and Small-Object Detection for UAV Railway Inspection；Railway Open-Set/Open-Vocabulary Detection；Track Context and Intrusion Risk；Risk Reliability and Calibration。必须说明已有能力、剩余缺口和本研究不重复什么。

## 3. Problem Formulation

定义已知/未知危险对象、YOLO检测输出、未知候选、轨道运行区域、侵界事件、高风险告警、成像/部署条件和评价协议。

## 4. Method

YOLO Baseline and Error-Driven Minimal Adaptation；Unknown Candidate Supplement；Track Context and Risk Alarm；Optional Risk Calibration。清楚区分原始YOLO、训练策略、模型规模和候选改动，不把通用模块包装成新架构。

## 5. Experiments

Dataset Audit；YOLO Scale/Training Baselines；Small-Object and Height-Stratified Results；Minimal-Change Ablation；RT-DETR Reference；Known/Unknown Evaluation；Risk Alarm Increment；Calibration/Review Ranking；Robustness；Efficiency；Failure Analysis。

## 6. Discussion and Limitations

数据规模、地域、风险标注、未知类别定义、分割依赖、相机几何近似和部署边界。

## 7. Conclusion

只总结RQ1–RQ4实际获得的证据。若YOLO改动无稳定收益，就按强基线/应用系统口径写作；若开放环境或风险模块无增量，则删除，不维持虚假的完整系统。
