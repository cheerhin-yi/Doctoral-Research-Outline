# 当前阶段（唯一入口）

> **目录纪律（2026-09-23）**：文献与实验仅按 papers/<PaperID>/ 槽位填写。P0 入口：Literature/papers/P0_EI/、Experiments/papers/P0_EI/。


更新：2026-09-20（Asia/Shanghai）。

本文件是全项目**唯一当前事项入口**。与源文件冲突时，以本页与 [`Research_Question_Decision_2026-09-16.md`](../00_Practice_UAV_Aerial_Detection/Research_Question_Decision_2026-09-16.md) 为准。

| 入口 | 路径 |
|---|---|
| 练手现行目录 | [`00_Practice_UAV_Aerial_Detection/`](../00_Practice_UAV_Aerial_Detection/README.md) |
| 主线 A 当前执行 | [`Mainline_A_Current.md`](../00_Practice_UAV_Aerial_Detection/Mainline_A_Current.md) |
| P0 Benchmark | [`Experiments/papers/P0_EI/`](../00_Practice_UAV_Aerial_Detection/Experiments/papers/P0_EI/) |
| UAVDT（G 盘） | `G:\Schloar Data\UAVDT\`（布局 PASS：50 序列／40735 帧／50×`*_gt_whole.txt`） |
| T4 过程目录（G 盘，仅历史过程件） | `G:\Schloar Data\P0_T4_Train\`（**训练轨已撤回**，不再开训） |

---

## 当前唯一事项

**Stage E 已 DONE／PASS。下一可检查事项：EI 包装增量（近邻协议对标表＋失败／边界例＋可复现附录；正式 4090 时序表可选、分列）。叙事保持「冻结权重上的推理协议对比」，不新训、不改映射、不开 Paper 2–7。**

用户于 2026-09-18 明确撤回 T4 真训练授权。Kaggle V1 Failed，**未产生任何新权重**。本地冻结权重未被改写。

Paper 2–7 仍 **PAUSED**。机制主张 P0-A-* 仍 **HOLD**。

---

## 进度

| 项 | 状态 |
|---|---|
| A–D／F（冻结 `last.pt`，1660SUPER） | **PASS** |
| E UAVDT 五方法同权推理＋评估 | **DONE／PASS**（`P0-BENCH-E-UAVDT-20260918-FULL`，40735 图；报告 [`P0_Benchmark_StageE_UAVDT_Report.md`](../00_Practice_UAV_Aerial_Detection/Experiments/papers/P0_EI/P0_Benchmark_StageE_UAVDT_Report.md)） |
| T4／Kaggle 训练轨 | **已撤回**；无新权重 |
| 4090 正式时序 | 仍缺；与 1660 分列披露 |

### 冻结权重（未改）

- 路径：`11_Datasets/processed/VisDrone/BT1/BT1-LOCAL-20260913-01/train/weights/last.pt`
- SHA256：`bc42d54e37acaf1f698af487439dc222fa86fb4498623e8cf954df14e0aa5533`
- Stage E 运行内复核：与冻结 SHA 一致

五方法协议名：`F640`／`F1280`／`DensK1`／`UnifAll`／`SAHI640`（磁盘名可能略异，以 Tracker／`summary.json` 为准）。

### Stage E 主数字（small_recall）

F1280 0.793 > UnifAll 0.782 > DensK1 0.767 > SAHI640 0.760 > F640 0.708。跨集粗趋势（F640 最弱；高分／切块抬召回、付精度代价）与 Stage D 一致；五方法排序不完全稳定——主张写「协议改权衡」，不写「通论排序」。

---

## 实验门（当前）

- **禁止**新训／微调／改网络／开 Paper 2–7，除非本页再次书面授权。
- 类别映射保持 FROZEN；不得因看到 E 分数回改映射。
- 终表／Run 记录进仓库 `Experiments/`；1660 时序≠正式 4090 表。
- 第三方 UAVDT 子集（含已拒 Kaggle JSON 包）禁止作主库。

---

## 下一步

1. **EI 包装：** 近邻协议对标表＋跨集一致／不一致厚写＋失败／边界例＋协议附录（与四区最小增量 1–4 重合）。
2. **可选：** 4090 正式时序表（正文时序只用 4090；D／E 精度表保留；1660 可注 pipeline validation）。
3. **不默认：** 同质第三集；新模块／重训。


---

## Post-EI 预备包登记（IDLE · 2026-09-24）

> **纪律：** 下表 **不**改变上文「当前唯一事项」。唯一 ACTIVE 仍为 **P0_EI 包装增量**。预备包在再授权前保持 IDLE。

| 代号 | 路径 | 状态 | 说明 |
|---|---|---|---|
| P0_EI | `00_Practice_UAV_Aerial_Detection/` | **ACTIVE** | 当前唯一执行 |
| A · RailUAV-SOD | [`../08_RailUAV_SOD/`](../08_RailUAV_SOD/README.md) | **IDLE / PREP** | Post-EI 数据文预备包；禁采集/训练 |
| B · Paper1 | [`../01_Paper1_OpenWorld_Risk/`](../01_Paper1_OpenWorld_Risk/README.md) | **IDLE / PREP** | Post-EI 方法文预备包；禁 Stage ④ |
| Paper 2–7 | `02_`…`07_` | **PAUSED** | 不变 |

## Venue / Claim 政策指针（案头 · 2026-09-24）

见 [`Venue_and_Claim_Policy_JCR_2026-09-24.md`](Venue_and_Claim_Policy_JCR_2026-09-24.md)。**不**改变上表 ACTIVE=P0_EI；A/B 仍 IDLE/PREP。

讨论产物总索引（政策 / 边界 / A·B 案头 / catalog）：[`INDEX_Discussion_Products_2026-09-24.md`](INDEX_Discussion_Products_2026-09-24.md)。**仅指针**；**不**改写上表、**不**解锁 A/B 采集或训练。
