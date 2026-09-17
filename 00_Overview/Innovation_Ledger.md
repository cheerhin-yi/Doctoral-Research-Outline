# 候选创新台账

本台账用于[每周文献审计](Literature_Tracking_Workflow.md)的证据联动，不替代研究计划，不确认创新成立，不增加主张。初始化日期2026-09-07；下列已有工作判断仅转录当前仓库矩阵，未在本轮重新核验原文。新论文通过审计后，所有直接受影响条目必须更新四个英文命名字段并追加变化记录。


2026-09-16变更：用户采用近程 EI 会议稿路线。新增 P0-EI-C1／P0-EI-C2（PROPOSED，非新算法）。P0-A-C1／C2 保持 HOLD。不删除旧行。

2026-09-10变更：用户授权P0切换主线A。旧P0-C0-1/2及其历史证据保留，下面对应两行四字段是旧判断，不再指导执行。P1两项主张及P2–7状态不变。

## 候选创新与来源

| Innovation ID | Related Paper | 候选主张/范围 | 原始依据 | 状态 |
|---|---|---|---|---|
| P0-C0-1 | P0 | 共享轻量P2–P4检测头的精度—计算折中 | [研究计划](../00_PrePaper_Lightweight_Detection/Research_Plan.md) C0-1 | 历史方案：2026-09-10退出执行，未验证 |
| P0-C0-2 | P0 | 理论轻量化转化为真实推理速度 | [研究计划](../00_PrePaper_Lightweight_Detection/Research_Plan.md) C0-2 | 历史方案：2026-09-10退出执行，未验证 |
| P0-A-C1 | P0 | 同整帧时间预算下提高无人机航拍已知小目标检出 | [主线A计划](../00_Startup_Railway_UAV_Detection/Research_Plan.md) | 当前区域机制HOLD；BTD9强基线挑战成立，未形成替代创新 |
| P0-A-C2 | P0 | 区域选择漏检与端到端预算控制 | 同一计算分配机制的失败边界 | HOLD；非独立创新，不再自动扩展旧选区方案 |
| P0-EI-C1 | P0 | 固定 YOLO11n 与已声明预算口径下，整图1280比当前密度单片更准且更快（协议／对比，非新算法） | [Mainline_A_Current](../00_Practice_UAV_Aerial_Detection/Mainline_A_Current.md)；cal48／F1280／密度单片已有证据 | PROPOSED；2026-09-16 采用；指导近程 EI 稿 |
| P0-EI-C2 | P0 | 区域分配可恢复空间≠可部署增益；须同时报告超时率与选择漏检（协议／对比，非新算法） | 同上；BTD1–7、BTD11；GT 选择净增33 | PROPOSED；2026-09-16 采用；指导近程 EI 稿 |
| P1-C1 | P1 | 已知＋未知双路径在固定告警预算下提高危险召回 | [研究计划](../01_Paper1_OpenWorld_Risk/Research_Plan.md) C1 | 暂定，执行等待练手论文 |
| P1-C2 | P1 | 轨道上下文风险排序提高告警决策价值 | [研究计划](../01_Paper1_OpenWorld_Risk/Research_Plan.md) C2 | 暂定，执行等待练手论文 |

## 创新证据与风险

| Innovation ID | Closest Prior Work | Existing Work | Remaining Gap | Novelty Risk | Evidence / Last Updated |
|---|---|---|---|---|---|
| P0-C0-1 | L1-01 LUD-YOLO；L1-02 BPD-YOLO；共享头直接近邻仍待补 | 已有UAV轻量化和高分辨率检测；精确共享范围未核验 | 待确认是否已有同构共享P2–P4头；B1→B2→M能否隔离收益 | Unknown；不能因尚未查到而判断低风险 | [练手矩阵](../00_PrePaper_Lightweight_Detection/Literature/Literature_Matrix.md)；2026-09-07，仓库转录 |
| P0-C0-2 | L3-02 EUAVDet；真实速度规范待补 | 已有边缘设备FPS证据，不能只比GFLOPs | 固定硬件、输入、batch和计时边界下，共享头是否改善延迟仍待验证 | Unknown；部署测速本身不是默认创新 | [练手矩阵](../00_PrePaper_Lightweight_Detection/Literature/Literature_Matrix.md)；2026-09-07，仓库转录 |
| P0-A-C1 | W-0002–W-0009区域近邻；W-0011小框度量；W-0013分布质量／W-0014条件校准；BCDet HOLD | 区域收益排序、小框度量已有；分布统计质量评分及尺寸条件校准亦已有 | BTD11低分GT修复补559仅为诊断；BTD12具体评分式没有已证独立机制差异，DISMISSED；新论文主张待决，不自动再试 | High；旧区域机制HOLD，新评分候选否决，换检测器或拟合形式不足以支持新颖 | [BTD12](../00_Startup_Railway_UAV_Detection/Literature/BTD12_Low_Score_Candidate_Review.md)；2026-09-14 |
| P0-A-C2 | W-0005/7/8/9；W-0010诊断参考、W-0012后处理近邻 | 全局保护、有限片数与回退已有；错误分解、密度自适应NMS已有 | 完整计时已做，当前区域路线无优势；缺F1280 NMS前轨迹，最终输出无法确证误删；BTD11已完成缓存筛查；35图截断，41个高GT重叠小目标不足以直接确证NMS瓶颈 | High；HOLD，预算计时或密度调阈值本身不是新机制 | [BTD10](../00_Startup_Railway_UAV_Detection/Research_Question_Reassessment_BTD10.md)、[W-0012](../00_Startup_Railway_UAV_Detection/Literature/W-0012_Audit.md)；2026-09-14 |
| P0-EI-C1 | 整图高分辨率与切片／选区近邻（仓库已有审计） | 本仓库 cal48 上 F1280 与密度单片对照已完成 | 会议披露口径、4090 同口径时间表是否补测、test-dev 终评是否需要 | Medium；主张是协议比较不是新检测头 | [Mainline_A_Current](../00_Practice_UAV_Aerial_Detection/Mainline_A_Current.md)；2026-09-16 |
| P0-EI-C2 | 预算／选区失败边界类近邻 | BTD 诊断已显示可恢复空间与超时／漏检张力 | 不得把 oracle／低分修复写成方法精度；须联合报告超时率与选择漏检 | Medium；失败边界主张 | 同上；2026-09-16 |
| P1-C1 | T2-01 ROSD；T2-02/T2-03强基线；T2-07未知路径候选；W-0001/W-0006仅已知检测参考 | 铁路开放集检测、通用开放世界及VLM OOD已有工作 | 固定告警预算下铁路危险召回仍待核验；W-0001/W-0006不提供未知／告警证据 | High（沿用原风险；2026-09-10补入已知路径参考，未改变主张） | [Paper 1矩阵](../01_Paper1_OpenWorld_Risk/Literature/Literature_Matrix.md)；2026-09-10增补边界，保留2026-09-07旧证据 |
| P1-C2 | T1-01、T3-02、T3-03；W-0001仅分割数据参考 | 轨道距离、边界、危险分级和风险量化已有直接工作 | 未知候选＋轨道上下文＋告警排序增量仍待核验；W-0001分割真值不提供风险标注 | High（沿用原风险；2026-09-10只补数据边界） | [Paper 1矩阵](../01_Paper1_OpenWorld_Risk/Literature/Literature_Matrix.md)；2026-09-10增补边界，保留2026-09-07旧证据 |

Novelty Risk统一用 `Low / Medium / High / Unknown`，附理由、证据及核验日期；新版本不得静默抹掉旧风险结论。Closest Prior Work可以列多个工作ID；旧ID需带方向，不能跨矩阵裸引用。Remaining Gap要写可被证伪的差异，不写笼统的“效果更好”。

主线A额外约束（W-0007）：MRU已有边际效用Top-K与全局保护；效用学习相对同预算密度选择的AP差只有0.035个百分点（两数据集），不能把局部观察总收益归因排序器。毫秒预算及走廊先验尚需独立证据，不能作为当然创新。

## 暂停方向边界观察

下列ID只是边界观察项，不是候选创新；Closest Innovation应写 `N/A（尚未定义候选创新；观察P2-SCOPE等）`。若新文献影响其方向，更新对应行；正式启动且用户确定主张后才创建创新ID，每篇最多两项。

| Scope ID | 方向依据 | Closest Prior Work | Existing Work | Remaining Gap | Novelty Risk |
|---|---|---|---|---|---|
| P2-SCOPE | [P2三维灾害定量](../02_Paper2_3D_Disaster/README.md) | 未审计 | 已存损伤分割/三维分割背景，非定量测量证据 | 尚未定义候选创新 | Unknown；PAUSED |
| P3-SCOPE | [P3通信受限感知](../03_Paper3_Comm_Perception/README.md) | 未审计 | 已存通信综述/边缘传输背景 | 尚未定义候选创新 | Unknown；PAUSED |
| P4-SCOPE | [P4风险ISAC](../04_Paper4_Risk_ISAC/README.md) | 未审计 | 已存定位通信/RIS背景，非风险驱动证明 | 尚未定义候选创新 | Unknown；PAUSED |
| P5-SCOPE | [P5多模态风险](../05_Paper5_Multimodal_Risk/README.md) | 未审计 | 已存视觉退化背景，非多模态证据 | 尚未定义候选创新 | Unknown；PAUSED |
| P6-SCOPE | [P6主动巡检](../06_Paper6_Active_Inspection/README.md) | 未审计 | 已存UAV-ITS/航迹背景，非风险复检证据 | 尚未定义候选创新 | Unknown；PAUSED |
| P7-SCOPE | [P7多机决策](../07_Paper7_MultiUAV_Decision/README.md) | 未审计 | 已存Agentic/网络背景，非任务分配直接证据 | 尚未定义候选创新 | Unknown；PAUSED |

## 文献影响与待决动作

本批2026-09-10-Mainline-A产生如下真实文献影响；这些是审查／预案，不是实验结果。每个影响ID一行。

| Impact ID / Batch | Work ID / Audit | Innovation or Scope ID | Changed Fields / Risk Before → After | 边界原条款与建议 | 最小验证：假设、唯一变量、指标、停止条件 | Target Experiment Plan / Entry | Status / Stage Gate | Decision / Run ID / Outcome |
|---|---|---|---|---|---|---|---|---|
| I-2026-09-10-Mainline-A-01 | [W-0001](../00_Startup_Railway_UAV_Detection/Literature/W-0001_Audit.md) | P0-A-C1/C2；P1-C1/C2（范围） | 四字段；P0 Unknown→High（批次综合）；P1 High→High | 旧LSM退出执行；Partial：任务已有，预算机制未覆盖 | 见该审计最小验证；固定策略变量，报告小目标/区域漏检/整帧成本；无增量或数据不成立则停 | [A2-DIAG](../00_Startup_Railway_UAV_Detection/Experiments/Experiment_Plan.md)；A0数据审计 | BLOCKED（模型）；A0静态审查允许 | 用户已选A，仅审查；Run ID=N/A，未运行 |
| I-2026-09-10-Mainline-A-02 | [W-0002](../00_Startup_Railway_UAV_Detection/Literature/W-0002_Audit.md) | P0-A-C1/C2 | 四字段；P0 Unknown→High（批次综合）；P1 High→High | 旧LSM退出执行；Partial：裁剪放大及融合已有 | 见该审计最小验证；固定策略变量，报告小目标/区域漏检/整帧成本；无增量或数据不成立则停 | [A2-DIAG](../00_Startup_Railway_UAV_Detection/Experiments/Experiment_Plan.md) | BLOCKED（模型）；A0静态审查允许 | 用户已选A，仅审查；Run ID=N/A，未运行 |
| I-2026-09-10-Mainline-A-03 | [W-0003](../00_Startup_Railway_UAV_Detection/Literature/W-0003_Audit.md) | P0-A-C1/C2 | 四字段；P0 Unknown→High（批次综合）；P1 High→High | 旧LSM退出执行；Partial：粗定位后精计算已有 | 见该审计最小验证；固定策略变量，报告小目标/区域漏检/整帧成本；无增量或数据不成立则停 | [A2-DIAG](../00_Startup_Railway_UAV_Detection/Experiments/Experiment_Plan.md) | BLOCKED（模型）；A0静态审查允许 | 用户已选A，仅审查；Run ID=N/A，未运行 |
| I-2026-09-10-Mainline-A-04 | [W-0004](../00_Startup_Railway_UAV_Detection/Literature/W-0004_Audit.md) | P0-A-C1/C2 | 四字段；P0 Unknown→High（批次综合）；P1 High→High | 旧LSM退出执行；Direct（广义区域节算机制）；具体铁路方案未核实 | 见该审计最小验证；固定策略变量，报告小目标/区域漏检/整帧成本；无增量或数据不成立则停 | [A2-DIAG](../00_Startup_Railway_UAV_Detection/Experiments/Experiment_Plan.md) | BLOCKED（模型）；A0静态审查允许 | 用户已选A，仅审查；Run ID=N/A，未运行 |
| I-2026-09-10-Mainline-A-05 | [W-0005](../00_Startup_Railway_UAV_Detection/Literature/W-0005_Audit.md) | P0-A-C1/C2 | 四字段；P0 Unknown→High（批次综合）；P1 High→High | 旧LSM退出执行；Direct：区域筛选、局部精检及阈值回退已有 | 见该审计最小验证；固定策略变量，报告小目标/区域漏检/整帧成本；无增量或数据不成立则停 | [A2-DIAG](../00_Startup_Railway_UAV_Detection/Experiments/Experiment_Plan.md) | BLOCKED（模型）；A0静态审查允许 | 用户已选A，仅审查；Run ID=N/A，未运行 |
| I-2026-09-10-Mainline-A-06 | [W-0006](../00_Startup_Railway_UAV_Detection/Literature/W-0006_Audit.md) | P0-A-C1/C2；P1-C1（已知路径） | 四字段；P0 Unknown→High（批次综合）；P1 High→High | 旧LSM退出执行；Partial：任务与轻量部署已有；无显式走廊ROI | 见该审计最小验证；固定策略变量，报告小目标/区域漏检/整帧成本；无增量或数据不成立则停 | [A2-DIAG](../00_Startup_Railway_UAV_Detection/Experiments/Experiment_Plan.md) | BLOCKED（模型）；A0静态审查允许 | 用户已选A，仅审查；Run ID=N/A，未运行 |

| I-2026-09-10-Mainline-A-07 | [W-0007](../00_Startup_Railway_UAV_Detection/Literature/W-0007_Audit.md) | P0-A-C1/C2 | 四字段；High→High，补充更直接预算/效用先例 | 固定K、边际效用、全局保护已有；不复制多模块 | 同检测器/融合只换选择策略；对照密度TopK，测小目标召回及完整延迟；无增量或数据不足则停 | [A2-DIAG](../00_Startup_Railway_UAV_Detection/Experiments/Experiment_Plan.md) | BLOCKED，等待A0 | Run ID=N/A，未运行 |

状态：`PROPOSED / BLOCKED / READY / IMPLEMENTED / DISMISSED`。只有阶段允许且方案决定明确时才更新实验计划；只有真实运行才填写Run ID。High风险必须提出核验或主张收缩建议，不能通过自动增加模块规避。

## A0-02补证影响

I-2026-09-10-A0-02-01：W-0001 → P0-A-C1/C2及P1数据边界。Closest Prior Work／Existing Work沿用上表已审计机制；Remaining Gap新增官方入口仍未补齐原图框和来源分组；Novelty Risk保持High，不因数据补证降低。最小动作是取得可复核作者资料并重审原图配对、来源组与小目标数量，无法取得则继续HOLD。目标：[实验计划](../00_Startup_Railway_UAV_Detection/Experiments/Experiment_Plan.md)保持BLOCKED；Run ID=N/A。P1仅补数据适用范围，主张不变。

## 用户范围决定：2026-09-10-A0-04

沿用P0-A-C1/C2并更新上表四字段：保留无人机、实时性、小目标，VisDrone优先；原轨道先验差异与UAV-RSOD数据门退为历史，不再要求等作者回复。旧判断仍由A0-01/A0-02审计和铁路版计划回链。风险High→High；下一项A0-05静态数据审计，方法／模型BLOCKED，Run ID=N/A。Paper 1及七篇路线不变。

## 数据补证2026-09-10-A0-05

未新增论文；P0-A-C1/C2的Closest Prior Work与Existing Work沿用既有近邻；Remaining Gap从文件未知推进为共享场景、忽略区评价与副本身份待确认。Novelty Risk保持High；284,915个标签层小框不证明算法创新或独立物理实例数。见[完整审计](../00_Startup_Railway_UAV_Detection/Experiments/A0-05_VisDrone_File_Audit.md)。下一项A0-06协议审查；模型BLOCKED，Run ID=N/A。

## 协议补证2026-09-11-A0-06

P0-A-C1/C2：Closest Prior Work与Existing Work沿用现有近邻；Remaining Gap进一步明确为评价器兼容性、真实预算下增量及共享场景限制，协议提案不证明这些缺口已解决；Novelty Risk仍High。见[A0-06草案](../00_Startup_Railway_UAV_Detection/Experiments/A0-06_Evaluation_Protocol_Draft.md)。下一项A0-07仅核验评价工具，模型BLOCKED，Run ID=N/A。无新增文献，Paper 1主张及暂停方向不变。

## 评价核验2026-09-11-A0-07

P0-A-C1/C2的Closest Prior Work与Existing Work不变；Remaining Gap中评价语义获得24个Python构造样例支持，原版数值兼容仍待交叉运行，数据来源和机制增量门未关闭；Novelty Risk仍High。见[A0-07报告](../00_Startup_Railway_UAV_Detection/Experiments/A0-07_Evaluator_Semantics_Check.md)。此为评价审计，不是创新或模型性能证据；下一项A0-08评测方案与剩余门审查，模型BLOCKED、Run ID=N/A。

## 可行性决策2026-09-11-A0-08

P0-A-C1/C2的Closest Prior Work与Existing Work沿用既有审计；Remaining Gap的首要研究问题是撤去铁路先验后尚无具体可区分机制，计时规范或评价修正不能独立构成算法贡献；Novelty Risk保持High。评测选择原版兼容＋小目标诊断，来源与运行兼容未通过。见[A0-08决策](../00_Startup_Railway_UAV_Detection/Experiments/A0-08_Feasibility_Decision.md)。下一项A0-09只审查一个候选及否决条件，不能自动叠加模块；无新文献、无模型Run ID。

## 候选否决影响2026-09-11-A0-09

I-2026-09-11-A0-09-01：新增[W-0008](../00_Startup_Railway_UAV_Detection/Literature/W-0008_Audit.md) → P0-A-C1/C2。上表四字段已同步：Closest Prior Work加入DZN；Existing Work补顺序收益选区、历史置零、像素成本和熵／贪心对照；Remaining Gap尚不能支持具体熵反馈／成本归一化候选的独立差异；Novelty Risk High→High。当前候选DISMISSED，广义研究问题保留。

最小可证伪对照仅作记录：固定检测器、候选、融合及同一时间准入器，对照初始排序、只抑制已处理区、实际结果反馈重排；同时检查片数控制与时间控制。若优势只来自更多片、融合或准入器，则否决反馈主张。目标[实验计划](../00_Startup_Railway_UAV_Detection/Experiments/Experiment_Plan.md)仍BLOCKED；没有执行，Run ID=N/A。当前停止自动扩展，交回用户方向决策，不启用RL或新增模块。P1与暂停方向无必要交叉更新。

## I-2026-09-12-N1-01：弱响应候选的保留范围

2026-09-14 BTD9强基线否决证据：F1280小TP1312、FP839，超过密度单片1172/1051与GT最佳1223/1038，实际时间亦优于密度。存在互补目标但GT逐图动作选择仅再增33，不支持直接包装为路由创新。暂缓当前区域排序机制，停止自动扩展实验。Closest Prior Work/Existing Work不变；Remaining Gap先退回研究问题重审，明确当前有限动作配置被强简单基线覆盖的范围及未解问题，不由互补集合推出新颖性；Novelty Risk High，v0.1 HOLD。见[报告](../00_Startup_Railway_UAV_Detection/Experiments/BTD9_F1280_Result.md)。无新文献/推理/训练，注册表和矩阵不变。下一项BTD10仅论证至多两个可证伪切入点，尚未执行。

2026-09-14 BTD8：单片GT上界对密度净增51小TP（+1.875pp），仅为有限动作诊断。密度K1均值37.36ms但20.83%帧次超重新校准40ms参考；F1280更快（27.33ms），效果尚未分析。暂缓新机制投入，下一项BTD9缓存强基线效果对照。Closest Prior Work/Existing Work不变；Remaining Gap先检查简单提高整图分辨率是否已覆盖单片选择上界，GT上界不证明新信号/同预算优势；Novelty Risk High，v0.1 HOLD。见[报告](../00_Startup_Railway_UAV_Detection/Experiments/BTD8_Single_Crop_Result.md)。本批cal48实际推理计时，无新训练/文献；注册表和矩阵状态不变。

2026-09-14 BTD7审查：105去重残差中26未覆盖、67覆盖未检出、12合并/匹配变化。固定第一片后的GT最佳第二片仅净增26小TP（+0.956pp），所查弱响应及第一片反馈计数未显示超越密度的排序证据；暂缓第二片重排作为唯一创新。Closest Prior Work/Existing Work仍为既有收益排序、顺序处理及历史抑制；Remaining Gap转为先确认预算能容纳的单片动作及其选择上界，不能从GT oracle推出实际信号或新颖性；Novelty Risk High，v0.1 HOLD。见[报告](../00_Startup_Railway_UAV_Detection/Experiments/BTD7_Conditional_Recovery_Result.md)。01归档失败与02接续均保留，无新文献、训练或推理；文献注册表/矩阵不变。下一项BTD8尚未运行。

2026-09-14 BTD6完整时间复测：3000次输出与BTD4逐值一致；固定两片平均约51.2ms、约99%帧次超过重新校准的40ms参考。工程实现更快仍不支持同预算优越，去重仅作强简单对照。Closest Prior Work/Existing Work不变；Remaining Gap仍是有限计算下条件新增检出价值，下一项BTD7核验去重剩余105个可恢复小GT及全窗口反例，区分推理可得信号与GT诊断上界；Novelty Risk High，弱响应v0.1 HOLD。见[结果](../00_Startup_Railway_UAV_Detection/Experiments/BTD6_Pipeline_Result.md)。无新增文献/训练；本次为既有规则实际推理与计时，文献注册表和矩阵状态不变。

2026-09-13 BTD5工程校核：有限构造/真实缓存输出完全一致，公共CPU合并平均约27ms降至6.27/6.57ms；不产生论文创新或整帧预算通过证据，资源协议偏差见[报告](../00_Startup_Railway_UAV_Detection/Experiments/BTD5_NMS_Result.md)。Closest Prior Work/Existing Work不变；Remaining Gap仍是完整预算内条件新增检出价值的可观测性，下一项BTD6须先校核真实流程并重新校准参考T；Novelty Risk High，弱响应v0.1 HOLD。无新论文、训练或推理，文献注册表与矩阵状态不变。

2026-09-13 BTD4预留开发验证：diag500固定去重规则净增273小GT、Recall+1.15pp，图像配对区间[+0.75,+1.56]pp；保留为强简单对照，不认定创新。两方法平均约90ms，约89%帧次超过相对T=61ms；预算仍未通过，公共结果合并约27ms。Closest Prior Work/Existing Work不变；Remaining Gap须在共用后处理合理实现和完整预算下重新判断条件新增价值，不能将去重或代码加速当创新；Novelty Risk High，跨尺度v0.1仍HOLD。见[报告](../00_Startup_Railway_UAV_Detection/Experiments/BTD4_Diag500_Result.md)。无新文献或训练，下一项公共后处理等价校核。

2026-09-13 BTD3简单对照更新：去重密度在cal48净增23个小GT、Recall+0.85个百分点，但逐图7/34/7且图像自助差区间跨0。保留为简单对照，不升级创新状态。Closest Prior Work/Existing Work仍沿用既有收益排序、覆盖抑制；Remaining Gap仍是条件新增检出价值的可观测性，先冻结两简单规则在diag500配对验证，不从48图继续加项；Novelty Risk=High，跨尺度v0.1=HOLD。见[结果](../00_Startup_Railway_UAV_Detection/Experiments/BTD3_Dedup_Density_Result.md)。无新论文、无训练或推理运行。

2026-09-13 BTD2缓存归因补记：密度残差129=77中心未覆盖+42覆盖但局部失败+10融合/匹配变化；77中66存在较大新增粗预测覆盖的未选恢复窗口，提示独立Top2的重复计数，但零新增粗框的重叠视图也有恢复反例。Closest Prior Work/Existing Work沿用MRU-YOLO收益排序、DZN历史抑制；Remaining Gap收窄为已选区域条件下新增检出价值能否由推理可得信号识别，先以简单去重密度排除；Novelty Risk=High，v0.1继续HOLD，不新增创新主张。见[归因报告](../00_Startup_Railway_UAV_Detection/Experiments/BTD2_Density_Miss_Analysis.md)。无新论文或模型运行。

2026-09-13实证更新：候选v0.1 **PROPOSED→HOLD**，新颖性风险High不变。BTD1-CAL48-20260913-01完成cal48固定对照：558个可恢复小GT，候选恢复336、P3-only338、密度429，未证明跨尺度额外选择价值。Closest Prior Work仍为既有MRU-YOLO/AutoFocus等；Existing Work仍覆盖响应选区与局部复检；Remaining Gap改为简单密度遗漏的可恢复目标是否具有额外推理可得信息，当前公式未解决；Novelty Risk不因实跑下降。见[实证报告](../00_Startup_Railway_UAV_Detection/Experiments/BT1_Cal48_Miss_Diagnosis.md)。下一项只读缓存归因密度遗漏的129个目标；不改公式、不训练、不自动增加模块。以下保留候选提出时依据，无新论文审计或阅读状态变化。

W-0009及[ViCrop-Det HOLD](../00_Startup_Railway_UAV_Detection/Literature/ViCrop_Det_HOLD_Review.md) → P0-A-C1/C2 → High保持。AutoFocus已覆盖粗尺度响应选区和可恢复GT诊断，ViCrop-Det已提出内部信号免训练裁剪；HOLD不代表可以忽略其冲突。旧A0-09否决结论保留。

[本批候选](../00_Startup_Railway_UAV_Detection/Literature/Weak_Response_Candidate_Review.md)只保留跨层空间／类别对应增加弱响应判别力这一可证伪假设。唯一变化为选区评分，固定权重、窗口、片数及融合；比较低阈值／匹配峰数／P3-only／原始跨层乘积／移位P4。指标为可恢复小GT检出、整体AP／误检、完整耗时及超预算比例。若简单替代解释收益、对应打乱仍等效或费用抵消收益则停止；不得增加模块挽救。

目标[Experiment_Plan](../00_Startup_Railway_UAV_Detection/Experiments/Experiment_Plan.md)的N1候选诊断条款；PROPOSED，模型运行BLOCKED，Run ID=N/A（未执行）。下一步仅制定受限普通YOLO11n训练执行方案，使后续模型观察服务这一候选；无个人学习验收门。P1／暂停方向无必要交叉变更。

## 2026-09-14-BTD10：主张收缩与问题观察

旧主张ID仅维持证据追踪；本批不新增P0-C3等创新主张。RQ-BTD10-1（定位／置信度失配）和RQ-BTD10-2（密集实例／重复框区分）只是问题观察，前者优先筛查、后者HOLD。BTD11后仍无可用信息差异则停止当前探索，不能把学习任务或无穷调参替代创新论证。

| Impact ID | Work ID | 影响项／四字段变化 | 最小变量与指标／停止条件 | 目标／状态／Run ID |
|---|---|---|---|---|
| I-2026-09-14-BTD10-01 | W-0010 | P0-A-C1/C2证据解释；Closest补TIDE、Existing错误分解已有、Gap本项目适配未证、Risk High不变 | 同缓存分别修复一种错误，统计变化；不相加oracle，语义不兼容则停止 | [BTD11](../00_Startup_Railway_UAV_Detection/Experiments/Experiment_Plan.md)预案；未执行／N/A |
| I-2026-09-14-BTD10-02 | W-0011 | P0-A-C1主张收缩／RQ1；Closest NWD、Existing小框度量已有、Gap本机失配瓶颈未知、Risk High | 固定预测检查定位／低分空间；无空间不开发新损失，有空间也不自动训练 | 同BTD11；新机制实现BLOCKED／N/A |
| I-2026-09-14-BTD10-03 | W-0012 | P0-A-C2边界／RQ2；Closest Adaptive NMS、Existing密度抑制已有、Gap原始删除轨迹缺失、Risk High | 当前仅检查邻接线索；未来固定原候选对照单一抑制规则，阈值即可解释则否决 | 同BTD11；原始模型取证未安排／N/A |

旧历史段落中的PROPOSED、未测等只反映当时状态，以本批主表为准。未修改P1创新四字段或P2–P7边界。

## 2026-09-14-BTD11：错误结构实证回链

[BTD11报告](../00_Startup_Railway_UAV_Detection/Experiments/BTD11_Error_Structure_Result.md)已完成。P0-A-C1/C2旧机制仍HOLD；RQ-BTD10-1收窄为低分真目标／假框判别的方案观察，RQ-BTD10-2不优先。Closest Prior Work保持W-0010/11/12及既有区域近邻；Existing Work仍包括错误分解、度量与密度抑制；Remaining Gap由“错误未分解”更新为“低分恢复空间已见，但可推理取得的信息差异及近邻外机制未知”；Novelty Risk High不变。

低分GT修复补559只是诊断；普通阈值.10补312而FP839→2170。不能把单调标定、换阈值或GT容量作为新方法。下一项BTD12仅一个方案与否决审查，无差异即停止候选开发。无新增文献／新创新ID、P1或暂停方向变更。

## 2026-09-14-BTD12：单机制否决

RQ-BTD12-1仅为审查对象，不是新创新主张ID；状态DISMISSED（书面新颖性否决，非实测失败）。Closest Prior Work=W-0013/14；Existing Work=分布质量评分与框尺度条件校准；Remaining Gap=尚无超出两者的独立可证伪关系；Novelty Risk=High。P0-A-C1主表四字段已更新，P0-A-C2与P1–P7不变。

| Impact ID | Work ID | 影响项／四字段变化 | 最小变量与指标／停止条件 | 目标／状态／Run ID |
|---|---|---|---|---|
| I-2026-09-14-BTD12-01 | W-0013 | P0-A-C1与RQ-BTD12-1；Closest新增GFLV2，Existing分布质量评分，Gap无独立关系，Risk High | 固定框池的分布信息组；固定FP召回/AP/完整耗时，现成评分解释收益则否决 | [BTD12计划](../00_Startup_Railway_UAV_Detection/Experiments/Experiment_Plan.md)；候选DISMISSED，无实验／N/A |
| I-2026-09-14-BTD12-02 | W-0014 | 同项；Closest条件校准，Existing尺寸条件评分，Gap组合式无独立证据，Risk High | 隔离校准与评价，先比较无分布类别/尺寸校准；仅校准误差改善不算检出贡献 | 同BTD12计划；候选DISMISSED，无实验／N/A |

[审查报告](../00_Startup_Railway_UAV_Detection/Literature/BTD12_Low_Score_Candidate_Review.md)保留条件性工程验证边界，但没有安排该实验。当前返回论文主张与投入方向决策，不自动创建BTD13，不恢复旧选区或加模块。
