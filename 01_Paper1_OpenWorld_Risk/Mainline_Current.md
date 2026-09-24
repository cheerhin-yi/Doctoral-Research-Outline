# 主线当前执行页：Paper1 / B

更新：2026-09-24 晚（Asia/Shanghai）。  
效力：预备叙述；与 `Current_Stage` 冲突时以 **Current_Stage** 为准。  
包状态：**PREP / IDLE**（未改 ACTIVE）。

## 1. 资源边界

- 算力与注意力优先 **P0_EI**；本包 IDLE 不抢训。
- 不把未采集/未授权数据写成已有结果。
- 未来可 UAV：方向前提，非今日 Stage ④ 授权。

## 2. 近 / 中 / 远

| 时段 | 做什么 | 不做 |
|---|---|---|
| **近**（P0_EI 收口前） | 维护预备包、文献划界、提纲、主张冻结 | 不采集、不新训、不开主 Run |
| **中**（再授权后） | 阶段①–③；再④数据协议 | 不等待 A 中稿；不把 A 主表当必要条件 |
| **远** | 阶段⑤–⑦；**JCR Q2–Q3** 中位 / TITS·TIM 上限成稿；必要时启用弱 fallback | 不堆 YOLO 模块；不把纯 OOD 当 Paper1 主成果（低于 floor） |

## 3. 当前研究问题

固定告警预算下，已知+未知双路径与轨道上下文风险排序能否提高可派发危险告警的价值？

## 4. 主张

C1 / C2 · **DESK-FROZEN · IDLE**（中位；弱 fallback 已文档化，见 `Writing/Claim_Freeze_C1_C2.md`）。  
Venue 政策：`../00_Overview/Venue_and_Claim_Policy_JCR_2026-09-24.md`。

## 5. 近案头清单（2026-09-24）

| 项 | 状态 |
|---|---|
| C1/C2 冻结卡（精确句/范围/判据/划界） | **DONE** · `Writing/Claim_Freeze_C1_C2.md` |
| 文献增补加厚（Practice 列式） | **DONE** · `Literature/Literature_Matrix_Addendum_2026-09-24.md` |
| Stage ① LN03/04/05 可核对知识 | **DONE**（案头块已写入） |
| Writing Intro+RW 骨架 | **DONE** · `Writing/B_OpenWorld_Risk_Outline.md` |
| MUST 精读与单篇笔记回链 | **剩余**（解锁/有空继续，仍 IDLE） |
| Stage ③ 最小复现 / Stage ④ 数据 | **剩余 · 未授权** |
| 正式训练与主 Run | **禁止** |

## 6. 成功标准（预备阶段）

1. Practice 同构目录齐；STATUS=PREP/IDLE。  
2. 既有 AB/可行性备忘均保留并可从 README 链到。  
3. Stage_Guide 无冲突标记。  
4. 不改变唯一 ACTIVE=P0_EI。
