# Innovation Ledger

以下均为待验证假设或系统接口，不是已证实贡献。方向校准后以YOLO铁路UAV感知为主线；不得把YOLO换版本、注意力模块、轨道中心线、开放集检测或校准本身宣称为创新。

## I01 YOLO铁路UAV小目标感知与错误驱动适配

- **Contribution Type**：候选检测方法/实证贡献；最终口径由实验决定。
- **Closest Prior Work**：YOLARC、YOLORS及铁路UAV/异物YOLO检测工作；投稿前必须补齐具体YOLO版本、数据和模块差异。
- **Already Published**：YOLO用于铁路/UAV、增加多尺度特征、注意力、检测头或数据增强均已有大量工作；单纯换成YOLO11不是创新。
- **Remaining Gap**：在严格场景划分下，哪些铁路UAV失败模式最关键；一个由错误证据选择的最小改动能否在相同计算预算下稳定改善小目标/远距离危险Recall。
- **Our Hypothesis H1**：相对原始YOLO11和等计算简单基线，一个预注册的最小适配可改善目标失败模式，同时维持可部署速度。
- **Evidence**：YOLO11n/s/m基线；尺寸/高度/遮挡/背景错误分层；单改动消融；参数/FLOPs/FPS；跨seed/场景结果。
- **Novelty Risk**：High。没有稳定增量时不称方法创新，改按强基线/应用系统论文写作。

## I02 开放环境候选对YOLO闭集盲区的增量价值

- **Contribution Type**：候选评估/系统贡献，不默认是开放集新方法。
- **Closest Prior Work**：通用OWOD、开放世界道路危险检测，以及ROSD铁路开放集异物检测；铁路几何风险推理也已有工作。
- **Already Published**：发现未见类别、铁路开放集异物检测、利用轨道关系判断侵入风险均已有近邻工作。
- **Remaining Gap**：在同一铁路UAV协议下，开放候选相对YOLO闭集检测能增加多少未见危险Recall，以及需要付出多少误报和复检负担。
- **Our Hypothesis H2**：YOLO-World或经核验的开放集候选能补充YOLO11闭集盲区，并在至少两组类别轮换中保持可接受候选负担。
- **Evidence**：严格held-out category轮换；Known mAP、Unknown Recall、FPR、每图候选数、速度和误报类型。
- **Novelty Risk**：High。铁路open-set已有工作；本项目只能争取公平协议、增量发现或系统价值。

## I03 YOLO检测到轨道风险告警的上下文转换

- **Contribution Type**：候选应用系统/决策价值贡献，不是新几何表示。
- **Closest Prior Work**：UAV铁路距离危险分级、标准轨距/中心距离风险量化、轨道边界关键点风险评估及中心线空间先验。
- **Already Published**：轨道Mask/中心线/边界、距离和区域风险分级均已有工作。
- **Remaining Gap**：在YOLO中心管线中，最简单的轨道上下文能否相对Detection-only降低无关告警，同时保持高风险Recall；未知候选是否因此变得可管理。
- **Our Hypothesis H3**：track-zone/boundary/distance上下文相对检测置信度告警提高风险AUPRC或降低每图误报；归一化几何只作可选消融。
- **Evidence**：Detection-only、类别规则、zone、boundary/distance及最小融合；高风险Recall/AUPRC、告警数和失败案例。
- **Novelty Risk**：High。只作为完整铁路应用价值时保留，不宣称首次提出空间风险。

## I04 风险可信度与后续接口

- **Candidate Role**：校准风险告警并输出供通信与主动感知使用的风险语义包；默认不是Paper 1独立创新。
- **Closest Prior Work**：待核验语义通信、任务导向通信和铁路协同感知工作。
- **Existing Work**：待核验。
- **Remaining Gap**：高风险事件概率校准是否改善复检排序，以及Paper 1信息是否足以支持后续“传什么”和“何时复检”。
- **Our Hypothesis H4**：校准后的高风险事件概率和来源字段可能改善top-k复检，并形成后续任务接口。
- **Method**：先定义语义责任，字段、单位和压缩方式由Paper 3冻结。
- **Evidence**：ECE/Brier/NLL、top-k review hit rate、接口完整性和后续任务模拟。
- **Novelty Risk**：High；Paper 1中只作为系统输出，不单独夸大为成熟贡献。

## 更新规则

- 新颖性风险为High时优先收缩为可证伪finding、降为辅助实验或删除。
- “使用了某个模块”不等于创新；只有相对最近工作的剩余差异及其证据才能进入论文贡献列表。
- 每次更新记录日期、触发文献/实验ID和变更理由。
- 代码投入不是保留创新的理由；证据与研究缺口才是。
