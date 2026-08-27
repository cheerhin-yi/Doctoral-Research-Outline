# Literature Matrix

所有条目在核验原文前标为“待核验”。研究周W01建立v1，研究周W10执行创新复核，写作阶段逐项清理元数据。

| ID | Title | Year | Venue | Problem | Dataset | Input | Output | Method | Contributions | Metrics | Limitations | Closest to Paper | Reusable | Innovation Conflict | Priority | Verified Link | Status |
|---|---|---:|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| L001 | 待核验 |  |  |  |  |  |  |  |  |  |  | Paper 1 |  |  | Must Read |  | 待核验 |
| L002 | UAV imagery based potential safety hazard evaluation for high-speed railroad using Real-time instance segmentation | 2023 | Advanced Engineering Informatics | UAV铁路危险识别与等级评价 | 论文UAV铁路数据 | UAV图像 | 轨道、危险物、危险等级 | YOLARC与距离型HLE | UAV场景检测、解析和距离风险评价 | 见原文 | 需精读方法和数据边界 | Paper 1 H1 | 距离基线/实验设计 | 高：UAV+轨道距离+危险分级已覆盖 | Must Read | https://www.sciencedirect.com/science/article/pii/S1474034622002774 | 初步核验 |
| L003 | Railway Intrusion Risk Quantification with Track Semantic Segmentation and Spatiotemporal Features | 2025 | Sensors | 铁路侵入风险量化 | 见原文 | 铁路图像/时序 | 风险等级 | 轨道分割、标准轨距参照、横向距离与时序特征 | 将轨距和轨道中心距离用于风险 | 见原文 | 需复核与UAV差异 | Paper 1 H1 | metric-gauge baseline | 高：轨距归一和风险量化已覆盖 | Must Read | https://pmc.ncbi.nlm.nih.gov/articles/PMC12431379/ | 初步核验 |
| L004 | Spatial Relation Reasoning Based on Keypoints for Railway Intrusion Detection and Risk Assessment | 2026 | Applied Sciences | 铁路异物检测与空间风险 | 见原文 | 图像 | 九级风险 | 轨道边界、框底关键点、横向距离和运动状态 | 轨道相对几何风险推理 | 见原文 | 需复核固定相机/UAV条件 | Paper 1 H1 | boundary/keypoint baseline | 高：轨道相对几何已覆盖 | Must Read | https://www.mdpi.com/2076-3417/16/6/3026 | 初步核验 |
| L005 | ROSD: Railway intrusion object generalized detection via Open-Set Detection | 2026 | Advanced Engineering Informatics | 铁路开放集异物检测 | RSDS/COCO | 图像/语义 | 已知及新类别检测 | CLIP导向开放集检测 | 铁路未见类别泛化 | 见原文 | 风险推理不是其主要目标，需精读 | Paper 1 H2 | open-set baseline | 高：铁路open-set本身已覆盖 | Must Read | https://www.sciencedirect.com/science/article/abs/pii/S1474034625011218 | 初步核验 |

## 阅读分组

- 铁路UAV数据与检测；
- 铁路场景分割与空间关系；
- Open-set / Open-vocabulary / Open-world；
- 风险量化与上下文推理；
- 不确定性与校准；
- 后续通信、ISAC与主动感知接口。

Paper 1最近工作审计见[Paper1_Novelty_Audit_2026-08-27.md](Paper1_Novelty_Audit_2026-08-27.md)。“初步核验”表示已核对出版页/正文公开信息，但尚未完成逐段精读和引用摘录。
