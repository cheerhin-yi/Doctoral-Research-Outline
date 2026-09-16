# 主线A直接近邻比较与否决条件

> 2026-09-10 A0-04范围更新：本表保留首批原文审计。当前优先VisDrone，轨道走廊及铁路专属候选差异已退出方法前提；通用区域计算近邻仍有效，High风险不变。新差异未冻结，不把历史铁路差异当成当前创新。

- 核验日期：2026-09-10；批次：2026-09-10-Mainline-A。
- 用途：支持已选“铁路UAV已知障碍物、固定端到端延迟预算下轨道走廊引导局部高分辨率检测”的可行性和新颖性审查。
- 性质：证据评估与待验证预测；不是方法有效性结论，不是正式实验结果。
- 本表汇总六项已完成相关性审计的近邻，并保留补充检索候选；不代表穷尽检索。发表状态、作者报告与审计判断在单篇审计中分开。

## 已经被覆盖的部分

| 工作与证据 | 区域/高分辨率信息从哪里来 | 明确的额外工作 | 已覆盖的主线A概念 | 对主线A仍需验证的差异 |
|---|---|---|---|---|
| [W-0002 SAHI](W-0002_Audit.md)，§3、图2 | 全图均匀重叠切片，放大后检测；可叠加全图分支 | 多片前向、坐标变换、融合 | 局部放大、切片与全图联合预测 | 轨道先验是否在同预算内优于均匀切片，不可只比较精度 |
| [W-0003 QueryDet](W-0003_Audit.md)，§3、图1 | 低分辨率QueryHead粗定位，引导高分辨率稀疏头 | 主干、查询、稀疏运算 | 粗定位引导局部精处理、降低背景计算 | 图像走廊是否提供可测量优势；不能把换到图像空间当作充分贡献 |
| [W-0004 ESOD](W-0004_Audit.md)，§III、表III–IV | 复用早期特征预测前景，选特征块并稀疏检测 | ObjSeeker、切片、稀疏头；训练额外掩码监督 | 区域筛选以支持高分辨率；自适应裁片；块比例和时延关联 | 铁路先验与固定预算是否有增量；不能将不使用SAM本身称为创新 |
| [W-0005 ROI-Gated SAHI](W-0005_Audit.md)，§III、Algorithm1 | 轻量检测器生成ROI，扩边并局部切片；覆盖高时回退全图切片 | proposer、合并、路由、refiner、NMS | ROI筛选、局部高分辨率、全局融合、阈值回退 | 轨道走廊覆盖可靠性、独立预算校准、可观测增量均未验证 |
| [W-0006 RVGC-YOLO](W-0006_Audit.md)，§IV–V | 全图轻量网络；无显式走廊ROI流程 | 多模块改动、剪枝与训练蒸馏 | UAV-RSOD已知异物＋轻量YOLO＋Jetson评价 | 只提供任务/部署近邻；区域机制仍须与上面四类工作比较 |
| [W-0007 MRU-YOLO](W-0007_Audit.md)，§2.1–2.5、表4–9 | 全图YOLO11n预测和几何状态，HGB预测局部剩余检出价值，3×3候选取Top-2 | 离线全9片GT效用监督，在线状态/HGB、2片前向、来源感知融合 | 固定裁片预算、边际收益排序、局部高分辨率、全局保留与冲突保护；已有K值扫描 | 必须证明轨道先验和实际毫秒控制的增量；“效用＋Top-K＋预算”已经不足以作为区别 |

## 数字的正确用途

以下只保留决定比较方式的事实，完整数值和表号见对应审计；不同论文的FPS和AP不可直接横向排序。

| 工作 | 必须保留的比较限制 | 对本项目的执行要求 |
|---|---|---|
| SAHI | v5表1报告AP50而非AP50–95；切片微调改变训练；未给可审计的硬件速度表 | 推理策略对照固定训练；速度单独实测；不能仅用mAP50支撑主张 |
| QueryDet | “约3倍”相对高分辨率无CSQ，不是相对原始RetinaNet；全流程计时边界不明确 | 写清速度分母；提供原始、提高分辨率、选择性计算三个层次的对照 |
| ESOD | 表III同分辨率AP略降，节省开销后提高分辨率得到另一折中；表III/IV基线FPS不一致 | 不混表拼接加速比；统一实现和测量，报告区域开销与保留比例 |
| ROI-Gated SAHI | 表I的静态版本整体更慢且精度更低；混合路由轻微加速仍有精度损失；阈值在同一COCO128全split校准 | 保留负面结果；校准与测试分离；三个挑选案例不能替代全测试集 |
| RVGC-YOLO | 接受稿明确排除CPU NMS，正式工作出版不等于该稿逐字等同最终版；来源分组隔离未说明 | 分开报告核心推理与完整检测时延；按原图/采集来源分组，不能照抄8:1:1随机划分 |
| MRU-YOLO | 学习效用相对同预算密度Top-2，两个数据集平均AP增量均仅0.035pp；预算是裁片数。表9声称端到端、代码t0前已读图及构造网格；计时SD是5次重复间SD，不是逐帧p95 | 密度Top-K必须作为简单强对照；相同融合下隔离选择增量；完整处理起止需明确。转换后VisDrone val不能冒充官方test-dev指标 |

## 主线A仍可讨论的问题，而非已确认空白

1. **P0-A-C1：同时间预算的小障碍物检出。** 预测：轨道走廊能保留关键目标所需图像细节，在计入先验获取和区域处理成本后，比简单全图放大/切片取得更好的召回—延迟折中。否决：实际数据没有足够分辨率，目标分布不集中，或简单对照已达到相同效果。
2. **P0-A-C2：区域漏检与端到端预算控制。** 预测：在训练/校准侧确定区域及预算设置后，独立测试侧的区域漏检和实际延迟可被清楚测量与控制。否决：依赖测试真值ROI，遗漏目标却宣称加速，或仅平均延迟达标而尾部频繁超预算。已有阈值fallback、固定Top-K、全局预测保留或简单保护不能作为独立创新；MRU-YOLO已经将按场景/计算约束自适应K列为未来工作，泛泛提出动态预算也是直接延伸，尚不构成贡献。

“固定预算”目前必须先操作化：设备、输入、精度模式、batch=1、计时起止、重复和同步方法、统计分位数及预算违反率。平均速度目标、p95目标与每帧硬截止时间不是同一保证；无相应实现和证据时不得写硬实时。ROI面积采用并集还是求和必须明确，不能沿用W-0005的定义歧义。

## 最低判别顺序

1. **数据条件先行。** 核对原始高分辨率图、增强派生关系、采集来源分组、目标框尺寸及目标相对轨道位置；数据结论引用W-0001与本批次数据审计，不从他人mAP推定本项目数据足够。
2. **冻结区域来源。** 测试时只能使用可部署的预测/几何信息；人工真值走廊若用于上界诊断，必须单列为oracle，不能计入方法实测。
3. **最小对照。** 固定同一个检测器和训练条件，至少比较原始全图、全图提高分辨率、均匀切片、简单固定/几何走廊裁剪、密度Top-K和候选区域分配；MRU-YOLO与ROI-Gated为直接流程近邻。选择机制消融必须固定融合策略；QueryDet/ESOD为机制比较及可复现条件下的参考，不因列入文献就强制同时复现全部重模型。
4. **公平测量。** 区域获取、全部裁剪、全部前向、坐标回映和融合都进入总时间；分别记录区域遗漏、切片截断、预测漏检、AP50–95、Recall-small及p50/p95。各策略可在同校准预算下各自选择合理配置，测试阶段锁定；不能故意用差的SAHI切片设置。
5. **停止条件。** 无独立无泄漏测试、候选依赖oracle、只在不计前后处理时加速、效果不优于简单对照，任一成立即停止相应主张；不自动叠加网络、蒸馏或风险模块。

以上是审计提出的判别要求；是否进入样例、数据或正式训练由[当前阶段](../../00_Overview/Current_Stage.md)、[研究计划](../Research_Plan.md)和[实验计划](../Experiments/Experiment_Plan.md)共同落实。本子任务未下载正式数据或运行模型。

## 与Paper 1的界线

P0仅研究固定已知类别检测与计算分配；轨道走廊在这里是空间先验。走廊内的检测框不自动等于危险、侵界或应急等级。未知类别发现、风险排序、告警预算和可信告警仍归Paper 1；“计算时间预算”与“告警数量预算”不可混写。W-0006只向P1提供已知检测基线参考，六篇近邻均不证明P1的未知/风险主张。区域覆盖和遗漏是检测质量/计算分配评价，不自动等于安全风险概率或可信告警。

## 补充检索与待审候选

截至2026-09-10，实际补查式包括：`"ClusDet" "DMNet" "AutoFocus" small object detection`、`"Clustered Object Detection in Aerial Images" CVF`、`"Density Map Guided Object Detection in Aerial Images" CVF`、`"AutoFocus: Efficient Multi-Scale Inference" CVF`、`"MRU-YOLO" "latency" "Table 6"`、`"MRU-YOLO" "2.6" "training"`、`"MRU-YOLO" "RTX" "utility" validation`、`"10.1016/j.neucom.2025.130327"`、`"10.3390/rs15051249"`。主任务提供MRU出版社页面后，追加出版社PDF、Crossref与作者代码核验。初始五项以arXiv号/DOI/标题检索全文；此处记录的是本轮明确执行的补查式，不伪造数据库批量检索记录。

| 新近邻候选 | 已核验的一手入口与关系 | 本轮处置及待补证据 |
|---|---|---|
| MRU-YOLO，2026，10.3390/rs18162680 | 出版社正式26页PDF、§2–4及表1–9；作者固定commit源代码 | PASS，W-0007；是最直接新增冲突。完整固定K效用分配已有先例；实际时间控制、铁路先验仍待具体化和进一步检索 |
| ClusDet：Clustered Object Detection in Aerial Images，ICCV2019 | [CVF正式入口](https://openaccess.thecvf.com/content_ICCV_2019/html/Yang_Clustered_Object_Detection_in_Aerial_Images_ICCV_2019_paper.html)，[arXiv1904.08008](https://arxiv.org/abs/1904.08008)；聚类区域与尺度归一化减少裁片 | HOLD候选；只核验身份/摘要与区域关系，未完成全文实验、划分与计时审计；不能把“目标集中所以按区域裁剪”当新发现 |
| DMNet：Density Map Guided Object Detection in Aerial Images，CVPR Workshops2020 | [CVF正文入口](https://openaccess.thecvf.com/content_CVPRW_2020/papers/w11/Li_Density_Map_Guided_Object_Detection_in_Aerial_Images_CVPRW_2020_paper.pdf)，[arXiv2004.05520](https://arxiv.org/abs/2004.05520)；密度图引导区域裁剪 | HOLD候选；未完成实验审计；注意这是workshop，不写作CVPR主会；不与2021 Coarse-Grained版本/CDMNet混合 |
| AutoFocus：Efficient Multi-Scale Inference，ICCV2019 | [CVF正式入口](https://openaccess.thecvf.com/content_ICCV_2019/html/Najibi_AutoFocus_Efficient_Multi-Scale_Inference_ICCV_2019_paper.html)，[arXiv1812.01600](https://arxiv.org/abs/1812.01600)；粗尺度FocusPixels激活细尺度FocusChips，并处理跨片合并错误 | HOLD候选；未逐项核验全文实验；正文存在不等于已完成PASS审计；待核验覆盖/速度协议 |
| GOIS：Enhancing Tiny Object Detection Using Guided Object Inference Slicing (GOIS): An efficient dynamic adaptive framework for fine-tuned and non-fine-tuned deep learning models | [出版社](https://www.sciencedirect.com/science/article/pii/S0925231225009993)，DOI10.1016/j.neucom.2025.130327，Neurocomputing2025；[作者代码](https://github.com/MMUZAMMUL/GOIS) | HOLD；粗筛背景、细分ROI为直接近邻。作者README出现VisDrone训练集评价，须回到正文核对用途/划分，不能凭他人issue判定泄漏；ResearchSquare/SSRN版本关系未完成核验 |
| ASAHI：Adaptive Slicing-Aided Hyper Inference for Small Object Detection in High-Resolution Remote Sensing Images | [出版社](https://www.mdpi.com/2072-4292/15/5/1249)，DOI10.3390/rs15051249，Remote Sensing15(5)1249；[版本记录](https://www.mdpi.com/2072-4292/15/5/1249/notes) | HOLD；2023-02-24首次VoR，02-28有PDF/XML更新，2025-09-04为HTML更新，不能改写为2025论文；自适应机制、数据和计时待全文核验 |

这些HOLD条目只进入候选/周报处置，不作为新增PASS数量、不假装已填满主矩阵；后续按工作级去重再审计。未系统查询Web of Science/Scopus，未完成引用追踪穷尽或全部2026增量；任何“没有人做过”的断言均不成立。

## 本批次结论与范围

**主线A的新颖性风险为High；可继续的是带否决门的数据和协议核验，不能宣布已找到新算法。** MRU-YOLO使冲突更直接：有限局部预算、效用排序和全局保护都已有明确实现。不能把“轨道场景＋同一方法”视为机制创新，也不能将“固定K”换成“固定预算”措辞规避近邻。六篇中未审计到“完整同构铁路走廊＋已冻结毫秒控制方案”，但有限检索无法证明它不存在；真实可检验差异尚未成立。

六项工作在单篇审计层面为PASS；五项补充候选为HOLD。六项方法工作加W-0001数据论文共7项PASS已联动；本表5个HOLD与主任务另3个HOLD合计8，见周报。论文审计不代表实验；用户授权的主线A计划调整见研究计划，旧学习正文完整保留。

## 2026-09-12-N1：当前差异结论

前述AutoFocus HOLD为2026-09-10历史状态。本批完成[W-0009全文审计](W-0009_Audit.md)，现为PASS：§4已覆盖粗尺度小目标响应选区，§5.2已检查细检测可恢复目标，不能将这些通用表述主张为首次。[ViCrop-Det公开全文审查](ViCrop_Det_HOLD_Review.md)发现内部信号／免训练／固定片数也已有覆盖，版本和实验协议疑点使其保持HOLD，不消除方法冲突。

当前唯一候选及逐项差异见[跨尺度同类弱响应审查](Weak_Response_Candidate_Review.md)第3–6节：固定检测器P3/P4同位置、同类别、局部归一化响应用于一次区域排序。精确统计的有效性待验证；必须优于低阈值、单尺度及破坏对应关系的对照。仅保留PROPOSED诊断资格、风险High；A0-09仍DISMISSED。没有检测实验或可用于论文的增益数字。
