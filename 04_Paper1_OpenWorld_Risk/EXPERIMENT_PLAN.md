# Paper 1 Experiment Plan

**Problem**：在相同物理侵界关系下，哪种铁路空间表示最能抵抗UAV高度、分辨率和轻度视角变化，并稳定支持高风险事件识别？  
**Finding Thesis**：本研究比较既有与候选空间表示，不宣称发明轨道中心坐标、归一化几何、开放集检测或风险校准；只有经严格对照支持的稳定性规律才可成为贡献。  
**Date**：2026-08-27  
**Version**：v2（H1–H3均为待证伪假设；v1保留在`versions/`）

## Claim Map

| Claim | 为什么重要 | 最小可信证据 | Linked Blocks |
|---|---|---|---|
| H1 局部轨道宽度归一化侵界量在UAV成像变化下比原始像素及现有空间表示更稳定 | 像素尺度随成像条件变化，但归一化的真实收益不能只靠直觉断言 | 同一场景/物理关系的跨高度、分辨率、视角比较；必须包含现有表示和误差传播 | B2、B4、B5 |
| H2 `unknownness × clearance violation`比单独未知度或几何更可靠地识别未知高风险事件 | 未知不等于危险，危险取决于侵界条件 | 无泄漏类别轮换、Unknown-only/Geometry-only/简单融合/随机Unknown对照 | B1、B3、B4、B5 |
| H3 高风险事件概率校准改善复检排序 | 检测置信度不等于风险概率，但校准并非方法创新 | 独立验证/测试、ECE/Brier/NLL及top-k复检命中率 | B3、B4、B5 |
| Anti-claim | 排除更强检测器、额外参数、标签捷径或数据泄漏 | 第二检测器、随机Unknown/删除研究、协议和哈希审计 | B1–B5 |

## Paper Storyline

- **Main paper最低要求**：最近工作差异清楚；匹配场景的成像条件协议可信；H1相对pixel、centerline、boundary、metric-gauge和可用BEV基线的证据充分；轨道分割误差不被隐藏。
- **有证据才保留**：H2未知高风险条件规律和H3复检排序校准。它们不自动升级为论文方法贡献。
- **Appendix支持**：额外类别轮换、退化强度、几何有效性分层和失败案例。
- **主动删除**：不服务H1–H3的检测器堆叠、通用开放集模块创新叙事、SLAM、多无人机通信和强化学习实验。

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

## B2 铁路解析与空间表示公平比较

- **Hypothesis**：局部轨道宽度归一化横向侵界量在匹配物理关系的UAV成像变化下，比原始像素及已有铁路空间表示波动更小，并与高风险事件保持更稳定关系。
- **Independent Variable**：空间表示类型；高度、分辨率和轻度视角条件。
- **Control**：同一场景、同一障碍物与物理位置；相同检测/分割结果或分别使用真值几何和预测几何；相同风险模型与训练预算。
- **Baseline**：raw pixel distance、centerline Euclidean distance、track-boundary/keypoint zone、standard-gauge metric distance、local-width-normalized clearance；标定可用时加入Homography/BEV。
- **Dataset/Split**：优先使用同场景多高度/多视角复采；否则使用保持物理关系且记录局限的可信重投影。普通缩放图只能支持缩放不变性，不能冒充飞行高度实验。
- **Metrics**：mIoU/Dice/Centerline Error；feature CV/variance、rank stability、与物理侵界/风险的monotonicity；风险AUPRC、高风险Recall和跨条件性能下降。
- **Success Criterion**：H1在预注册的多数条件和场景划分中相对最强现有表示有稳定效应，并在预测轨道几何下仍成立；不以单一退化或单一split判定成功。
- **Failure Interpretation**：若只优于raw pixel但不优于metric/BEV/boundary表示，则将结论降为基线复现；若真值几何成立而预测几何失败，论文问题转为误差传播；若均不成立，拒绝H1并停止扩大系统。
- **Output**：Geometry Table、可视化、误差传播图。
- **Priority**：MUST-RUN。

## B3 条件化未知高风险识别与辅助校准

- **Hypothesis**：未知度只有与clearance violation联合时才改善未知高风险识别；对高风险事件概率校准可能改善复检排序。
- **Independent Variable**：Unknownness使用方式、clearance条件形式、是否校准。
- **Control**：检测器、数据划分、风险训练预算和特征维度对照。
- **Baseline**：Unknownness only、Geometry only、简单拼接、`unknownness × clearance`、随机Unknown、no Calibration、Temperature Scaling。
- **Dataset/Split**：Split A/B/C，Known与Unknown对象分组报告。
- **Metrics**：未知高风险AUPRC/Recall、误报率、Macro-F1、ECE、Brier、NLL、top-k review hit rate与Reliability Diagram。
- **Success Criterion**：条件化融合相对Unknown-only、Geometry-only和简单拼接跨类别轮换稳定改善；校准在独立测试集改善概率质量或复检排序且不显著损害高风险Recall。
- **Failure Interpretation**：若简单拼接或随机Unknown同样有效，拒绝H2；若校准只改善ECE但不改善概率质量/复检动作，H3只保留为诊断；不添加复杂模块补救。
- **Output**：Risk Baseline、Calibration Results、关键案例。
- **Priority**：MUST-RUN。

## B4 完整消融与简洁性检查

- **Hypothesis**：H1–H3涉及的差异可被分别隔离，且不存在为了维持“大系统”而保留的无作用组件。
- **Independent Variable**：Semantic、Geometry、Unknown、Uncertainty及几何坐标形式的删除/替换。
- **Control**：主干、优化预算、种子、split和评价保持一致。
- **Baseline**：各空间表示；Unknown-only、Geometry-only、简单融合、条件化融合；未校准/校准。仅在H2/H3通过前置门后定义Full Model。
- **Dataset/Split**：主split加至少两组Unknown轮换；随机性显著时默认3 seeds。
- **Metrics**：风险Macro-F1/高风险Recall、开放集指标、ECE/Brier、参数与时延。
- **Success Criterion**：关键组件作用方向跨seed/split一致；Full相对更简单变体的收益足以支持复杂度。
- **Failure Interpretation**：删除组件无损时移除该组件并缩小论文主张，不添加更多模块补救。
- **Output**：Core Ablation Table、组件效应图。
- **Priority**：MUST-RUN。

## B5 鲁棒性、泛化、效率与失败诊断

- **Hypothesis**：H1在真实或可信匹配的高度、分辨率和轻度视角变化下具有边界清晰的优势；blur/brightness只用于感知误差诊断，不作为几何不变性主证据。
- **Independent Variable**：真实/可信成像条件、感知退化、Unknown类别轮换、可用时的第二数据集。
- **Control**：固定生成参数、原图映射、模型与评价流程。
- **Baseline**：B2全部空间表示；通过前置门的条件化模型与最强简单基线。
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
| M2 H1 Pilot | 解析与空间表示比较 | R007–R011 | H1相对现有表示有可重复信号才继续H2/H3 | 中高 | H1失败则停止扩大系统并重构论文 |
| M3 Conditional Tests | 仅对通过前置门的H2/H3做关键对照 | R012–R017 | 作用跨seed/split一致 | 高 | 无作用组件直接删除 |
| M4 Polish | 鲁棒性、效率、失败与写作 | R018–R023 | 表图可回链且结论不越界 | 中 | 冻结后不扩张范围 |

## Compute and Data Budget

- GPU型号、显存和可用时数尚未提供，因此不虚构GPU-hour估计；每个Run在启动前补填预算和超时条件。
- 默认在随机性会影响核心结论时使用3 seeds；若预算不足，先跑单seed决策实验，再只扩展关键配置。
- 最大瓶颈预计是数据规模、风险标注可信度和开放环境划分，而不只是算力。

## Final Checklist

- [ ] 最近工作差异表完成，未把已发表组成写成创新。
- [ ] 主表首先回答H1；H2/H3未通过门槛时已删除或降级。
- [ ] 数据与增强泄漏审计为0。
- [ ] 新颖性由删除研究隔离。
- [ ] 简洁性得到辩护，无作用组件被删除。
- [ ] 必做与可选运行已分开。
- [ ] 每个结论能回链到Run ID、配置和原始指标。
