# 航拍基准与评测口径 · 阅读清单

**主题问题：** VisDrone／UAVDT 等航拍集上，小目标口径、表轴与跨集陈述应如何写？

> 合并说明（2026-10-07）：原「必读清单」与「候选文献事实表（2026-10-06 检索）」合并为本表，一篇一行。优先级：原 MUST → 必读（原 T4-01 已并入 T4-03，T4-03 因此为必读）；助手按事实建议的“建议优先读”保留；原 SHOULD 与“候选”→ 选读（原 SHOULD 已注明）。状态默认“未读”，读到哪一步请自己改为“在读／已读”。末列由你填写。数据集／检测器／指标／时延读自原文（原 MUST／SHOULD 条目于 2026-10-07 按 arXiv／CVF 全文补齐），查不到的写 **待补**。“核心做法”一句话见 [`../Literature_Matrix.md`](../Literature_Matrix.md) §2 定位列与 §5。

| 编号 | 题目 + 链接 | 年／Venue | 数据集 | 检测器 | 指标 | 时延／硬件 | 阅读优先级 | 状态 | 与P0关系（用户填） |
|---|---|---|---|---|---|---|---|---|---|
| T4-03 | Detection and Tracking Meet Drones Challenge（Zhu et al.）<br>[DOI 10.1109/TPAMI.2021.3119563](https://doi.org/10.1109/TPAMI.2021.3119563)；[arXiv:2001.06303](https://arxiv.org/abs/2001.06303)；笔记 [notes/T4-01_VisDrone.md](notes/T4-01_VisDrone.md)（原 T4-01“VisDrone Challenge / DET overview”2026-10-07 并入本行） | 2022 · IEEE TPAMI 44, 7380–7399（arXiv 2020） | VisDrone（DET 10,209 张：train 6,471／val 548／test-challenge 1,580／test-dev 1,610） | 赛事提交方法与基线（Faster R-CNN、FPN、RefineDet 等） | AP、AP50、AP75、AR1／10／100／500 | DET 部分未报 FPS | 必读 | 未读 |  |
| T4-07 | Statistical Comparisons of Classifiers over Multiple Data Sets（Demšar）<br>[JMLR](https://www.jmlr.org/papers/v7/demsar06a.html) | 2006 · Journal of Machine Learning Research 7, 1–30 | 不适用（方法论） | 不适用 | 不适用（统计检验方法） | 不适用 | 选读 | 未读 |  |
| T4-05 | Speed/Accuracy Trade-Offs for Modern Convolutional Object Detectors（Huang et al.）<br>[DOI 10.1109/CVPR.2017.351](https://doi.org/10.1109/CVPR.2017.351)；[arXiv:1611.10012](https://arxiv.org/abs/1611.10012) | 2017 · CVPR 2017 | COCO | Faster R-CNN、R-FCN、SSD × 多种特征提取器 | mAP、GPU 时间、内存、FLOPs、参数量 | 是：GPU 时间，GTX Titan X（主机 CPU Xeon E5-1650 v2） | 选读 | 未读 |  |
| T4-02 | The Unmanned Aerial Vehicle Benchmark: Object Detection and Tracking（UAVDT）（Du et al.）<br>[DOI 10.1007/978-3-030-01249-6_23](https://doi.org/10.1007/978-3-030-01249-6_23)；[CVF](https://openaccess.thecvf.com/content_ECCV_2018/html/Dawei_Du_The_Unmanned_Aerial_ECCV_2018_paper.html)；笔记 [notes/T4-02_UAVDT.md](notes/T4-02_UAVDT.md) | 2018 · ECCV 2018（原登记 ECCV Workshops，2026-10-06 已改正） | UAVDT（约 80k 帧，1080×540，车辆；DET／MOT／SOT） | Faster-RCNN、R-FCN、SSD、RON（DET 基线） | AP（DET） | **待补**（DET 部分未查到检测器时延） | 选读（原 SHOULD） | 未读 |  |
| T4-04 | VisDrone-DET2021: The Vision Meets Drone Object Detection Challenge Results（Cao et al.）<br>[DOI 10.1109/ICCVW54120.2021.00319](https://doi.org/10.1109/ICCVW54120.2021.00319)；[CVF](https://openaccess.thecvf.com/content/ICCV2021W/VisDrone/html/Cao_VisDrone-DET2021_The_Vision_Meets_Drone_Object_Detection_Challenge_Results_ICCVW_2021_paper.html) | 2021 · ICCV Workshops 2021（VisDrone） | VisDrone-DET test-challenge（1,580 张） | 参赛方法（多为 YOLOv5、Cascade R-CNN 等的变体） | AP、AP50、AP75、AR1／10／100／500 | 否 | 选读 | 未读 |  |
| T4-06 | Towards Large-Scale Small Object Detection: Survey and Benchmarks（SODA）（Cheng et al.）<br>[DOI 10.1109/TPAMI.2023.3290594](https://doi.org/10.1109/TPAMI.2023.3290594)；[arXiv:2207.14096](https://arxiv.org/abs/2207.14096) | 2023 · IEEE TPAMI 45(11), 13467–13488 | SODA-D（24,828 张，278,433 实例）、SODA-A（2,513 张，872,069 实例） | 多种主流检测器的基准评测 | AP、AP50、AP75，及按尺度的 APeS／APrS／APgS／APN | 仅附录一张表：Oriented RCNN 不同提议数下的 FPS（单块 RTX 2080Ti） | 选读 | 未读 |  |

**建议优先读的理由（事实）：**

- T4-03：P0 主评测集 VisDrone2019-DET test-dev（1,610 张）的正式出处

**核心做法（事实，一句；原事实表列）：**

- T4-03：VisDrone 数据集（DET／VID／SOT／MOT）与 2018–2020 挑战赛综述
- T4-04：汇总 VisDrone-DET2021 挑战赛提交方法与结果
- T4-05：在统一实现下系统比较多种检测元架构与特征提取器的速度／精度／内存权衡
- T4-06：小目标检测综述，并发布驾驶与航拍两个大规模小目标基准
- T4-07：推荐用 Wilcoxon 符号秩检验比较两个分类器，多个分类器用 Friedman 检验及事后检验

## 阅读顺序

1. 必读先读，再读建议优先读；选读在写 Related Work 对表时补。
2. 每篇只记模板三样；细节证据回 Matrix §3。

## PDF 放置

文件名建议：`ID_ShortTitle.pdf`（例：`T1-01_SAHI.pdf`）。放入后在本表“题目 + 链接”格末尾加上 PDF 文件名。
