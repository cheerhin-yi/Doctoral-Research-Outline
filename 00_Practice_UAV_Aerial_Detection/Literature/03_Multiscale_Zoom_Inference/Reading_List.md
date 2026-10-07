# 多尺度／局部放大推理 · 阅读清单

**主题问题：** 多尺度或动态放大如何分配推理预算？方法图与前向次数怎么报？

**收录范围补充（2026-10-06）：** 本主题同时收密度／聚类／区域引导的聚焦检测（DMNet、CDMNet、UFPMP-Det、AdaZoom、GLSAN、Focus-and-Detect、YOLC、CZ Det），与 T3-03 ClusDet 同类，故不另开文件夹。

> 合并说明（2026-10-07）：原「必读清单」与「候选文献事实表（2026-10-06 检索）」合并为本表，一篇一行。优先级：原 MUST → 必读；助手按事实建议的“建议优先读”保留；原 SHOULD 与“候选”→ 选读（原 SHOULD 已注明）。状态默认“未读”，读到哪一步请自己改为“在读／已读”。末列由你填写。数据集／检测器／指标／时延读自原文（原 MUST／SHOULD 条目于 2026-10-07 按 arXiv／CVF 全文补齐），查不到的写 **待补**。“核心做法”一句话见 [`../Literature_Matrix.md`](../Literature_Matrix.md) §2 定位列与 §5。

| 编号 | 题目 + 链接 | 年／Venue | 数据集 | 检测器 | 指标 | 时延／硬件 | 阅读优先级 | 状态 | 与P0关系（用户填） |
|---|---|---|---|---|---|---|---|---|---|
| T3-01 | Dynamic Zoom-in Network for Fast Object Detection in Large Images（Gao et al.）<br>[arXiv:1711.05187](https://arxiv.org/abs/1711.05187)；笔记 [notes/T3-01_Dynamic_Zoom_in.md](notes/T3-01_Dynamic_Zoom_in.md) | 2018 · CVPR 2018 | Caltech Pedestrian（CPD）、Web Pedestrian（WP，取自 YFCC100M） | Faster R-CNN（另对比 SSD、YOLOv2） | AP、处理像素比例、推理时间 | 是：K-80 GPU | 必读 | 未读 |  |
| T3-02 | AutoFocus: Efficient Multi-Scale Inference（Najibi et al.）<br>[arXiv:1812.01600](https://arxiv.org/abs/1812.01600)；笔记 [notes/T3-02_AutoFocus.md](notes/T3-02_AutoFocus.md) | 2019 · ICCV 2019 | COCO、PASCAL VOC | SNIPER 系 Faster R-CNN | mAP（COCO 与 AP50）、每秒图像数、处理像素数 | 是：6.4 张／秒，Titan X（Pascal） | 必读 | 未读 |  |
| T3-04 | Density Map Guided Object Detection in Aerial Images（DMNet）（Li et al.）<br>[DOI 10.1109/CVPRW50498.2020.00103](https://doi.org/10.1109/CVPRW50498.2020.00103)；[arXiv:2004.05520](https://arxiv.org/abs/2004.05520) | 2020 · CVPR Workshops 2020（EarthVision） | VisDrone、UAVDT | MCNN（密度图）+ Faster R-CNN（FPN；ResNet50／101、ResNeXt101） | AP、AP50、AP75、APs／m／l；#img | 是：s/img，单块 GTX 1080 Ti（ResNet50／101／ResNeXt101：0.29／0.36／0.61 s/img） | 建议优先读 | 未读 |  |
| T3-06 | UFPMP-Det: Toward Accurate and Efficient Object Detection on Drone Imagery（Huang et al.）<br>[DOI 10.1609/aaai.v36i1.19986](https://doi.org/10.1609/aaai.v36i1.19986)；[arXiv:2112.10415](https://arxiv.org/abs/2112.10415) | 2022 · AAAI 2022 | VisDrone（输入 1333×800）、UAVDT（输入 1000×600） | GFL（MMDetection；ResNet-50／101、ResNeXt-101） | AP、AP50、AP75；#img；推理时间 | 是：推理时间，单块 GTX 1080Ti | 建议优先读 | 未读 |  |
| T3-07 | AdaZoom: Towards Scale-Aware Large Scene Object Detection（Xu et al.）<br>[DOI 10.1109/TMM.2022.3178871](https://doi.org/10.1109/TMM.2022.3178871)；[arXiv:2106.10409](https://arxiv.org/abs/2106.10409) | 2023 · IEEE Transactions on Multimedia（arXiv 2021 版题为 *AdaZoom: Adaptive Zoom Network for Multi-Scale Object Detection in Large Scenes*） | VisDrone2019（test-dev）、UAVDT、DOTA | Faster R-CNN、Cascade R-CNN | AP、AP50、AP75；s/img（GPU） | 是：s/img；GPU 型号 **待补**（arXiv 版未写明；TMM 正式版未核） | 建议优先读 | 未读 |  |
| T3-11 | Cascaded Zoom-in Detector for High Resolution Aerial Images（CZ Det）（Meethal et al.）<br>[DOI 10.1109/CVPRW59228.2023.00198](https://doi.org/10.1109/CVPRW59228.2023.00198)；[arXiv:2303.08747](https://arxiv.org/abs/2303.08747) | 2023 · CVPR Workshops 2023 | VisDrone、DOTA | Faster R-CNN（主）与 FCOS，ResNet50-FPN（Detectron2） | COCO AP、AP50、AP75、APs／m／l、FPS | 是：FPS；测速 GPU 文中未写明（训练用单块 A100） | 建议优先读 | 未读 |  |
| T3-03 | Clustered Object Detection in Aerial Images（ClusDet）（Yang et al.）<br>[DOI 10.1109/ICCV.2019.00840](https://doi.org/10.1109/ICCV.2019.00840)；[arXiv:1904.08008](https://arxiv.org/abs/1904.08008)；笔记 [notes/T3-03_ClusDet.md](notes/T3-03_ClusDet.md) | 2019 · ICCV 2019 | VisDrone、UAVDT、DOTA | Faster R-CNN／RetinaNet + FPN（另含 CPNet、ScaleNet） | AP、AP50、AP75、APs／m／l；#img；推理时间 | 是：推理时间，GTX 1080 Ti | 选读（原 SHOULD） | 未读 |  |
| T3-05 | Coarse-grained Density Map Guided Object Detection in Aerial Images（CDMNet）（Duan et al.）<br>[DOI 10.1109/ICCVW54120.2021.00313](https://doi.org/10.1109/ICCVW54120.2021.00313)；[CVF](https://openaccess.thecvf.com/content/ICCV2021W/VisDrone/html/Duan_Coarse-Grained_Density_Map_Guided_Object_Detection_in_Aerial_Images_ICCVW_2021_paper.html) | 2021 · ICCV Workshops 2021（VisDrone） | VisDrone、UAVDT | Faster R-CNN（MMDetection；输入 1000×600） | AP、AP50、AP75、APs／m／l；#img | 否（只报 #img） | 选读 | 未读 |  |
| T3-08 | A Global-Local Self-Adaptive Network for Drone-View Object Detection（GLSAN）（Deng et al.）<br>[DOI 10.1109/TIP.2020.3045636](https://doi.org/10.1109/TIP.2020.3045636)；[代码](https://github.com/dengsutao/glsan) | 2021 · IEEE Transactions on Image Processing 30, 1556–1569 | VisDrone、UAVDT（据官方代码仓库） | Faster R-CNN（Detectron2，R-50／R-101；据官方代码仓库） | **待补**（全文未取到） | **待补** | 选读 | 未读 |  |
| T3-09 | Focus-and-Detect: A Small Object Detection Framework for Aerial Images（Koyun et al.）<br>[DOI 10.1016/j.image.2022.116675](https://doi.org/10.1016/j.image.2022.116675)；[arXiv:2203.12976](https://arxiv.org/abs/2203.12976) | 2022 · Signal Processing: Image Communication 104, 116675 | VisDrone、UAVDT | 两阶段均为 GFL + FPN（Focus：ResNet-50；Detect：ResNeXt-101） | COCO AP 系列；送检图数；每图平均推理时间 | 是：本文与 CRENet 在 RTX 2080 Ti 上，其余对比方法引用 GTX 1080 Ti 数字 | 选读 | 未读 |  |
| T3-10 | YOLC: You Only Look Clusters for Tiny Object Detection in Aerial Images（Liu et al.）<br>[DOI 10.1109/TITS.2024.3386928](https://doi.org/10.1109/TITS.2024.3386928)；[arXiv:2404.06180](https://arxiv.org/abs/2404.06180) | 2024 · IEEE Transactions on Intelligent Transportation Systems 25, 13863–13875 | VisDrone、UAVDT | CenterNet（Hourglass-104，MMDetection） | AP、AP50、AP75、APs／m／l；#img；s/img（GPU） | 是：s/img，RTX 2080 Ti（文中实现平台） | 选读 | 未读 |  |

**建议优先读的理由（事实）：**

- T3-04：同两集 + 密度引导裁剪 + 报每图张数（#img）与 s/img（GTX 1080 Ti）
- T3-06：同两集 + 报打包图数与推理时间（单块 GTX 1080Ti，对比 ClusDet、DMNet）
- T3-07：VisDrone test-dev + UAVDT + 与均匀划分 UP(1×1／2×2／3×3) 并列报 s/img
- T3-11：VisDrone + 均匀裁剪与密度裁剪同表对照 + 报 FPS

**核心做法（事实，一句；原事实表列）：**

- T3-04：由密度图生成裁剪区域，整图与裁剪图送同一检测器，结果融合
- T3-05：粗粒度密度图聚类目标、量化尺度，按簇裁剪子区域检测后用 NMS 合并；改进 mosaic 增强
- T3-06：粗检测得到子区域后打包成一张 mosaic 统一检测，并用多代理（multi-proxy）检测头
- T3-07：自适应缩放网络选择需要放大的区域并放大检测；对照均匀划分 UP 与多尺度 UP
- T3-08：全局–局部检测：自适应区域选择（SARSA）裁剪 + 局部超分（LSRN）；代码提供 NoCrop／UniformlyCrop／SelfAdaptiveCrop 三种评测模式
- T3-09：第一阶段用 GMM 监督的检测器生成聚焦区域，第二阶段在区域上检测，IBS 去除截断框
- T3-10：局部尺度模块（LSM）自适应搜索目标簇区域并缩放后检测
- T3-11：把密度裁剪作为额外类别由检测器自己预测，第二轮推理放大这些裁剪区；对照“均匀切 4 块”

## 阅读顺序

1. 必读先读，再读建议优先读；选读在写 Related Work 对表时补。
2. 每篇只记模板三样；细节证据回 Matrix §3。

## PDF 放置

文件名建议：`ID_ShortTitle.pdf`（例：`T1-01_SAHI.pdf`）。放入后在本表“题目 + 链接”格末尾加上 PDF 文件名。
