# 高分辨／高效小目标检测 · 必读清单

**主题问题：** 为抬高分辨或效率，别人改了网络还是只改推理？和本篇冻结权重差在哪？

| ID | 优先级 | 题目 | 年 | Venue | 笔记 | PDF |
|---|---|---|---:|---|---|---|
| T2-01 | MUST | QueryDet（Yang et al.；arXiv:2103.09136） | 2022 | CVPR | [notes/T2-01_QueryDet.md](notes/T2-01_QueryDet.md) | `pdfs/` 待放入 |
| T2-02 | SHOULD | ESOD（Liu et al.；arXiv:2407.16424） | 2025 | TIP | [notes/T2-02_ESOD.md](notes/T2-02_ESOD.md) | `pdfs/` 待放入 |
| T2-03 | 建议优先读 | CEASC（Du et al.；DOI 10.1109/CVPR52729.2023.01291） | 2023 | CVPR | —（未建笔记） | `pdfs/` 待放入 |
| T2-04 | 候选 | TPH-YOLOv5（Zhu et al.；DOI 10.1109/ICCVW54120.2021.00312） | 2021 | ICCVW | —（未建笔记） | `pdfs/` 待放入 |

## 候选文献事实表（2026-10-06 检索）

> 只记事实：元数据经 DOI／arXiv／会议官方页／官方文档核对，数据集、检测器、指标、时延硬件读自原文（或注明来源）；查不到的写 **待补**。优先级「建议优先读／候选」为助手按事实给出的阅读顺序建议，与上表 MUST／SHOULD（用户定）不是一回事。最后一列「与P0关系（用户填）」留空，由你本人填写；本表不写 gap 判断。汇总与核验记录见 [`../Literature_Matrix.md`](../Literature_Matrix.md) §5。

| ID | 建议优先读（理由） | 题目 | 作者 | 年 | Venue | 链接 | 数据集 | 检测器 | 报告指标 | 时延／FPS（硬件） | 核心做法（事实，一句） | 与P0关系（用户填） |
|---|---|---|---|---:|---|---|---|---|---|---|---|---|
| T2-03 | **是**：同两集（VisDrone、UAVDT）+ 报 GFLOPs 与 FPS（单块 RTX 2080Ti） | Adaptive Sparse Convolutional Networks with Global Context Enhancement for Faster Object Detection on Drone Images（CEASC） | Du et al. | 2023 | CVPR 2023 | [DOI 10.1109/CVPR52729.2023.01291](https://doi.org/10.1109/CVPR52729.2023.01291)；[arXiv:2303.14488](https://arxiv.org/abs/2303.14488) | VisDrone（输入 1333×800）、UAVDT（输入 1024×540） | GFL V1（默认，ResNet18）、RetinaNet、Faster R-CNN、FSAF | mAP、AP50、AP75、AR1／10／100／500、GFLOPs、FPS | 是：FPS，单块 RTX 2080Ti | 检测头改为自适应稀疏卷积并加全局上下文增强，以降低检测头计算量 |  |
| T2-04 | — | TPH-YOLOv5: Improved YOLOv5 Based on Transformer Prediction Head for Object Detection on Drone-captured Scenarios | Zhu et al. | 2021 | ICCV Workshops 2021（VisDrone） | [DOI 10.1109/ICCVW54120.2021.00312](https://doi.org/10.1109/ICCVW54120.2021.00312)；[arXiv:2108.11539](https://arxiv.org/abs/2108.11539) | VisDrone2021-DET | YOLOv5 改（多一个预测头、Transformer 预测头、CBAM） | mAP（0.5:0.95）、AP50 | 否（未报 FPS） | YOLOv5 上加一个预测头并换成 Transformer 预测头；输入长边 1536，另用多尺度测试与模型集成 |  |

## 阅读顺序

1. MUST 先读；SHOULD 在写 Related Work 对表时补。
2. 每篇只记模板三样；细节证据回 Matrix §3。

## PDF 放置

文件名建议：`ID_ShortTitle.pdf`（例：`T1-01_SAHI.pdf`）。放入后把上表 PDF 列改为文件名。
