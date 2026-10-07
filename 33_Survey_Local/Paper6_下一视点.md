# Paper 6：不确定时下一帧看哪里，以及何时停止

日期：2026-10-07。案头协议，不授权实验。Paper 6 仍 PAUSED。不飞真机。

这篇只留两个主张：R1 和 R2。视点在已有图集或网格上选，不优化真实航迹。

## R1：按不确定性选下一视点是否少漏

主张在说什么。固定航线会重复看已经清楚的地方。R1 要证明：在同一视点预算下，优先看 Paper 1 低分或 Paper 5 拒判的格子，漏掉的危险少于按固定顺序看。

它不说：新的下一最佳视点理论。遮挡下的下一视点已有 Strand 等. *IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing*, 2025. https://doi.org/10.1109/JSTARS.2025.3638881 主动监视综述见 *ACM Computing Surveys*, 2025, 58(2): 35. https://doi.org/10.1145/3760389 本文只比两种选格规则。

具体干什么。

1. 建 `P6_proxy_01/`。把图分成冻结网格，例如 `grid: 4x4`。每格有危险框数和最低分数。没有 Paper 5 时，最低分数低于 0.3 的格记为不确定，并写 `uncertainty_source: score_proxy`。
2. 写 `freeze.md`：`view_budget: 6`，`uncertain_score: 0.3`。看完漏检再改预算，作废。
3. 固定顺序：按格编号看，满 6 格停止。不确定优先：先看低分格，再看其余。
4. 填 `tables/r1_view.csv`，列：`policy,views_used,risk_found,risk_missed`。参照是全部格子里的危险框，不是只在看过的格子里算。

怎样算成立。不确定优先的 `risk_missed` 必须更少。不少则 R1 不成立。难度中。公开图就能做。

## R2：停止规则是否少看空格

主张在说什么。预算没用完也可以停。R2 要证明：连续两格都高于冻结分数就停止，看到的空格少于用满预算；漏检不能高于用满预算超过冻结容差。

具体干什么。容差写死，例如 `miss_tolerance: 0`。填 `tables/r2_stop.csv`，列：`policy,views_used,empty_views,risk_missed`。行是 `full_budget` 和 `early_stop`。

怎样算成立。`early_stop` 的空格更少，且漏检不超过容差。漏检增加，停止规则不进贡献。难度中。和 R1 写成同一篇的第二项。

不做真实航时和禁飞区。那些没有线路许可就测不了。
