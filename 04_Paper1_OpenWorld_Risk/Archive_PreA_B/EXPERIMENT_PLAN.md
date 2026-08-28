# Paper 1 Experiment Plan

> **PAUSED（2026-08-28）**：本计划不是当前运行计划，所有B1–B5与M0–M4均保持未启动。A/B完成后必须根据其结果重新冻结主张和运行矩阵，尤其删除与前置论文A重复的封闭集校准实验。

**Problem**：如何以YOLO为铁路UAV实时感知核心，在小目标、复杂背景和开放类别条件下检测已知危险、补充未见危险候选，并转化为可复核的风险告警？  
**Research Thesis**：先建立和理解YOLO铁路危险检测能力，再用开放环境候选与轨道风险上下文弥补闭集检测的决策盲区；所有附加模块必须证明相对YOLO主基线的增量价值。  
**Date**：2026-08-27  
**Version**：v3（恢复YOLO感知主线；空间表示稳定性降为H3支撑消融）

## Claim Map

| Claim | 为什么重要 | 最小可信证据 | Linked Blocks |
|---|---|---|---|
| H1 YOLO主基线及一个错误驱动的最小适配改善铁路UAV危险检测 | YOLO是实时感知核心，必须先证明已知危险检测和小目标能力 | YOLO11n/s/m、固定训练预算、尺度/高度分层、单改动消融、速度与重复性 | B1、B2、B5 |
| H2 开放环境候选补充YOLO闭集盲区 | 实际危险类别无法穷举，但开放候选可能引入大量误报 | 无泄漏类别轮换；YOLO closed-set、YOLO-World及开放集基线；Unknown Recall与误报 | B1、B3、B5 |
| H3 轨道上下文将检测转成更有用的风险告警 | 检测到对象不等于发生侵界风险 | Detection-only、zone/boundary/distance规则与简单融合；高风险Recall、AUPRC和告警负担 | B4、B5 |
| H4 高风险事件概率校准改善复检排序 | 检测置信度不等于风险概率，但校准并非方法创新 | 独立验证/测试、ECE/Brier/NLL及top-k复检命中率 | B4、B5 |
| Anti-claim | 排除更强检测器、额外参数、标签捷径或数据泄漏 | 第二检测器、随机Unknown/删除研究、协议和哈希审计 | B1–B5 |

## Paper Storyline

- **Main paper最低要求**：YOLO11主基线可复现；铁路UAV小目标/高度/场景失败分层可信；任何YOLO改动有公平消融；开放候选和风险告警分别证明增量价值。
- **有证据才保留**：H1中的候选YOLO改动、H2开放环境补充、H4校准。无稳定收益就删除或降为附录。
- **Appendix支持**：RT-DETR参考结果、额外类别轮换、几何表示稳定性、阈值敏感性和更多失败案例。
- **主动删除**：同时堆叠Backbone/Neck/Head/Loss、与失败模式无关的注意力模块、SLAM、多无人机通信和强化学习实验。

## B1 数据完整性与YOLO主基线

- **Hypothesis**：YOLO11在严格划分和可复现配置下能够形成铁路UAV已知危险实时检测基线，不同模型规模呈现可解释的精度—速度折中。
- **Independent Variable**：YOLO11模型规模n/s/m；输入尺寸；只在预注册后比较一个必要训练设置。
- **Control**：同一原图组划分、输入尺度、评价代码和测试集；记录无法对齐的预训练差异。
- **Baseline**：YOLO11n为主基线，YOLO11s/m用于规模对照；RT-DETR仅作参考交叉验证，不决定主线。
- **Dataset/Split**：UAV-RSOD及Split A/B/C；许可、数量与类别均以审计结果为准。
- **Metrics**：mAP50–95、Precision、Recall、逐类AP、AP_small/尺寸分层Recall、FPS、latency、Params、FLOPs与显存。
- **Success Criterion**：数据与增强无泄漏；YOLO训练闭环和指标代码可复现；模型规模与速度测量公平；失败样例可按尺寸、高度、遮挡和背景分层。
- **Failure Interpretation**：若基线不稳定，先修数据/配置；若更大模型只是增加成本而不提高危险Recall，选择更小模型；未通过本块不得进入下游融合。
- **Output**：YOLO Baseline Table、Scale/Efficiency Curve、Failure Taxonomy。
- **Priority**：MUST-RUN。

## B2 YOLO错误驱动的最小铁路适配

- **Hypothesis**：针对B1中占比最高且可操作的铁路UAV失败模式，一个最小改动可能在可接受成本下稳定改善危险Recall。
- **Independent Variable**：仅一个预注册候选改动，例如切片/输入策略、多尺度特征、检测头或铁路数据增强；候选由B1证据选择，不预先堆叠。
- **Control**：同一YOLO规模、预训练权重、输入尺寸、epoch、增强预算、种子和评价；同时报告参数/FLOPs变化。
- **Baseline**：原始YOLO11；等参数或等计算对照；若改动涉及分辨率，加入只提高输入尺寸的简单基线。
- **Dataset/Split**：主split与至少一个场景/高度分层测试。
- **Metrics**：总体与小目标mAP50–95/Recall、高风险类别Recall、参数、FLOPs、FPS、显存和跨场景下降。
- **Success Criterion**：核心效应跨seed/场景方向一致，且相对简单计算扩张基线仍有价值。
- **Failure Interpretation**：无稳定收益则删除改动，论文转为强YOLO基线/应用系统；不得再叠加第二、第三个模块掩盖失败。
- **Output**：YOLO Minimal-Change Ablation、错误类型变化、效率曲线。
- **Priority**：MUST-RUN。

## B3 开放环境候选补充

- **Hypothesis**：开放词汇/开放集候选可以补充闭集YOLO未见类别盲区，但必须以可控误报为代价。
- **Independent Variable**：closed-set YOLO、YOLO-World及一个最终核验的开放集/异常候选基线；阈值在验证集冻结。
- **Control**：Known/Unknown文件清单、输入尺寸、测试集、对象匹配规则和指标代码；明确预训练知识差异。
- **Baseline**：YOLO11 closed-set、YOLO-World、可用的ROSD/OWOD或异常检测基线；Grounding DINO为NICE参考。
- **Dataset/Split**：Split A/B/C，Known与Unknown对象分组报告。
- **Metrics**：Known mAP/Recall、Unknown Recall、FPR、AUROC/FPR95及适用时的A-OSE/Wilderness Impact；每图候选数和推理成本。
- **Success Criterion**：至少两组held-out类别轮换中，未知Recall相对闭集YOLO提高且误报/候选负担可报告、可解释。
- **Failure Interpretation**：若误报不可控或结果只在单一轮换成立，H2降为失败分析；不能把开放词汇命名能力直接等同于open-world发现。
- **Output**：Open-Environment Baseline Table、Known/Unknown审计、误报案例。
- **Priority**：MUST-RUN。

## B4 轨道上下文风险告警与可信复检

- **Hypothesis**：简单轨道运行区域/侵界关系可以减少“检测到但不危险”的告警；风险概率校准可能进一步改善人工复检排序。
- **Independent Variable**：Detection-only、track zone/boundary、distance/overlap、可选归一化表示；未校准/校准。
- **Control**：固定YOLO/未知候选结果、风险标签、训练预算和split；轨道真值与预测结果分开报告。
- **Baseline**：Detection confidence alarm、类别规则、track-zone rule、boundary/distance rule、最小融合；Temperature Scaling只作辅助。
- **Dataset/Split**：主split及Known/Unknown分组；风险标注协议冻结。
- **Metrics**：高风险Recall、AUPRC、Macro-F1、每图告警数/误报、ECE/Brier/NLL、top-k review hit rate。
- **Success Criterion**：轨道上下文相对Detection-only降低无关告警且不明显牺牲高风险Recall；校准只有改善概率质量或复检收益才保留。
- **Failure Interpretation**：空间表示差异只作为消融；归一化无优势则采用最简单zone/boundary规则；校准无实际收益则删除。
- **Output**：Risk Alarm Table、空间/风险消融、Review Queue结果。
- **Priority**：MUST-RUN。

## B5 鲁棒性、泛化、效率与失败诊断

- **Hypothesis**：YOLO主基线、保留的最小改动、开放候选和风险告警在关键铁路UAV条件下具有可描述的性能边界。
- **Independent Variable**：目标尺寸/高度、分辨率、模糊、亮度、遮挡、场景、Unknown轮换和可用第二数据集。
- **Control**：固定生成参数、原图映射、模型与评价流程。
- **Baseline**：原始YOLO11、保留的YOLO改动、开放候选、Detection-only与最小风险告警。
- **Dataset/Split**：冻结测试集的受控副本；第二数据集仅在许可与标签映射完成后使用。
- **Metrics**：检测/未知/风险指标下降率、FPS、latency、GPU memory、Params、FLOPs；几何波动仅作风险环节诊断。
- **Success Criterion**：明确优势区间与失效点；所有效率测量可由硬件和批量设置复现。
- **Failure Interpretation**：若退化改变标签语义或产生伪影，该实验无效；若无第二数据集，只主张受控鲁棒性，不主张跨域泛化。
- **Output**：Robustness Table、Generalization Results、Failure Analysis。
- **Priority**：核心退化MUST-RUN；第二数据集NICE-TO-HAVE。

## Run Order and Decision Gates

| Milestone | 目标 | 主要Runs | Stop/Go Gate | 成本 | 风险与处理 |
|---|---|---|---|---|---|
| M0 Sanity | 数据、标签、指标、最小过拟合正确 | R000–R002 | 泄漏为0且手算指标一致才继续 | 低 | 先修数据/评价，不跑大实验 |
| M1 YOLO Baseline | 固定YOLO规模、速度和失败分层 | R003–R007 | YOLO主基线可复现且失败类型可信 | 中 | 基线失败则不做下游 |
| M2 YOLO Decision | 运行一个错误驱动的最小改动 | R008–R010 | 相对原始/简单扩算基线有稳定价值才保留 | 中高 | 无收益则回退原始YOLO |
| M3 Open/Risk Value | 分别检验未知候选和风险告警增量 | R011–R017 | 每个模块独立增加决策价值 | 高 | 无作用模块直接删除 |
| M4 Polish | 鲁棒性、效率、失败与写作 | R018–R023 | 表图可回链且结论不越界 | 中 | 冻结后不扩张范围 |

## Compute and Data Budget

- GPU型号、显存和可用时数尚未提供，因此不虚构GPU-hour估计；每个Run在启动前补填预算和超时条件。
- 默认在随机性会影响核心结论时使用3 seeds；若预算不足，先跑单seed决策实验，再只扩展关键配置。
- 最大瓶颈预计是数据规模、风险标注可信度和开放环境划分，而不只是算力。

## Final Checklist

- [ ] 最近工作差异表完成，未把已发表组成写成创新。
- [ ] 主表首先回答YOLO基线、失败模式和最小改动；开放环境与风险告警分别报告增量。
- [ ] RT-DETR只作参考，没有挤占YOLO主线预算。
- [ ] 没有同时堆叠多个YOLO改动；每项改变可单独归因。
- [ ] 数据与增强泄漏审计为0。
- [ ] 新颖性由删除研究隔离。
- [ ] 简洁性得到辩护，无作用组件被删除。
- [ ] 必做与可选运行已分开。
- [ ] 每个结论能回链到Run ID、配置和原始指标。
