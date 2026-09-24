# Paper 1 阶段任务指南（干净稿 · PREP/IDLE）

> **2026-09-24：** 本文件替换历史上带冲突标记的稿，为 **Post-EI 预备包**进度表。  
> 全文默认 **IDLE**；**不得**从本文件选题覆盖 [`../00_Overview/Current_Stage.md`](../00_Overview/Current_Stage.md)（唯一 ACTIVE=P0_EI）。  
> 再授权后按阶段①→⑦推进；阶段④采集/训练须另书面授权。

更新：2026-09-24（Asia/Shanghai）。

学习笔记写法见 [`../00_Overview/Learning_Note_Method.md`](../00_Overview/Learning_Note_Method.md)。

## 总状态

| 阶段 | 名称 | 状态 |
|---|---|---|
| ① | Paper 1 专项知识 | IDLE（材料可读） |
| ② | 最近工作与问题冻结 | IDLE |
| ③ | 最小技术复现 | IDLE |
| ④ | 数据审计与建立 | IDLE · **禁提前开工** |
| ⑤ | 强基线与错误分析 | IDLE |
| ⑥ | 核心证据 | IDLE |
| ⑦ | 写作与投稿 | IDLE |

## 前置条件

练手论文（P0）中的 YOLO / 可复现基础可复用，不在本目录重复维护一份冲突副本。P0 未收口前本包保持 IDLE。

## 阶段①：Paper 1 专项知识

按顺序填写：

1. [`Learning_Notes/03_Open_World_Perception.md`](Learning_Notes/03_Open_World_Perception.md)  
2. [`Learning_Notes/04_Railway_Context_and_Risk.md`](Learning_Notes/04_Railway_Context_and_Risk.md)  
3. [`Learning_Notes/05_Experiment_Design_and_Uncertainty.md`](Learning_Notes/05_Experiment_Design_and_Uncertainty.md)

**完成门：** 能区分 closed-set / open-set / open-vocabulary / open-world / anomaly；能解释检测框 ≠ 铁路风险；能设计含 Known/Unknown 轮换、告警预算、场景隔离与失败判据的公平实验。

**数据政策：** 不收集项目数据。只允许框架样例、极小公开样例或合成张量验证概念。

## 阶段②：最近工作与问题冻结

按 [`Literature/Literature_Matrix.md`](Literature/Literature_Matrix.md) 检索：铁路侵界（Cao TITS、TIM OID）、OWOD/OSOD、SRLF/Meng、风险量化、conformal/预算近邻、UAV-OOD。使用精读模板并把证据写回矩阵。

**完成门：** ≥15 篇直接相关且近三年≥10 篇核验；C1/C2 均有「最近工作—缺口—方法—证据」链；主张、三类基线、主指标与失败判据冻结。若无明确缺口，修改或停止主张。

此阶段只记录数据需求，不下载大数据。

## 阶段③：最小技术复现

用官方小样例跑通：已知检测、一个未知候选、简单轨道区域风险规则；对齐手算与代码指标；建立运行记录。

**完成门：** 图像→风险告警最小链可运行；每步 I/O 可检查；正式数据需求明确。结果只证明流程正确。

## 阶段④：数据审计与建立（未开放）

仅 `Current_Stage` 再授权后开放。审计许可、类别、分辨率、视角、场景重复与标注质量；定义 Known/Unknown、风险标签与轨道区域；按物理场景/航次划分并冻结清单、哈希与标签版本。

**完成门：** 许可明确、泄漏检查为零、≥2 组 Unknown 轮换可执行、风险标签不只编码类别、测试集冻结。

**可用数据：** 公开/代理重组 + 异物道具等；**不要求** A（RailUAV-SOD）已发布。

## 阶段⑤：强基线与错误分析（未开放）

建立已知检测、未知候选、简单轨道风险三类基线；固定数据、预算、输入与评价；按尺寸/高度/遮挡/背景/类别分析错误。仅当证据指出瓶颈时，才测一个最小 YOLO 改动。

**决策门：** 基线不可复现则停；YOLO 改动无稳定价值则删；未知误报不可控则收缩 C1；简单轨道规则足够则不造复杂网络。

## 阶段⑥：核心证据（未开放）

最多五块：① 已知检测与错误分层；② 危险召回—告警预算；③ 轨道上下文风险排序；④ 删除未知支路 / 风险层；⑤ 场景/高度/遮挡/Unknown 轮换鲁棒性。随机性影响结论时用 3 种子。

## 阶段⑦：写作与投稿（未开放）

先冻主表、消融与失败图，再写 Methods/Experiments，最后 Intro/Related Work。数字回链 Run ID；Venue 按中位 TIM/Measurement 准备。

## 当前下一步（预备期）

**不要**从阶段④或数据集开始。维持 P0_EI；本包仅完善文献矩阵与提纲可读性。再授权后从阶段①检查项继续。
