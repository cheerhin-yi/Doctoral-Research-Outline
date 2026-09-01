# 练手论文文献矩阵

本文件统一管理主题问题、阅读顺序、发表载体、证据、同构风险和完成门。检索过程写入[Search_Log.md](Search_Log.md)，单篇精读使用[Paper_Note_Template.md](Paper_Note_Template.md)并保存在对应主题目录。

状态：`TODO`未核验；`SCREENED`完成摘要级初筛；`READING`精读中；`DONE`证据已写回；`EXCLUDED`保留排除理由。载体A–D定义见[全项目阅读等级](../../00_Overview/Paper_Reading_Guide.md)。

## 1. 主题与完成门

| 主题 | 必须回答 | 完成门 |
|---|---|---|
| L1 小目标与多尺度 | P2何时稳定增益？移除P5损失什么？ | ≥3篇精读；普通P2与P2–P4公平对照；小目标分层规则 |
| L2 轻量共享检测头 | 跨尺度共享是否同构？参数减少是否改善真实执行？ | ≥3篇精读；结构冲突表；B2→M唯一变量 |
| L3 效率与部署 | 参数量、GFLOPs、延迟、FPS如何公平比较？ | ≥3篇精读；固定计时协议；C0-2证据门 |
| L4 评价与复现 | 小目标/遮挡如何分层？结果如何回链？ | ≥3篇精读；随机性与泄漏规则；Run ID回链 |

方法冻结总门：至少12篇直接相关工作完成核验，其中最近三年不少于8篇。

## 2. 论文索引与阅读顺序

| ID | 主题 | 年份 | 论文/入口 | 载体 | 优先级 | 状态 | 重点与本文关系 |
|---|---|---:|---|---|---|---|---|
| L1-01 | L1 | 2025 | [LUD-YOLO](01_Small_Object_and_Multiscale/LUD-YOLO%20-%20A%20Novel%20Lightweight%20Object%20Detection%20Network%20for%20Unmanned%20Aerial%20Vehicle.pdf) | Information Sciences，A | MUST-1 | SCREENED | UAV轻量检测直接近邻；结构、消融、数据与速度口径 |
| L1-02 | L1 | 2025 | [BPD-YOLO](01_Small_Object_and_Multiscale/A%20Lightweight%20Small%20Object%20Detection%20Model%20for%20UAV%20Images%20Based%20on%20Deep%20Semantic%20Integration.pdf) | Scientific Reports，B | MUST-2 | SCREENED | P2/高分辨率、多尺度、AP_small和公平基线 |
| L3-02 | L3 | 2024 | [EUAVDet](03_Efficiency_and_Deployment/EUAVDet%20-%20An%20Efficient%20and%20Lightweight%20Object%20Detector%20for%20UAV%20Aerial%20Images%20with%20an%20Edge-Based%20Computing%20Platform.pdf) | Drones，B | MUST-3 | SCREENED | Jetson Nano、FPS、计时范围和精度—速度权衡 |
| L2-01 | L2 | 2019 | [MobileNetV3](02_Lightweight_Shared_Head/Searching%20for%20MobileNetV3.pdf) | 当前副本arXiv，C | SHOULD | SCREENED | 硬件感知设计基础，不是共享头直接近邻 |
| L2-02 | L2 | 2024 | [YOLOv9](02_Lightweight_Shared_Head/YOLOv9%20-%20Learning%20What%20You%20Want%20to%20Learn%20Using%20Programmable%20Gradient%20Information.pdf) | 当前副本arXiv，C | SHOULD | SCREENED | 架构背景，不直接支持唯一头改动 |
| L2-03 | L2 | 2025 | [GlimmerNet](02_Lightweight_Shared_Head/GlimmerNet%20-%20A%20Lightweight%20Grouped%20Dilated%20Depthwise%20Convolutions%20for%20UAV-Based%20Emergency%20Monitoring.pdf) | arXiv，C | OPTIONAL | SCREENED | 分类任务；只在算子问题时定向阅读 |
| L2-04 | L2 | 2025 | [EADI-YOLO](02_Lightweight_Shared_Head/EADI-YOLO%20-%20A%20Lightweight%20and%20Efficient%20Model%20for%20Rail%20Surface%20Defect%20Detection.pdf) | Research Square，C | OPTIONAL | SCREENED | 铁路表面缺陷，域与任务不一致 |
| L3-01 | L3 | 2025 | [TakuNet](03_Efficiency_and_Deployment/TakuNet%20-%20an%20Energy-Efficient%20CNN%20for%20Real-Time%20Inference%20on%20Embedded%20UAV%20Systems%20in%20Emergency%20Response%20Scenarios.pdf) | arXiv，C | OPTIONAL | SCREENED | 分类端侧部署；只参考硬件/FP16口径 |
| L4-01 | L4 | 2026 | [Does YOLO Really Need to See Every Training Image in Every Epoch](04_Evaluation_and_Reproducibility/Does%20YOLO%20Really%20Need%20to%20See%20Every%20Training%20Image%20in%20Every%20Epoch.pdf) | arXiv，C | OPTIONAL | SCREENED | 训练效率与公平预算，不是推理轻量化 |
| L1-03 | L1 | 近三年 | P2或高分辨率小目标检测直接近邻 | 待核验 | MUST | TODO | 尺度设计、AP_small、直接基线 |
| L2-05 | L2 | 近三年 | 跨尺度共享检测头直接近邻 | 待核验 | MUST | TODO | 共享范围、算子、消融与同构风险 |
| L3-03 | L3 | 近三年 | 真实推理速度评价规范 | 待核验 | MUST | TODO | 预热、同步、batch、计时边界 |
| L4-02 | L4 | 近三年 | 小目标/遮挡评价与复现规范 | 待核验 | MUST | TODO | 标签定义、统计单位、报告规则 |

## 3. 新颖性冲突表

精读后填写；空白表示未知，不表示没有冲突。

| ID | 使用P2 | 移除P5 | 跨尺度共享 | 轻量卷积 | 同报AP_small与延迟 | 冲突等级 | 决策 |
|---|---|---|---|---|---|---|---|
| L1-01 |  |  |  |  |  |  |  |
| L1-02 |  |  |  |  |  |  |  |
| L3-02 |  |  |  |  |  |  |  |
| L2-05 |  |  |  |  |  |  |  |

## 4. 方法冻结前必须回答

- [ ] 最近工作是否已有同构的共享P2–P4检测头？
- [ ] 普通P2的精度收益和速度代价分别多大？
- [ ] 移除P5在小目标数据上是否有充分依据？
- [ ] 参数共享只降低参数量，还是也降低GFLOPs和真实延迟？
- [ ] 哪些工作使用相同数据和同代YOLO，可作为直接对照？
- [ ] 如果方法差异很小，能否只主张经严格验证的精度—速度折中？
