# 多尺度／局部放大推理 · 必读清单

**主题问题：** 多尺度或动态放大如何分配推理预算？方法图与前向次数怎么报？

**收录范围补充（2026-10-06）：** 本主题同时收密度／聚类／区域引导的聚焦检测（DMNet、CDMNet、UFPMP-Det、AdaZoom、GLSAN、Focus-and-Detect、YOLC、CZ Det），与 T3-03 ClusDet 同类，故不另开文件夹。

| ID | 优先级 | 题目 | 年 | Venue | 笔记 | PDF |
|---|---|---|---:|---|---|---|
| T3-01 | MUST | Dynamic Zoom-in Network（Gao et al.；arXiv:1711.05187） | 2018 | CVPR | [notes/T3-01_Dynamic_Zoom_in.md](notes/T3-01_Dynamic_Zoom_in.md) | `pdfs/` 待放入 |
| T3-02 | MUST | AutoFocus（Najibi et al.；arXiv:1812.01600） | 2019 | ICCV | [notes/T3-02_AutoFocus.md](notes/T3-02_AutoFocus.md) | `pdfs/` 待放入 |
| T3-03 | SHOULD | ClusDet（Yang et al.；DOI 10.1109/ICCV.2019.00840；arXiv:1904.08008） | 2019 | ICCV | [notes/T3-03_ClusDet.md](notes/T3-03_ClusDet.md) | `pdfs/` 待放入 |
| T3-04 | 建议优先读 | DMNet（Li et al.；DOI 10.1109/CVPRW50498.2020.00103） | 2020 | CVPRW | —（未建笔记） | `pdfs/` 待放入 |
| T3-05 | 候选 | CDMNet（Duan et al.；DOI 10.1109/ICCVW54120.2021.00313） | 2021 | ICCVW | —（未建笔记） | `pdfs/` 待放入 |
| T3-06 | 建议优先读 | UFPMP-Det（Huang et al.；DOI 10.1609/aaai.v36i1.19986） | 2022 | AAAI | —（未建笔记） | `pdfs/` 待放入 |
| T3-07 | 建议优先读 | AdaZoom（Xu et al.；DOI 10.1109/TMM.2022.3178871） | 2023 | TMM | —（未建笔记） | `pdfs/` 待放入 |
| T3-08 | 候选 | GLSAN（Deng et al.；DOI 10.1109/TIP.2020.3045636） | 2021 | TIP | —（未建笔记） | `pdfs/` 待放入 |
| T3-09 | 候选 | Focus-and-Detect（Koyun et al.；DOI 10.1016/j.image.2022.116675） | 2022 | SPIC | —（未建笔记） | `pdfs/` 待放入 |
| T3-10 | 候选 | YOLC（Liu et al.；DOI 10.1109/TITS.2024.3386928） | 2024 | T-ITS | —（未建笔记） | `pdfs/` 待放入 |
| T3-11 | 建议优先读 | CZ Det（Meethal et al.；DOI 10.1109/CVPRW59228.2023.00198） | 2023 | CVPRW | —（未建笔记） | `pdfs/` 待放入 |

## 候选文献事实表（2026-10-06 检索）

> 只记事实：元数据经 DOI／arXiv／会议官方页／官方文档核对，数据集、检测器、指标、时延硬件读自原文（或注明来源）；查不到的写 **待补**。优先级「建议优先读／候选」为助手按事实给出的阅读顺序建议，与上表 MUST／SHOULD（用户定）不是一回事。最后一列「与P0关系（用户填）」留空，由你本人填写；本表不写 gap 判断。汇总与核验记录见 [`../Literature_Matrix.md`](../Literature_Matrix.md) §5。

| ID | 建议优先读（理由） | 题目 | 作者 | 年 | Venue | 链接 | 数据集 | 检测器 | 报告指标 | 时延／FPS（硬件） | 核心做法（事实，一句） | 与P0关系（用户填） |
|---|---|---|---|---:|---|---|---|---|---|---|---|---|
| T3-04 | **是**：同两集 + 密度引导裁剪 + 报每图张数（#img）与 s/img（GTX 1080 Ti） | Density Map Guided Object Detection in Aerial Images（DMNet） | Li et al. | 2020 | CVPR Workshops 2020（EarthVision） | [DOI 10.1109/CVPRW50498.2020.00103](https://doi.org/10.1109/CVPRW50498.2020.00103)；[arXiv:2004.05520](https://arxiv.org/abs/2004.05520) | VisDrone、UAVDT | MCNN（密度图）+ Faster R-CNN（FPN；ResNet50／101、ResNeXt101） | AP、AP50、AP75、APs／m／l；#img | 是：s/img，单块 GTX 1080 Ti（ResNet50／101／ResNeXt101：0.29／0.36／0.61 s/img） | 由密度图生成裁剪区域，整图与裁剪图送同一检测器，结果融合 |  |
| T3-05 | — | Coarse-grained Density Map Guided Object Detection in Aerial Images（CDMNet） | Duan et al. | 2021 | ICCV Workshops 2021（VisDrone） | [DOI 10.1109/ICCVW54120.2021.00313](https://doi.org/10.1109/ICCVW54120.2021.00313)；[CVF](https://openaccess.thecvf.com/content/ICCV2021W/VisDrone/html/Duan_Coarse-Grained_Density_Map_Guided_Object_Detection_in_Aerial_Images_ICCVW_2021_paper.html) | VisDrone、UAVDT | Faster R-CNN（MMDetection；输入 1000×600） | AP、AP50、AP75、APs／m／l；#img | 否（只报 #img） | 粗粒度密度图聚类目标、量化尺度，按簇裁剪子区域检测后用 NMS 合并；改进 mosaic 增强 |  |
| T3-06 | **是**：同两集 + 报打包图数与推理时间（单块 GTX 1080Ti，对比 ClusDet、DMNet） | UFPMP-Det: Toward Accurate and Efficient Object Detection on Drone Imagery | Huang et al. | 2022 | AAAI 2022 | [DOI 10.1609/aaai.v36i1.19986](https://doi.org/10.1609/aaai.v36i1.19986)；[arXiv:2112.10415](https://arxiv.org/abs/2112.10415) | VisDrone（输入 1333×800）、UAVDT（输入 1000×600） | GFL（MMDetection；ResNet-50／101、ResNeXt-101） | AP、AP50、AP75；#img；推理时间 | 是：推理时间，单块 GTX 1080Ti | 粗检测得到子区域后打包成一张 mosaic 统一检测，并用多代理（multi-proxy）检测头 |  |
| T3-07 | **是**：VisDrone test-dev + UAVDT + 与均匀划分 UP(1×1／2×2／3×3) 并列报 s/img | AdaZoom: Towards Scale-Aware Large Scene Object Detection | Xu et al. | 2023 | IEEE Transactions on Multimedia（arXiv 2021 版题为 *AdaZoom: Adaptive Zoom Network for Multi-Scale Object Detection in Large Scenes*） | [DOI 10.1109/TMM.2022.3178871](https://doi.org/10.1109/TMM.2022.3178871)；[arXiv:2106.10409](https://arxiv.org/abs/2106.10409) | VisDrone2019（test-dev）、UAVDT、DOTA | Faster R-CNN、Cascade R-CNN | AP、AP50、AP75；s/img（GPU） | 是：s/img；GPU 型号 **待补**（arXiv 版未写明；TMM 正式版未核） | 自适应缩放网络选择需要放大的区域并放大检测；对照均匀划分 UP 与多尺度 UP |  |
| T3-08 | — | A Global-Local Self-Adaptive Network for Drone-View Object Detection（GLSAN） | Deng et al. | 2021 | IEEE Transactions on Image Processing 30, 1556–1569 | [DOI 10.1109/TIP.2020.3045636](https://doi.org/10.1109/TIP.2020.3045636)；[代码](https://github.com/dengsutao/glsan) | VisDrone、UAVDT（据官方代码仓库） | Faster R-CNN（Detectron2，R-50／R-101；据官方代码仓库） | **待补**（全文未取到） | **待补** | 全局–局部检测：自适应区域选择（SARSA）裁剪 + 局部超分（LSRN）；代码提供 NoCrop／UniformlyCrop／SelfAdaptiveCrop 三种评测模式 |  |
| T3-09 | — | Focus-and-Detect: A Small Object Detection Framework for Aerial Images | Koyun et al. | 2022 | Signal Processing: Image Communication 104, 116675 | [DOI 10.1016/j.image.2022.116675](https://doi.org/10.1016/j.image.2022.116675)；[arXiv:2203.12976](https://arxiv.org/abs/2203.12976) | VisDrone、UAVDT | 两阶段均为 GFL + FPN（Focus：ResNet-50；Detect：ResNeXt-101） | COCO AP 系列；送检图数；每图平均推理时间 | 是：本文与 CRENet 在 RTX 2080 Ti 上，其余对比方法引用 GTX 1080 Ti 数字 | 第一阶段用 GMM 监督的检测器生成聚焦区域，第二阶段在区域上检测，IBS 去除截断框 |  |
| T3-10 | — | YOLC: You Only Look Clusters for Tiny Object Detection in Aerial Images | Liu et al. | 2024 | IEEE Transactions on Intelligent Transportation Systems 25, 13863–13875 | [DOI 10.1109/TITS.2024.3386928](https://doi.org/10.1109/TITS.2024.3386928)；[arXiv:2404.06180](https://arxiv.org/abs/2404.06180) | VisDrone、UAVDT | CenterNet（Hourglass-104，MMDetection） | AP、AP50、AP75、APs／m／l；#img；s/img（GPU） | 是：s/img，RTX 2080 Ti（文中实现平台） | 局部尺度模块（LSM）自适应搜索目标簇区域并缩放后检测 |  |
| T3-11 | **是**：VisDrone + 均匀裁剪与密度裁剪同表对照 + 报 FPS | Cascaded Zoom-in Detector for High Resolution Aerial Images（CZ Det） | Meethal et al. | 2023 | CVPR Workshops 2023 | [DOI 10.1109/CVPRW59228.2023.00198](https://doi.org/10.1109/CVPRW59228.2023.00198)；[arXiv:2303.08747](https://arxiv.org/abs/2303.08747) | VisDrone、DOTA | Faster R-CNN（主）与 FCOS，ResNet50-FPN（Detectron2） | COCO AP、AP50、AP75、APs／m／l、FPS | 是：FPS；测速 GPU 文中未写明（训练用单块 A100） | 把密度裁剪作为额外类别由检测器自己预测，第二轮推理放大这些裁剪区；对照“均匀切 4 块” |  |

## 阅读顺序

1. MUST 先读；SHOULD 在写 Related Work 对表时补。
2. 每篇只记模板三样；细节证据回 Matrix §3。

## PDF 放置

文件名建议：`ID_ShortTitle.pdf`（例：`T1-01_SAHI.pdf`）。放入后把上表 PDF 列改为文件名。
