# Paper1 / B 写作提纲（预备 · Intro + Related Work 骨架）

依据：`Research_Plan.md` · `Writing/Claim_Freeze_C1_C2.md`（**DESK-FROZEN**）· AB 边界 · AB 方向判断。  
状态：PREP/IDLE；**不**写入未跑通的实验数字。  
**主张不定死：** Intro 默认挂中位 C1/C2；若启用 Claim_Freeze **弱 fallback（W1–W3）**，贡献列表与 venue 须同步收缩到 **JCR Q2/Q3 related**（见政策文件）。

## 贡献类型（摘要口令 · 对齐冻结卡）

1. **C1**：已知+未知双路径，在**固定告警预算**下提高危险召回（相对闭集 YOLO / 强未知基线）。  
2. **C2**：轨道上下文风险排序提高可派发告警价值（相对 Detection-only / Unknown-only / 简单规则）；删除未知支路或风险层应变弱。

## 建议结构

1. **Introduction** — 见下节骨架。  
2. **Related Work** — 见下节差异化骨架。  
3. **Method** — Known 骨干；未知候选；零泄漏协议；风险层；告警预算决策。  
4. **Experiments** — 主图预算曲线；Known 性能；误报负担；两处删除；失败分析。  
5. **Conclusion** — 两项以内、证据支持。

---

## Introduction 骨架（段落级 · 指向冻结主张）

| 段 | 功能 | 可写要点（案头） | 禁止 |
|---|---|---|---|
| I-1 场景痛点 | 铁路 UAV 巡检：小目标/远距/背景复杂；类别不可穷举 | 闭集检测回答「像什么」；运维还要「是否侵界、是否值得复核」 | 宣称已有自采大数据集 |
| I-2 现有缺口 | 检出 ≠ 可派发；unknown AP ≠ 危险召回 | 指向 SRLF/Meng/OOD：缺固定预算与派单层 | 贬低近邻无依据 |
| I-3 本文问题 | 固定预算下双路径 + 轨道上下文能否提高可派发危险告警 | 直接挂 C1/C2 冻结句 | 把 A 的数据文贡献写入 |
| I-4 贡献列表 | 仅 C1、C2 两条；各挂最低证据与删除实验 | 与 `Claim_Freeze_C1_C2.md` 一字不漂移 | 第三条「新 YOLO 模块」 |
| I-5 范围边界 | 单目 RGB；公开/代理数据协议；不做三维/通信/多机 | 一句指向 A 可引用但非必要 | 「无 A 则无 B」 |

**引言收束句（草案）：**  
本文不追求开放世界基准刷分，而验证：在固定告警预算下，已知+未知双路径与轨道上下文风险排序是否提高可派发危险告警的价值（C1/C2）。

---

## Related Work 差异化骨架（必须对表）

| 小节 | 覆盖文献（增补 ID） | 差异化一句（对齐冻结卡） |
|---|---|---|
| RW-1 铁路侵界/障碍 | T3-CAO；T3-TIM；T3-SENS | 场景合法；本文贡献在告警预算与双路径，不在综述重写 |
| RW-2 OWOD/OSOD/OVD | T2-OWOD；T2-OSOD；T2-YW/CAST/UOVD | 术语跟 Survey；指标跟 OSOD 反思；OVD **只作基线** |
| RW-3 铁路/UAV 未知近邻 | T2-SRLF；T2-MENG | vs SRLF：预算+派单+排序；vs Meng：决策层与删除实验 |
| RW-4 风险控制/预算 | T4-CRC；T4-FNB | vs conformal：双路径×配额×派单；vs false-novelty：补轨旁风险 |
| RW-5 UAV OOD | T2-OOD | 与纯 OOD 滤波划界；主图是危险召回–预算 |
| RW-6 轨道几何风险 | 主矩阵 T1-01；T3-02；T3-03 | 距离/区域已有；本文增量在**未知候选接入后的排序价值** |

**Related Work 收束（草案）：**  
既有工作分别覆盖侵界综述、开放世界检出、校准式风险控制与轨道几何风险，但缺少在固定告警预算下将已知+未知双路径与轨道上下文排序联合为可派发危险告警的系统证据——此即 C1/C2。

---

## 证据槽指针（授权后）

| 章节需要 | 路径 |
|---|---|
| 主张冻结 | `Claim_Freeze_C1_C2.md` |
| 冻结与协议 | `../Experiments/papers/B_Paper1_OpenWorld/00_freeze/` |
| 主评测 | `../Experiments/papers/B_Paper1_OpenWorld/01_main_eval/` |
| 预算曲线 | `../Experiments/papers/B_Paper1_OpenWorld/02_alarm_budget/` |
| 删除实验 | `../Experiments/papers/B_Paper1_OpenWorld/03_ablation/` |
| 包装 | `../Experiments/papers/B_Paper1_OpenWorld/05_packaging/` |

## Venue 一句（案头）

中位：**JCR Q2–Q3** 应用刊；上限 TITS/TIM（quartile Unknown，以当年 JCR 为准）；弱 fallback 仍保 Q2/Q3 related。

## 本篇不做

把 A 的数据集当本文贡献；无预算曲线的 unknown AP 刷分；与 SRLF 同构；未授权即写主表数字；把强主张写成唯一允许的成功形态。
