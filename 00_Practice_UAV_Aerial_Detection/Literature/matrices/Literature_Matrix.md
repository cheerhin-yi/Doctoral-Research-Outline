# 练手论文文献矩阵

本文件统一管理主题问题、阅读顺序、发表载体、证据、同构风险和完成门。检索过程写入[Search_Log.md](Search_Log.md)，单篇精读使用[Paper_Note_Template.md](../../00_Practice_UAV_Aerial_Detection/Literature/Paper_Note_Template.md)并保存在对应主题目录。

状态：`TODO`未核验；`SCREENED`完成摘要级初筛；`READING`精读中；`DONE`证据已写回；`EXCLUDED`保留排除理由。载体A–D定义见[全项目阅读等级](../../00_Overview/Paper_Reading_Guide.md)。

## 当前适用范围（2026-09-10 A0-04）

用户已接受VisDrone优先与通用无人机航拍范围；铁路专属走廊退出方法前提。当前数据入口见[VisDrone预审](../Experiments/VisDrone_Feasibility_Audit.md)。下列原文证据保留，论文事实不因范围调整改写；W-0001转历史数据参考，W-0006转历史场景／效率参考，W-0002/3/4/5/7继续用于直接机制比较。未新增论文PASS或精读DONE。

## 首批主线A审计历史（2026-09-10）

首批六个入口及补充近邻比较见[比较表](Mainline_A_Prior_Work_Comparison.md)。P0-A-C1/C2均为待验证问题，新颖性风险High；A0-01已交付且HOLD，不运行模型。HOLD候选只列[周报](../../00_Overview/Weekly_Literature_Audits/Weekly_Literature_Audit_2026-09-10.md)，不计为PASS或精读DONE。

当前审查问：区域来源是否推理可得；是否依赖轨道；分辨率／额外成本如何分配；如何漏检；数据是否按原始来源隔离；计时是否包含整个处理链。六份学习笔记／12篇计数门和固定B0/B1/B2/M均为原目录历史方案要求，不再作为主线A当前门。

历史LSM-Head文献见[原文献矩阵](../../00_Practice_UAV_Aerial_Detection/Literature/matrices/Literature_Matrix.md)，不属于当前执行要求。

## 每周审计记录（主归属）

执行[审计流程](../../00_Overview/Literature_Tracking_Workflow.md)，使用[审计模板](../../00_Overview/Literature_Audit_Template.md)并联动[全局注册表](../../00_Overview/Literature_Registry.md)和[创新台账](../../00_Overview/Innovation_Ledger.md)。本区每项工作只保留一条当前记录，新版本更新原行并回链版本历史。旧索引保持不动；遇到旧工作时匹配旧ID后补齐本区，不视为新增。旧数据的Date Added未知则写Unknown，不猜测历史日期。

下表字段均必填；Unknown必须在审计记录解释缺口，N/A必须有理由。核心身份或技术证据不足时不能PASS。本区登记本批PASS论文，旧索引不自动升级为已审计。

| Work ID / Legacy ID | Title | Year | Venue | Publication Status | Problem | Dataset | Method | Contribution | Metrics | Limitations | Related Paper | Closest Innovation | Novelty Conflict | Reading Priority | Local Path/Reference | Date Added | Audit Reference / Status | Last Audited / Sync Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| W-0001 / N/A | An unmanned aerial vehicle captured dataset for railroad segmentation and obstacle detection | 2024 | Scientific Data 11:1315 | published | 铁路UAV分割与六类已知障碍物 | 315原图/2002增强；原包审计另见Data Audit | 轨道掩膜、增强检测框、常见检测器验证 | 公开铁路航拍数据和基准 | 表3 YOLO AP50:95=49.45%，MobileNet=52.90%；均为作者报告 | A0-01已发现split重复；A0-02未取得原图框／映射；small列定义仍待作者澄清 | P0；P1（数据/边界参考） | P0-A-C1/C2 | Partial：任务已有，预算机制未覆盖 | Reference Only；SCREENED，非DONE | [主全文](https://www.nature.com/articles/s41597-024-03952-3) | 2026-09-10 | [审计](../audits/W-0001_Audit.md) / PASS | 2026-09-10 / COMPLETE |
| W-0002 / N/A | Slicing Aided Hyper Inference and Fine-tuning for Small Object Detection | 2022 | IEEE ICIP | published | 整图缩放损失小目标细节 | VisDrone2019 test-dev；xView 75/25 | 均匀重叠切片、可选全图与切片微调 | 通用切片推理与微调 | 表1 TOOD AP50 29.4→34.7，640切片/25%重叠；非AP50:95 | 额外前向成本；SF改变训练；硬件测速未报告 | P0；N/A（无必要次方向） | P0-A-C1/C2 | Partial：裁剪放大及融合已有 | Must Read；SCREENED，非DONE | [主全文](https://arxiv.org/pdf/2202.06934v5) | 2026-09-10 | [审计](../audits/W-0002_Audit.md) / PASS | 2026-09-10 / COMPLETE |
| W-0003 / N/A | QueryDet: Cascaded Sparse Query for Accelerating High-Resolution Small Object Detection | 2022 | IEEE/CVF CVPR | published | 高分辨率头背景计算 | COCO mini-val/VisDrone val | 低分辨率QueryHead→CSQ稀疏高分辨率头 | 查询驱动空间稀疏计算 | 表1 COCO 无CSQ 38.53AP/4.85FPS→CSQ 38.36/14.88；2080Ti | 加速分母是高分辨率版本；端到端范围Unknown | P0；N/A（无必要次方向） | P0-A-C1/C2 | Partial：粗定位后精计算已有 | Must Read；SCREENED，非DONE | [主全文](https://arxiv.org/pdf/2103.09136v2) | 2026-09-10 | [审计](../audits/W-0003_Audit.md) / PASS | 2026-09-10 / COMPLETE |
| W-0004 / N/A | ESOD: Efficient Small Object Detection on High-Resolution Images | 2024（引用v2）；正式卷2025 | IEEE TIP 34:183–195 | published | 高分辨率稀疏小目标与冗余背景 | VisDrone/UAVDT/TinyPerson官方集合，见审计 | ObjSeeker/AdaSlicer/SparseHead，复用早期特征 | 选择特征块与稀疏检测 | 表III V100/batch1：36.2AP/26.1FPS→36.0/36.4，同1536 | 不同表FPS有差异；计时边界未全；SAM训练监督 | P0；N/A（无必要次方向） | P0-A-C1/C2 | Direct（广义区域节算机制）；具体铁路方案未核实 | Must Read；SCREENED，非DONE | [主全文](https://arxiv.org/pdf/2407.16424v2) | 2026-09-10 | [审计](../audits/W-0004_Audit.md) / PASS | 2026-09-10 / COMPLETE |
| W-0005 / N/A | ROI-Gated SAHI: Content-Adaptive Slicing-Based Inference for Efficient Object Detection | 2026 | arXiv | preprint | Full SAHI背景切片开销 | COCO128同split校准/报告；另3案例 | YOLOv8n ROI→v8s切片；覆盖率阈值回退 | 区域门控与自适应路由 | 表I Full 263.73ms/.7569 AP50；ROI 298.24/.6602；混合258.46/.7305 | 硬件/完整计时Unknown；调参隔离不足；ROI求和/并集歧义 | P0；N/A（无必要次方向） | P0-A-C1/C2 | Direct：区域筛选、局部精检及阈值回退已有 | Must Read；SCREENED，非DONE | [主全文](https://arxiv.org/html/2608.23923v1) | 2026-09-10 | [审计](../audits/W-0005_Audit.md) / PASS | 2026-09-10 / COMPLETE |
| W-0006 / N/A | Integrated Visual Sensing and Efficient Deep Learning for UAV-Based Track Foreign Object Detection (RVGC-YOLO) | 2026 | IEEE Sensors Journal 26(7):10316–10326 | published | 铁路UAV异物精度与机载计算 | UAV-RSOD 2002，8:1:1；来源组隔离未报告 | C2f-RVG/GSConv/CA；Tiny再剪枝蒸馏 | 轻量铁路异物网络与Orin NX评价 | 表VI RVGC 89.60/63.72 mAP50/50:95；Tiny87.95/61.78及226.08FPS | FP16/batch1；计时排除CPU NMS；输入乱码Unknown；多模块 | P0；P1（已知路径基线） | P0-A-C1/C2 | Partial：任务与轻量部署已有；无显式走廊ROI | Reference Only；SCREENED，非DONE | [主全文](https://www.researchgate.net/publication/401474971_Integrated_Visual_Sensing_and_Efficient_Deep_Learning_for_UAV-Based_Track_Foreign_Object_Detection) | 2026-09-10 | [审计](../audits/W-0006_Audit.md) / PASS | 2026-09-10 / COMPLETE |
| W-0007 / N/A | MRU-YOLO: Marginal-Utility-Guided Selective Local Re-Observation for Small-Object Detection in UAV Imagery | 2026 | Remote Sensing 18(16):2680 | published | 预测后按剩余收益分配局部观察 | SeaDronesSee ODv2/VisDrone转换val；3seed | 9候选HGB效用Top2＋全局保护融合；K为片数预算 | 边际收益引导的有限局部计算 | 表4 Sea density/learned AP41.784/41.819；Vis21.690/21.725；表9 RTX3090 32.40/30.09ms | 同预算密度差仅0.035pp；无毫秒约束；val选checkpoint，计时排除网格生成 | P0；N/A（无必要次方向） | P0-A-C1/C2 | Direct：效用TopK与全局保护已有；铁路毫秒预算差异待核验 | Must Read；SCREENED，非DONE | [主全文](https://mdpi-res.com/d_attachment/remotesensing/remotesensing-18-02680/article_deploy/remotesensing-18-02680.pdf) | 2026-09-10 | [审计](../audits/W-0007_Audit.md) / PASS | 2026-09-10 / COMPLETE |
| W-0008 / N/A | Dynamic Zoom-in Network for Fast Object Detection in Large Images | 2018 | IEEE/CVF CVPR pp.6926–6935 | published | 高分辨率检测的顺序局部计算成本 | CPD train4321/test4088；WP100测试图 | R-net收益图＋Q-net顺序选区、历史置零、像素成本；含熵/贪心对照 | 成本感知的顺序放大检测 | 表2 CPD像素≤45%：相对AP102%、时间80%；WP≤35%：AP93%、时间45%；K-80 | 非VisDrone；像素非毫秒；p95/完整计时未报告；不等同新检测反馈重估 | P0；N/A（无必要次方向） | P0-A-C1/C2 | Direct（广义顺序收益/成本）；精确反馈机制Partial/Unknown | Must Read；SCREENED，非DONE | [主全文](https://openaccess.thecvf.com/content_cvpr_2018/papers/Gao_Dynamic_Zoom-In_Network_CVPR_2018_paper.pdf) | 2026-09-11 | [审计](../audits/W-0008_Audit.md) / PASS | 2026-09-11 / COMPLETE |

| W-0009 / N/A（原A10线索） | AutoFocus: Efficient Multi-Scale Inference | 2019 | IEEE/CVF ICCV pp.9745–9755 | published | 粗尺度定位小目标并减少多尺度细检测计算 | COCO train2017/val分析/test-dev；VOC2007 test | 新增FocusPixels预测头→FocusChips→跨尺度边界处理 | 学习粗尺度小目标支持并按区域放大 | 表1 COCO test-dev AP47.9/AP50 68.3；Titan X Pascal 6.4图/s，SNIPER同AP2.5图/s；作者报告 | 需训练额外头；批处理吞吐非整帧p95；无VisDrone证据 | P0；N/A（无必要次方向） | P0-A-C1/C2 | Direct：低响应选区与可恢复目标诊断已有；精确跨层统计Partial | Must Read；SCREENED，非DONE | [主全文](https://arxiv.org/pdf/1812.01600v2) | 2026-09-12 | [审计](../audits/W-0009_Audit.md) / PASS | 2026-09-12 / COMPLETE |

Metrics需含关键数值、指标定义/单位、数据划分与比较协议，并回链原文表号；完整身份、各发表日期、版本号、载体评级来源在审计记录和注册表核验。Closest Innovation引用台账ID；不存在候选时写N/A及范围观察项。Novelty Conflict使用None/Partial/Direct/Unknown并附理由，不能用空白表示无冲突。

## 跨方向索引（非主归属）

只引用主矩阵和唯一正文，不复制正文或完整事实行；主方向版本/结论变化时复核以下关系。各方向阶段门不因文献进入索引而解除。

| Work ID | Primary Paper | Main Matrix / Audit / Reference | 与本方向的关系 | Innovation / Scope ID | 阶段条件 / Last Checked |
|---|---|---|---|---|---|

A0-05数据证据更新：VisDrone文件级审计已交付，小目标数量支持继续；来源隔离与评价口径仍待确认。见[完整报告](../Experiments/A0-05_VisDrone_File_Audit.md)。未新增论文或精读DONE，既有机制的新颖性风险High不变。

A0-06协议更新（2026-09-11）：[数据用途与评价草案](../Experiments/A0-06_Evaluation_Protocol_Draft.md)已交付、未冻结；近邻数字须按其原评价器解释，不能因都标AP50:95就认为可直接比较。官方工具包的行排序、类别汇总和ignore分母待A0-07构造样例核验。无新增论文、Work ID、PASS或精读DONE。

A0-07更新（2026-09-11）：[有限语义核验](../Experiments/A0-07_Evaluator_Semantics_Check.md)的Python构造样例24/24通过；原版运行未完成，不能据此重算或改写近邻论文数字。无新增文献或阅读状态变化；风险High、A0整体HOLD。

A0-08决策（2026-09-11）：[剩余门审查](../Experiments/A0-08_Feasibility_Decision.md)选择先做一次单机制候选差异审查，复用既有证据，按候选定向补证；不是重开全方向检索。本轮未新增论文或改变PASS／HOLD／阅读状态。既有近邻的铁路候选描述仅作历史，当前通用无人机边界以研究计划为准。

## A0-09当前结论（2026-09-11）

新增W-0008全文PASS，阅读SCREENED；SRENet仅HOLD线索，详见周报。原有行保留历史证据，当前执行状态以[A0-09候选卡](../reviews/A0-09_Candidate_Review.md)为准：熵反馈／成本归一化候选DISMISSED，暂缓实现，A0整体HOLD，返回用户方向决策；不自动创建后续候选任务。

## 当前候选更新（2026-09-12-N1）

2026-09-13运行回链：100轮普通基线与cal48诊断已完成；跨尺度弱响应v0.1转HOLD，风险High不变。候选恢复336/558、P3-only338/558、密度429/558，暂不支持独立增量；见[实证报告](../Experiments/BT1_Cal48_Miss_Diagnosis.md)。下一项仅缓存失败归因，不重新制定训练方案。无新增论文、PASS、精读DONE或跨方向变更；下方为2026-09-12书面审查时状态。

[跨尺度同类弱响应候选](../reviews/Weak_Response_Candidate_Review.md)完成书面差异审查：PROPOSED、High风险，尚无模型证据，不能称创新成立。W-0009由原A10 HOLD升级为首次PASS，阅读仍SCREENED。[ViCrop-Det](../reviews/ViCrop_Det_HOLD_Review.md)因版本／协议疑点HOLD，但其内部信号免训练裁剪机制仍构成挑战；ASAHI2026原A14继续HOLD。旧A0-09熵反馈候选仍DISMISSED。下一项仅确定服务该候选的受限普通YOLO11n训练执行方案，模型运行未开放。


## 2026-09-14-BTD10：研究问题重审新增审计

旧选择机制HOLD，研究问题观察不自动升级为创新；下一项以[重审报告](../Research_Question_Reassessment_BTD10.md)为准。以下PASS仅表示审计用途明确。

| Work ID / Legacy ID | Title | Year | Venue | Publication Status | Problem | Dataset | Method | Contribution | Metrics | Limitations | Related Paper | Closest Innovation | Novelty Conflict | Reading Priority | Local Path/Reference | Date Added | Audit Reference / Status | Last Audited / Sync Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| W-0010 / N/A | TIDE: A General Toolbox for Identifying Object Detection Errors | 2020 | ECCV | published | 检测错误归因 | COCO/VOC/Cityscapes/LVIS；既有模型输出 | 六类错误及独立oracle ΔAP | 避免顺序修复混淆 | 附录表3定位ΔAP随IoU阈值变化；不是本项目召回 | 不可加；ignored处理曾更正；本项目语义未适配 | P0；N/A（无次方向） | N/A（BTD10未形成新主张；影响P0-A-C1/C2收缩） | Partial：诊断框架已有，不是新检测器 | Must Read；SCREENED，非DONE | [主全文](https://dbolya.github.io/tide/paper.pdf) | 2026-09-14 | [审计](../audits/W-0010_Audit.md) / PASS | 2026-09-14 / COMPLETE |
| W-0011 / N/A | A Normalized Gaussian Wasserstein Distance for Tiny Object Detection | 2022 | arXiv | preprint | 小框位置偏差与度量敏感 | AI-TOD test、VisDrone2019 val | 高斯框＋NWD，用于分配/NMS/损失 | 已有小目标相似度与训练分配机制 | 表4 AI-TOD Faster R-CNN AP11.1→17.8；表5 VisDrone AP50 38.0→38.5 | anchor-based主体；完整时延未报告；扩展版关系HOLD | P0；N/A（无次方向） | N/A（BTD10未形成新主张；影响P0-A-C1/C2收缩） | Direct：简单换距离/损失的提法已覆盖 | Must Read；SCREENED，非DONE | [主全文](https://arxiv.org/pdf/2110.13389v2) | 2026-09-14 | [审计](../audits/W-0011_Audit.md) / PASS | 2026-09-14 / COMPLETE |
| W-0012 / N/A | Adaptive NMS: Refining Pedestrian Detection in a Crowd | 2019 | CVPR | published | 密集行人抑制与重复框 | CityPersons/CrowdHuman训练及验证 | 学习密度子网→动态NMS阈值 | 按实例密度自适应抑制 | 表5 CrowdHuman FPN MR−2 52.35→49.73，非本项目指标 | 需密度网络；松阈值保留假框；无整帧p95 | P0；N/A（无次方向） | N/A（BTD10未形成新主张；影响P0-A-C1/C2收缩） | Direct：密度调NMS提法已覆盖 | Must Read；SCREENED，非DONE | [主全文](https://arxiv.org/pdf/1904.03629v1) | 2026-09-14 | [审计](../audits/W-0012_Audit.md) / PASS | 2026-09-14 / COMPLETE |

## 2026-09-14-BTD12：单机制否决审查

两项PASS均为近邻证据，非用户精读完成；RQ-BTD12-1 DISMISSED，不新增已成立创新。次归属N/A，无必要交叉索引。

| Work ID / Legacy ID | Title | Year | Venue | Publication Status | Problem | Dataset | Method | Contribution | Metrics | Limitations | Related Paper | Closest Innovation | Novelty Conflict | Reading Priority | Local Path/Reference | Date Added | Audit Reference / Status | Last Audited / Sync Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| W-0013 / N/A | Generalized Focal Loss V2: Learning Reliable Localization Quality Estimation for Dense Object Detection | 2020（引用v1） | CVPR2021 | published | 检测框质量排序 | COCO trainval35k/minival5K/test-dev | 四边分布Top-k与均值→DGQP质量评分 | 分布统计辅助定位质量估计 | 表2/4 R50 12轮minival AP40.2→41.1；表4均19.4FPS | 非YOLO11n/VisDrone；完整I/O与p95未明；正框质量不等于前景判别 | P0；N/A（无次方向） | N/A（RQ-BTD12-1观察；影响P0-A-C1） | Direct：分布质量评分已有，精确熵尺度式未认定同构 | Must Read；SCREENED，非DONE | [主全文](https://arxiv.org/pdf/2011.12885v1) | 2026-09-14 | [审计](../audits/W-0013_Audit.md) / PASS | 2026-09-14 / COMPLETE |
| W-0014 / N/A | Multivariate Confidence Calibration for Object Detection | 2020 | CVPR2020 Workshops / SAIAD | published | 检测分数条件校准 | COCO val许可子集70/30随机图像划分20次 | 分数＋位置/尺寸，多变量逻辑及beta校准 | 检测回归信息条件校准与D-ECE | 表1c SSD IoU.6、5维D-ECE：仅分数LC7.575%→相关LC5.111% | 非AP；原分数≥.3；无UAV低分恢复或整帧计时；高维过拟合 | P0；N/A（无次方向） | N/A（RQ-BTD12-1观察；影响P0-A-C1） | Direct：尺寸条件重评分已有；未覆盖全部精确公式 | Must Read；SCREENED，非DONE | [主全文](https://arxiv.org/pdf/2004.13546v1) | 2026-09-14 | [审计](../audits/W-0014_Audit.md) / PASS | 2026-09-14 / COMPLETE |
