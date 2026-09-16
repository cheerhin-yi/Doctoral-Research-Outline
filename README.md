# 轨道交通无人机智能巡检博士研究项目

更新：2026-09-14。BTD12单机制审查已完成：尺度条件DFL分布统计重评分候选DISMISSED，GFLV2与多变量校准已覆盖核心关系，尚无独立机制差异；这是书面否决，非实测失败。100轮及BTD1–BTD11完成且不重跑。当前返回论文主张与投入方向决策，停止自动候选开发／新模型运行，不创建BTD13。旧区域机制及A0整体HOLD。 见[BTD12审查](00_Startup_Railway_UAV_Detection/Literature/BTD12_Low_Score_Candidate_Review.md)。

详细证据以[当前阶段](00_Overview/Current_Stage.md)为准；下方未同步的旧准入措辞只记录历史前提，不触发重复执行。

2026-09-12历史平台约定（已由本机执行及100轮完成状态替代）：只先用Kaggle，每轮保存恢复包、每5轮保留副本、默认约60分钟轮末暂停并封存平台输出；Kaggle额度耗尽且旧会话停止后才转Colab续训。目前Kaggle手机验证未完成，尚无云端模型训练。此约定替代旧“二选一／不允许恢复”描述；本机完成项不重跑，详见当前阶段与BT1交接报告。
本项目围绕“无线通信与人工智能关键技术”，以铁路无人机巡检为统一应用场景，规划七篇相互衔接的论文。

## 你现在只需要做什么

当前练手论文主线A：**面向无人机航拍的时间预算约束小目标检测**。100轮普通基线及cal48漏检诊断已完成，当前候选暂缓。单片预算/上界及F1280强基线对照均已完成；当前区域排序机制暂缓，BTD10重审及BTD11筛查已完成；BTD12已完成并否决本候选；下一项为论文主张与投入方向决策；见[诊断报告](00_Startup_Railway_UAV_Detection/Experiments/BT1_Cal48_Miss_Diagnosis.md)。

从[当前阶段](00_Overview/Current_Stage.md)开始。S0-01仍未通过；方向调整不代表学习完成。LSM-Head退出当前执行方案，历史依据、学习初稿和未运行记录保留。

## 项目入口

- [跨会话项目上下文](PROJECT_CONTEXT.md)：当前目标、代码结构、数据、模型、实验结果、失败记录与下一步边界；重要变化时同步维护。
- [项目总指南](00_Overview/Project_Guide.md)：目录、阶段、工作方式和范围控制；
- [当前阶段](00_Overview/Current_Stage.md)：现在具体学什么、做什么；
- [七篇论文路线](00_Overview/Seven_Paper_Roadmap.md)：每篇论文的作用和知识依赖；
- [每周论文审计与归档](00_Overview/Literature_Tracking_Workflow.md)：接收ChatGPT检索结果，先审计去重，再联动各方向文献矩阵、创新台账和周报；
- [Paper 1任务指南](01_Paper1_OpenWorld_Risk/Stage_Guide.md)：从学习、文献、复现、数据、实验到投稿；
- [Paper 1研究计划](01_Paper1_OpenWorld_Risk/Research_Plan.md)：问题、两项主张和研究边界。
- [主线A练手论文](00_Startup_Railway_UAV_Detection/README.md)：固定整帧时间预算下分配局部高分辨率计算；
- [项目英语学习支持线](90_English_Learning/README.md)：领域英语优先的文献阅读、论文写作与四级计划；
- [Codex使用指南](99_Attachments/Codex_Usage_Guide.md)：项目指令、检查点、上下文压缩、Token、Skills和Plugins的使用方法；
- [论文阅读指南](00_Overview/Paper_Reading_Guide.md)：历史材料和新审计文献的阅读等级、当前用途及边界；
- [项目参考材料](00_Overview/Reference_Materials/README.md)：博士科研计划书等方向依据。
- [全项目附件](99_Attachments/README.md)：博士研究外部条件、资源需求、模板和写法说明；
- [外部条件与资源需求](99_Attachments/Doctoral_Research_External_Conditions.md)：无人机、工作站、铁路数据、传感器、通信平台、人员和许可的分阶段配置。

## 文件夹

| 文件夹 | 内容 | 当前状态 |
|---|---|---|
| `00_Overview` | 新聊天交接、项目指南、当前阶段和七论文路线 | ACTIVE |
| `00_Startup_Railway_UAV_Detection` | 实时轻量小目标检测练手论文及其独立学习、文献、实验和写作材料 | ACTIVE |
| `00_PrePaper_Lightweight_Detection` | 原练手论文学习笔记、文献及历史计划；不写入主线A交付物 | 历史保留／学习参考 |
| `90_English_Learning` | 与当前科研阶段同步的领域英语、论文写作和四级能力支持 | SUPPORT |
| `01_Paper1_OpenWorld_Risk` | Paper 1开放世界风险研究、笔记、文献、实验和写作文件 | ACTIVE |
| `02_Paper2_3D_Disaster` | 三维灾害定量评估 | PAUSED |
| `03_Paper3_Comm_Perception` | 通信受限协同感知 | PAUSED |
| `04_Paper4_Risk_ISAC` | 风险驱动ISAC | PAUSED |
| `05_Paper5_Multimodal_Risk` | 多模态风险理解 | PAUSED |
| `06_Paper6_Active_Inspection` | 主动无人机巡检 | PAUSED |
| `07_Paper7_MultiUAV_Decision` | 多无人机协同决策 | PAUSED |
| `99_Attachments` | 全项目共用的附件和写法模板 | REFERENCE |

## 当前阶段完成前禁止

- 训练模型、开展检测推理实验或部署；
- 在当前VisDrone静态审计范围之外下载数据，或自行补造标注；
- 修改YOLO网络结构；
- 同时启动Paper 2–7；
- 学习三维、通信、ISAC、多模态、RL、MARL或GNN；
- 用“看完课程”代替结构图、手算、代码输出和自己的解释。

## 数据什么时候开始

主线A允许学术用途核验后的VisDrone审计下载，原包存入被忽略的`11_Datasets/raw/VisDrone/`，处理产物存`11_Datasets/processed/VisDrone/`。本批不冻结训练划分、不运行模型。后续按[主线A阶段门](00_Startup_Railway_UAV_Detection/Stage_Guide.md)执行。UAV-RSOD及询问信保留历史证据，不再阻塞当前优先审计。

## 项目纪律

- 每篇论文最多两个主要主张；
- 每项实验必须对应一个主张；
- 当前只维护当前阶段需要的文件；
- 后续论文允许维护审计通过的候选PDF、审计记录、文献矩阵和创新风险索引；正式学习笔记、系统检索、实验和写作子目录仍在对应论文启动时创建；
- 删除内容可从Git历史恢复，不在项目里保留重复归档。
