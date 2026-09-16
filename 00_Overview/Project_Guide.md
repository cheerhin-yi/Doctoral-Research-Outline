# 博士研究项目总指南

## 1. 项目主线

研究方向是“无线通信与人工智能关键技术”，铁路无人机巡检是统一应用载体：

> 看见危险（Paper 1）→ 量化严重程度（Paper 2）→ 有限带宽共享（Paper 3）→ 通信—感知资源分配（Paper 4）→ 视觉退化下多模态判断（Paper 5）→ 主动复检（Paper 6）→ 多无人机联合决策（Paper 7）

当前在Paper 1之前先完成主线A练手论文“面向无人机航拍的时间预算约束小目标检测”。它研究封闭集已知目标与计算分配，不计入七篇主论文，也不改变Paper 1的两项主张。

## 2. 文件职责

| 文件或目录 | 唯一职责 |
|---|---|
| [Current_Stage.md](Current_Stage.md) | 当前阶段、唯一任务、完成门和禁止事项 |
| [Seven_Paper_Roadmap.md](Seven_Paper_Roadmap.md) | 七篇论文的稳定边界、依赖和接口 |
| [Paper_Reading_Guide.md](Paper_Reading_Guide.md) | 跨项目论文载体、阅读等级和归档边界 |
| [Literature_Tracking_Workflow.md](Literature_Tracking_Workflow.md) | 周检索输入的审计、去重、归档、跨方向矩阵与周报联动 |
| [Literature_Registry.md](Literature_Registry.md) | 工作级唯一ID、版本历史和正文主位置 |
| [Innovation_Ledger.md](Innovation_Ledger.md) | 文献对候选创新、边界与待验证实验的影响 |
| [Learning_Note_Method.md](Learning_Note_Method.md) | 学习、文献、实验、写作的执行顺序与低负担记录方法 |
| [练手论文学习枢纽](../00_Practice_UAV_Aerial_Detection/README.md) | 合并后的练手文目录；学习看 Completion_Metrics；事项看 Current_Stage |
| [英语学习支持线](../90_English_Learning/README.md) | 与当前科研阶段同步的领域英语、写作和四级能力训练；不改变科研任务 |
| [Paper 1](../01_Paper1_OpenWorld_Risk/README.md) | 练手论文完成后的开放世界铁路风险研究 |
| `02_Paper2_3D_Disaster`—`07_Paper7_MultiUAV_Decision` | 后续论文边界；当前全部`PAUSED` |
| `99_Attachments` | 外部条件、格式和参考附件；不是当前任务表 |

各论文目录统一保留实际工作文件：`Research_Plan.md`、`Stage_Guide.md`、`Learning_Notes/`、`Literature/`、`Experiments/`与`Writing/`。README只作入口，不重复维护阶段细节。

## 3. 工作规则

1. 每轮先读[当前阶段](Current_Stage.md)，只选择其中一个任务；
2. 输出必须写入对应学习笔记、文献矩阵、实验记录或稿件；
3. 按当前阶段授权执行；A0-01允许许可核验后的公开数据审计下载，禁止模型训练、检测推理实验、网络修改与部署；
4. 数据、配置、代码版本、运行ID和论文数字必须可回链；
5. Git中已有的未提交和未跟踪内容视为用户资产，不覆盖、不清理；
6. 未经明确要求，不提交、不推送、不重写历史，不修改或删除`99_Attachments/paper/`。

## 4. 范围控制

- 每篇论文最多两个主要主张，每项实验必须服务于主张；
- 练手论文只研究时间预算约束的局部高分辨率计算分配；VisDrone为优先审计对象，轨道走廊退出方法前提；LSM-Head为历史方案，不预先冻结新机制；
- Paper 1只研究已知/未知候选、轨道上下文风险和可信告警；
- 当前不研究三维、通信、ISAC、多模态、强化学习、航迹规划或多无人机协同；
- 后续论文的候选PDF可以归档，但`PAUSED`状态不因文献存在而改变。
