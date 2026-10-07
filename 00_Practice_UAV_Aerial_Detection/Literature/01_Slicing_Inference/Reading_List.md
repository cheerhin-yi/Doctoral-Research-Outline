# 切片／分块推理（SAHI 族） · 阅读清单

**主题问题：** 固定检测器上，切片与重叠聚合如何改变小目标可见性与前向代价？

> 合并说明（2026-10-07）：原「必读清单」与「候选文献事实表（2026-10-06 检索）」合并为本表，一篇一行。优先级：原 MUST → 必读；助手按事实建议的“建议优先读”保留；原 SHOULD 与“候选”→ 选读（原 SHOULD 已注明）。状态默认“未读”，读到哪一步请自己改为“在读／已读”。末列由你填写。数据集／检测器／指标／时延读自原文（原 MUST／SHOULD 条目于 2026-10-07 按 arXiv／CVF 全文补齐），查不到的写 **待补**。“核心做法”一句话见 [`../Literature_Matrix.md`](../Literature_Matrix.md) §2 定位列与 §5。

| 编号 | 题目 + 链接 | 年／Venue | 数据集 | 检测器 | 指标 | 时延／硬件 | 阅读优先级 | 状态 | 与P0关系（用户填） |
|---|---|---|---|---|---|---|---|---|---|
| T1-01 | Slicing Aided Hyper Inference and Fine-tuning for Small Object Detection（SAHI）（Akyon et al.）<br>[arXiv:2202.06934](https://arxiv.org/abs/2202.06934)；笔记 [notes/T1-01_SAHI.md](notes/T1-01_SAHI.md) | 2022 · ICIP 2022 | VisDrone2019-DET test-dev、xView（val） | FCOS、VFNet、TOOD | COCO AP50（含 small／medium／large） | 否（未报时延） | 必读 | 未读 |  |
| T1-03 | The Power of Tiling for Small Object Detection（Unel et al.）<br>[DOI 10.1109/CVPRW.2019.00084](https://doi.org/10.1109/CVPRW.2019.00084)；[CVF](https://openaccess.thecvf.com/content_CVPRW_2019/html/UAVision/Unel_The_Power_of_Tiling_for_Small_Object_Detection_CVPRW_2019_paper.html) | 2019 · CVPR Workshops 2019（UAVision） | VisDrone2018（只取行人与车辆） | PeleeNet 主干的 SSD（Pelee／Pelee38） | mAP（IoU 0.5）、FPS | 是：FPS，NVIDIA Jetson TX1／TX2 | 建议优先读 | 未读 |  |
| T1-05 | Tackling the Background Bias in Sparse Object Detection via Cropped Windows（Varga et al.）<br>[DOI 10.1109/ICCVW54120.2021.00311](https://doi.org/10.1109/ICCVW54120.2021.00311)；[arXiv:2106.02288](https://arxiv.org/abs/2106.02288) | 2021 · ICCV Workshops 2021（VisDrone） | VisDrone-DET、SeaDronesSee、DOTA-2（val） | EfficientDet-d0／d4、YOLOv4、CenterNet（ResNet18／50／101、Hourglass104） | mAP（COCO 计算方式；DOTA 报 mAP0.5），mean ± std；FPS；参数量 | 是：FPS，RTX 2080 Ti（桌面）与 Jetson TX2（嵌入式，半精度） | 建议优先读 | 未读 |  |
| T1-04 | Efficient ConvNet-based Object Detection for Unmanned Aerial Vehicles by Selective Tile Processing（Plastiras et al.）<br>[DOI 10.1145/3243394.3243692](https://doi.org/10.1145/3243394.3243692)；[arXiv:1911.06073](https://arxiv.org/abs/1911.06073) | 2018 · ICDSC 2018（ACM） | 自建行人测试集（197 帧，960×544，1181 个行人） | DroNet、Tiny-YOLOv2 | 灵敏度（sensitivity）、平均处理时间（APT）／FPS | 是：CPU（i5-8250U 笔记本） | 选读 | 未读 |  |
| T1-06 | Adaptive Slicing-Aided Hyper Inference for Small Object Detection in High-Resolution Remote Sensing Images（ASAHI）（Zhang et al.）<br>[DOI 10.3390/rs15051249](https://doi.org/10.3390/rs15051249) | 2023 · Remote Sensing 15(5), 1249 | VisDrone、xView | TPH-YOLOv5 预训练模型 | mAP50；计算时间 | 是：摘要称计算时间较现有切片方法减少 20–25%；硬件 **待补**（全文未取到） | 选读 | 未读 |  |
| T1-02 | ROI-Gated SAHI: Content-Adaptive Slicing-Based Inference for Efficient Object Detection（Riyadh et al.）<br>[arXiv:2608.23923](https://arxiv.org/abs/2608.23923)；笔记 [notes/T1-02_ROI_Gated_SAHI.md](notes/T1-02_ROI_Gated_SAHI.md) | 2026 · arXiv preprint | COCO128（full split 及代表性高分辨图） | YOLOv8n（proposer）+ YOLOv8s（refiner），Ultralytics COCO 预训练 | mAP@0.5、每图时延（ms）、加速比、与 Full SAHI 一致性（F1、Mean IoU） | 是：ms／图；硬件 **待补**（文中未写明） | 选读（原 SHOULD） | 未读 |  |

**建议优先读的理由（事实）：**

- T1-03：VisDrone + 训练与推理均分块 + 报嵌入式 FPS（Jetson TX1／TX2）
- T1-05：VisDrone + 推理时用整图最大分辨率 + 报桌面与嵌入式 FPS；`P0_C1C2.md` 已引用

**核心做法（事实，一句；原事实表列）：**

- T1-03：训练与推理都把高分辨图切成固定尺寸 tile 输入网络，以减少缩放造成的小目标细节丢失
- T1-04：用注意力机制只选部分 tile 处理，用记忆机制保留未处理 tile 的历史检测
- T1-05：训练时用裁窗（CroW）减少背景像素、允许更高分辨率；推理时输入整图最大分辨率
- T1-06：按图像分辨率自适应调整切片尺寸以控制切片数；后处理用 Cluster-DIoU-NMS 替换标准 NMS

## 阅读顺序

1. 必读先读，再读建议优先读；选读在写 Related Work 对表时补。
2. 每篇只记模板三样；细节证据回 Matrix §3。

## PDF 放置

文件名建议：`ID_ShortTitle.pdf`（例：`T1-01_SAHI.pdf`）。放入后在本表“题目 + 链接”格末尾加上 PDF 文件名。
