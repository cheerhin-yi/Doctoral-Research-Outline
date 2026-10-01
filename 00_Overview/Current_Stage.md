# 当前阶段（唯一入口）

更新：2026-10-01（Asia/Shanghai；本机 GPU 换为 RTX 5060 Ti 16GB，Run G 正式时序由 4090 改为 5060 Ti，计划中未跑）。ACTIVE 不变：**P0_EI**。总览清理见 [`Cleanup_2026-09-29.md`](Cleanup_2026-09-29.md)，不改变下面的唯一事项。

本文件是全项目**唯一当前事项入口**。研究问题、实验设置与 C1／C2 主张全文见 [`Research_Plan.md`](../00_Practice_UAV_Aerial_Detection/Research_Plan.md)；近中远边界见 [`Mainline_A_Current.md`](../00_Practice_UAV_Aerial_Detection/Mainline_A_Current.md)。

| 入口 | 路径 |
|---|---|
| 练手现行目录 | [`00_Practice_UAV_Aerial_Detection/`](../00_Practice_UAV_Aerial_Detection/README.md) |
| 研究计划（主张全文） | [`Research_Plan.md`](../00_Practice_UAV_Aerial_Detection/Research_Plan.md) |
| P0 证据槽 | [`Experiments/papers/P0_EI/`](../00_Practice_UAV_Aerial_Detection/Experiments/papers/P0_EI/Run_Index.md)（Run 索引） |
| 论文概况与实验内容（导读） | [`P0_EI_Paper_Overview_and_Experiments.md`](../00_Practice_UAV_Aerial_Detection/P0_EI_Paper_Overview_and_Experiments.md) |
| UAVDT（G 盘） | `G:\Schloar Data\P0\UAVDT\`（2026-09-27 核实：50 序列 `*_gt_whole.txt`／40735 帧；Stage E 运行时路径 `G:\Schloar Data\UAVDT\` 已迁移） |

---

## 当前唯一事项

**Stage A–F 全部 PASS；EI 包装（近邻协议对标表＋失败／边界例＋可复现附录＋图 1–5）已完成；C1／C2 已按 Stage B–F 结果改为终稿措辞（2026-09-27）。下一步：① 5060 Ti 正式时序（Run G，结果单独写 `Timing_5060Ti_Table.md`，不与 1660 合并）；② 稿件正文（按 `Writing/P0_EI_Outline.md`）。叙事保持「冻结权重上的推理协议对比」，不新训、不改映射、不开 Paper 2–7。**

T4／Kaggle 训练轨已于 2026-09-18 撤回，未产生任何新权重；本地冻结权重未被改写。Paper 2–7 仍 **PAUSED**；机制主张 P0-A-* 仍 **HOLD**。

---

## 进度

| 项 | Run ID | 状态 |
|---|---|---|
| A 冻结（权重／环境／协议定义） | `P0-BENCH-A-ENV-20260917-01` | **PASS** |
| B 1660 流水线计时（cal48） | `P0-BENCH-B-TIMING-20260917-01` | **PASS** |
| C cal48 精度（开发证据） | `P0-BENCH-C-CAL48-20260917-01` | **PASS** |
| D VisDrone test-dev 一次性终评 | `P0-BENCH-D-TESTDEV-20260917-01` | **PASS** |
| E UAVDT 跨集（40735 帧） | `P0-BENCH-E-UAVDT-20260918-FULL` | **PASS** |
| F 图级配对统计 | `P0-BENCH-F-TESTDEV-20260917-01` | **PASS** |
| EI 包装 | — | **DONE** |
| C1／C2 主张措辞 | — | **FINAL**（2026-09-27） |
| G 5060 Ti 正式时序 | `P0-BENCH-G-5060TI-{SMOKE,CAL48,TESTDEV}-20261001-01` | **未跑**；结果单列 |
| 稿件正文 | — | **未开始** |

### 冻结权重（未改）

- 路径：`11_Datasets/processed/VisDrone/BT1/BT1-LOCAL-20260913-01/train/weights/last.pt`
- SHA256：`bc42d54e37acaf1f698af487439dc222fa86fb4498623e8cf954df14e0aa5533`
- 五协议：`F640`／`F1280`／`DensK1`／`UnifAll`／`SAHI640`

### 主张（终稿措辞摘要）

- **C1：** F1280 比 DensK1 更准（VisDrone test-dev small recall +0.0409，95% CI [0.0355, 0.0462]；precision +0.0681），1660 上时延统计上不可区分（Wilcoxon p = 0.235）；不主张"更快"。
- **C2：** 选区／覆盖协议只移动召回–精度–时延权衡：VisDrone 上 UnifAll small recall 最高但时延约 3.3×、精度下降；SAHI640 在两集上均被 F1280 支配；UAVDT 排序为 F1280 0.793 > UnifAll 0.782 > DensK1 0.767 > SAHI640 0.760 > F640 0.708。
- **范围：** 仅 1660 计时；匹配器 precision／small recall，不是 AP；单一冻结权重。

---

## 实验门（当前）

- **禁止**新训／微调／改网络／开 Paper 2–7，除非本页再次书面授权。
- 类别映射保持 FROZEN；不得因看到分数回改映射或 conf。
- 终表／Run 记录进仓库 `Experiments/papers/P0_EI/`；1660 时序≠正式 5060 Ti 表。
- 第三方 UAVDT 子集（含已拒 Kaggle JSON 包）禁止作主库。

---

## 下一步

1. **5060 Ti 正式时序表：** 按 Run G（`P0-BENCH-G-5060TI-SMOKE/CAL48/TESTDEV-20261001-01`，UAVDT 可选）在本机 RTX 5060 Ti 16GB 上跑（计划中，未跑；5060 Ti 为 Blackwell（sm_120），冻结环境 torch 2.7.1+cu126（`00_freeze/pip_freeze.txt`）不支持；2026-10-04 已建 conda 环境 `UAV_BT2`（Python 3.10，torch 2.7.1+cu128，ultralytics／sahi 已装），跑 Run G 前须把该环境快照（pip freeze、nvidia-smi）写入 `00_freeze/` 并登记与冻结环境的差异；权重／协议／评价器不变）；结果单独写 `Experiments/papers/P0_EI/04_timing/Timing_5060Ti_Table.md`，**不与 1660 合并**。
2. **稿件正文：** 按 `Writing/P0_EI_Outline.md` 起草，主张只用 C1／C2 终稿措辞。
3. **会期：** 选定 2027 年 EI 会期（主跟踪 ICIP 2027 全文）并写入本页。
4. **不默认：** 同质第三集；新模块／重训。

---

## Post-EI 预备包登记（IDLE · 2026-09-24）

> **纪律：** 下表 **不**改变上文「当前唯一事项」。唯一 ACTIVE 仍为 **P0_EI**。预备包在再授权前保持 IDLE。

| 代号 | 路径 | 状态 | 说明 |
|---|---|---|---|
| P0_EI | `00_Practice_UAV_Aerial_Detection/` | **ACTIVE** | 当前唯一执行 |
| A · RailUAV-SOD | [`../08_RailUAV_SOD/`](../08_RailUAV_SOD/README.md) | **IDLE / PREP** | Post-EI 数据文预备包；禁采集/训练 |
| B · Paper1 | [`../01_Paper1_OpenWorld_Risk/`](../01_Paper1_OpenWorld_Risk/README.md) | **IDLE / PREP** | Post-EI 方法文预备包；禁 Stage ④ |
| Paper 2–7 | `02_`…`07_` | **PAUSED** | 不变 |

## Venue / 学位分（案头）

信息学院学位分：[`SWJTU_Info_College_Degree_Credit_Note_2026-09-28.md`](SWJTU_Info_College_Degree_Credit_Note_2026-09-28.md)。学术博士：普通 EI／CCF-C **不计分**；两篇一作 SCI 二区为正常评阅最低线。

## 基础手册应读（2026-09-29）

不改变上文唯一事项。阶段变了就改本段，并同步 [`../10_Foundations/00_How_To_Use.md`](../10_Foundations/00_How_To_Use.md)。

现在读：[`01_Notation.md`](../10_Foundations/01_Notation.md)、[`02_Linear_Algebra_Vision.md`](../10_Foundations/02_Linear_Algebra_Vision.md)、[`04_Probability_Detection.md`](../10_Foundations/04_Probability_Detection.md)。读损失时再翻 `03`。组网、相机、强化学习、GAN、A\*、凸优化现在不读。
