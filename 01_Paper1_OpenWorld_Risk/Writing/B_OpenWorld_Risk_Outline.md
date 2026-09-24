# Paper1 / B 写作提纲（预备）

依据：`Research_Plan.md` · AB 边界 · AB 方向判断。

## 贡献类型（摘要口令）

1. 已知+未知双路径，在**固定告警预算**下提高危险召回（相对闭集 YOLO / 强未知基线）。  
2. 轨道上下文风险排序提高可派发告警价值（相对 Detection-only / Unknown-only / 简单规则）；删除未知支路或风险层应变弱。

## 建议结构

1. **Introduction** — 问题=闭集盲区 + 告警负担；不是又一个 YOLO。  
2. **Related Work** — 侵界综述（Cao/TIM OID）；OWOD/OSOD；SRLF/Meng；风险量化；conformal/预算；UAV-OOD。  
3. **Method** — Known 骨干；未知候选；零泄漏协议；风险层；告警预算决策。  
4. **Experiments** — 主图预算曲线；Known 性能；误报负担；两处删除；失败分析。  
5. **Conclusion** — 两项以内、证据支持。

## 证据槽指针（授权后）

| 章节需要 | 路径 |
|---|---|
| 冻结与协议 | `../Experiments/papers/B_Paper1_OpenWorld/00_freeze/` |
| 主评测 | `../Experiments/papers/B_Paper1_OpenWorld/01_main_eval/` |
| 预算曲线 | `../Experiments/papers/B_Paper1_OpenWorld/02_alarm_budget/` |
| 删除实验 | `../Experiments/papers/B_Paper1_OpenWorld/03_ablation/` |
| 包装 | `../Experiments/papers/B_Paper1_OpenWorld/05_packaging/` |

## 本篇不做

把 A 的数据集当本文贡献；无预算曲线的 unknown AP 刷分；与 SRLF 同构。
