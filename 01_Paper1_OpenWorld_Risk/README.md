# Paper 1：铁路UAV开放世界危险感知与风险告警（论文 B）

目录名：`01_Paper1_OpenWorld_Risk`  
论文代号：**B / Paper1 OpenWorld Risk**（与 RailUAV-SOD「A」独立发表）

> **状态：PREP / IDLE（Post-EI 预备包）** — 研究路线脚手架已按 Practice 架构补齐；**不是** Stage ④ / 采集 / 训练授权。  
> 当前全仓库唯一 ACTIVE 仍是 **P0_EI**（见 [`../00_Overview/Current_Stage.md`](../00_Overview/Current_Stage.md)）。  
> 解锁条件：P0_EI 收口后由 `Current_Stage.md` **书面再授权**。

## 你需要看的文件

| 文件 | 用途 |
|---|---|
| [`../00_Overview/Current_Stage.md`](../00_Overview/Current_Stage.md) | **唯一当前事项** |
| [`Research_Plan.md`](Research_Plan.md) | 问题与 C1/C2 |
| [`Stage_Guide.md`](Stage_Guide.md) | 阶段门（干净稿 · IDLE） |
| [`Mainline_Current.md`](Mainline_Current.md) | 近/中/远 |
| [`Completion_Metrics.md`](Completion_Metrics.md) | 学习关卡 |
| [`Literature/`](Literature/) | 主题矩阵 |
| [`Writing/`](Writing/) | 提纲 |
| [`Experiments/`](Experiments/) | 实验槽（IDLE） |
| [`Learning_Notes/`](Learning_Notes/) | 知识块 |

## 已有备忘（保留，勿删）

| 文件 | 说明 |
|---|---|
| [`AB_Independent_Publication_Boundary.md`](AB_Independent_Publication_Boundary.md) | A/B 贡献与结果互不绑定 |
| [`AB_Direction_Judgment_With_Literature_2026-09-24.md`](AB_Direction_Judgment_With_Literature_2026-09-24.md) | 分轨方向/档位（含附录界变） |
| [`Paper1_Dataset_Feasibility_Memo.md`](Paper1_Dataset_Feasibility_Memo.md) | 数据集前置可行性 |
| [`Paper1_Direction_Worth_Judgment_2026-09-24.md`](Paper1_Direction_Worth_Judgment_2026-09-24.md) | 方向再评估 |

A 侧预备包：[`../08_RailUAV_SOD/`](../08_RailUAV_SOD/README.md)

## 处理链

> UAV图像 → 已知目标检测 → 未知候选 → 轨道上下文 → 风险排序 → 可信告警（固定告警预算）

YOLO 结构改动不是默认贡献。A 的数据集**不是** B 的必要条件；B 可用公开/代理数据讲完 C1/C2。

## 🔒 解锁条件与禁令（2026-09-26 由原 POST_EI_HANDOFF 并入）

**解锁条件：**

1. P0_EI 包装收口，或用户书面切换 `../00_Overview/Current_Stage.md`。
2. 本页或 `Current_Stage.md` 出现「授权启动 01_Paper1 / 阶段①或④」类字样。
3. A/B 独立边界仍有效：B **不**等待 A 中稿；A 与 B 可互相引用，但不得互为必要条件。

**解锁前禁止：**

- Stage ④ 数据采集与正式训练。
- 把本目录标成 ACTIVE。
- 把 A 的标注效率或合成曲线写成 B 的主证据。
- 静默合并其他目录的冲突稿。

**解锁后第一动作：** 按干净的 `Stage_Guide.md`，从阶段①知识和阶段②文献冻结推进；数据建立只在阶段④、且再次授权后进行。
## 硬边界

- **C1**：已知 + 未知双路径，在**固定告警预算**下提高危险召回。  
- **C2**：轨道上下文风险排序提高告警决策价值。  
- 划界：SRLF、Meng、conformal risk control、false-novelty budget、UAV-OOD 滤波——须写出增量，忌同构「又一篇未知检出」。  
- 不研究三维重建、通信、ISAC、多模态、下一视点、RL/多机。  
- 未授权前：不采集、不新训、不开正式主表 Run。

## 投稿锚（计划，非承诺）

| 档 | 目标 |
|---|---|
| 中位 | TIM / Measurement（JCR 三区应用向） |
| 上限 | TITS / TIM（双路径+预算+轨旁风险齐全） |
| 下限 | Drones / Access（近似 UAV-OOD / YOLO+启发式时） |
