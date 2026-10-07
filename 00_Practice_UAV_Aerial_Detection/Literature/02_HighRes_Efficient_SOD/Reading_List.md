# 高分辨／高效小目标检测 · 阅读清单

**主题问题：** 为抬高分辨或效率，别人改了网络还是只改推理？和本篇冻结权重差在哪？

> 合并说明（2026-10-07）：原「必读清单」与「候选文献事实表（2026-10-06 检索）」合并为本表，一篇一行。优先级：原 MUST → 必读；助手按事实建议的“建议优先读”保留；原 SHOULD 与“候选”→ 选读（原 SHOULD 已注明）。状态默认“未读”，读到哪一步请自己改为“在读／已读”。末列由你填写。数据集／检测器／指标／时延读自原文（原 MUST／SHOULD 条目于 2026-10-07 按 arXiv／CVF 全文补齐），查不到的写 **待补**。“核心做法”一句话见 [`../Literature_Matrix.md`](../Literature_Matrix.md) §2 定位列与 §5。

| 编号 | 题目 + 链接 | 年／Venue | 数据集 | 检测器 | 指标 | 时延／硬件 | 阅读优先级 | 状态 | 与P0关系（用户填） |
|---|---|---|---|---|---|---|---|---|---|
| T2-01 | QueryDet: Cascaded Sparse Query for Accelerating High-Resolution Small Object Detection（Yang et al.）<br>[arXiv:2103.09136](https://arxiv.org/abs/2103.09136)；笔记 [notes/T2-01_QueryDet.md](notes/T2-01_QueryDet.md) | 2022 · CVPR 2022 | MS-COCO、VisDrone2018 | RetinaNet（主）、FCOS、Faster R-CNN 加 CSQ（Detectron2） | AP、APs、AR、FPS | 是：FPS，NVIDIA 2080Ti | 必读 | 未读 |  |
| T2-03 | Adaptive Sparse Convolutional Networks with Global Context Enhancement for Faster Object Detection on Drone Images（CEASC）（Du et al.）<br>[DOI 10.1109/CVPR52729.2023.01291](https://doi.org/10.1109/CVPR52729.2023.01291)；[arXiv:2303.14488](https://arxiv.org/abs/2303.14488) | 2023 · CVPR 2023 | VisDrone（输入 1333×800）、UAVDT（输入 1024×540） | GFL V1（默认，ResNet18）、RetinaNet、Faster R-CNN、FSAF | mAP、AP50、AP75、AR1／10／100／500、GFLOPs、FPS | 是：FPS，单块 RTX 2080Ti | 建议优先读 | 未读 |  |
| T2-04 | TPH-YOLOv5: Improved YOLOv5 Based on Transformer Prediction Head for Object Detection on Drone-captured Scenarios（Zhu et al.）<br>[DOI 10.1109/ICCVW54120.2021.00312](https://doi.org/10.1109/ICCVW54120.2021.00312)；[arXiv:2108.11539](https://arxiv.org/abs/2108.11539) | 2021 · ICCV Workshops 2021（VisDrone） | VisDrone2021-DET | YOLOv5 改（多一个预测头、Transformer 预测头、CBAM） | mAP（0.5:0.95）、AP50 | 否（未报 FPS） | 选读 | 未读 |  |
| T2-02 | ESOD: Efficient Small Object Detection on High-Resolution Images（Liu et al.）<br>[arXiv:2407.16424](https://arxiv.org/abs/2407.16424)；笔记 [notes/T2-02_ESOD.md](notes/T2-02_ESOD.md) | 2025 · IEEE TIP | VisDrone、UAVDT、TinyPerson | YOLOv5 基线（另适配 RTMDet、YOLOv8 及 ViT 类检测器） | AP、AP50、GFLOPs、FPS | 是：FPS，Nvidia V100，batch size 1 | 选读（原 SHOULD） | 未读 |  |

**建议优先读的理由（事实）：**

- T2-03：同两集（VisDrone、UAVDT）+ 报 GFLOPs 与 FPS（单块 RTX 2080Ti）

**核心做法（事实，一句；原事实表列）：**

- T2-03：检测头改为自适应稀疏卷积并加全局上下文增强，以降低检测头计算量
- T2-04：YOLOv5 上加一个预测头并换成 Transformer 预测头；输入长边 1536，另用多尺度测试与模型集成

## 阅读顺序

1. 必读先读，再读建议优先读；选读在写 Related Work 对表时补。
2. 每篇只记模板三样；细节证据回 Matrix §3。

## PDF 放置

文件名建议：`ID_ShortTitle.pdf`（例：`T1-01_SAHI.pdf`）。放入后在本表“题目 + 链接”格末尾加上 PDF 文件名。
