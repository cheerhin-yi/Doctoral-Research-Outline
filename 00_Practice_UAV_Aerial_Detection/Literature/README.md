# Literature（练习论文 · 主题文献区）

结构对齐 `01_Paper1_OpenWorld_Risk/Literature`：**第一层是主题文件夹**，不是论文槽位堆砌。

## 主题一览

| 主题 | 文件夹 | 主要回答的问题 | 支撑主张 |
|---|---|---|---|
| T1 切片／分块推理 | [01_Slicing_Inference](01_Slicing_Inference/Reading_List.md) | 切片如何改小目标可见性与代价 | Related Work 主近邻 |
| T2 高分辨／高效 SOD | [02_HighRes_Efficient_SOD](02_HighRes_Efficient_SOD/Reading_List.md) | 别人改网络还是只改推理 | 划界：本篇只改协议 |
| T3 多尺度／局部放大 | [03_Multiscale_Zoom_Inference](03_Multiscale_Zoom_Inference/Reading_List.md) | 推理预算与前向次数怎么报 | DensK1／放大叙事对照 |
| T4 航拍基准与评测 | [04_Aerial_Benchmarks_Eval](04_Aerial_Benchmarks_Eval/Reading_List.md) | VisDrone／UAVDT 口径与表轴 | Stage D／E／F 写法 |
| T5 检测器出处 | [05_Detector_References](05_Detector_References/Reading_List.md) | 冻结检测器 YOLO11n 的正式引用 | Method／Setup 引用（2026-10-06 新建，理由见 Matrix §5） |

## 根目录文件

- [P0_C1C2.md](P0_C1C2.md) — 当前稿与后续稿能用的全文结论
- [Literature_Matrix.md](Literature_Matrix.md) — 全主题文献总表（优先级：必读／建议优先读／选读）与证据摘要（§5：2026-10-06 候选 22 篇检索记录与建议优先读）
- [Coarse_Reading_Notes.md](Coarse_Reading_Notes.md) — 粗读学习笔记（主题级，不替代篇笔记）
- [Paper_Note_Template.md](Paper_Note_Template.md) — 单篇笔记模板（三样：问题句／表轴／边界）
- 各主题下：`Reading_List.md`（每主题一张阅读清单表：编号、题目+链接、年／Venue、数据集、检测器、指标、时延／硬件、优先级、状态、与P0关系）、`notes/`、`pdfs/`（PDF 放入对应 `pdfs/`，清单里登记）

## 纪律

1. 正式引用前核 DOI／会议页；预印本与正式版不一致时以正式版为准。  
2. 长审计过程文不进本目录（旧 `papers/P0_EI/notes/*_Audit.md` 已归档）。  
3. 后续新主题：新建 `0N_ThemeName/`，并同步 Matrix 与本 README 表。  
