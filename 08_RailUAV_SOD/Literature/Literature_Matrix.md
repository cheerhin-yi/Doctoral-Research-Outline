# Literature 矩阵（A · RailUAV-SOD）

> 只记「主题 × 证据」；细读写在各主题 `notes/`。  
> 主张边界：数据基础设施 + 双审计；**不是**告警系统。  
> 条目来自已同意文献（AB 判断及附录）；状态多为 SCREENED，精读后改 DONE。

## 1. 主题与状态

| 主题 | 名称 | 对应写作位置 |
|---|---|---|
| T1 | UAV 铁路数据集 | Related Work · 数据近邻 |
| T2 | Sci Data 近邻与披露 | Related Work / Data Records |
| T3 | 自动标注 / OVD | Methods · 预标注；Related Work |
| T4 | 合成缺陷生成 vs 审计 | Methods · 合成审计 |
| T5 | 航拍 SOD / 封闭集基线 | Experiments 基线 |

状态：`TODO` / `SCREENED` / `READING` / `DONE` / `EXCLUDED`。

## 2. 文献总表（已同意条目）

| ID | 主题 | 年 | 题目/工作 | 会议/期刊 | 状态 | 优先级 | 定位 |
|---|---|---:|---|---|---|---|---|
| T1-01 | T1 | 2024 | UAV-RSOD | Scientific Data；doi:10.1038/s41597-024-03952-3 | SCREENED | MUST | 已占低空 UAV 铁路分割+异物；禁「首个」 |
| T1-02 | T1 | 2024 | RailFOD23 | Scientific Data；doi:10.1038/s41597-024-02918-9 | SCREENED | MUST | 接触网异物+大量合成；审计对照 |
| T1-03 | T1 | 2026 | RFDD | Scientific Data；doi:10.1038/s41597-026-07851-7 | SCREENED | MUST | 扣件全景+真实缺陷；须硬切 UAV+审计 |
| T1-04 | T1 | 2024 | RSD_UAV（UTCRS/USDOT 报告） | 报告 2024-09 | SCREENED | SHOULD | UAV 轨面缺陷大规模；加固禁 first |
| T1-05 | T1 | 2024 | Electronics UAV 扣件 | doi:10.3390/electronics13091781 | SCREENED | SHOULD | 压低单点新颖性；无审计→下限 |
| T2-01 | T2 | 2024 | Aela 等 UAV railway infrastructure monitoring | Automation in Construction | SCREENED | MUST | 场景正当性综述 |
| T2-02 | T2 | 2025 | A Review of Computer Vision for Railways | IEEE 铁路视觉综述 | SCREENED | SHOULD | CV 需求与作业约束 |
| T3-01 | T3 | 2025 | Auto-Labeling Data for Object Detection | arXiv:2506.02359 | SCREENED | MUST | 开词表自动标注成本–质量可量化 |
| T3-02 | T3 | 2024 | DART（DreamBooth+Grounding DINO） | ESWA；doi:10.1016/j.eswa.2024.125124 | SCREENED | MUST | 管线已有；本篇卖效率审计 |
| T4-01 | T4 | 2024 | Ferdousi 等；YOLOv8-FAM+style transfer 等 | Cogn. Comput. / Autom. Constr. | SCREENED | SHOULD | 合成生成已占；卖审计非生成器 |
| T4-02 | T4 | 2023–2025 | SRDA 等 sim-to-real | CACIE 等 | SCREENED | SHOULD | 合成→真实有可测差距 |
| T5-01 | T5 | — | YOLO / RT-DETR 封闭集基线族 | — | TODO | MUST | 本篇基线工具，非贡献 |

## 3. 与本篇主张的关系

| ID | 覆盖点 | 本篇用法 | 冲突度 |
|---|---|---|---|
| T1-01 | UAV 铁路公开集 | 主划界；禁 first | 高（叙事） |
| T1-02 | 合成异物数据文 | 合成须审计 | 中 |
| T1-03 | 小部件×真实缺陷 Sci Data | 中位上移为硬条件：UAV+效率+合成审计 | 高 |
| T3-02 | 半自动管线 | 踢出「管线发明」上界 | 高 |
| T3-01 | 效率量化先例 | 支撑 A-C2 写法 | 低 |

## 4. 仍缺的证据（阅读侧）

- MUST 篇 PDF 入主题 `pdfs/` 并在 Reading_List 勾选；
- NeurIPS 2026 E&D Call 条款精读（若冲上界）；
- 正式投稿前：Data Records 披露清单与基线表轴冻结。
