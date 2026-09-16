# 当前阶段与唯一事项

更新：2026-09-16（Asia/Shanghai）。

本文件是全项目**唯一当前事项入口**：同时覆盖**学习**与**论文实验**。后续随学习验收与实验授权更新本页。

| 入口 | 路径 |
|---|---|
| 练手文目录 | [`00_Practice_UAV_Aerial_Detection/`](../00_Practice_UAV_Aerial_Detection/README.md) |
| 学习完成指标 | [`Completion_Metrics.md`](../00_Practice_UAV_Aerial_Detection/Completion_Metrics.md) |
| 旧目录归档 | [`Archive_2026-09-16_PracticePaper/`](../99_Attachments/Archive_2026-09-16_PracticePaper/) |
| 缩写映射 | [`Abbreviation_Glossary.md`](../99_Attachments/Abbreviation_Glossary.md) |

---

## 当前唯一事项

1. **学习：** 按 `Completion_Metrics.md` 从关卡 **L0** 起推进；**指标达标后才进入下一关**，不按每日任务数推进。  
2. **实验：** **HOLD**——不新训模型、不创建 BTD13、不重跑已完成的 100 轮／BTD1–12；结果保留在练手目录 `Experiments/` 与归档中。  
3. **主张 × 投入方向：** 待学习关卡 **L4** 通过后再决策。  
4. **英语：** 并行 CET-4（目标 2026-12，考试日待确认）＋领域英语，跟随当前关卡；见 [`90_English_Learning/`](../90_English_Learning/README.md)。

本阶段成功标准：L0 按完成指标通过并留下本人证据；实验侧无违规新跑。

---

## 练手文边界

题目：**面向无人机航拍的时间预算约束小目标检测**。  
单目 RGB、无人机视角、已知类别二维小目标；轨道走廊退出方法前提。  
Paper 1 主张保留；Paper 2–7 **PAUSED**。LSM-Head 为历史候选，非当前默认实现。

---

## 学习关卡进度

以 `Completion_Metrics.md` 为准；变更时同步改本表。

| 关卡 | 内容 | 状态 |
|---|---|---|
| L0 | 检测链与指标 | TODO |
| L1 | 可复现与实验设计 | TODO |
| L2 | 小目标／多尺度／轻量（历史候选） | TODO |
| L3 | 切片／时间预算／数据评价纪律 | TODO |
| L4 | 文献边界与可证伪实验卡 | TODO |

---

## 实验资产（默认只读）

100 轮 YOLO11n 基线及 BTD1–BTD12 已完成；A0 整体 HOLD。  
BTD12：尺度条件 DFL 重评分 **DISMISSED**（书面否决）。  
详见 `00_Practice_UAV_Aerial_Detection/Experiments/`。

---

## 禁止（当前）

未在本页授权前：训练、改网络、部署、新建诊断编号、启动 Paper 2–7。  
不以「看过／AI 讲过」代替完成指标。  
不删除归档或已有负结果记录。

---

## 下一步

完成 L0 → 更新本页进度 → 开始 L1。  
L0–L4 全部通过后，再开主张×投入方向与三个月实验讨论，并改写本页实验事项。
