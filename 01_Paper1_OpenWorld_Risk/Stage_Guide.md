# Paper 1阶段任务指南

本文件是Paper 1唯一进度表。Paper 1当前等待练手论文完成；不得从本文件选择任务覆盖[总项目当前任务](../00_Overview/Current_Stage.md)。

## 前置条件

练手论文中的[YOLO研究核心](../PrePaper_Lightweight_Detection/Learning_Notes/01_YOLO_Research_Core.md)和[PyTorch与可复现性](../PrePaper_Lightweight_Detection/Learning_Notes/02_PyTorch_and_Reproducibility.md)作为共用基础，只维护一份，不在Paper 1目录重复复制。

## 阶段1：Paper 1专项知识

练手论文完成后，按顺序填写：

1. [开放世界感知](Learning_Notes/03_Open_World_Perception.md)；
2. [铁路上下文与风险](Learning_Notes/04_Railway_Context_and_Risk.md)；
3. [实验设计与不确定性](Learning_Notes/05_Experiment_Design_and_Uncertainty.md)。

完成门：能区分closed-set/open-set/open-vocabulary/open-world/anomaly detection；能解释检测框为何不等于铁路风险；能设计包含Known/Unknown轮换、告警预算、场景隔离和失败判据的公平实验。

数据政策：不收集项目数据。只允许框架样例、极小公开样例或合成张量验证概念。

## 阶段2：最近工作与问题冻结

按[文献矩阵](Literature/Literature_Matrix.md)检索铁路UAV检测、铁路开放集异物检测、开放词汇检测、轨道侵界风险和风险校准；使用[论文模板](Literature/Paper_Note_Template.md)精读并把证据写回矩阵。

完成门：至少15篇直接相关论文完成核验，其中最近三年不少于10篇；C1/C2均形成“最近工作—缺口—方法—证据”链；主张、三类基线、主要指标和失败判据冻结。若无明确缺口，修改或停止主张。

此阶段只记录数据需求，不下载大数据。

## 阶段3：最小技术复现

用官方小样例跑通已知检测、一个未知候选和简单轨道区域风险规则，对齐手算与代码指标，并建立运行记录。

完成门：从图像到风险告警的最小链可运行，每步输入输出可保存检查，正式数据需求明确。结果只证明流程正确。

## 阶段4：数据审计与建立

此时才正式处理数据：审计许可、类别、分辨率、视角、场景重复和标注质量；定义Known/Unknown、风险标签与轨道区域；按物理场景或航次划分并冻结文件清单、哈希和标签版本。

完成门：许可明确、泄漏检查为零、至少两组Unknown轮换可执行、风险标签不只编码类别、测试集冻结。

## 阶段5：强基线与错误分析

建立已知检测、未知候选和简单轨道风险三类基线；固定数据、预算、输入和评价；按尺寸、高度、遮挡、背景和类别分析错误。只有证据指出明确瓶颈时，才测试一个最小YOLO改动。

决策门：基线不可复现则停止；YOLO改动无稳定价值则删除；未知误报不可控则收缩C1；简单轨道规则足够则不构造复杂网络。

## 阶段6：核心证据

最多五块：已知检测与错误分层；危险召回—告警预算；轨道上下文风险排序；必要删除实验；场景/高度/遮挡/未知轮换鲁棒性。随机性影响结论时使用3个种子。

## 阶段7：写作与投稿

先冻结主表、消融和失败图，再写Methods与Experiments，最后写Introduction和Related Work。所有数字回链到Run ID；投稿前核验正式版本、期刊范围、分区、预警和学校规则。
