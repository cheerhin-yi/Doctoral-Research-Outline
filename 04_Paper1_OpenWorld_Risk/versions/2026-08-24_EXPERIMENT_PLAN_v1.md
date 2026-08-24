# Paper 1 Experiment Plan

**Problem**：UAV铁路开放环境中的未知对象能否通过铁路结构获得可靠风险判断？  
**Method Thesis**：铁路归一化几何提供稳定风险坐标，未知性和经校准的不确定性使开放环境风险输出更可信。  
**Date**：2026-08-24  
**Version**：v1（所有主张均待实验验证）

## Claim Map

| Claim | 为什么重要 | 最小可信证据 | Linked Blocks |
|---|---|---|---|
| C1 铁路归一化几何比像素几何稳定 | 风险取决于相对线路位置，不应被分辨率/高度轻易改变 | 公平控制下跨退化比较、风险消融和失败分析 | B2、B4、B5 |
| C2 未知对象仍可借助几何与校准获得有用风险判断 | 开放环境不可能预先列举全部危险类别 | 严格无泄漏轮换、未知子集高风险Recall、no Unknown/no Calibration消融 | B1、B3、B4、B5 |
| Anti-claim | 排除更强检测器、额外参数、标签捷径或数据泄漏 | 第二检测器、随机Unknown/删除研究、协议和哈希审计 | B1–B5 |

## Paper Storyline

- **Main paper必须证明**：无泄漏开放环境协议；铁路几何对风险的必要性；未知性与校准的增量作用；完整系统在鲁棒性和效率上的边界。
- **Appendix支持**：额外轮换、退化强度、提示词敏感性和更多失败案例。
- **主动删除**：不服务C1/C2的检测器堆叠、SLAM、多无人机通信和强化学习实验。

## B1 数据完整性与检测/开放世界基线

- **Hypothesis**：在严格划分下，闭集、开放词汇和开放集方法呈现不同的已知/未知能力，且结果可由第二检测器交叉验证。
- **Independent Variable**：模型家族与开放环境机制。
- **Control**：同一原图组划分、输入尺度、评价代码和测试集；记录无法对齐的预训练差异。
- **Baseline**：YOLO11、RT-DETR、YOLO-World、Grounding DINO及1–2个最终核验的开放集基线。
- **Dataset/Split**：UAV-RSOD及Split A/B/C；许可、数量与类别均以审计结果为准。
- **Metrics**：mAP50–95、Recall、Unknown Recall；按定义选择AUROC/FPR95/A-OSE/Wilderness Impact；效率指标。
- **Success Criterion**：无Unknown训练实例、无增强泄漏；两类检测器结果可复现；开放环境指标通过手算测试。
- **Failure Interpretation**：若检测对象性不足，风险研究被上游瓶颈限制；若轮换排名剧变，主张必须改为类别条件化。
- **Output**：Baseline Table、Known/Unknown审计表、失败案例图。
- **Priority**：MUST-RUN。

## B2 铁路解析与归一化几何

- **Hypothesis**：Track Mask与Centerline可提供比原始像素坐标更稳定的铁路相关几何。
- **Independent Variable**：Pixel Geometry vs Railway-Normalized Geometry；退化强度。
- **Control**：相同目标、相同检测/分割输入与相同风险模型。
- **Baseline**：像素距离、仅框尺度；铁路归一化横向距离/纵向位置/重叠/相对尺度。
- **Dataset/Split**：有轨道Mask的冻结测试集及受控退化副本。
- **Metrics**：mIoU、Dice、Centerline Error、几何波动、下游Macro-F1/高风险Recall。
- **Success Criterion**：铁路几何在多数合理退化下波动更小，并对风险判断有一致增益。
- **Failure Interpretation**：若中心线误差抵消收益，先改进有效性标记或缩小到轨道结构可靠样本，不能夸大泛化。
- **Output**：Geometry Table、可视化、误差传播图。
- **Priority**：MUST-RUN。

## B3 未知感知风险与校准

- **Hypothesis**：Unknownness+Geometry提升未知对象风险识别；风险输出单独校准后可靠性改善。
- **Independent Variable**：是否使用Unknownness、是否使用Calibration。
- **Control**：检测器、数据划分、风险训练预算和特征维度对照。
- **Baseline**：Semantic only、Geometry only、Semantic+Geometry、随机Unknown、no Calibration、Temperature Scaling。
- **Dataset/Split**：Split A/B/C，Known与Unknown对象分组报告。
- **Metrics**：Macro-F1、高风险Recall、ECE、Brier、Reliability Diagram。
- **Success Criterion**：未知子集上获得稳定而非单一split的风险改善；测试集ECE/Brier改善且高风险Recall不被明显牺牲。
- **Failure Interpretation**：若随机Unknown同样有效，增益可能只来自额外参数；若校准无改善，检查验证集规模和分布漂移。
- **Output**：Risk Baseline、Calibration Results、关键案例。
- **Priority**：MUST-RUN。

## B4 完整消融与简洁性检查

- **Hypothesis**：C1/C2所需组件各自提供可隔离作用，Full Model不依赖不必要复杂度。
- **Independent Variable**：Semantic、Geometry、Unknown、Uncertainty及几何坐标形式的删除/替换。
- **Control**：主干、优化预算、种子、split和评价保持一致。
- **Baseline**：Semantic only、Geometry only、no Unknown、no Uncertainty、Pixel Geometry、Railway Geometry、Full Model。
- **Dataset/Split**：主split加至少两组Unknown轮换；随机性显著时默认3 seeds。
- **Metrics**：风险Macro-F1/高风险Recall、开放集指标、ECE/Brier、参数与时延。
- **Success Criterion**：关键组件作用方向跨seed/split一致；Full相对更简单变体的收益足以支持复杂度。
- **Failure Interpretation**：删除组件无损时移除该组件并缩小论文主张，不添加更多模块补救。
- **Output**：Core Ablation Table、组件效应图。
- **Priority**：MUST-RUN。

## B5 鲁棒性、泛化、效率与失败诊断

- **Hypothesis**：铁路几何主张在blur、brightness、resolution、scale和altitude-like degradation下仍有边界清晰的优势。
- **Independent Variable**：退化类型/强度、Unknown类别轮换、可用时的第二数据集。
- **Control**：固定生成参数、原图映射、模型与评价流程。
- **Baseline**：Pixel Geometry与Railway Geometry；完整模型与最强简单基线。
- **Dataset/Split**：冻结测试集的受控副本；第二数据集仅在许可与标签映射完成后使用。
- **Metrics**：各任务指标下降率、几何波动、FPS、latency、GPU memory、Params、FLOPs。
- **Success Criterion**：明确优势区间与失效点；所有效率测量可由硬件和批量设置复现。
- **Failure Interpretation**：若退化改变标签语义或产生伪影，该实验无效；若无第二数据集，只主张受控鲁棒性，不主张跨域泛化。
- **Output**：Robustness Table、Generalization Results、Failure Analysis。
- **Priority**：核心退化MUST-RUN；第二数据集NICE-TO-HAVE。

## Run Order and Decision Gates

| Milestone | 目标 | 主要Runs | Stop/Go Gate | 成本 | 风险与处理 |
|---|---|---|---|---|---|
| M0 Sanity | 数据、标签、指标、最小过拟合正确 | R000–R002 | 泄漏为0且手算指标一致才继续 | 低 | 先修数据/评价，不跑大实验 |
| M1 Baselines | 固定检测与开放环境基线 | R003–R006 | 至少两个检测家族可复现 | 中 | 上游失败则缩小主张 |
| M2 Main Method | 解析、几何、风险和校准贯通 | R007–R010 | 模块契约和主要指标有效 | 中高 | 分层定位错误传播 |
| M3 Decisions | 关键消融隔离C1/C2 | R011–R017 | 组件作用跨seed/split一致 | 高 | 无作用组件直接删除 |
| M4 Polish | 鲁棒性、效率、失败与写作 | R018–R023 | 表图可回链且结论不越界 | 中 | 冻结后不扩张范围 |

## Compute and Data Budget

- GPU型号、显存和可用时数尚未提供，因此不虚构GPU-hour估计；每个Run在启动前补填预算和超时条件。
- 默认在随机性会影响核心结论时使用3 seeds；若预算不足，先跑单seed决策实验，再只扩展关键配置。
- 最大瓶颈预计是数据规模、风险标注可信度和开放环境划分，而不只是算力。

## Final Checklist

- [ ] 主表覆盖C1/C2。
- [ ] 数据与增强泄漏审计为0。
- [ ] 新颖性由删除研究隔离。
- [ ] 简洁性得到辩护，无作用组件被删除。
- [ ] 必做与可选运行已分开。
- [ ] 每个结论能回链到Run ID、配置和原始指标。
