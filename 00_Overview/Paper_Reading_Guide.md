# 论文归档与阅读等级

本文件只维护跨项目的发表载体、阅读等级和归档边界。具体问题、证据、冲突和单篇笔记由各论文的`Literature_Matrix.md`管理；当前任务只由[Current_Stage.md](Current_Stage.md)管理。

## 1. 状态与等级

- `SCREENED`：已核对题名、摘要、方法概述和结论，不等于精读或可引用证据。
- `DONE`：原文方法、数据、实验、局限和项目关系均已形成笔记并写回矩阵。
- **精读**：直接决定当前方法、强基线、实验协议或研究边界。
- **重点**：启动对应任务后定向阅读。
- **了解/暂缓**：只作背景或边界记录。

发表载体为仓库内部核验等级，不冒充中科院/JCR/CCF或学校目录：

- **A**：仓库PDF明确显示强正式期刊或主要同行评审会议；
- **B**：仓库PDF明确显示正式期刊；
- **C**：当前副本只确认arXiv、Research Square或未核实正式载体；
- **D**：学位论文、技术报告或专题工作坊。

正式写作前仍须核验DOI、卷期、最终版本和当年学校规则。

## 2. 当前练手论文

详细证据和检索缺口见[练手论文文献矩阵](../PrePaper_Lightweight_Detection/Literature/Literature_Matrix.md)。

| 顺序 | 论文 | 可确认载体 | 等级 | 决策 |
|---:|---|---|:---:|---|
| 1 | LUD-YOLO | Information Sciences 686 (2025) 121366 | A | 精读；UAV轻量小目标直接近邻 |
| 2 | BPD-YOLO | Scientific Reports 15 (2025) 31888 | B | 精读；P2/高分辨率直接证据 |
| 3 | EUAVDet | Drones 8 (2024) 261 | B | 精读；UAV检测与Jetson Nano实测 |
| 4 | MobileNetV3 | 当前副本为arXiv:1905.02244v5 | C | 了解；轻量设计基础 |
| 5 | YOLOv9 | 当前副本为arXiv:2402.13616v2 | C | 了解；架构背景 |
| 6 | GlimmerNet | arXiv:2512.07391v1 | C | 了解；分类预印本 |
| 7 | EADI-YOLO | Research Square，2025-08-01 | C | 了解；铁路表面缺陷，域不一致 |
| 8 | TakuNet | arXiv:2501.05880v3 | C | 了解；分类端侧部署 |
| 9 | Does YOLO Really Need to See Every Training Image in Every Epoch | arXiv:2603.17684v1 | C | 了解；训练效率而非推理轻量化 |

只有前三篇进入当前阶段2的优先精读序列；阶段0–1完成前不得提前开始。

## 3. Paper 1

详细证据见[Paper 1文献矩阵](../01_Paper1_OpenWorld_Risk/Literature/Literature_Matrix.md)。

| 论文 | 可确认载体 | 等级 | 决策 |
|---|---|:---:|---|
| CSEANet | Sensors 25 (2025) 3500 | B | 练手论文完成后精读 |
| YOLO-IOD | 2026 AAAI正式版权标记 | A | 重点；用于增量与未知边界 |
| YOLOE | 当前副本为arXiv:2503.07465v2 | C | 条件精读；正式版本待核验 |
| NegAS | 当前副本为arXiv:2606.22537v2 | C | 条件精读；结论暂定 |
| Real-Time Source-Free Object Detection | 当前副本为arXiv:2606.31834v1 | C | 了解；域适应不等于开放世界 |

## 4. Paper 2–7与范围外材料

这些论文只证明候选材料已归档，不改变对应论文的`PAUSED`状态。

| 主归档 | 载体核验摘要 | 当前决策 |
|---|---|---|
| Paper 2 | 1篇Applied Sciences（B）、1篇AAAI 2026（A） | 暂不精读 |
| Paper 3 | 3篇强正式载体（A）、2篇正式期刊（B）、1篇arXiv教程（C） | 暂不启动通信学习 |
| Paper 4 | IEEE TWC（A）、Future Internet（B） | 暂不启动ISAC/优化 |
| Paper 5 | 1篇arXiv视觉退化论文（C） | 暂不启动多模态 |
| Paper 6 | 1篇Applied Sciences综述（B） | 暂不启动主动感知 |
| Paper 7 | 1篇arXiv综述（C）、1篇博士论文/技术报告（D） | 暂不启动多无人机研究 |
| 范围外 | VPD-100K、无线能量传输、稻米分类、YOLO-Count | 只保留边界记录，不进入主线 |

## 5. 归档规则

1. 一篇论文只保留一个主PDF和一份主笔记；跨主题只在矩阵引用。
2. 预印本可作前沿线索，不能写成“同行评审已确认”的定论。
3. 直接相关性优先于期刊名；强载体但范围外仍然暂缓。
4. 阅读顺序由当前论文矩阵和阶段门决定，不在本文件维护“下一任务”。
5. 已确认的LUD-YOLO重复副本不再保留；论文附件目录不得由自动整理任务修改。
