# 轨道交通无人机智能巡检与应急响应博士研究框架

本仓库用于管理“无线通信与人工智能关键技术”博士研究，以轨道交通无人机巡检与应急响应为长期工程载体。统一主线为：

> Communication-Aware + Risk-Aware + Uncertainty-Aware

当前唯一活动任务是 **前置论文A：飞行条件感知风险校准**。学习计划自2026-08-28重新从第1周计时，每周投入8–10小时；前置论文B、Paper 1、桥接M1、Paper 2、桥接M2和Paper 6按门槛串行启动。原Paper 1十六周计划及周记保留为未来恢复Paper 1时使用，当前不得据此启动开放世界、三维、VoI、主动视点或多无人机实验。

## 从这里开始

1. 先阅读[当前框架详细使用说明](00_Project/Framework_Usage_Guide.md)和[总体实施入口](00_Project/PrePaper_Bridge_Implementation_README.md)。
2. 阅读[博士研究总计划](00_Project/Master_Plan.md)、[七篇论文与前置/桥接路线图](00_Project/Roadmap.md)和[学习框架导航](03_Learning/README.md)，确认当前只做前置论文A。
3. 从[重启学习计划](00_Project/Restarted_Learning_Plan_2026-08-28.md)和[20周执行清单](00_Project/PrePaper_20_Week_Execution_Backlog.md)找到当前周；当前为第1周。
4. 本周先更新[前置论文文献与期刊矩阵](00_Project/PrePaper_Literature_and_Venue_Matrix.md)，完成20篇证据矩阵和A—Paper 1—M1创新重叠图。
5. 正式实验前在[前置论文实验注册表](00_Project/PrePaper_Experiment_Registry.csv)登记；运行后再同步[运行索引](13_Experiment_Log/Run_Index.md)。
6. 原[Paper 1十六周计划](00_Project/Paper1_16_Week_Weekly_Plan.md)和[旧周记](00_Project/Weekly_Notes/)当前为暂停资料，不作为本阶段进度入口。

## 目录导航

| 目录 | 用途 |
|---|---|
| `00_Project` | 当前20周计划、未来Paper 1弹性周计划、周记录、检查与原始需求 |
| `01_Literature` | 文献矩阵、阅读笔记和检索记录 |
| `02_Innovation` | 创新台账与新颖性风险 |
| `03_Learning` | [N01–N16学习框架导航](03_Learning/README.md)与结构化笔记；当前仅N07/N08激活，N01–N04/N06按A需要限定启用，其余暂停 |
| `04_Paper1_OpenWorld_Risk` | 暂停的Paper 1协议、实验、论文提纲和未来接口 |
| `05`–`10_Paper*` | 后续六篇论文的研究接口和启动门槛 |
| `11_Datasets` | 数据元信息与版本说明；不存放大型数据 |
| `12_Code` | 未来代码结构与复现约定 |
| `13_Experiment_Log` | 实验运行索引与单次实验模板 |
| `14_Figures` | 图表清单与生成来源 |

## 证据规则

- 未运行的实验只能写“计划”或“待验证”，不得写成结果。
- 文献条目在核验标题、作者、年份、出处和链接前标记为“待核验”。
- 数据划分、随机种子、配置、运行环境和原始指标都必须可追踪。
- 数据集、模型权重、缓存、令牌和密钥不进入Git。

原始要求见[项目总说明V3归档](00_Project/项目总说明_V3_原文归档.md)。其中面向GPT的段落已转写为[项目协作指南](00_Project/Collaboration_Guide.md)，仅作为本项目的工作约定。
