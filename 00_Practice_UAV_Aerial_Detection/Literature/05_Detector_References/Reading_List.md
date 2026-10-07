# 检测器出处（YOLO／Ultralytics） · 阅读清单

**主题问题：** 本篇冻结检测器（YOLO11n，Ultralytics）在 Method／Experimental Setup 里应引用哪些正式出处？

**为什么单开文件夹（2026-10-06）：** T1–T4 收的是推理协议、选区与评测口径方面的近邻工作；这里收的是被冻结的检测器本身的出处（Method 节引用），两类用途不同，混放会让 Related Work 与 Setup 的引用难以区分。

> 合并说明（2026-10-07）：原「必读清单」与「候选文献事实表（2026-10-06 检索）」合并为本表，一篇一行。优先级：原 MUST → 必读；助手按事实建议的“建议优先读”保留；原 SHOULD 与“候选”→ 选读（原 SHOULD 已注明）。状态默认“未读”，读到哪一步请自己改为“在读／已读”。末列由你填写。数据集／检测器／指标／时延读自原文（原 MUST／SHOULD 条目于 2026-10-07 按 arXiv／CVF 全文补齐），查不到的写 **待补**。“核心做法”一句话见 [`../Literature_Matrix.md`](../Literature_Matrix.md) §2 定位列与 §5。

| 编号 | 题目 + 链接 | 年／Venue | 数据集 | 检测器 | 指标 | 时延／硬件 | 阅读优先级 | 状态 | 与P0关系（用户填） |
|---|---|---|---|---|---|---|---|---|---|
| T5-01 | You Only Look Once: Unified, Real-Time Object Detection（Redmon et al.）<br>[DOI 10.1109/CVPR.2016.91](https://doi.org/10.1109/CVPR.2016.91)；[arXiv:1506.02640](https://arxiv.org/abs/1506.02640) | 2016 · CVPR 2016 | PASCAL VOC 2007／2012 | YOLO、Fast YOLO | mAP、FPS | 是：Titan X GPU（YOLO 45 fps；Fast YOLO 155 fps） | 选读 | 未读 |  |
| T5-02 | Ultralytics YOLO11（软件，v11.0.0，AGPL-3.0；官方说明未发表论文，DOI pending）（Jocher et al.）<br>[官方文档](https://docs.ultralytics.com/models/yolo11/)；[GitHub](https://github.com/ultralytics/ultralytics) | 2024 · 软件（GitHub） | COCO（官方模型表） | YOLO11 n／s／m／l／x | mAP50-95（val）、CPU ONNX 与 T4 TensorRT10 速度、参数量、FLOPs | 是：官方表 YOLO11n（640）mAP 39.5，T4 TensorRT10 1.5 ± 0.0 ms，CPU ONNX 56.1 ± 0.8 ms | 选读 | 未读 |  |
| T5-03 | YOLOv11: An Overview of the Key Architectural Enhancements（Khanam et al.）<br>[arXiv:2410.17725](https://arxiv.org/abs/2410.17725) | 2024 · arXiv preprint | COCO（转引官方对比图） | YOLOv11 | 架构说明；COCO mAP50-95 与时延（转引） | 转引官方曲线，文中未写硬件 | 选读 | 未读 |  |

**核心做法（事实，一句；原事实表列）：**

- T5-01：单个网络一次前向直接回归边框与类别概率
- T5-02：Ultralytics 官方 YOLO11 模型族与引用格式；P0 冻结检测器即 YOLO11n（Ultralytics 8.4.90，`00_freeze/provenance/BT1_100_Epoch_Archive.md`）
- T5-03：介绍 YOLOv11 的 C3k2、SPPF、C2PSA 等架构组件

## 阅读顺序

1. 只需核对引用格式与版本号（P0 运行用 Ultralytics 8.4.90，pinned zip `ultralytics-07958a7.zip`，见 `00_freeze/provenance/BT1_100_Epoch_Archive.md`）。
2. 每篇只记模板三样；细节证据回 Matrix §3。

## PDF 放置

文件名建议：`ID_ShortTitle.pdf`（例：`T5-01_YOLO.pdf`）。放入后在本表“题目 + 链接”格末尾加上 PDF 文件名。
