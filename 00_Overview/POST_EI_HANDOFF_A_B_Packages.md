# Post-EI 交接：A/B 预备包登记

更新：2026-09-24（Asia/Shanghai）

## 目的

在 **不改变** `Current_Stage.md` 唯一 ACTIVE=**P0_EI** 的前提下，登记两篇独立论文的路线预备包，便于 EI 收口后按架构启动。

## 包位置

| 代号 | 目录 | 状态 | 说明 |
|---|---|---|---|
| **A** RailUAV-SOD | [`../08_RailUAV_SOD/`](../08_RailUAV_SOD/README.md) | PREP / IDLE | 数据+OVD效率审计+合成审计；中位 Sci Data |
| **B** Paper1 OpenWorld Risk | [`../01_Paper1_OpenWorld_Risk/`](../01_Paper1_OpenWorld_Risk/README.md) | PREP / IDLE | C1 双路径预算 + C2 轨旁风险排序；中位 TIM/Measurement |

独立边界：[`../01_Paper1_OpenWorld_Risk/AB_Independent_Publication_Boundary.md`](../01_Paper1_OpenWorld_Risk/AB_Independent_Publication_Boundary.md)

## 解锁规则

1. 仅当本页或 `Current_Stage.md` **书面**将某包从 IDLE 改为授权执行时，才可采集/训练/主 Run。  
2. A 与 B **分开发表**；可引用，不得互为必要条件。  
3. 未解锁前禁止把预备包写成 ACTIVE。

## 与七篇路线关系

- B = 原七篇中的 Paper 1（开放世界风险）。  
- A = 独立数据文预备包（编号 `08_`，因 `02`–`07` 已占用 Paper2–7）；**不**计入七篇主论文替代关系，也不并入 B 充贡献。
