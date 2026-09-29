# 当前阶段（唯一入口）

更新：2026-09-27（Asia/Shanghai）。ACTIVE 不变：**P0_EI**。

本文件是全项目**唯一当前事项入口**。研究问题、实验设置与 C1／C2 主张全文见 [`Research_Plan.md`](../00_Practice_UAV_Aerial_Detection/Research_Plan.md)；近中远边界见 [`Mainline_A_Current.md`](../00_Practice_UAV_Aerial_Detection/Mainline_A_Current.md)。

| 入口 | 路径 |
|---|---|
| 练手现行目录 | [`00_Practice_UAV_Aerial_Detection/`](../00_Practice_UAV_Aerial_Detection/README.md) |
| 研究计划（主张全文） | [`Research_Plan.md`](../00_Practice_UAV_Aerial_Detection/Research_Plan.md) |
| P0 证据槽 | [`Experiments/papers/P0_EI/`](../00_Practice_UAV_Aerial_Detection/Experiments/papers/P0_EI/Run_Index.md)（Run 索引） |
| 论文概况与实验内容（导读） | [`P0_EI_Paper_Overview_and_Experiments.md`](../00_Practice_UAV_Aerial_Detection/P0_EI_Paper_Overview_and_Experiments.md) |
| UAVDT（G 盘） | `G:\\Schloar Data\\P0\\UAVDT\\`（2026-09-27 核实：50 序列 `*_gt_whole.txt`／40735 帧；Stage E 运行时路径 `G:\\Schloar Data\\UAVDT\\` 已迁移） |

---

## 当前唯一事项

**Stage A–F 全部 PASS；EI 包装（近邻协议对标表＋失败／边界例＋可复现附录＋图 1–5）已完成；C1／C2 已按 Stage B–F 结果改为终稿措辞（2026-09-27）。下一步：① 4090 正式时序（Run G，结果单独写 `Timing_4090_Table.md`，不与 1660 合并）；② 稿件正文（按 `Writing/P0_EI_Outline.md`）。叙事保持「冻结权重上的推理协议对比」，不新训、不改映射、不开 Paper 2–7。**

T4／Kaggle 训练轨已于 2026-09-18 撤回，未产生任何新权重；本地冻结权重未被改写。Paper 2–7 仍 **PAUSED**；机制主张 P0-A-* 仍 **HOLD**。

---

## 进度

| 项 | Run ID | 状态 |
|---|---|---|
| A 冻结（权重／环境／协议定义） | `P0-BENCH-A-ENV-20260917-01` | **PASS** |
| B 1660 流水线计时（cal48） | `P0-BENCH-B-TIMING-20260917-01` | **PASS** |
| C cal48 精度（开发证据） | `P0-BENCH-C-CAL48-20260917-01` | **PASS** |
| D VisDrone test-dev 一次性终评 | `P0-BENCH-D-TESTDEV-20260917-01` | **PASS** |
| E UAVDT 跨集（40735 帧） | `P0-BENCH-E-UAVDT-20260918-FULL` | **PASS**（[`StageE_UAVDT_Report.md`](../00_Practice_UAV_Aerial_Detection/Experiments/papers/P0_EI/03_cross_uavdt/StageE_UAVDT_Report.md)） |
| F 图级配对统计 | `P0-BENCH-F-TESTDEV-20260917-01` | **PASS** |
| EI 包装 | — | **DONE**（[`Neighbor_Protocol_Table.md`](../00_Practice_UAV_Aerial_Detection/Experiments/papers/P0_EI/05_packaging/Neighbor_Protocol_Table.md)、失败例、复现附录、图 1–5） |
| C1／C2 主张措辞 | — | **FINAL**（2026-09-27，仅依据 Stage B–F；见 Research_Plan §3） |
| G 4090 正式时序 | `P0-BENCH-G-4090-{SMOKE,CAL48,TESTDEV}-20260920-01` | **未跑**；结果单列 |
| 稿件正文 | — | **未开始** |

### 冻结权重（未改）

- 路径：`11_Datasets/processed/VisDrone/BT1/BT1-LOCAL-20260913-01/train/weights/last.pt`
- SHA256：`bc42d54e37acaf1f698af487439dc222fa86fb4498623e8cf954df14e0aa5533`（Stage B／D／E 运行内复核一致）
- 五协议：`F640`／`F1280`／`DensK1`／`UnifAll`／`SAHI640`

### 主张（终稿措辞摘要）

- **C1：** F1280 比 DensK1 更准（VisDrone test-dev small recall +0.0409，95% CI [0.0355, 0.0462]；precision +0.0681），1660 上时延统计上不可区分（Wilcoxon p = 0.235）；不主张"更快"。
- **C2：** 选区／覆盖协议只移动召回–精度–时延权衡：VisDrone 上 UnifAll small recall 最高但时延约 3.3×、精度下降；SAHI640 在两集上均被 F1280 支配；UAVDT 排序为 F1280 0.793 > UnifAll 0.782 > DensK1 0.767 > SAHI640 0.760 > F640 0.708。
- **范围：** 仅 1660 计时；匹配器 precision／small recall，不是 AP；单一冻结权重。

---

## 实验门（当前）

- **禁止**新训／微调／改网络／开 Paper 2–7，除非本页再次书面授权。
- 类别映射保持 FROZEN；不得因看到分数回改映射或 conf。
- 终表／Run 记录进仓库 `Experiments/papers/P0_EI/`；1660 时序≠正式 4090 表。
- 第三方 UAVDT 子集（含已拒 Kaggle JSON 包）禁止作主库。

---

## 下一步

1. **4090 正式时序表：** 按已登记 Run G（`P0-BENCH-G-4090-SMOKE/CAL48/TESTDEV-20260920-01`，UAVDT 可选）在 4090 机上跑；结果单独写 `Experiments/papers/P0_EI/04_timing/Timing_4090_Table.md`，**不与 1660 合并**；正文时序只用 4090，1660 注 pipeline validation。
2. **稿件正文：** 按 `Writing/P0_EI_Outline.md` 起草，主张只用 C1／C2 终稿措辞。
3. **会期：** 选定 2027 年 EI 会期（主跟踪 ICIP 2027 全文）并写入本页。
4. **不默认：** 同质第三集；新模块／重训。

---

## Post-EI 预备包登记（IDLE · 2026-09-24）

> **纪律：** 下表 **不**改变上文「当前唯一事项」。唯一 ACTIVE 仍为 **P0_EI**（当前工作：4090 时序表与稿件正文）。预备包在再授权前保持 IDLE。

| 代号 | 路径 | 状态 | 说明 |
|---|---|---|---|
| P0_EI | `00_Practice_UAV_Aerial_Detection/` | **ACTIVE** | 当前唯一执行 |
| A · RailUAV-SOD | [`../08_RailUAV_SOD/`](../08_RailUAV_SOD/README.md) | **IDLE / PREP** | Post-EI 数据文预备包；禁采集/训练 |
| B · Paper1 | [`../01_Paper1_OpenWorld_Risk/`](../01_Paper1_OpenWorld_Risk/README.md) | **IDLE / PREP** | Post-EI 方法文预备包；禁 Stage ④ |
| Paper 2–7 | `02_`…`07_` | **PAUSED** | 不变 |

## Venue / Claim 政策指针（案头 · 2026-09-24）

见 [`Venue_and_Claim_Policy_JCR_2026-09-24.md`](Venue_and_Claim_Policy_JCR_2026-09-24.md)。**不**改变上表 ACTIVE=P0_EI；A/B 仍 IDLE/PREP。

信息学院学位分（2021 细则对照，案头）：[`SWJTU_Info_College_Degree_Credit_Note_2026-09-28.md`](SWJTU_Info_College_Degree_Credit_Note_2026-09-28.md)。学术博士：普通 EI／CCF-C **不计分**；正常评阅最低线为两篇可计 15 分的 SCI 二区（或一区）；「3 篇高水平」仅提前答辩。

讨论产物总索引（政策 / 边界 / A·B 案头 / catalog）：[`INDEX_Discussion_Products_2026-09-24.md`](INDEX_Discussion_Products_2026-09-24.md)。**仅指针**；**不**改写上表、**不**解锁 A/B 采集或训练。
