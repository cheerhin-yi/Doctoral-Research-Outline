# Literature 矩阵（P0 练习论文）

> 只记「主题 × 证据」；细读写在各主题 `notes/`。主张边界：冻结检测器上的**推理协议对照**，不是新检测器。

## 1. 主题与状态

| 主题 | 名称 | 对应写作位置 |
|---|---|---|
| T1 | 切片／分块推理（SAHI 族） | Related Work · 推理时增强 |
| T2 | 高分辨／高效小目标 | Related Work · 划界 |
| T3 | 多尺度／局部放大推理 | Related Work · 预算与方法图参考 |
| T4 | 航拍基准与评测口径 | Experiments／附录口径 |

状态：`TODO` 未核元数据；`SCREENED` 已核标题摘要；`READING` 精读中；`DONE` 笔记与矩阵齐；`EXCLUDED` 已排除。

## 2. 文献总表

| ID | 主题 | 年 | 题目 | 会议/期刊 | 状态 | 优先级 | 作者 | 定位 |
|---|---|---:|---|---|---|---|---|---|
| T1-01 | 01 | 2022 | SAHI / Slicing Aided Hyper Inference | ICIP | SCREENED | MUST | Akyon et al. | 主近邻：切片推理协议；学定义与代价报告 |
| T1-02 | 01 | 2026 | ROI-Gated SAHI | arXiv preprint | SCREENED | SHOULD | Riyadh et al. | 自适应切片近邻；对照 DensK1，非新门控主张 |
| T2-01 | 02 | 2022 | QueryDet | CVPR | SCREENED | MUST | Yang et al. | 改查询机制加速高分辨；本篇不改网络 |
| T2-02 | 02 | 2025 | ESOD | TIP | SCREENED | SHOULD | Liu et al. | 高效小目标／稀疏计算叙事对照 |
| T3-01 | 03 | 2018 | Dynamic Zoom-in Network | CVPR | SCREENED | MUST | Gao et al. | 局部放大问题陈述；对照 DensK1 |
| T3-02 | 03 | 2019 | AutoFocus | ICCV | SCREENED | MUST | Najibi et al. | 多尺度推理预算；学边界写法 |
| T3-03 | 03 | 2019 | ClusDet | ICCV | SCREENED | SHOULD | Yang et al. | 聚类切块再检测；学方法图与额外前向 |
| T4-01 | 04 | 2019 | VisDrone Challenge / DET overview | ICCVW etc. | SCREENED | MUST | Zhu / Du et al. | 学航拍表怎么排、小目标口径 |
| T4-02 | 04 | 2018 | UAVDT | ECCV Workshops | SCREENED | SHOULD | Du et al. | 跨集外推评测口径；对应 Stage E |

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

## 4. 仍缺的证据（阅读侧）

- 各 MUST 篇 PDF 放入主题 `pdfs/` 并在 Reading_List 勾选。
- ClusDet／DMNet 正式书目元数据需补 DOI 后再改状态 DONE。
- 正式投稿前：Related Work 只进「推理时增强／切片评测」栏，不进「新检测器」栏。
