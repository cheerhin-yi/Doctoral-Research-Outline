# 轨道交通无人机智能巡检与应急响应博士研究框架

本仓库用于管理“无线通信与人工智能关键技术”博士研究，以轨道交通无人机巡检与应急响应为长期工程载体。统一主线为：

> Communication-Aware + Risk-Aware + Uncertainty-Aware

当前唯一实验主任务是 **Paper 1：无人机铁路开放环境风险感知**。计划按16个“研究周”依次推进，不绑定固定日历日期；一个研究周可跨越多个自然周。Paper 2–7仅维护知识接口与研究依赖，不启动大规模实验。

## 从这里开始

1. 阅读[博士研究总计划](00_Project/Master_Plan.md)和[七篇论文路线图](00_Project/Roadmap.md)。
2. 在[Paper 1十六个研究周弹性计划](00_Project/Paper1_16_Week_Weekly_Plan.md)中找到当前研究周，每次有空时选择一个MUST任务推进，不要求当天完成。
3. 在对应的[研究周学习记录](00_Project/Weekly_Notes/)记录实际会话、证据和复述；MUST完成并通过检查后再进入下一研究周。
4. 实验前先登记[实验计划](04_Paper1_OpenWorld_Risk/EXPERIMENT_PLAN.md)，运行后更新[实验跟踪表](04_Paper1_OpenWorld_Risk/EXPERIMENT_TRACKER.md)和[运行索引](13_Experiment_Log/Run_Index.md)。
5. 达到研究周完成门后提交检查；Codex按[检查量表](00_Project/Review_Rubric.md)生成评审文件并更新[研究周状态](00_Project/Weekly_Status.md)。

## 目录导航

| 目录 | 用途 |
|---|---|
| `00_Project` | 总计划、弹性研究周计划、周记录、检查与原始需求 |
| `01_Literature` | 文献矩阵、阅读笔记和检索记录 |
| `02_Innovation` | 创新台账与新颖性风险 |
| `03_Learning` | N01–N16结构化学习笔记 |
| `04_Paper1_OpenWorld_Risk` | 当前论文的协议、实验、论文提纲和接口 |
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
