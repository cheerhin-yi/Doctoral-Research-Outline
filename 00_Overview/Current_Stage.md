# 当前阶段（唯一入口）

更新：2026-09-16（Asia/Shanghai）。

本文件是全项目**唯一当前事项入口**：同时覆盖学习与论文实验。与源文件冲突时，以 [`Research_Question_Decision_2026-09-16.md`](../00_Practice_UAV_Aerial_Detection/Research_Question_Decision_2026-09-16.md) 与本页为准。

| 入口 | 路径 |
|---|---|
| 练手现行目录 | [`00_Practice_UAV_Aerial_Detection/`](../00_Practice_UAV_Aerial_Detection/README.md) |
| 主线 A 当前执行 | [`Mainline_A_Current.md`](../00_Practice_UAV_Aerial_Detection/Mainline_A_Current.md) |
| 2026-09-16 决定 | [`Research_Question_Decision_2026-09-16.md`](../00_Practice_UAV_Aerial_Detection/Research_Question_Decision_2026-09-16.md) |
| 掌握指标（学习） | [`Completion_Metrics.md`](../00_Practice_UAV_Aerial_Detection/Completion_Metrics.md) |
| 缩写映射 | [`Abbreviation_Glossary.md`](../99_Attachments/Abbreviation_Glossary.md) |
| 旧目录归档 | [`Archive_2026-09-16_PracticePaper/`](../99_Attachments/Archive_2026-09-16_PracticePaper/) |

---

## 当前唯一事项

**撰写 P0 EI 会议稿，并选定 2027 年会期。**

主张仅限 **P0-EI-C1／P0-EI-C2**（PROPOSED，协议／对比，非新算法）。  
旧机制主张 **P0-A-C1／P0-A-C2** 保持 **HOLD**（历史追踪）。  
Paper 1 两项主张与 Paper 2–7 保持 **PAUSED**；七篇总路线叙事保留。

本阶段成功标准：有可投稿的 EI 对比／协议稿提纲与会期候选；口径与开发证据已披露；无违规新训／新机制实验。

---

## 近中远（摘要）

| 时段 | 事项 |
|---|---|
| 近（现在–约 8 周） | 只写 P0 EI 稿 |
| 中（高原数据可复核后） | 域偏移／沿轨跟随／续航航线三选一，另开 |
| 远 | 单机沿轨与能耗模型稳定后再做 P1；P2／真 ISAC 不启动 |

资源：现有双 4090。高原数据集、自主航线、多机协同**还没有**，不能当本篇实验条件。  
3000 m = 线路高程，不是相对轨面航高。

详见 [`Mainline_A_Current.md`](../00_Practice_UAV_Aerial_Detection/Mainline_A_Current.md)。

---

## 实验门（当前）

- A0 对「独立新机制」：**HOLD**
- A2／A3／A4 新机制实验：**未开放**
- **A5：仅对本 EI 稿有限开放**（整理已有表；若缺同口径 4090 时间表或一次 test-dev 终评，须先登记 Run ID）
- **禁止**：新训练；改 backbone／loss／头；重跑 100 轮；新诊断拆分；创建 BTD13；用未采集高原数据占位写结果

100 轮 YOLO11n 基线及 BTD1–BTD12 已完成；BTD12（尺度条件 DFL 重评分）**DISMISSED**。结果在 `Experiments/` 与归档中，默认只读。

---

## 学习（并行，不替代唯一事项）

可按 `Completion_Metrics.md` 从 L0 推进能力建设；**不阻断** EI 稿整理。  
英语：CET-4（目标 2026-12）并行，见 [`90_English_Learning/`](../90_English_Learning/README.md)。

---

## 禁止（当前）

未在本页授权前：训练、改网络、部署、新建诊断编号、启动 Paper 2–7。  
文中不写「已证明新方法」「铁路安全有效」「高原数据已用」。  
不承诺期刊录用；本阶段目标是 EI 会议。  
不删除归档或已有负结果记录。

---

## 下一步

1. 打开 `Mainline_A_Current.md`，按 P0-EI-C1／C2 整理已有表。  
2. 选定 2027 EI 会期候选，回写本页。  
3. 需要 4090 同口径时间表或 test-dev 终评时，先登记 Run ID，再向本页申请一次性授权。
