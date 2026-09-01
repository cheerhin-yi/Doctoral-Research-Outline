# Paper 1：铁路UAV开放世界危险感知与风险告警

- **状态**：研究计划保留，执行等待练手论文完成。
- **研究问题与两项暂定主张**：[Research_Plan.md](Research_Plan.md)。
- **唯一进度表**：[Stage_Guide.md](Stage_Guide.md)。
- **总项目当前任务**：[Current_Stage.md](../00_Overview/Current_Stage.md)。

## 处理链

> UAV图像 → 已知目标检测 → 未知候选 → 轨道上下文 → 风险排序 → 可信告警

YOLO结构改动不是Paper 1的默认贡献。练手论文只提供可选的封闭集已知检测基线；Paper 1仍须独立审计开放世界协议、轨道风险价值和数据泄漏。

## 工作文件

| 路径 | 内容 |
|---|---|
| `Learning_Notes/` | Paper 1专属的开放世界、铁路风险和实验设计笔记 |
| [Literature_Matrix.md](Literature/Literature_Matrix.md) | 主题、阅读顺序、证据链和冲突 |
| [Search_Log.md](Literature/Search_Log.md) | 检索式、日期和筛选记录 |
| [Paper_Note_Template.md](Literature/Paper_Note_Template.md) | 单篇精读模板 |
| [Experiment_Plan.md](Experiments/Experiment_Plan.md) | 阶段门通过后使用的实验设计 |
| [Experiment_Tracker.md](Experiments/Experiment_Tracker.md) | 运行记录与论文数字回链 |
| [Paper_Outline.md](Writing/Paper_Outline.md) | 证据冻结后的写作结构 |

## 硬边界

Paper 1不研究三维重建、通信、ISAC、多模态、下一视点、强化学习、多无人机协同或多个YOLO模块堆叠。Paper 2–7继续`PAUSED`。
