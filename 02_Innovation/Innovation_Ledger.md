# Innovation Ledger

以下均为候选创新和待验证假设，不是已证实贡献。

## I01 Railway-Normalized Geometry

- **Candidate Innovation**：以铁路方向、中心线和局部宽度归一化表达对象空间关系。
- **Closest Prior Work**：待Week 1/10核验3–5篇。
- **Existing Work**：待核验。
- **Remaining Gap**：是否缺少面向开放环境风险、并在UAV尺度退化下验证的铁路坐标表达。
- **Our Hypothesis**：归一化铁路几何比像素距离在尺度和高度样退化下更稳定。
- **Method**：Track Mask→Centerline/Width→longitudinal/lateral/overlap/scale。
- **Evidence**：Pixel vs Railway Geometry受控比较、误差传播和风险消融。
- **Novelty Risk**：Medium（待文献核验）。

## I02 Unknown-Aware Hazard Perception

- **Candidate Innovation**：对象语义未知时仍利用铁路空间关系判断风险。
- **Closest Prior Work**：待核验3–5篇。
- **Existing Work**：待核验开放集检测、铁路风险量化和空间关系方法的交集。
- **Remaining Gap**：未知发现是否真正进入风险推理而非只做检测评价。
- **Our Hypothesis**：Unknownness+Geometry在未知类别上提升高风险识别。
- **Method**：Semantic/Unknown score与Railway Geometry融合。
- **Evidence**：已知/未知分组结果、no Unknown与随机Unknown对照。
- **Novelty Risk**：High（Week 10必须复核）。

## I03 Uncertainty-Aware Risk Reasoning

- **Candidate Innovation**：对风险输出单独校准，并表达可用于主动感知的认知不确定性。
- **Closest Prior Work**：待核验3–5篇。
- **Existing Work**：待核验风险校准和铁路不确定性工作。
- **Remaining Gap**：检测分数是否被错误当作风险可信度，以及铁路风险输出是否缺少校准。
- **Our Hypothesis**：独立校准能改善风险概率可靠性，并识别需要复核的高风险高不确定样本。
- **Method**：Temperature Scaling、ECE、Brier、Reliability Diagram。
- **Evidence**：校准前后测试集比较与失败案例。
- **Novelty Risk**：Medium。

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

- 新颖性风险为High时优先重新设计或削弱主张。
- 每次更新记录日期、触发文献/实验ID和变更理由。
- 代码投入不是保留创新的理由；证据与研究缺口才是。
