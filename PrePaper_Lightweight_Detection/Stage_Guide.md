# 练手论文阶段任务指南

本文件是练手论文唯一进度表。每次只执行一个任务；完成证据直接写入学习笔记、文献矩阵或实验记录，不另建说明性任务清单。

## 阶段0：共同基础（当前）

按顺序完成：

1. [YOLO研究核心](Learning_Notes/01_YOLO_Research_Core.md)：检测链、指标手算、错误分类；
2. [PyTorch与可复现性](Learning_Notes/02_PyTorch_and_Reproducibility.md)：训练流程、运行记录、泄漏检查；
3. [实验设计与不确定性](Learning_Notes/03_Experiment_Design_and_Uncertainty.md)：公平对照、失败判据和统计边界。

每份笔记必须记录日期和资料，用自己的话回答问题，并至少留下一个结构图、手算或可检查流程。当前唯一任务由[Current_Stage.md](../00_Overview/Current_Stage.md)指定。

完成门：能解释YOLO完整检测链，能写出最小训练/验证流程，能手算主要指标并定义公平对照。此阶段不下载数据、不运行正式训练、不修改模型。

## 阶段1：专项学习

按顺序完成：

1. [小目标与多尺度](Learning_Notes/04_Small_Object_and_Multiscale.md)；
2. [轻量共享检测头](Learning_Notes/05_Lightweight_Shared_Head.md)；
3. [速度评价与部署](Learning_Notes/06_Efficiency_and_Deployment.md)。

完成门：P3–P5/P2–P5/P2–P4结构图、普通卷积与深度可分离卷积参数量手算、LSM-Head草图、B0/B1/B2/M唯一变量表和固定计时协议全部完成。此阶段仍不下载VisDrone、不修改模型。

## 阶段2：文献查新与方法冻结

在[文献矩阵](Literature/Literature_Matrix.md)中核验最近三年的P2、小目标检测头、参数共享和真实速度评价工作，并用[单篇模板](Literature/Paper_Note_Template.md)形成证据笔记。

完成门：至少12篇直接相关工作完成核验，其中最近三年不少于8篇；LUD-YOLO、BPD-YOLO和EUAVDet完成精读；同构风险、直接基线、速度口径和唯一方法改动冻结。若已有同构方法，修改叙事或终止，不增加模块规避冲突。

## 阶段3：最小代码复现

只用框架样例或极小公开样例跑通YOLO11n推理、训练、验证和复杂度/延迟导出，再实现普通P2版本并检查特征尺度。所有运行登记到[实验跟踪表](Experiments/Experiment_Tracker.md)。

完成门：B0和B1均能运行，输出逻辑与手算/官方定义一致。此阶段不追求论文精度。

## 阶段4：公共数据与基线

此时才审计并下载VisDrone2019-DET，记录来源、版本、许可、校验值、目录和官方划分；依次运行B0、B1并冻结小目标/遮挡评价、训练设置和计时协议。

完成门：基线可复现、划分无泄漏、测试集和评价协议冻结。

## 阶段5：单一方法

依次实现B2非共享P2–P4检测头和M共享轻量P2–P4检测头。先单seed排错，只有达到研究计划中的继续条件才运行三个种子。禁止加入第二种注意力、损失、增强、蒸馏或剪枝方法。

## 阶段6：核心实验与可选部署

冻结三张核心表：总体与小目标精度；参数量/GFLOPs/模型大小/真实延迟；B0/B1/B2/M消融与遮挡分层。有现成条件时补ONNX、TensorRT FP16或Jetson，没有设备则如实报告统一GPU结果。

## 阶段7：写作与投稿

先冻结结果表和成功/失败图，再写Method与Experiments，最后写Introduction、Related Work和Abstract。投稿前重新核验期刊范围、分区、预警和学校规则。
