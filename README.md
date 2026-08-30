# 轨道交通无人机智能巡检博士研究项目

本项目围绕“无线通信与人工智能关键技术”，以铁路无人机巡检为统一应用场景，规划七篇相互衔接的论文。

## 你现在只需要做什么

当前只负责Paper 1研究链，近期先完成一篇实时轻量小目标检测练手论文。现在仍处于共同知识补齐阶段；你已经学习卷积和基本YOLO，下一步不是找数据集，也不是改网络，而是依次完成：

1. YOLO完整检测链、损失、NMS与评价指标；
2. PyTorch科研训练、调试和可复现性；
3. closed-set、open-set、open-vocabulary、open-world和异常检测；
4. 铁路轨道上下文、侵界关系与风险告警；
5. 对照实验、数据泄漏、统计和不确定性评价。
6. 小目标多尺度检测、轻量共享检测头和真实速度评价。

立即从[当前阶段指南](00_Overview/Current_Stage.md)开始。每次只完成其中一个任务，并把答案写入对应学习笔记。

## 项目入口

- [项目总指南](00_Overview/Project_Guide.md)：目录、阶段、工作方式和范围控制；
- [当前阶段](00_Overview/Current_Stage.md)：现在具体学什么、做什么；
- [七篇论文路线](00_Overview/Seven_Paper_Roadmap.md)：每篇论文的作用和知识依赖；
- [Paper 1任务指南](01_Paper1_OpenWorld_Risk/Stage_Guide.md)：从学习、文献、复现、数据、实验到投稿；
- [Paper 1研究计划](01_Paper1_OpenWorld_Risk/Research_Plan.md)：问题、两项主张和研究边界。
- [实时轻量检测练手论文](01_Paper1_OpenWorld_Risk/PrePaper_Lightweight_Detection/README.md)：独立练手成果，只保留一个检测头改动；
- [项目参考材料](00_Overview/Reference_Materials/README.md)：博士科研计划书等方向依据。
- [全项目附件](99_Attachments/README.md)：博士研究外部条件、资源需求、模板和写法说明；
- [外部条件与资源需求](99_Attachments/Doctoral_Research_External_Conditions.md)：无人机、工作站、铁路数据、传感器、通信平台、人员和许可的分阶段配置。

## 文件夹

| 文件夹 | 内容 | 当前状态 |
|---|---|---|
| `00_Overview` | 项目指南、当前阶段和七论文路线 | ACTIVE |
| `01_Paper1_OpenWorld_Risk` | 当前论文全部研究、笔记、文献、实验和写作文件 | ACTIVE |
| `02_Paper2_3D_Disaster` | 三维灾害定量评估 | PAUSED |
| `03_Paper3_Comm_Perception` | 通信受限协同感知 | PAUSED |
| `04_Paper4_Risk_ISAC` | 风险驱动ISAC | PAUSED |
| `05_Paper5_Multimodal_Risk` | 多模态风险理解 | PAUSED |
| `06_Paper6_Active_Inspection` | 主动无人机巡检 | PAUSED |
| `07_Paper7_MultiUAV_Decision` | 多无人机协同决策 | PAUSED |
| `99_Attachments` | 全项目共用的附件和写法模板 | REFERENCE |

## 当前阶段完成前禁止

- 收集、下载或标注正式项目数据；
- 修改YOLO网络结构；
- 同时启动Paper 2–7；
- 学习三维、通信、ISAC、多模态、RL、MARL或GNN；
- 用“看完课程”代替结构图、手算、代码输出和自己的解释。

## 数据什么时候开始

数据工作放在Paper 1阶段4。在此之前先完成知识门、最近工作审计和小样例技术复现。届时才根据已经冻结的研究主张决定需要什么公开数据、是否需要自采以及怎样划分Known/Unknown和物理场景。

## 项目纪律

- 每篇论文最多两个主要主张；
- 每项实验必须对应一个主张；
- 当前只维护当前阶段需要的文件；
- 后续论文启动时再创建自己的学习、文献、实验和写作子目录；
- 删除内容可从Git历史恢复，不在项目里保留重复归档。
