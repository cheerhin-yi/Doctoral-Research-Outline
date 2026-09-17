# 当前阶段（唯一入口）

更新：2026-09-17（Asia/Shanghai）。

本文件是全项目**唯一当前事项入口**：同时覆盖学习与论文实验。与源文件冲突时，以 [`Research_Question_Decision_2026-09-16.md`](../00_Practice_UAV_Aerial_Detection/Research_Question_Decision_2026-09-16.md) 与本页为准。

| 入口 | 路径 |
|---|---|
| 练手现行目录 | [`00_Practice_UAV_Aerial_Detection/`](../00_Practice_UAV_Aerial_Detection/README.md) |
| 主线 A 当前执行 | [`Mainline_A_Current.md`](../00_Practice_UAV_Aerial_Detection/Mainline_A_Current.md) |
| 2026-09-16 决定 | [`Research_Question_Decision_2026-09-16.md`](../00_Practice_UAV_Aerial_Detection/Research_Question_Decision_2026-09-16.md) |
| P0 Benchmark 产物 | [`Experiments/P0_Benchmark/`](../00_Practice_UAV_Aerial_Detection/Experiments/P0_Benchmark/) |
| 掌握指标（学习） | [`Completion_Metrics.md`](../00_Practice_UAV_Aerial_Detection/Completion_Metrics.md) |
| 学习检查基准 | [`Learning_Check_Baseline.md`](../00_Practice_UAV_Aerial_Detection/Learning_Check_Baseline.md) |
| 缩写映射 | [`Abbreviation_Glossary.md`](../99_Attachments/Abbreviation_Glossary.md) |

---

## 当前唯一事项

**撰写 P0 EI 会议对比／协议稿，并选定 2027 年会期。**

主张仅限 **P0-EI-C1／P0-EI-C2**（PROPOSED，协议／对比，非新算法）。  
旧机制主张 **P0-A-C1／P0-A-C2** 保持 **HOLD**。  
Paper 1–7 保持 **PAUSED**。

本阶段成功标准：可投稿的 EI 对比／协议稿提纲 + 会期候选；主表数字均可回溯 Run ID；无违规新训／新机制。

---

## P0 Benchmark 进度（A5 对照实验）

五方法（冻结 `last.pt`，不改网络）：`F640` / `F1280` / `DensK1` / `UnifAll` / `SAHI640`。

| Stage | 内容 | 状态 |
|---|---|---|
| A | 环境冻结 | **PASS** |
| B | cal48 计时（1660SUPER） | **PASS** |
| C | cal48 精度 | **PASS** |
| D | VisDrone test-dev 一次性五方法 | **PASS**（`P0-BENCH-D-TESTDEV-20260917-01`） |
| E | 外数据集（UAVDT） | **BLOCKED**（等百度 Benchmark-M + DET 工具包落盘并过哈希／布局门） |
| F | 图级配对 Wilcoxon + bootstrap | **PASS**（`P0-BENCH-F-TESTDEV-20260917-01`；主比较 F1280 vs DensK1，Δrecall_small CI 不过 0） |

开发机时序与终评均在 **GTX 1660 SUPER**。正式 **4090 同口径时序表**仍缺，未授权前不编造。

---

## 近中远（摘要）

| 时段 | 事项 |
|---|---|
| 近 | 整理 EI 提纲与主表（D+F）；选定 2027 会期；可选：4090 时序／Stage E |
| 中 | 高原数据可复核后，域偏移／沿轨／续航三选一另开 |
| 远 | 单机沿轨与能耗稳定后再做 P1；真 ISAC 不启动 |

---

## 实验门（当前）

- 新机制／新训练／改 backbone·loss·头：**关闭**
- A5 对照整理：**开放**（只读已有 Run；补 4090 或 Stage E 前须先登记 Run ID 并回写本页授权）
- BTD1–BTD12：默认只读；BTD12 **DISMISSED**

---

## 学习（并行，不阻断 EI 整理）

按 `Completion_Metrics.md` + `Learning_Check_Baseline.md` 推进。  
**P0 优先块：** `03` → `04` → `06` → `07` → `08`（图级配对）；`01` 仍为单部版（按你的要求暂不改双部）；`02` 为双部样板。  
英语：CET-4（目标 2026-12）并行。

---

## 禁止（当前）

未在本页授权：训练、改网络、部署、BTD13、启动 Paper 2–7。  
文中不写「已证明新方法」「铁路安全有效」「高原数据已用」。  
不删除归档或负结果。

---

## 下一步

1. 按 D+F 整理 P0-EI-C1／C2 主表与披露清单。  
2. 选定 2027 EI 会期候选，回写本页。  
3. 需要 4090 时序或 Stage E 时：数据／机时就绪 → 登记 Run ID → 本页授权 → 再跑。  
4. 学习：从 `03`（若 L0/L1 未过则先 `01`/`02`）按基准提交第二部分。
