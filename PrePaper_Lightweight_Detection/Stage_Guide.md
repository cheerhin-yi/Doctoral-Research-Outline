# 练手论文阶段任务指南

本指南是这篇练手论文的唯一进度表。各阶段按完成门推进，不按日期强行赶进度。数据下载排在学习和最小复现之后。

## 阶段0：共同基础（独立副本）

先完成本论文学习区中独立保存的：

1. [YOLO研究核心](Learning_Notes/01_YOLO_Research_Core.md)；
2. [PyTorch与可复现性](Learning_Notes/02_PyTorch_and_Reproducibility.md)；
3. [实验设计与不确定性](Learning_Notes/03_Experiment_Design_and_Uncertainty.md)。

完成门：能解释YOLO完整检测链，能运行官方YOLO训练/验证，能手算主要指标并写公平对照。

## 阶段1：专项学习（当前优先）

按顺序填写：

1. [小目标与多尺度检测](Learning_Notes/04_Small_Object_and_Multiscale.md)；
2. [轻量共享检测头](Learning_Notes/05_Lightweight_Shared_Head.md)；
3. [速度评价与简单部署](Learning_Notes/06_Efficiency_and_Deployment.md)。

完成门：

- [ ] 画出P3–P5、P2–P5和P2–P4三种检测尺度；
- [ ] 手算普通卷积与深度可分离卷积参数量；
- [ ] 解释参数量、FLOPs、延迟和端到端FPS的区别；
- [ ] 写出LSM-Head的输入、共享部分和独立输出；
- [ ] 写出四组模型的唯一变量和公平条件。

此阶段不下载VisDrone、不修改模型。

## 阶段2：文献查新与方法冻结

使用[Literature](Literature/README.md)中的主题和空白矩阵，核验最近三年的P2、小目标检测头、参数共享和真实速度评价工作。

完成门：

- 至少核验12篇直接相关工作，其中最近三年不少于8篇；
- 明确普通P2、P2–P4重配置和共享检测头的最近基线；
- 将方法冻结为一个检测头改动；
- 如果发现同构方法，优先修改叙事或终止，不增加模块规避冲突。

## 阶段3：最小代码复现

只使用框架自带样例或极小公开样例：

1. 跑通YOLO11n推理、训练和验证；
2. 导出模型参数量、GFLOPs和单图延迟；
3. 实现普通P2版本并检查每个特征尺度；
4. 建立[实验跟踪表](Experiments/Experiment_Tracker.md)。

完成门：B0和B1均能运行，指标输出与手算/官方结果逻辑一致，暂不追求论文精度。

## 阶段4：公共数据与基线

此时才下载主数据并记录版本、许可和官方划分。优先使用VisDrone2019-DET；不自采、不重标整个数据集。

依次运行：

1. B0原始YOLO11n；
2. B1普通P2；
3. 建立小目标和遮挡分层评价；
4. 冻结训练设置和测试集。

完成门：基线可复现、划分无泄漏、速度计时协议固定。

## 阶段5：实现单一方法

1. 实现B2非共享P2–P4检测头；
2. 在B2上实现M共享轻量检测头；
3. 先单seed排错；
4. 只有达到[研究计划](Research_Plan.md)中的继续条件才运行三个种子。

禁止加入第二种注意力、损失、增强、蒸馏或剪枝方法。

## 阶段6：核心实验与可选部署

完成三张核心表：

1. 总体与小目标精度；
2. 参数量、GFLOPs、模型大小与延迟；
3. B0/B1/B2/M消融及遮挡分层。

有现成条件时补TensorRT FP16或Jetson实验；没有设备就如实报告统一GPU/ONNX结果，不购买设备、不搭建真实无人机系统。

## 阶段7：写作、投稿和返修

1. 先冻结三张表和典型成功/失败图；
2. 按[论文提纲](Writing/Paper_Outline.md)先写Method和Experiments；
3. 再写Introduction、Related Work和Abstract；
4. 投稿前核验期刊分区、预警和学校规则；
5. 保存投稿稿、审稿意见、回复、校样和最终版本。

## 现在下一步

继续补齐本目录中的共同YOLO、PyTorch和实验设计基础；完成后从[小目标与多尺度检测](Learning_Notes/04_Small_Object_and_Multiscale.md)开始。不要提前下载数据或实现检测头。
