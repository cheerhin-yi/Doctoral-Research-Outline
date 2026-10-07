# Literature 矩阵（P0 练习论文）

> 只记「主题 × 证据」；细读写在各主题 `notes/`。主张边界：冻结检测器上的**推理协议对照**，不是新检测器。

## 1. 主题与状态

| 主题 | 名称 | 对应写作位置 |
|---|---|---|
| T1 | 切片／分块推理（SAHI 族） | Related Work · 推理时增强 |
| T2 | 高分辨／高效小目标 | Related Work · 划界 |
| T3 | 多尺度／局部放大推理 | Related Work · 预算与方法图参考 |
| T4 | 航拍基准与评测口径 | Experiments／附录口径 |
| T5 | 检测器出处（YOLO／Ultralytics；2026-10-06 新增） | Method／Experimental Setup 引用 |

优先级（2026-10-07 统一）：`必读`（原 MUST）／`建议优先读`（助手按事实建议）／`选读`（原 SHOULD 与“候选”）；与各主题 `Reading_List.md` 合并表一致。各篇的阅读状态（未读／在读／已读）以 `Reading_List.md` 为准；下面「状态」只表示元数据核查程度。

状态：`TODO` 未核元数据；`SCREENED` 已核标题摘要；`READING` 精读中；`DONE` 笔记与矩阵齐；`EXCLUDED` 已排除。

## 2. 文献总表

| ID | 主题 | 年 | 题目 | 会议/期刊 | 状态 | 优先级 | 作者 | 定位 |
|---|---|---:|---|---|---|---|---|---|
| T1-01 | 01 | 2022 | SAHI / Slicing Aided Hyper Inference | ICIP | SCREENED | 必读 | Akyon et al. | 主近邻：切片推理协议；学定义与代价报告 |
| T1-02 | 01 | 2026 | ROI-Gated SAHI | arXiv preprint | SCREENED | 选读（原 SHOULD） | Riyadh et al. | 自适应切片近邻；对照 DensK1，非新门控主张 |
| T2-01 | 02 | 2022 | QueryDet | CVPR | SCREENED | 必读 | Yang et al. | 改查询机制加速高分辨；本篇不改网络 |
| T2-02 | 02 | 2025 | ESOD | TIP | SCREENED | 选读（原 SHOULD） | Liu et al. | 高效小目标／稀疏计算叙事对照 |
| T3-01 | 03 | 2018 | Dynamic Zoom-in Network | CVPR | SCREENED | 必读 | Gao et al. | 局部放大问题陈述；对照 DensK1 |
| T3-02 | 03 | 2019 | AutoFocus | ICCV | SCREENED | 必读 | Najibi et al. | 多尺度推理预算；学边界写法 |
| T3-03 | 03 | 2019 | ClusDet | ICCV | SCREENED | 选读（原 SHOULD） | Yang et al. | 聚类切块再检测；学方法图与额外前向 |
| T4-01 | 04 | 2019 | VisDrone Challenge / DET overview | ICCVW etc. | SCREENED | 必读 | Zhu / Du et al. | 学航拍表怎么排、小目标口径 |
| T4-02 | 04 | 2018 | UAVDT | ECCV（2026-10-06 核：主会，DOI 10.1007/978-3-030-01249-6_23；原登记 ECCV Workshops） | SCREENED | 选读（原 SHOULD） | Du et al. | 跨集外推评测口径；对应 Stage E |
| T1-03 | 01 | 2019 | The Power of Tiling | CVPRW | SCREENED | 建议优先读 | Unel et al. | 事实：训练与推理均分块；VisDrone；报 FPS（TX1／TX2）（与 P0 关系待用户填） |
| T1-04 | 01 | 2018 | Selective Tile Processing | ICDSC | SCREENED | 选读 | Plastiras et al. | 事实：注意力选 tile + 记忆；自建行人集；报 CPU 处理时间（与 P0 关系待用户填） |
| T1-05 | 01 | 2021 | Cropped Windows（CroW） | ICCVW | SCREENED | 建议优先读 | Varga et al. | 事实：训练裁窗、推理整图；VisDrone 等三集；报 FPS（2080 Ti／TX2）（与 P0 关系待用户填） |
| T1-06 | 01 | 2023 | ASAHI | Remote Sensing | SCREENED | 选读 | Zhang et al. | 事实：自适应切片尺寸控制片数；VisDrone、xView；报计算时间（硬件待补）（与 P0 关系待用户填） |
| T2-03 | 02 | 2023 | CEASC | CVPR | SCREENED | 建议优先读 | Du et al. | 事实：检测头稀疏卷积；VisDrone、UAVDT；报 GFLOPs／FPS（2080Ti）（与 P0 关系待用户填） |
| T2-04 | 02 | 2021 | TPH-YOLOv5 | ICCVW | SCREENED | 选读 | Zhu et al. | 事实：YOLOv5 加 Transformer 预测头、输入长边 1536；VisDrone；未报 FPS（与 P0 关系待用户填） |
| T3-04 | 03 | 2020 | DMNet | CVPRW | SCREENED | 建议优先读 | Li et al. | 事实：密度图引导裁剪；VisDrone、UAVDT；报 #img 与 s/img（1080 Ti）（与 P0 关系待用户填） |
| T3-05 | 03 | 2021 | CDMNet | ICCVW | SCREENED | 选读 | Duan et al. | 事实：粗粒度密度图聚类裁剪；VisDrone、UAVDT；只报 #img（与 P0 关系待用户填） |
| T3-06 | 03 | 2022 | UFPMP-Det | AAAI | SCREENED | 建议优先读 | Huang et al. | 事实：子区域打包 mosaic；VisDrone、UAVDT；报推理时间（1080Ti）（与 P0 关系待用户填） |
| T3-07 | 03 | 2023 | AdaZoom | TMM | SCREENED | 建议优先读 | Xu et al. | 事实：自适应缩放选区；VisDrone、UAVDT、DOTA；报 s/img（GPU 待补）（与 P0 关系待用户填） |
| T3-08 | 03 | 2021 | GLSAN | TIP | SCREENED | 选读 | Deng et al. | 事实：全局–局部 + 自适应裁剪 + 局部超分；VisDrone、UAVDT；指标与时延待补（与 P0 关系待用户填） |
| T3-09 | 03 | 2022 | Focus-and-Detect | SPIC | SCREENED | 选读 | Koyun et al. | 事实：GMM 聚焦区域再检测；VisDrone、UAVDT；报每图时间（2080 Ti）（与 P0 关系待用户填） |
| T3-10 | 03 | 2024 | YOLC | T-ITS | SCREENED | 选读 | Liu et al. | 事实：局部尺度模块搜簇区域；VisDrone、UAVDT；报 s/img（2080 Ti）（与 P0 关系待用户填） |
| T3-11 | 03 | 2023 | CZ Det | CVPRW | SCREENED | 建议优先读 | Meethal et al. | 事实：检测器自预测密度裁剪 + 二次放大；VisDrone、DOTA；报 FPS（与 P0 关系待用户填） |
| T4-03 | 04 | 2022 | VisDrone（TPAMI） | TPAMI | SCREENED | 建议优先读 | Zhu et al. | 事实：VisDrone 数据集与挑战赛综述；test-dev 1,610 张（与 P0 关系待用户填） |
| T4-04 | 04 | 2021 | VisDrone-DET2021 Results | ICCVW | SCREENED | 选读 | Cao et al. | 事实：DET2021 挑战赛结果汇总；test-challenge 1,580 张（与 P0 关系待用户填） |
| T4-05 | 04 | 2017 | Speed/Accuracy Trade-offs | CVPR | SCREENED | 选读 | Huang et al. | 事实：统一实现下速度／精度／内存对照；COCO；GPU 时间（Titan X）（与 P0 关系待用户填） |
| T4-06 | 04 | 2023 | SODA | TPAMI | SCREENED | 选读 | Cheng et al. | 事实：小目标检测综述 + SODA-D／SODA-A 基准（与 P0 关系待用户填） |
| T4-07 | 04 | 2006 | Demšar 2006 | JMLR | SCREENED | 选读 | Demšar | 事实：分类器比较的统计检验（Wilcoxon／Friedman）（与 P0 关系待用户填） |
| T5-01 | 05 | 2016 | YOLO（v1） | CVPR | SCREENED | 选读 | Redmon et al. | 事实：单阶段一次前向检测；VOC；报 FPS（Titan X）（与 P0 关系待用户填） |
| T5-02 | 05 | 2024 | Ultralytics YOLO11 | 软件 | SCREENED | 选读 | Jocher et al. | 事实：YOLO11 官方出处与引用格式；官方速度表（与 P0 关系待用户填） |
| T5-03 | 05 | 2024 | YOLOv11 Overview | arXiv preprint | SCREENED | 选读 | Khanam et al. | 事实：YOLOv11 架构组件综述（与 P0 关系待用户填） |

## 3. 与本篇主张的关系（一句话）

| ID | 覆盖点 | 本篇用法 | 冲突度 |
|---|---|---|---|
| T1-01 | 切片推理定义与代价 | 主近邻；协议对照而非提出 SAHI | 低（设定不同） |
| T1-02 | 自适应减片 | 对照 DensK1 | 中（易被说成换皮） |
| T2-01 | 高分辨加速 | 划界：他们改网络 | 低 |
| T2-02 | 高效 SOD | 效率叙事对照 | 低 |
| T3-01 | 局部放大 | 问题起笔／DensK1 对照 | 低 |
| T3-02 | 多尺度预算 | 预算轴对照 | 低 |
| T3-03 | 聚类切块 | 方法图表格式参考 | 低 |
| T4-01 | VisDrone 口径 | 主评测表 | — |
| T4-02 | UAVDT | 跨集；排序不稳可作负结果边界 | — |

2026-10-06 新增的 T1-03 … T5-03（22 篇）本节不预填；「与P0关系」由你在各主题 `Reading_List.md` 阅读清单（2026-10-07 已与原必读清单合并为一张表）末列填写。

## 4. 仍缺的证据（阅读侧）

- 各必读篇 PDF 放入主题 `pdfs/` 并在 Reading_List 勾选。
- ClusDet／DMNet 正式书目元数据需补 DOI 后再改状态 DONE。（2026-10-06：ClusDet DOI 10.1109/ICCV.2019.00840；DMNet 已登记为 T3-04，DOI 10.1109/CVPRW50498.2020.00103；改 DONE 仍需笔记。）
- 正式投稿前：Related Work 只进「推理时增强／切片评测」栏，不进「新检测器」栏。

## 5. 候选检索记录（2026-10-06）

**范围：** 按 P0（冻结 YOLO11n 上五协议对照，VisDrone test-dev + UAVDT，分 GPU 时延）检索 22 篇候选，元数据与关键事实写在各主题 `Reading_List.md`（2026-10-07 起与原必读清单合并为一张阅读清单表；原 9 篇 MUST／SHOULD 的数据集／检测器／指标／时延同日按全文补齐）。

| 主题 | 新增篇数 | 新增 ID |
|---|---:|---|
| T1 01_Slicing_Inference | 4 | T1-03 … T1-06 |
| T2 02_HighRes_Efficient_SOD | 2 | T2-03 … T2-04 |
| T3 03_Multiscale_Zoom_Inference（含密度／聚类／区域引导） | 8 | T3-04 … T3-11 |
| T4 04_Aerial_Benchmarks_Eval | 5 | T4-03 … T4-07 |
| T5 05_Detector_References（新建） | 3 | T5-01 … T5-03 |
| 合计 | 22 | |

**新建 `05_Detector_References/` 的原因：** T1–T4 收推理协议、选区与评测口径方面的近邻工作；YOLO／Ultralytics 是被冻结检测器本身的出处，用途是 Method 节引用，不是对照工作，混放会让两类引用难以区分。密度／聚类／区域引导类（建议主题 c）与已有 T3-03 ClusDet 同类，并入 T3，不另开文件夹。

**建议优先读（8 篇，理由只写事实）：**

| ID | 题目 | 理由 | 链接 |
|---|---|---|---|
| T1-03 | The Power of Tiling | VisDrone + 训练与推理均分块 + 报嵌入式 FPS（Jetson TX1／TX2） | https://doi.org/10.1109/CVPRW.2019.00084 |
| T1-05 | Cropped Windows（CroW） | VisDrone + 推理时用整图最大分辨率 + 报桌面与嵌入式 FPS；`P0_C1C2.md` 已引用 | https://doi.org/10.1109/ICCVW54120.2021.00311 |
| T2-03 | CEASC | 同两集（VisDrone、UAVDT）+ 报 GFLOPs 与 FPS（单块 RTX 2080Ti） | https://doi.org/10.1109/CVPR52729.2023.01291 |
| T3-04 | DMNet | 同两集 + 密度引导裁剪 + 报每图张数（#img）与 s/img（GTX 1080 Ti） | https://doi.org/10.1109/CVPRW50498.2020.00103 |
| T3-06 | UFPMP-Det | 同两集 + 报打包图数与推理时间（单块 GTX 1080Ti，对比 ClusDet、DMNet） | https://doi.org/10.1609/aaai.v36i1.19986 |
| T3-07 | AdaZoom | VisDrone test-dev + UAVDT + 与均匀划分 UP(1×1／2×2／3×3) 并列报 s/img | https://doi.org/10.1109/TMM.2022.3178871 |
| T3-11 | CZ Det | VisDrone + 均匀裁剪与密度裁剪同表对照 + 报 FPS | https://doi.org/10.1109/CVPRW59228.2023.00198 |
| T4-03 | VisDrone（TPAMI） | P0 主评测集 VisDrone2019-DET test-dev（1,610 张）的正式出处 | https://doi.org/10.1109/TPAMI.2021.3119563 |

**核验方式：** 题目、作者、年份、venue 用 Crossref（DOI）或 arXiv API 逐条核对；数据集、检测器、指标、时延硬件从 arXiv／CVF／JMLR 全文或官方文档读取。

**未能完全核实（已标 待补）：**

- T1-06 ASAHI：出版社页面拒绝访问，只读到 Crossref 摘要；时延硬件 **待补**。
- T3-07 AdaZoom：内容读自 arXiv 2021 版；GPU 型号未写明，TMM 正式版数字未核。
- T3-08 GLSAN：TIP 全文未取到；数据集与检测器取自官方代码仓库，指标与时延 **待补**。
- T3-11 CZ Det：报 FPS，但测速 GPU 文中未写明。
- 已有条目订正：T4-02 UAVDT 原登记 ECCV Workshops，经 Crossref 核为 ECCV 2018 主会论文集（DOI 10.1007/978-3-030-01249-6_23）。
