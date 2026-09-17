# 练手论文：无人机航拍时间预算约束小目标检测

目录名：`00_Practice_UAV_Aerial_Detection`  
由原 `00_PrePaper_Lightweight_Detection` 与 `00_Startup_Railway_UAV_Detection` **整理合并**而成。两个旧目录全文已移入 [`99_Attachments/Archive_2026-09-16_PracticePaper/`](../99_Attachments/Archive_2026-09-16_PracticePaper/)，**源内容不丢**。

## 你需要看的文件

| 文件 | 用途 |
|---|---|
| [`../00_Overview/Current_Stage.md`](../00_Overview/Current_Stage.md) | **唯一当前事项**（学习＋实验都在这里更新） |
| [`Completion_Metrics.md`](Completion_Metrics.md) | **学习完成指标**（过关才进下一关） |
| [`Learning_Notes/`](Learning_Notes/) | 当前学习教材与记录模板 |
| [`Research_Plan.md`](Research_Plan.md) | 问题与边界 |
| [`Experiments/`](Experiments/) | 已有实验协议／结果（默认不重跑） |
| [`Literature/`](Literature/) | 矩阵／审计／审查（见 `Literature/README.md`） |
| [`Writing/`](Writing/) | 写作提纲 |

缩写释义：[`99_Attachments/Abbreviation_Glossary.md`](../99_Attachments/Abbreviation_Glossary.md)

## 硬边界（摘要）

- 单目 RGB、无人机视角、已知类别二维小目标；轨道走廊退出方法前提。
- LSM-Head／旧区域机制为历史候选或 HOLD，不是默认要实现的创新。
- 每篇最多两个主张；未在 `Current_Stage` 授权前不新训模型、不建新诊断编号。
