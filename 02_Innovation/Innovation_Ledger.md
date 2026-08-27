# Innovation Ledger

以下均为待验证假设或系统接口，不是已证实贡献。2026-08-27最近工作审计后，I01–I03均已降级：不得把既有技术组成单独宣称为创新。

## I01 UAV成像变化下的铁路空间表示稳定性

- **Contribution Type**：候选实验发现与比较协议，不是新坐标系。
- **Closest Prior Work**：Wu et al. (2023) UAV铁路危险物距离分级；铁路风险量化工作使用轨道中心/标准轨距；Ning et al. (2026)使用轨道边界关键点和横向距离；CMF-Net使用轨道中心线距离衰减先验。详见`../01_Literature/Paper1_Novelty_Audit_2026-08-27.md`。
- **Already Published**：轨道中心线/边界作为参照、目标到轨道距离、标准轨距换算、距离风险分级均不能再称创新。
- **Remaining Gap**：是否缺少同一物理场景下，针对UAV跨高度、跨分辨率和轻度视角扰动，对pixel、centerline、track-boundary、metric-gauge、local-width-normalized及可用BEV表示进行受控比较。
- **Our Hypothesis H1**：局部轨道宽度归一化横向侵界量在上述变化下波动更小，并更稳定预测高风险事件。
- **Evidence**：同场景复采或可信重投影；feature variance、rank/monotonic stability、风险AUPRC/高风险Recall、跨条件性能下降；轨道分割误差传播。
- **Novelty Risk**：High。只有严格实验发现和比较协议可能保留；禁止宣称“首次提出铁路归一化几何”。

## I02 条件化未知高风险识别

- **Contribution Type**：候选条件规律/评估发现，不是开放集检测器创新。
- **Closest Prior Work**：通用OWOD、开放世界道路危险检测，以及ROSD铁路开放集异物检测；铁路几何风险推理也已有工作。
- **Already Published**：发现未见类别、铁路开放集异物检测、利用轨道关系判断侵入风险均已有近邻工作。
- **Remaining Gap**：未知度是否只有在发生clearance violation时才应提高风险，以及这种条件化关系能否跨未知类别轮换稳定成立。
- **Our Hypothesis H2**：`unknownness × normalized clearance violation`比unknownness-only、geometry-only和简单拼接更可靠地识别未知高风险事件。
- **Evidence**：严格held-out category轮换；Unknownness-only、Geometry-only、简单融合和随机Unknown对照；未知高风险AUPRC/Recall、误报和top-k复检命中率。
- **Novelty Risk**：High。H1未成立或铁路开放集最近工作已覆盖同一设定时，降为附加分析或删除。

## I03 高风险事件概率校准

- **Contribution Type**：辅助可靠性验证，不作为独立方法创新。
- **Closest Prior Work**：安全检测器校准和不确定性感知风险识别已有成熟工作，近期工作已报告calibrated risk scores与risk uncertainty。
- **Already Published**：Temperature Scaling、ECE、Brier、风险概率校准和风险不确定性本身均非创新。
- **Remaining Gap**：在本任务定义下，校准高风险事件概率是否改善人工复检排序；该问题只有在风险标签和部署动作清晰时才有意义。
- **Our Hypothesis H3**：验证集拟合的风险校准可改善Brier/NLL/ECE和top-k review hit rate，但不保证改善检测精度。
- **Evidence**：独立验证/测试、分布漂移分层、校准前后复检排序与失败案例。
- **Novelty Risk**：High。默认只作为Paper 1完整性实验；没有新设定或形式保证时不列为核心贡献。

## I04 Risk Semantic Representation

- **Candidate Innovation**：输出供通信与主动感知使用的风险语义包。
- **Closest Prior Work**：待核验语义通信、任务导向通信和铁路协同感知工作。
- **Existing Work**：待核验。
- **Remaining Gap**：Paper 1信息是否足以支持后续“传什么”和“何时复检”。
- **Our Hypothesis**：语义/未知、铁路几何、风险和不确定性的紧凑表示可作为后续任务接口。
- **Method**：先定义语义责任，字段、单位和压缩方式由Paper 3冻结。
- **Evidence**：接口完整性、消融和后续任务模拟。
- **Novelty Risk**：High；Paper 1中只作为系统输出，不单独夸大为成熟贡献。

## 更新规则

- 新颖性风险为High时优先收缩为可证伪finding、降为辅助实验或删除。
- “使用了某个模块”不等于创新；只有相对最近工作的剩余差异及其证据才能进入论文贡献列表。
- 每次更新记录日期、触发文献/实验ID和变更理由。
- 代码投入不是保留创新的理由；证据与研究缺口才是。
