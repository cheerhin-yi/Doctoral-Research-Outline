# 练手论文：实时轻量小目标检测

- **定位**：用一个检测头改动完成“学习—查新—复现—数据—实验—写作—投稿”的独立练习。
- **当前阶段**：阶段0共同基础；当前任务见[总项目当前阶段](../00_Overview/Current_Stage.md)。
- **研究问题与边界**：[Research_Plan.md](Research_Plan.md)。
- **唯一进度表**：[Stage_Guide.md](Stage_Guide.md)。

## 唯一方法方向

在YOLO11n中把P3–P5检测头替换为部署友好的共享轻量P2–P4检测头（LSM-Head）。Backbone、Loss、标签分配和训练增强保持基线设置，Neck只允许增加输出P2所需的连接。

## 工作文件

| 路径 | 内容 |
|---|---|
| `Learning_Notes/` | 六份实际学习笔记；顺序由阶段指南规定 |
| [Literature_Matrix.md](Literature/Literature_Matrix.md) | 阅读顺序、载体、证据、冲突和检索缺口 |
| [Search_Log.md](Literature/Search_Log.md) | 数据库、检索式、日期和筛选记录 |
| [Paper_Note_Template.md](Literature/Paper_Note_Template.md) | 单篇精读模板 |
| [Experiment_Plan.md](Experiments/Experiment_Plan.md) | B0/B1/B2/M及公平条件 |
| [Experiment_Tracker.md](Experiments/Experiment_Tracker.md) | 每次运行的唯一登记表 |
| [Paper_Outline.md](Writing/Paper_Outline.md) | 证据冻结后的写作结构 |

## 硬边界

本论文不研究开放世界、未知目标、铁路风险推理、通信、三维、多模态、强化学习或多无人机协同；不叠加注意力、损失、增强、蒸馏、剪枝或量化训练。若LSM-Head无稳定收益，按止损条件收缩或终止，不增加第二个模块。
