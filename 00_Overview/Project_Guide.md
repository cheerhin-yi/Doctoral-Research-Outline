# 博士研究项目总指南

## 1. 项目主线

研究方向是“无线通信与人工智能关键技术”，铁路无人机巡检是统一应用载体：

> 看见危险（Paper 1）→ 量化严重程度（Paper 2）→ 有限带宽共享（Paper 3）→ 通信—感知资源分配（Paper 4）→ 视觉退化下多模态判断（Paper 5）→ 主动复检（Paper 6）→ 多无人机联合决策（Paper 7）

当前在Paper 1之前先完成一篇“实时轻量小目标检测”练手论文。它只交付封闭集已知目标检测与轻量部署基础，不计入七篇主论文，也不改变Paper 1的两项主张。

## 2. 文件职责

| 文件或目录 | 唯一职责 |
|---|---|
| [Current_Stage.md](Current_Stage.md) | 当前阶段、唯一任务、完成门和禁止事项 |
| [Seven_Paper_Roadmap.md](Seven_Paper_Roadmap.md) | 七篇论文的稳定边界、依赖和接口 |
| [Paper_Reading_Guide.md](Paper_Reading_Guide.md) | 跨项目论文载体、阅读等级和归档边界 |
| [练手论文](../PrePaper_Lightweight_Detection/README.md) | 当前优先执行的独立练手成果 |
| [Paper 1](../01_Paper1_OpenWorld_Risk/README.md) | 练手论文完成后的开放世界铁路风险研究 |
| `02_Paper2_3D_Disaster`—`07_Paper7_MultiUAV_Decision` | 后续论文边界；当前全部`PAUSED` |
| `99_Attachments` | 外部条件、格式和参考附件；不是当前任务表 |

各论文目录统一保留实际工作文件：`Research_Plan.md`、`Stage_Guide.md`、`Learning_Notes/`、`Literature/`、`Experiments/`与`Writing/`。README只作入口，不重复维护阶段细节。

## 3. 工作规则

1. 每轮先读[当前阶段](Current_Stage.md)，只选择其中一个任务；
2. 输出必须写入对应学习笔记、文献矩阵、实验记录或稿件；
3. 未通过阶段完成门，不下载数据、不训练正式模型、不修改网络；
4. 数据、配置、代码版本、运行ID和论文数字必须可回链；
5. Git中已有的未提交和未跟踪内容视为用户资产，不覆盖、不清理；
6. 未经明确要求，不提交、不推送、不重写历史，不修改或删除`99_Attachments/paper/`。

## 4. 范围控制

- 每篇论文最多两个主要主张，每项实验必须服务于主张；
- 练手论文只允许一个共享轻量P2–P4检测头改动；
- Paper 1只研究已知/未知候选、轨道上下文风险和可信告警；
- 当前不研究三维、通信、ISAC、多模态、强化学习、航迹规划或多无人机协同；
- 后续论文的候选PDF可以归档，但`PAUSED`状态不因文献存在而改变。
