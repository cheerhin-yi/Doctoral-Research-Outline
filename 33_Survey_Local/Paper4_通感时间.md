# Paper 4：能量固定时，先拍照还是先转发

日期：2026-10-07。案头协议，不授权实验。Paper 4 仍 PAUSED。样例数是冻结格式，不是实测能耗。

这篇只留两个主张：R1 和 R2。不做同波形通感。Liu, Fan; Cui, Yuanhao; Masouros, Christos; Xu, Jie; Han, Tony Xiao; Eldar, Yonina C.; Buzzi, Stefano. Integrated Sensing and Communications. *IEEE Journal on Selected Areas in Communications*, 2022. https://doi.org/10.1109/JSAC.2022.3156632 机构稿：https://discovery.ucl.ac.uk/id/eprint/10147120 该文的通感是通信与感知共用频段和硬件。这里没有雷达前端，不能写成 ISAC。

## R1：按风险分时间是否多送到高风险包

主张在说什么。一架中继机的电量要同时够悬停拍照和把 Paper 3 的包发出去。R1 要证明：在同一能量预算下，按风险分数把时间分给拍照和转发，送达的高风险包多于拍照和转发各一半。

它不说：联合波形优化已经做成。也不说山区路径损耗已经测过。

具体干什么。

1. 建 `P4_proxy_01/`。输入用 Paper 3 的 `packet` 表。没有正式包时，用 `frames/dets.csv` 的分数当代理，并写 `packet_source: missing_proxy`。
2. 写 `freeze.md`。冻结总能量、拍照一次的能量、转发一个包的能量、高风险阈值。例子：`energy_budget: 100`，`energy_per_shot: 5`，`energy_per_packet: 2`，`high_risk_score: 0.5`。这些是账本单位，不是瓦时。看完送达数再改单价，这组作废。
3. 两种分配。均等：一半能量拍照，一半转发。按风险：分数高于阈值的包先占转发能量，剩下的才拍照。
4. 填 `tables/r1_split.csv`，列：`policy,shots,packets_sent,high_risk_delivered,energy_used`。行是 `equal` 和 `risk`。

怎样算成立。`risk` 的 `high_risk_delivered` 必须高于 `equal`。不高则 R1 不成立，只留能量账本，不称通感。

难度中。5060 Ti 上的表计算就能做，不需要信道仪。可投应用向通信刊，对照 Zeng, Yong; Wu, Qingqing; Zhang, Rui. Accessing From the Sky. *Proceedings of the IEEE*, 2019, 107: 2327–2375. https://doi.org/10.1109/JPROC.2019.2952892 能耗方法综述见 Jin, Huilong 等. *Vehicular Communications*, 2023, 41: 100594. https://doi.org/10.1016/j.vehcom.2023.100594 合著者未从摘要页核全。JCR 当年核。会议不计入七篇。

## R2：链路变差时是否少拍照

主张在说什么。转发变贵时，还按原比例拍照会把高风险包挤掉。R2 要证明：把每个包的能量乘上一个冻结的恶化系数后，按风险的分配会减少拍照、保住高风险送达；均等分配做不到。

具体干什么。在 freeze 里写 `link_penalty: 2`，只作用于转发能量。重跑 R1 的两种策略。填 `tables/r2_penalty.csv`，列与 R1 相同，另加 `penalty`。看完再改系数，作废。

怎样算成立。恶化后 `risk` 的拍照次数下降，且高风险送达仍高于 `equal`。否则 R2 不成立。难度中。和 R1 写成同一篇的第二项。

## 不做的检查

轨迹优化、频谱分配、雷达共用硬件，都不进贡献。年龄和能量不能同时最优已有仿真结论，见 Zhang, Xin 等. *IEEE Transactions on Communications*, 2024, 72: 1849–1861. https://doi.org/10.1109/tcomm.2023.3337400 合著者未核全。所以本文不把“又快又省”写成主张。
