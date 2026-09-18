# 当前阶段（唯一入口）

更新：2026-09-18（Asia/Shanghai）。

本文件是全项目**唯一当前事项入口**。与源文件冲突时，以本页与 [`Research_Question_Decision_2026-09-16.md`](../00_Practice_UAV_Aerial_Detection/Research_Question_Decision_2026-09-16.md) 为准。

| 入口 | 路径 |
|---|---|
| 练手现行目录 | [`00_Practice_UAV_Aerial_Detection/`](../00_Practice_UAV_Aerial_Detection/README.md) |
| 主线 A 当前执行 | [`Mainline_A_Current.md`](../00_Practice_UAV_Aerial_Detection/Mainline_A_Current.md) |
| P0 Benchmark | [`Experiments/P0_Benchmark/`](../00_Practice_UAV_Aerial_Detection/Experiments/P0_Benchmark/) |
| UAVDT（G 盘） | `G:\Schloar Data\UAVDT\`（布局 PASS：50 序列／40735 帧／50×`*_gt_whole.txt`） |
| T4 过程目录（G 盘，仅历史过程件） | `G:\Schloar Data\P0_T4_Train\`（**训练轨已撤回**，不再开训） |

---

## 当前唯一事项

**回到 P0 冻结推理对比轨：冻结 VisDrone `last.pt`，不新训、不微调；完成 Stage E（UAVDT 五方法同权推理）并整理 EI 协议对比稿（主张骨架 P0-EI-C1／C2）。**

用户于 2026-09-18 明确撤回 2026-09-17 的 T4 真训练授权（原选 B）。Kaggle Version #1 已 Failed（venv／ensurepip，约 21.6s），**未产生任何新权重**。本地冻结权重未被改写。

Paper 2–7 仍 **PAUSED**。机制主张 P0-A-* 仍 **HOLD**。

---

## 进度

| 项 | 状态 |
|---|---|
| A–D／F（冻结 `last.pt`，1660SUPER） | **PASS**（历史对照，保留） |
| E 数据 UAVDT | **布局 PASS**；五方法推理／评估 **未跑** |
| T4／Kaggle 训练轨 | **已撤回**；V1 Failed，无 `last.pt`／`best.pt` 产出 |
| 4090 正式时序 | 仍缺；与 1660／T4 分列披露 |

### 冻结权重（未改）

- 路径：`11_Datasets/processed/VisDrone/BT1/BT1-LOCAL-20260913-01/train/weights/last.pt`
- SHA256：`bc42d54e37acaf1f698af487439dc222fa86fb4498623e8cf954df14e0aa5533`
- 本机复核（2026-09-18）：Hash 一致；`LastWriteTime` = 2026-09-13 14:41:20

五方法协议名：`F640`／`F1280`／`DensK1`／`UnifAll`／`SAHI640`（磁盘名可能略异，以 Tracker 为准）。

---

## 实验门（当前）

- **禁止**新训／微调／改网络／开 Paper 2–7，除非本页再次书面授权。
- Stage E：沿用已冻结的 VisDrone→UAVDT 类别映射；推理权重 = 上列冻结 `last.pt`。
- 过程文件若仍落 G 盘，可进 `P0_T4_Train` 仅作归档；**终表／Run 记录进仓库 `Experiments/`**。
- 第三方 UAVDT 子集（含已拒 Kaggle JSON 包）禁止作主库。

---

## 下一步

1. 用冻结 `last.pt` 跑 Stage E 五方法 UAVDT 推理＋评估（映射已冻）。
2. 正式 4090 时序表仍可选、分列。
3. 以 D＋F（＋E 若完成）写 EI 协议对比草稿；叙事保持「冻结权重上的推理协议对比」，**不得**写 T4 已训成新权重。
