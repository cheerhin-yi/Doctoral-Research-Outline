# 已归档论文阅读指南

本指南只依据仓库中现有 PDF 及项目规划整理。2026-08-31 共检查 33 个 PDF，确认 1 组重复后保留 32 篇唯一论文。这里的 `SCREENED` 表示已核对题名、摘要、方法概述和结论，不等于完成精读或形成可引用证据。

发表载体复筛结果见[论文发表载体与质量再筛选](Publication_Venue_Screening.md)。阅读等级已同时考虑载体可信度和课题直接相关性；不能仅按期刊名排序。

## 阅读规则

- **精读**：直接决定当前方法、强基线、实验协议或研究边界，需要建立单篇笔记并核对方法、数据、消融和局限。
- **重点**：对当前或对应未来论文有明确帮助，先读摘要、方法图、实验表和局限，启动相关任务时再形成完整笔记。
- **了解**：用于概念、技术谱系或边界判断，选择性阅读即可。
- **暂缓**：与当前目标弱相关或属于远期背景，现在不投入时间。

当前阅读顺序严格保持为：练手论文直接近邻 → 练手论文效率与评价 → Paper 1 开放世界与铁路证据。Paper 2–7 仍为 `PAUSED`，其候选论文归档不表示提前启动。

## A. 当前练手论文：实时轻量小目标检测

| 顺序 | 等级 | 论文 | 当前用途与阅读重点 |
|---:|---|---|---|
| 1 | 精读 | [LUD-YOLO - A Novel Lightweight Object Detection Network for Unmanned Aerial Vehicle](../PrePaper_Lightweight_Detection/Literature/01_Small_Object_and_Multiscale/LUD-YOLO%20-%20A%20Novel%20Lightweight%20Object%20Detection%20Network%20for%20Unmanned%20Aerial%20Vehicle.pdf) | UAV轻量检测直接近邻；核对小目标设计、轻量模块、消融、数据和速度口径。 |
| 2 | 精读 | [A Lightweight Small Object Detection Model for UAV Images Based on Deep Semantic Integration](../PrePaper_Lightweight_Detection/Literature/01_Small_Object_and_Multiscale/A%20Lightweight%20Small%20Object%20Detection%20Model%20for%20UAV%20Images%20Based%20on%20Deep%20Semantic%20Integration.pdf) | P2/高分辨率与多尺度融合直接证据；核对 VisDrone/TinyPerson、分层指标和公平基线。 |
| 3 | 精读 | [EUAVDet - An Efficient and Lightweight Object Detector for UAV Aerial Images with an Edge-Based Computing Platform](../PrePaper_Lightweight_Detection/Literature/03_Efficiency_and_Deployment/EUAVDet%20-%20An%20Efficient%20and%20Lightweight%20Object%20Detector%20for%20UAV%20Aerial%20Images%20with%20an%20Edge-Based%20Computing%20Platform.pdf) | 同时覆盖 UAV 检测与 Jetson Nano 实测；用于冻结真实延迟、FPS和端侧评价口径。 |
| 4 | 了解 | [GlimmerNet - A Lightweight Grouped Dilated Depthwise Convolutions for UAV-Based Emergency Monitoring](../PrePaper_Lightweight_Detection/Literature/02_Lightweight_Shared_Head/GlimmerNet%20-%20A%20Lightweight%20Grouped%20Dilated%20Depthwise%20Convolutions%20for%20UAV-Based%20Emergency%20Monitoring.pdf) | 当前仅有arXiv版本且任务是分类；只在需要对应算子时定向查阅。 |
| 5 | 了解 | [EADI-YOLO - A Lightweight and Efficient Model for Rail Surface Defect Detection](../PrePaper_Lightweight_Detection/Literature/02_Lightweight_Shared_Head/EADI-YOLO%20-%20A%20Lightweight%20and%20Efficient%20Model%20for%20Rail%20Surface%20Defect%20Detection.pdf) | 当前是Research Square预印本，且表面缺陷和UAV小目标存在域差异。 |
| 6 | 了解 | [TakuNet - an Energy-Efficient CNN for Real-Time Inference on Embedded UAV Systems in Emergency Response Scenarios](../PrePaper_Lightweight_Detection/Literature/03_Efficiency_and_Deployment/TakuNet%20-%20an%20Energy-Efficient%20CNN%20for%20Real-Time%20Inference%20on%20Embedded%20UAV%20Systems%20in%20Emergency%20Response%20Scenarios.pdf) | 当前仅有arXiv版本且属于分类；有部署问题时再查硬件和FP16细节。 |
| 7 | 了解 | [Does YOLO Really Need to See Every Training Image in Every Epoch](../PrePaper_Lightweight_Detection/Literature/04_Evaluation_and_Reproducibility/Does%20YOLO%20Really%20Need%20to%20See%20Every%20Training%20Image%20in%20Every%20Epoch.pdf) | 当前仅有arXiv版本；影响训练成本与复现，不是推理轻量化证据。 |
| 8 | 了解 | [Searching for MobileNetV3](../PrePaper_Lightweight_Detection/Literature/02_Lightweight_Shared_Head/Searching%20for%20MobileNetV3.pdf) | 硬件感知 NAS、NetAdapt 和延迟意识的基础；用于理解轻量设计，不是共享检测头直接近邻。 |
| 9 | 了解 | [YOLOv9 - Learning What You Want to Learn Using Programmable Gradient Information](../PrePaper_Lightweight_Detection/Literature/02_Lightweight_Shared_Head/YOLOv9%20-%20Learning%20What%20You%20Want%20to%20Learn%20Using%20Programmable%20Gradient%20Information.pdf) | PGI/GELAN 与参数利用率背景；用于基线谱系，不直接支持拟议的唯一检测头改动。 |

## B. Paper 1：开放世界铁路风险

| 建议时点 | 等级 | 论文 | 与 Paper 1 的关系 |
|---|---|---|---|
| 练手论文完成后 | 精读 | [CSEANet - Cross-Stage Enhanced Aggregation Network for Detecting Surface Bolt Defects in Railway Steel Truss Bridges](../01_Paper1_OpenWorld_Risk/Literature/01_Railway_UAV_Detection/CSEANet%20-%20Cross-Stage%20Enhanced%20Aggregation%20Network%20for%20Detecting%20Surface%20Bolt%20Defects%20in%20Railway%20Steel%20Truss%20Bridges.pdf) | 铁路 UAV、小目标和结构改进近邻；约束铁路场景下已知检测基础。 |
| 开放世界概念门后 | 条件精读 | [YOLOE - Real-Time Seeing Anything](../01_Paper1_OpenWorld_Risk/Literature/02_Open_World_Detection/YOLOE%20-%20Real-Time%20Seeing%20Anything.pdf) | 实时开放词汇强基线，但当前副本只确认arXiv；精读方法，正式结论待最终版本核验。 |
| 开放世界概念门后 | 条件精读 | [NegAS - Negative Label Guided Attention and Scoring for Out-of-Distribution Object Detection with Vision-Language Models](../01_Paper1_OpenWorld_Risk/Literature/02_Open_World_Detection/NegAS%20-%20Negative%20Label%20Guided%20Attention%20and%20Scoring%20for%20Out-of-Distribution%20Object%20Detection%20with%20Vision-Language%20Models.pdf) | 与OOD候选直接相关，但当前副本只确认arXiv；结论按前沿预印本处理。 |
| 同期 | 重点 | [YOLO-IOD - Towards Real-Time Incremental Object Detection](../01_Paper1_OpenWorld_Risk/Literature/02_Open_World_Detection/YOLO-IOD%20-%20Towards%20Real-Time%20Incremental%20Object%20Detection.pdf) | 用于区分增量检测与未知检测，并审计持续学习的数据与协议边界。 |
| 评价阶段 | 了解 | [Real-Time Source-Free Object Detection](../01_Paper1_OpenWorld_Risk/Literature/04_Uncertainty_and_Evaluation/Real-Time%20Source-Free%20Object%20Detection.pdf) | 处理无源域适应和域偏移，不等同于开放世界检测；作为 T4 稳健性背景。 |

## C. Paper 2–7：仅作未来候选归档

| 论文目录 | 等级 | 论文 | 未来用途 |
|---|---|---|---|
| Paper 2 | 了解 | [Deep Learning Strategy for UAV-Based Multi-Class Damage Detection on Railway Bridges Using U-Net with Different Loss Functions](../02_Paper2_3D_Disaster/Literature/01_Railway_Damage_and_3D_Open_Vocabulary/Deep%20Learning%20Strategy%20for%20UAV-Based%20Multi-Class%20Damage%20Detection%20on%20Railway%20Bridges%20Using%20U-Net%20with%20Different%20Loss%20Functions.pdf) | UAV 铁路桥损伤分割背景；不提供三维定量测量证据。 |
| Paper 2 | 了解 | [Retrieving Objects from 3D Scenes with Box-Guided Open-Vocabulary Instance Segmentation](../02_Paper2_3D_Disaster/Literature/01_Railway_Damage_and_3D_Open_Vocabulary/Retrieving%20Objects%20from%203D%20Scenes%20with%20Box-Guided%20Open-Vocabulary%20Instance%20Segmentation.pdf) | 三维开放词汇实例检索背景；启动 Paper 2 后再判断是否与测量主张相连。 |
| Paper 3 | 重点 | [Comprehensive Survey of UAVs Communication Networks](../03_Paper3_Comm_Perception/Literature/01_UAV_Communication_Foundations/Comprehensive%20Survey%20of%20UAVs%20Communication%20Networks.pdf) | UAV 通信网络总体框架。 |
| Paper 3 | 重点 | [A Tutorial on UAVs for Wireless Networks - Applications, Challenges, and Open Problems](../03_Paper3_Comm_Perception/Literature/01_UAV_Communication_Foundations/A%20Tutorial%20on%20UAVs%20for%20Wireless%20Networks%20-%20Applications,%20Challenges,%20and%20Open%20Problems.pdf) | 无线网络中的 UAV 基础教程，适合作为通信知识入口。 |
| Paper 3 | 重点 | [Edge Intelligence-Based Rail Transit Equipment Inspection System](../03_Paper3_Comm_Perception/Literature/02_Edge_Semantic_Transmission/Edge%20Intelligence-Based%20Rail%20Transit%20Equipment%20Inspection%20System.pdf) | 轨道巡检、边缘计算、事件触发上传和带宽/时延实证案例。 |
| Paper 3 | 了解 | [6G Service-Oriented Space-Air-Ground Integrated Network - A Survey](../03_Paper3_Comm_Perception/Literature/01_UAV_Communication_Foundations/6G%20Service-Oriented%20Space-Air-Ground%20Integrated%20Network%20-%20A%20Survey.pdf) | 空天地一体化宏观背景。 |
| Paper 3 | 了解 | [Survey on UAV Cellular Communications - Practical Aspects, Standardization Advancements, Regulation, and Security Challenges](../03_Paper3_Comm_Perception/Literature/01_UAV_Communication_Foundations/Survey%20on%20UAV%20Cellular%20Communications%20-%20Practical%20Aspects,%20Standardization%20Advancements,%20Regulation,%20and%20Security%20Challenges.pdf) | 蜂窝 UAV 的标准、监管和安全背景。 |
| Paper 3 | 了解 | [UAV Communications for 5G and Beyond - Recent Advances and Future Trends](../03_Paper3_Comm_Perception/Literature/01_UAV_Communication_Foundations/UAV%20Communications%20for%205G%20and%20Beyond%20-%20Recent%20Advances%20and%20Future%20Trends.pdf) | 5G/后 5G 技术谱系。 |
| Paper 4 | 重点 | [Energy-Efficient Joint Localization and Communication via Air-Ground Collaboration in UAV-Assisted Emergency Systems](../04_Paper4_Risk_ISAC/Literature/01_Localization_Communication_and_RIS/Energy-Efficient%20Joint%20Localization%20and%20Communication%20via%20Air-Ground%20Collaboration%20in%20UAV-Assisted%20Emergency%20Systems.pdf) | 定位—通信联合优化与能耗约束的近邻。 |
| Paper 4 | 了解 | [Integrating UAVs and RISs in Future Wireless Networks - A Review and Tutorial on IoTs and Vehicular Communications](../04_Paper4_Risk_ISAC/Literature/01_Localization_Communication_and_RIS/Integrating%20UAVs%20and%20RISs%20in%20Future%20Wireless%20Networks%20-%20A%20Review%20and%20Tutorial%20on%20IoTs%20and%20Vehicular%20Communications.pdf) | UAV-RIS 基础与应用背景；不直接等于风险驱动 ISAC。 |
| Paper 5 | 重点 | [Delving into Cascaded Instability - A Lipschitz Continuity View on Image Restoration and Object Detection Synergy](../05_Paper5_Multimodal_Risk/Literature/01_Adverse_Condition_Robustness/Delving%20into%20Cascaded%20Instability%20-%20A%20Lipschitz%20Continuity%20View%20on%20Image%20Restoration%20and%20Object%20Detection%20Synergy.pdf) | 雾、低照等退化下恢复—检测级联稳定性；适合作为视觉退化单模态基线。 |
| Paper 6 | 了解 | [Advancements in UAV-Enabled Intelligent Transportation Systems - A Three-Layered Framework and Future Directions](../06_Paper6_Active_Inspection/Literature/01_UAV_ITS_and_Trajectory_Background/Advancements%20in%20UAV-Enabled%20Intelligent%20Transportation%20Systems%20-%20A%20Three-Layered%20Framework%20and%20Future%20Directions.pdf) | UAV-ITS 与航迹应用背景；不直接提供主动复检或 NBV 方法。 |
| Paper 7 | 了解 | [UAVs Meet LLMs - Overviews and Perspectives Toward Agentic Low-Altitude Mobility](../07_Paper7_MultiUAV_Decision/Literature/01_Agentic_MultiUAV_Systems/UAVs%20Meet%20LLMs%20-%20Overviews%20and%20Perspectives%20Toward%20Agentic%20Low-Altitude%20Mobility.pdf) | Agentic 低空移动与多 UAV 系统远期综述。 |
| Paper 7 | 暂缓 | [Directional Wireless Mesh Network Design](../07_Paper7_MultiUAV_Decision/Literature/02_Directional_Mesh_Networks/Directional%20Wireless%20Mesh%20Network%20Design.pdf) | 定向无线 Mesh 设计背景；篇幅长且与当前决策主张距离较远，未来按章节选读。 |

## D. 范围外或弱相关背景

这些论文保留是为了记录已筛选边界，不进入当前或七篇论文的核心阅读数量。

| 等级 | 论文 | 暂不纳入的原因 |
|---|---|---|
| 暂缓 | [An Overall Real-Time Mechanism for Classification and Quality Evaluation of Rice](../99_Attachments/paper/90_Out_of_Scope_and_Background/An%20Overall%20Real-Time%20Mechanism%20for%20Classification%20and%20Quality%20Evaluation%20of%20Rice.pdf) | 稻米分类/质量评价，场景和检测任务均不匹配。 |
| 暂缓 | [VPD-100K - Towards Generalizable and Fine-Grained Visual Privacy Protection](../99_Attachments/paper/90_Out_of_Scope_and_Background/VPD-100K%20-%20Towards%20Generalizable%20and%20Fine-Grained%20Visual%20Privacy%20Protection.pdf) | 视觉隐私保护数据与模型，不是铁路风险检测目标。 |
| 暂缓 | [YOLO-Count - Differentiable Object Counting for Text-to-Image Generation](../99_Attachments/paper/90_Out_of_Scope_and_Background/YOLO-Count%20-%20Differentiable%20Object%20Counting%20for%20Text-to-Image%20Generation.pdf) | 面向文生图的可微计数，不是当前真实图像检测协议。 |
| 暂缓 | [Physically Large Apertures for Wireless Power Transfer - Performance and Regulatory Aspects](../99_Attachments/paper/90_Out_of_Scope_and_Background/Physically%20Large%20Apertures%20for%20Wireless%20Power%20Transfer%20-%20Performance%20and%20Regulatory%20Aspects.pdf) | 无线能量传输与监管背景，未直接支撑现有通信/ISAC主张。 |

## 重复与命名处理

- 删除的重复副本：`99_Attachments/paper/LUD-YOLO.pdf`。
- 保留并改名的副本：`LUD-YOLO - A Novel Lightweight Object Detection Network for Unmanned Aerial Vehicle.pdf`。
- 两个源文件的二进制哈希不同，但完整提取文本的 SHA-256 均为 `6D60946926E1FF593DB7C923D1CD01B5D2E4A171B5120D27F15D081D08DC056D`，页数、题名和作者一致。
- 文件名统一使用论文完整题名；Windows 文件名不允许的标点以连字符替代。

## 下一项最小任务

只精读 `LUD-YOLO` 一篇，并在 L1 目录建立单篇笔记：提取问题、结构图、与基线的唯一变量、数据划分、AP/AP_small、参数量、GFLOPs、真实速度、消融、失败条件和可复现性信息。完成后再决定是否读取第二篇，暂不改网络、找数据或启动 Paper 1 实验。
