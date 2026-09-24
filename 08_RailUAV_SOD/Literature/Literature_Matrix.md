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


---

## 5. A0 近邻划界表（已覆盖 / 未证实缺口 / A增量）· 2026-09-24 晚

> 案头加厚；不虚构指标。不确定标 **Unknown**。精读后回填原文表号。

| ID | 工作 | 年 | 已覆盖 | 未证实缺口（相对 A） | A增量（主张落点） |
|---|---|---:|---|---|---|
| T1-01 | UAV-RSOD（Sci Data；doi:10.1038/s41597-024-03952-3） | 2024 | 低空 UAV 铁路分割+异物公开集 | 小部件×真实缺陷细类；标注人时审计；合成 fidelity–utility | **硬切**：部件×缺陷 taxonomy + 双审计；禁「首个 UAV 铁路集」 |
| T1-02 | RailFOD23（Sci Data；doi:10.1038/s41597-024-02918-9） | 2024 | 接触网异物；大量合成 | 真实缺陷主导叙事；合成披露是否达 fidelity–utility 曲线 Unknown | 合成须走**审计曲线+披露清单**，不堆生成器 |
| T1-03 | RFDD（Sci Data；doi:10.1038/s41597-026-07851-7） | 2026 | 高铁扣件全景+计量学真实缺陷 | UAV 视角；跨部件细类；标注效率审计 | **硬切 UAV 视角** + 效率审计 + 合成审计；taxonomy 须**超越扣件-only** |
| T1-04 | RSD_UAV（UTCRS/USDOT 报告） | 2024 | UAV 轨面缺陷大规模图集 | 期刊级 Data Records 披露；部件 taxonomy Unknown | 禁 first-dataset；差异化在细类+双审计 |
| T1-05 | Electronics 2024 UAV 扣件（doi:10.3390/electronics13091781） | 2024 | UAV×扣件方法文 | 无受控人时/合成审计 | 无审计则下限滑向 Electronics/Sensors；本篇上移靠审计 |
| T3-02 | DART（ESWA；doi:10.1016/j.eswa.2024.125124） | 2024 | DreamBooth+Grounding DINO 半自动管线 | 受控 D4 人时协议；误差模式表 Unknown | **不卖管线发明**；卖受控加速比/修错率/Kappa/误差模式 |
| T3-01 | Auto-Labeling for OD（arXiv:2506.02359） | 2025 | 开词表自动标注成本–质量可量化先例 | 铁路小部件域 Unknown | 支撑 A-C2 写法；域迁移需自证 |
| T2-01 | Aela 等 UAV railway monitoring | 2024 | UAV 铁路基础设施监测综述 | — | 场景正当性；不构成数据贡献 |
| T2-02 | Railway CV Review | 2025 | 铁路 CV 需求与约束 | UAV 小部件基准 Unknown | 需求背书 |
| T4-01 | Ferdousi 等 style-transfer 合成 | 2024 | 合成生成已占 | 审计协议 | 卖审计非生成器 |
| T4-02 | SRDA 等 sim-to-real | 2023–2025 | 合成→真实可测差距 | 铁路部件缺陷曲线 Unknown | 支撑 fidelity–utility 动机 |
| T5-01 | YOLO / RT-DETR 族 | — | 通用封闭集检测器 | — | **基线工具，非贡献** |

### A0 结论句（案头）

- Sci Data 中位仍成立，当且仅当：**UAV 视角 × 小部件（不止扣件）× 真实缺陷** + **双引擎 OVD 人时审计** + **合成 fidelity–utility 披露** 同时可写清。  
- RFDD 重叠 → taxonomy **必须多元化**（扣件以外的扣件/弹条/轨距块/鱼尾板/垫板/道钉等候选，定稿前冻结）。  
- 未授权前：本表只服务 A0 划界与 A1 草稿，**不**启动采集/训练。
