# 航拍基准与评测口径 · 必读清单

**主题问题：** VisDrone／UAVDT 等航拍集上，小目标口径、表轴与跨集陈述应如何写？

| ID | 优先级 | 题目 | 年 | Venue | 笔记 | PDF |
|---|---|---|---:|---|---|---|
| T4-01 | MUST | VisDrone Challenge / DET overview（Zhu / Du et al.；VisDrone project page） | 2019 | ICCVW etc. | [notes/T4-01_VisDrone.md](notes/T4-01_VisDrone.md) | `pdfs/` 待放入 |
| T4-02 | SHOULD | UAVDT（Du et al.；UAVDT benchmark） | 2018 | ECCV（2026-10-06 核：ECCV 2018 主会论文集，DOI 10.1007/978-3-030-01249-6_23；原登记 ECCV Workshops） | [notes/T4-02_UAVDT.md](notes/T4-02_UAVDT.md) | `pdfs/` 待放入 |
| T4-03 | 建议优先读 | VisDrone（TPAMI）（Zhu et al.；DOI 10.1109/TPAMI.2021.3119563） | 2022 | TPAMI | —（未建笔记） | `pdfs/` 待放入 |
| T4-04 | 候选 | VisDrone-DET2021 Results（Cao et al.；DOI 10.1109/ICCVW54120.2021.00319） | 2021 | ICCVW | —（未建笔记） | `pdfs/` 待放入 |
| T4-05 | 候选 | Speed/Accuracy Trade-offs（Huang et al.；DOI 10.1109/CVPR.2017.351） | 2017 | CVPR | —（未建笔记） | `pdfs/` 待放入 |
| T4-06 | 候选 | SODA（Cheng et al.；DOI 10.1109/TPAMI.2023.3290594） | 2023 | TPAMI | —（未建笔记） | `pdfs/` 待放入 |
| T4-07 | 候选 | Demšar 2006（Demšar；JMLR） | 2006 | JMLR | —（未建笔记） | `pdfs/` 待放入 |

## 候选文献事实表（2026-10-06 检索）

> 只记事实：元数据经 DOI／arXiv／会议官方页／官方文档核对，数据集、检测器、指标、时延硬件读自原文（或注明来源）；查不到的写 **待补**。优先级「建议优先读／候选」为助手按事实给出的阅读顺序建议，与上表 MUST／SHOULD（用户定）不是一回事。最后一列「与P0关系（用户填）」留空，由你本人填写；本表不写 gap 判断。汇总与核验记录见 [`../Literature_Matrix.md`](../Literature_Matrix.md) §5。

| ID | 建议优先读（理由） | 题目 | 作者 | 年 | Venue | 链接 | 数据集 | 检测器 | 报告指标 | 时延／FPS（硬件） | 核心做法（事实，一句） | 与P0关系（用户填） |
|---|---|---|---|---:|---|---|---|---|---|---|---|---|
| T4-03 | **是**：P0 主评测集 VisDrone2019-DET test-dev（1,610 张）的正式出处 | Detection and Tracking Meet Drones Challenge | Zhu et al. | 2022 | IEEE TPAMI 44, 7380–7399（arXiv 2020） | [DOI 10.1109/TPAMI.2021.3119563](https://doi.org/10.1109/TPAMI.2021.3119563)；[arXiv:2001.06303](https://arxiv.org/abs/2001.06303) | VisDrone（DET 10,209 张：train 6,471／val 548／test-challenge 1,580／test-dev 1,610） | 赛事提交方法与基线（Faster R-CNN、FPN、RefineDet 等） | AP、AP50、AP75、AR1／10／100／500 | DET 部分未报 FPS | VisDrone 数据集（DET／VID／SOT／MOT）与 2018–2020 挑战赛综述 |  |
| T4-04 | — | VisDrone-DET2021: The Vision Meets Drone Object Detection Challenge Results | Cao et al. | 2021 | ICCV Workshops 2021（VisDrone） | [DOI 10.1109/ICCVW54120.2021.00319](https://doi.org/10.1109/ICCVW54120.2021.00319)；[CVF](https://openaccess.thecvf.com/content/ICCV2021W/VisDrone/html/Cao_VisDrone-DET2021_The_Vision_Meets_Drone_Object_Detection_Challenge_Results_ICCVW_2021_paper.html) | VisDrone-DET test-challenge（1,580 张） | 参赛方法（多为 YOLOv5、Cascade R-CNN 等的变体） | AP、AP50、AP75、AR1／10／100／500 | 否 | 汇总 VisDrone-DET2021 挑战赛提交方法与结果 |  |
| T4-05 | — | Speed/Accuracy Trade-Offs for Modern Convolutional Object Detectors | Huang et al. | 2017 | CVPR 2017 | [DOI 10.1109/CVPR.2017.351](https://doi.org/10.1109/CVPR.2017.351)；[arXiv:1611.10012](https://arxiv.org/abs/1611.10012) | COCO | Faster R-CNN、R-FCN、SSD × 多种特征提取器 | mAP、GPU 时间、内存、FLOPs、参数量 | 是：GPU 时间，GTX Titan X（主机 CPU Xeon E5-1650 v2） | 在统一实现下系统比较多种检测元架构与特征提取器的速度／精度／内存权衡 |  |
| T4-06 | — | Towards Large-Scale Small Object Detection: Survey and Benchmarks（SODA） | Cheng et al. | 2023 | IEEE TPAMI 45(11), 13467–13488 | [DOI 10.1109/TPAMI.2023.3290594](https://doi.org/10.1109/TPAMI.2023.3290594)；[arXiv:2207.14096](https://arxiv.org/abs/2207.14096) | SODA-D（24,828 张，278,433 实例）、SODA-A（2,513 张，872,069 实例） | 多种主流检测器的基准评测 | AP、AP50、AP75，及按尺度的 APeS／APrS／APgS／APN | 仅附录一张表：Oriented RCNN 不同提议数下的 FPS（单块 RTX 2080Ti） | 小目标检测综述，并发布驾驶与航拍两个大规模小目标基准 |  |
| T4-07 | — | Statistical Comparisons of Classifiers over Multiple Data Sets | Demšar | 2006 | Journal of Machine Learning Research 7, 1–30 | [JMLR](https://www.jmlr.org/papers/v7/demsar06a.html) | 不适用（方法论） | 不适用 | 不适用（统计检验方法） | 不适用 | 推荐用 Wilcoxon 符号秩检验比较两个分类器，多个分类器用 Friedman 检验及事后检验 |  |

## 阅读顺序

1. MUST 先读；SHOULD 在写 Related Work 对表时补。
2. 每篇只记模板三样；细节证据回 Matrix §3。

## PDF 放置

文件名建议：`ID_ShortTitle.pdf`（例：`T1-01_SAHI.pdf`）。放入后把上表 PDF 列改为文件名。
