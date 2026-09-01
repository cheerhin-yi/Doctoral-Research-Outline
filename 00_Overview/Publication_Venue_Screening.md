# 论文发表载体与质量再筛选

本次筛选只使用仓库中32篇PDF首页、版权页和文内明确标注的发表信息，不使用旧聊天、搜索引擎或外部分区表。结论日期为2026-08-31。

## 1. 等级定义与限制

这里给出的是**项目内部载体等级**，用于安排阅读，不冒充中科院分区、JCR分区、影响因子或学校认定目录：

- **A：强正式载体**。PDF明确显示正式期刊或主要同行评审会议，适合作为关键论据来源；仍须在正式写作前核验卷期、页码和DOI。
- **B：正式发表载体**。PDF明确显示正式期刊，但是否能承担关键主张还要看方法严谨性、数据、复现和与课题的直接程度。
- **C：前沿但未完成正式载体核验**。当前仓库副本只证明arXiv、Research Square或未标明正式录用载体；可用于查新和基线跟踪，不能仅凭它冻结“已被同行评审确认”的结论。
- **D：非核心发表形态**。博士论文、技术报告或专题工作坊；可作背景，不作为当前核心方法证据。

等级评价的是仓库内能够确认的发表载体，不评价作者、机构或论文结论本身。高载体等级但主题不相关的论文仍然暂缓；直接相关的预印本仍需跟踪，但结论标记为暂定。

## 2. 当前练手论文

| 论文 | PDF中可确认的载体 | 等级 | 新阅读决策 | 判断 |
|---|---|---|---|---|
| LUD-YOLO | Information Sciences 686 (2025) 121366 | A | **精读1** | 正式期刊且与UAV轻量小目标检测直接同题，是当前最优先证据。 |
| A Lightweight Small Object Detection Model for UAV Images Based on Deep Semantic Integration（BPD-YOLO） | Scientific Reports 15 (2025) 31888 | B | **精读2** | 正式期刊、P2/高分辨率和UAV小目标直接相关；必须核查消融和速度公平性。 |
| EUAVDet | Drones 8 (2024) 261 | B | **精读3** | 正式专业期刊，直接覆盖UAV检测和Jetson Nano端侧实测。 |
| Searching for MobileNetV3 | 当前副本仅明确显示arXiv:1905.02244v5 | C | 了解 | 方法基础价值高，但仓库副本未给出正式载体；正式引用前补核验。 |
| YOLOv9 | 当前副本仅明确显示arXiv:2402.13616v2 | C | 了解 | 重要架构背景，但既非共享检测头直接近邻，当前载体也未核实。 |
| GlimmerNet | arXiv:2512.07391v1 | C | **由重点降为了解** | 预印本且任务是分类，不足以支撑当前检测主张。 |
| EADI-YOLO | Research Square预印本，posted 2025-08-01 | C | **由重点降为了解** | 铁路轻量检测有启发，但未确认正式发表，且是表面缺陷而非UAV小目标。 |
| TakuNet | arXiv:2501.05880v3 | C | **由重点降为了解** | 有端侧实测价值，但属于分类预印本，不能作为检测方法主证据。 |
| Does YOLO Really Need to See Every Training Image in Every Epoch | arXiv:2603.17684v1 | C | **由重点降为了解** | 仅支撑训练效率与复现讨论，不支撑推理轻量化。 |

**练手论文筛选结论**：当前只精读前三篇。其他6篇先不建立完整精读笔记，遇到具体结构、算子或训练协议问题时再定向查阅。

## 3. Paper 1

| 论文 | PDF中可确认的载体 | 等级 | 新阅读决策 | 判断 |
|---|---|---|---|---|
| CSEANet | Sensors 25 (2025) 3500 | B | 练手论文后精读 | 正式期刊且与铁路UAV小目标直接相关，但任务是桥梁螺栓缺陷。 |
| YOLO-IOD | PDF含2026 Association for the Advancement of Artificial Intelligence正式版权标记 | A | 重点 | 正式会议论文；用于增量检测、数据泄漏和未知检测边界，不是Paper 1未知候选的直接替代。 |
| YOLOE | 当前副本仅明确显示arXiv:2503.07465v2 | C | 条件精读 | 方法与实时开放词汇强相关；在Paper 1阶段精读，但正式写作前核验发表版本。 |
| NegAS | 当前副本仅明确显示arXiv:2606.22537v2 | C | 条件精读 | 与OOD目标候选直接相关，前沿价值高，但同行评审状态在仓库中未确认。 |
| Real-Time Source-Free Object Detection | 当前副本仅明确显示arXiv:2606.31834v1 | C | 了解 | 域适应背景，不是开放世界检测核心证据。 |

**Paper 1筛选结论**：CSEANet与YOLO-IOD可作为正式发表证据；YOLOE和NegAS继续作为必须跟踪的前沿方法，但矩阵中应明确“结论暂定、正式版本待核验”。

## 4. Paper 2-7候选论文

| 论文 | 主归档 | PDF中可确认的载体 | 等级 | 启动后的用途 |
|---|---|---|---|---|
| Deep Learning Strategy for UAV-Based Multi-Class Damage Detection on Railway Bridges | Paper 2 | Applied Sciences 15 (2025) 8719 | B | 了解；是二维损伤分割，不是三维定量测量。 |
| Retrieving Objects from 3D Scenes with Box-Guided Open-Vocabulary Instance Segmentation | Paper 2 | PDF含2026 AAAI正式版权标记 | A | 重点候选；正式会议，但与铁路三维测量仍是间接关系。 |
| 6G Service-Oriented Space-Air-Ground Integrated Network | Paper 3 | Chinese Journal of Aeronautics 35(9) (2022) 1-18 | A | Paper 3启动后重点读体系架构与资源编排。 |
| Survey on UAV Cellular Communications | Paper 3 | Journal of Communications Surveys and Tutorials（PDF页眉） | A | Paper 3启动后的通信基础精读入口。 |
| UAV Communications for 5G and Beyond | Paper 3 | IEEE Internet of Things Journal录用稿 | A | Paper 3启动后的5G/B5G技术综述。 |
| Comprehensive Survey of UAVs Communication Networks | Paper 3 | Computer Standards & Interfaces 72 (2020) 103451 | B | 重点了解网络协议、架构和多UAV通信。 |
| A Tutorial on UAVs for Wireless Networks | Paper 3 | 当前副本仅明确显示arXiv:1803.00680v2 | C | 内容可作教程，但正式引用前先核验最终载体。 |
| Edge Intelligence-Based Rail Transit Equipment Inspection System | Paper 3 | Sensors 26 (2026) 236 | B | 正式轨道巡检案例，重点看5G、边缘部署和事件上传。 |
| Energy-Efficient Joint Localization and Communication via Air-Ground Collaboration | Paper 4 | IEEE Transactions on Wireless Communications 25 (2026) | A | Paper 4启动后的强方法近邻；注意其定位-通信不等于风险驱动ISAC。 |
| Integrating UAVs and RISs in Future Wireless Networks | Paper 4 | Future Internet 16 (2024) 433 | B | 了解RIS和IoV背景，不作核心主张证据。 |
| Delving into Cascaded Instability | Paper 5 | arXiv:2510.24232v3 | C | 前沿跟踪；只能作为视觉退化候选，正式载体待核验。 |
| Advancements in UAV-Enabled Intelligent Transportation Systems | Paper 6 | Applied Sciences 14 (2024) 9455 | B | 了解应用框架，不直接支持主动复检或NBV。 |
| UAVs Meet LLMs | Paper 7 | arXiv:2501.02341v2 | C | 远期前沿综述，暂不精读。 |
| Directional Wireless Mesh Network Design | Paper 7 | UC Berkeley博士论文及技术报告UCB/EECS-2021-17 | D | 按章节选读的网络背景，不作为期刊证据。 |

**未来论文筛选结论**：Paper 3和Paper 4中存在多篇正式强载体论文，但当前阶段仍禁止阅读扩展和启动实验；高载体等级不改变 `PAUSED` 状态。

## 5. 范围外或弱相关背景

| 论文 | PDF中可确认的载体 | 等级 | 决策 |
|---|---|---|---|
| VPD-100K | Proceedings of the 43rd International Conference on Machine Learning (2026) | A | 载体强但主题是视觉隐私，继续范围外。 |
| Physically Large Apertures for Wireless Power Transfer | IEEE Wireless Communications (2026) | A | 正式强载体但主题是无线能量传输，继续范围外。 |
| An Overall Real-Time Mechanism for Classification and Quality Evaluation of Rice | Agri AI专题工作坊，co-located with AAAI 2026 | D | 任务和场景均不相关，继续范围外。 |
| YOLO-Count | arXiv:2508.00728v1 | C | 文生图计数，继续范围外。 |

## 6. 重新排序后的最小阅读序列

1. `LUD-YOLO`：正式期刊、直接同题；
2. `BPD-YOLO`：正式期刊、直接回答P2/小目标；
3. `EUAVDet`：正式专业期刊、端侧实测；
4. 完成前三篇的结构冲突表和速度口径表后，再决定是否定向阅读MobileNetV3、EADI-YOLO或TakuNet；
5. 练手论文结束后进入Paper 1，优先CSEANet和YOLO-IOD，再跟踪YOLOE与NegAS的正式版本。

## 7. 尚不能从仓库确认的信息

- 中科院分区、JCR分区、影响因子、CCF等级和学校认可目录；
- 仅有arXiv副本的论文是否后来正式发表，以及最终题名、页码和版本；
- 2026年新论文的最终卷期、检索状态和勘误。

若要按这些外部指标继续筛选，需要单独授权联网，并明确采用哪一套分区和年份。
