# 检测器出处（YOLO／Ultralytics） · 必读清单

**主题问题：** 本篇冻结检测器（YOLO11n，Ultralytics）在 Method／Experimental Setup 里应引用哪些正式出处？

**为什么单开文件夹（2026-10-06）：** T1–T4 收的是推理协议、选区与评测口径方面的近邻工作；这里收的是被冻结的检测器本身的出处（Method 节引用），两类用途不同，混放会让 Related Work 与 Setup 的引用难以区分。

| ID | 优先级 | 题目 | 年 | Venue | 笔记 | PDF |
|---|---|---|---:|---|---|---|
| T5-01 | 候选 | YOLO（v1）（Redmon et al.；DOI 10.1109/CVPR.2016.91） | 2016 | CVPR | —（未建笔记） | `pdfs/` 待放入 |
| T5-02 | 候选 | Ultralytics YOLO11（Jocher et al.；官方文档） | 2024 | 软件 | —（未建笔记） | `pdfs/` 待放入 |
| T5-03 | 候选 | YOLOv11 Overview（Khanam et al.；arXiv:2410.17725） | 2024 | arXiv preprint | —（未建笔记） | `pdfs/` 待放入 |

## 候选文献事实表（2026-10-06 检索）

> 只记事实：元数据经 DOI／arXiv／会议官方页／官方文档核对，数据集、检测器、指标、时延硬件读自原文（或注明来源）；查不到的写 **待补**。优先级「建议优先读／候选」为助手按事实给出的阅读顺序建议，与上表 MUST／SHOULD（用户定）不是一回事。最后一列「与P0关系（用户填）」留空，由你本人填写；本表不写 gap 判断。汇总与核验记录见 [`../Literature_Matrix.md`](../Literature_Matrix.md) §5。

| ID | 建议优先读（理由） | 题目 | 作者 | 年 | Venue | 链接 | 数据集 | 检测器 | 报告指标 | 时延／FPS（硬件） | 核心做法（事实，一句） | 与P0关系（用户填） |
|---|---|---|---|---:|---|---|---|---|---|---|---|---|
| T5-01 | — | You Only Look Once: Unified, Real-Time Object Detection | Redmon et al. | 2016 | CVPR 2016 | [DOI 10.1109/CVPR.2016.91](https://doi.org/10.1109/CVPR.2016.91)；[arXiv:1506.02640](https://arxiv.org/abs/1506.02640) | PASCAL VOC 2007／2012 | YOLO、Fast YOLO | mAP、FPS | 是：Titan X GPU（YOLO 45 fps；Fast YOLO 155 fps） | 单个网络一次前向直接回归边框与类别概率 |  |
| T5-02 | — | Ultralytics YOLO11（软件，v11.0.0，AGPL-3.0；官方说明未发表论文，DOI pending） | Jocher et al. | 2024 | 软件（GitHub） | [官方文档](https://docs.ultralytics.com/models/yolo11/)；[GitHub](https://github.com/ultralytics/ultralytics) | COCO（官方模型表） | YOLO11 n／s／m／l／x | mAP50-95（val）、CPU ONNX 与 T4 TensorRT10 速度、参数量、FLOPs | 是：官方表 YOLO11n（640）mAP 39.5，T4 TensorRT10 1.5 ± 0.0 ms，CPU ONNX 56.1 ± 0.8 ms | Ultralytics 官方 YOLO11 模型族与引用格式；P0 冻结检测器即 YOLO11n（Ultralytics 8.4.90，`00_freeze/provenance/BT1_100_Epoch_Archive.md`） |  |
| T5-03 | — | YOLOv11: An Overview of the Key Architectural Enhancements | Khanam et al. | 2024 | arXiv preprint | [arXiv:2410.17725](https://arxiv.org/abs/2410.17725) | COCO（转引官方对比图） | YOLOv11 | 架构说明；COCO mAP50-95 与时延（转引） | 转引官方曲线，文中未写硬件 | 介绍 YOLOv11 的 C3k2、SPPF、C2PSA 等架构组件 |  |

## 阅读顺序

1. 只需核对引用格式与版本号（P0 运行用 Ultralytics 8.4.90，pinned zip `ultralytics-07958a7.zip`，见 `00_freeze/provenance/BT1_100_Epoch_Archive.md`）。
2. 每篇只记模板三样；细节证据回 Matrix §3。

## PDF 放置

文件名建议：`ID_ShortTitle.pdf`（例：`T5-01_YOLO.pdf`）。放入后把上表 PDF 列改为文件名。
