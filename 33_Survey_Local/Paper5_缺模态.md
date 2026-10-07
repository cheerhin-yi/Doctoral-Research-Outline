# Paper 5：图像不可靠时，停判还是改用旁证

日期：2026-10-07。案头协议，不授权实验。Paper 5 仍 PAUSED。

这篇只留两个主张：R1 和 R2。不采集雷达，不把医疗缺测综述当成铁路数据。

## R1：低可信时拒判是否少误报

主张在说什么。雾、逆光和运动模糊会让检测分数不可用。R1 要证明：分数低于冻结阈值时直接拒判，误报少于照样输出框；拒判会漏掉一些真危险，漏检必须同时报。

它不说：新的开放世界检测器。Paper 1 已经负责未知类。本文只处理“这张图的判断还能不能用”。

具体干什么。

1. 建 `P5_proxy_01/`。`frames/dets.csv` 用冻结检测器的框和分数。另做一份退化图：模糊或遮挡，规则写进 `freeze.md`，例如 `blur_ksize: 15`。先冻结再跑。
2. 两种输出。强制：退化图上的框全部保留。拒判：分数低于 `abstain_score` 的框删除。阈值写死，看完误报再改则作废。
3. 填 `tables/r1_abstain.csv`，列：`policy,recall,false_per_frame,abstain_rate`。行是 `force` 和 `abstain`。召回用清晰图上的框当参照，IoU 大于 0.5 算命中。0.5 是本协议匹配线。

怎样算成立。`abstain` 的每帧误报必须低于 `force`。召回掉太多，主张改成“拒判会漏检”，不能写成更可靠。

难度中。公开图加退化就能做。缺模态问题已有综述：Wu, Renjie; Wang, Hu; Chen, Hsiang-Ting. A Comprehensive Survey on Deep Multimodal Learning with Missing Modality. arXiv:2409.07825. https://arxiv.org/abs/2409.07825 所以增量只在拒判表，不在新融合网。可投计算机视觉应用刊或遥感应用刊。JCR 当年核。

## R2：旁证是否只在拒判帧有用

主张在说什么。第二路信号不是永远都要融合。R2 要证明：只在拒判帧启用旁证，误报低于全程融合；旁证本身也不可用时，仍保持拒判，而不是猜一个类别。

旁证用什么。没有雷达时，只用图像派生量：饱和像素比例、模糊度。这是代理，不是射频。写 `side_source: image_proxy`。许可核清的公开热红外可以替换，未核许可证之前不用。

具体干什么。

1. 全程融合：所有帧都用旁证改分数。
2. 仅拒判帧融合：R1 没拒的帧不动。
3. 旁证缺失：把旁证列置空，输出必须等于拒判，不能填默认类别。
4. 填 `tables/r2_side.csv`，列：`policy,recall,false_per_frame,used_side_rate`。

怎样算成立。仅拒判帧的误报不高于全程融合，且旁证缺失时没有新增类别。否则 R2 不成立，这篇只留 R1。

难度中。和 R1 写成同一篇的第二项。不做的是端到端多模态网络。医疗缺测综述不能当本文方法：*Computer Science Review*, 2025, 56: 100720. https://www.sciencedirect.com/science/article/abs/pii/S1574013724001035
