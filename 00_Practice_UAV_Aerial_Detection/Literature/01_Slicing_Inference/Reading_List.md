# 切片／分块推理（SAHI 族） · 必读清单

**主题问题：** 固定检测器上，切片与重叠聚合如何改变小目标可见性与前向代价？

| ID | 优先级 | 题目 | 年 | Venue | 笔记 | PDF |
|---|---|---|---:|---|---|---|
| T1-01 | MUST | SAHI / Slicing Aided Hyper Inference（Akyon et al.；arXiv:2202.06934） | 2022 | ICIP | [notes/T1-01_SAHI.md](notes/T1-01_SAHI.md) | `pdfs/` 待放入 |
| T1-02 | SHOULD | ROI-Gated SAHI（Riyadh et al.；arXiv:2608.23923） | 2026 | arXiv preprint | [notes/T1-02_ROI_Gated_SAHI.md](notes/T1-02_ROI_Gated_SAHI.md) | `pdfs/` 待放入 |
| T1-03 | 建议优先读 | The Power of Tiling（Unel et al.；DOI 10.1109/CVPRW.2019.00084） | 2019 | CVPRW | —（未建笔记） | `pdfs/` 待放入 |
| T1-04 | 候选 | Selective Tile Processing（Plastiras et al.；DOI 10.1145/3243394.3243692） | 2018 | ICDSC | —（未建笔记） | `pdfs/` 待放入 |
| T1-05 | 建议优先读 | Cropped Windows（CroW）（Varga et al.；DOI 10.1109/ICCVW54120.2021.00311） | 2021 | ICCVW | —（未建笔记） | `pdfs/` 待放入 |
| T1-06 | 候选 | ASAHI（Zhang et al.；DOI 10.3390/rs15051249） | 2023 | Remote Sensing | —（未建笔记） | `pdfs/` 待放入 |

## 候选文献事实表（2026-10-06 检索）

> 只记事实：元数据经 DOI／arXiv／会议官方页／官方文档核对，数据集、检测器、指标、时延硬件读自原文（或注明来源）；查不到的写 **待补**。优先级「建议优先读／候选」为助手按事实给出的阅读顺序建议，与上表 MUST／SHOULD（用户定）不是一回事。最后一列「与P0关系（用户填）」留空，由你本人填写；本表不写 gap 判断。汇总与核验记录见 [`../Literature_Matrix.md`](../Literature_Matrix.md) §5。

| ID | 建议优先读（理由） | 题目 | 作者 | 年 | Venue | 链接 | 数据集 | 检测器 | 报告指标 | 时延／FPS（硬件） | 核心做法（事实，一句） | 与P0关系（用户填） |
|---|---|---|---|---:|---|---|---|---|---|---|---|---|
| T1-03 | **是**：VisDrone + 训练与推理均分块 + 报嵌入式 FPS（Jetson TX1／TX2） | The Power of Tiling for Small Object Detection | Unel et al. | 2019 | CVPR Workshops 2019（UAVision） | [DOI 10.1109/CVPRW.2019.00084](https://doi.org/10.1109/CVPRW.2019.00084)；[CVF](https://openaccess.thecvf.com/content_CVPRW_2019/html/UAVision/Unel_The_Power_of_Tiling_for_Small_Object_Detection_CVPRW_2019_paper.html) | VisDrone2018（只取行人与车辆） | PeleeNet 主干的 SSD（Pelee／Pelee38） | mAP（IoU 0.5）、FPS | 是：FPS，NVIDIA Jetson TX1／TX2 | 训练与推理都把高分辨图切成固定尺寸 tile 输入网络，以减少缩放造成的小目标细节丢失 |  |
| T1-04 | — | Efficient ConvNet-based Object Detection for Unmanned Aerial Vehicles by Selective Tile Processing | Plastiras et al. | 2018 | ICDSC 2018（ACM） | [DOI 10.1145/3243394.3243692](https://doi.org/10.1145/3243394.3243692)；[arXiv:1911.06073](https://arxiv.org/abs/1911.06073) | 自建行人测试集（197 帧，960×544，1181 个行人） | DroNet、Tiny-YOLOv2 | 灵敏度（sensitivity）、平均处理时间（APT）／FPS | 是：CPU（i5-8250U 笔记本） | 用注意力机制只选部分 tile 处理，用记忆机制保留未处理 tile 的历史检测 |  |
| T1-05 | **是**：VisDrone + 推理时用整图最大分辨率 + 报桌面与嵌入式 FPS；`P0_C1C2.md` 已引用 | Tackling the Background Bias in Sparse Object Detection via Cropped Windows | Varga et al. | 2021 | ICCV Workshops 2021（VisDrone） | [DOI 10.1109/ICCVW54120.2021.00311](https://doi.org/10.1109/ICCVW54120.2021.00311)；[arXiv:2106.02288](https://arxiv.org/abs/2106.02288) | VisDrone-DET、SeaDronesSee、DOTA-2（val） | EfficientDet-d0／d4、YOLOv4、CenterNet（ResNet18／50／101、Hourglass104） | mAP（COCO 计算方式；DOTA 报 mAP0.5），mean ± std；FPS；参数量 | 是：FPS，RTX 2080 Ti（桌面）与 Jetson TX2（嵌入式，半精度） | 训练时用裁窗（CroW）减少背景像素、允许更高分辨率；推理时输入整图最大分辨率 |  |
| T1-06 | — | Adaptive Slicing-Aided Hyper Inference for Small Object Detection in High-Resolution Remote Sensing Images（ASAHI） | Zhang et al. | 2023 | Remote Sensing 15(5), 1249 | [DOI 10.3390/rs15051249](https://doi.org/10.3390/rs15051249) | VisDrone、xView | TPH-YOLOv5 预训练模型 | mAP50；计算时间 | 是：摘要称计算时间较现有切片方法减少 20–25%；硬件 **待补**（全文未取到） | 按图像分辨率自适应调整切片尺寸以控制切片数；后处理用 Cluster-DIoU-NMS 替换标准 NMS |  |

## 阅读顺序

1. MUST 先读；SHOULD 在写 Related Work 对表时补。
2. 每篇只记模板三样；细节证据回 Matrix §3。

## PDF 放置

文件名建议：`ID_ShortTitle.pdf`（例：`T1-01_SAHI.pdf`）。放入后把上表 PDF 列改为文件名。
