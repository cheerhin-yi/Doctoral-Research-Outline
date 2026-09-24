# 研究计划：RailUAV-SOD（论文 A）

更新：2026-09-24。  
效力：预备计划；**执行以 `Current_Stage.md` 再授权为准**。  
独立边界：[`../01_Paper1_OpenWorld_Risk/AB_Independent_Publication_Boundary.md`](../01_Paper1_OpenWorld_Risk/AB_Independent_Publication_Boundary.md)  
方向判断：[`../01_Paper1_OpenWorld_Risk/AB_Direction_Judgment_With_Literature_2026-09-24.md`](../01_Paper1_OpenWorld_Risk/AB_Direction_Judgment_With_Literature_2026-09-24.md)  
Venue/Claim 政策：[`../00_Overview/Venue_and_Claim_Policy_JCR_2026-09-24.md`](../00_Overview/Venue_and_Claim_Policy_JCR_2026-09-24.md)  
部件族难度×发表界：[`Writing/PartFamily_CollectionDifficulty_and_VenueBounds_2026-09-24.md`](Writing/PartFamily_CollectionDifficulty_and_VenueBounds_2026-09-24.md)

## 1. 当前问题与边界

在 **UAV 航拍视角**下，面向铁路 **小部件 × 真实缺陷** 的检测基准是否可公开复用？双引擎开放词汇（OVD）半自动预标注在受控人时下能否量化加速比与修错成本？合成缺陷在 fidelity–utility 曲线上是否可审计？

- 论文类型：**数据基础设施**（基准 + 标注管线 + 审计协议），不是告警系统。
- 边界：单目 RGB、UAV 视角、铁路小部件与缺陷细类；许可与可下载发布必须可复核。
- **不**以「首个 UAV 铁路数据集」为卖点。
- **不**把告警预算、轨道风险排序写成主贡献（属 B；可一句引用）。
- 每篇最多两项主张（本篇建议 C1 数据+效率、C2 合成审计；或合并为「基准+双审计」叙事，投稿前冻结）。

## 2. 主张表（预备 / PROPOSED）

| ID | 主张 | 状态 |
|---|---|---|
| A-C1 | 公开可复用的 UAV×铁路小部件×真实缺陷检测基准，并报告封闭集强基线（YOLO / RT-DETR 等） | PROPOSED · IDLE |
| A-C2 | 双引擎 OVD 预标注在受控人时协议下可量化加速比、修错率与一致性；合成比例–性能（fidelity–utility）曲线可审计披露 | PROPOSED · IDLE |

### 必须划界的近邻（不得再写「首个」）

| 近邻 | 含义 | 本篇增量落点 |
|---|---|---|
| UAV-RSOD（Sci Data 2024） | 低空 UAV 铁路分割+异物已占 | 小部件×真实缺陷 + 效率/合成审计 |
| RailFOD23（Sci Data 2024） | 接触网异物、大量合成 | 合成须走审计曲线，非再堆合成 |
| RFDD（Sci Data 2026） | 高铁扣件全景+计量学缺陷 | **硬切 UAV 视角** + 标注效率审计 |
| RSD_UAV（UTCRS 2024） | UAV 轨面缺陷大规模图集 | 禁止 first-dataset；部件细类与审计仍可差异化 |
| DART（ESWA 2024） | DreamBooth+Grounding DINO 管线 | 不卖管线发明；卖受控效率审计 |
| Electronics 2024 UAV 扣件 | 单点 UAV×扣件方法文 | 无审计则下限滑向 Electronics/Sensors |

文献条目与 DOI 以 `Literature/Literature_Matrix.md` 及 AB 判断附录为准；**不虚构指标**。

## 3. 方法章节规划（授权后）

1. **采集协议（未来 UAV）**：航高/视角、线别与场景隔离、许可、缺陷稀缺披露、隐私与安全。
2. **分类体系（taxonomy）**：部件 × 缺陷细类；与 RFDD/UAV-RSOD 标签映射表。
3. **双引擎 OVD 预标注**：文本提示 + 视觉提示；术语表/Prompt 五元组可与 B 共享资产，但本篇只报**标注召回/人时**。
4. **D4 式计时审计**：人标对照、加速比、修错率、Kappa/抽检一致性、误差模式。
5. **合成审计曲线**：合成比例–封闭集性能；fidelity 披露清单（生成器类型、域差、是否混入测试）。
6. **封闭集基线**：YOLO 系列与 RT-DETR 等同协议表；不作告警决策实验。

## 4. 阶段门（摘要）

见 `Stage_Guide.md`。当前整体 **IDLE**。A0 可行性通过前禁止采集与训练。

## 5. 与论文 B 的关系

- 可引用 B 的动机句；**不得**互为必要条件。
- 删掉对 B 的全部引用后，A 的主表与贡献句仍须完整。
- 若自采严重受阻：A 降级/延期（Data in Brief / 技术报告），**禁止**把 A 贡献块塞进 B。

## 6. 停止条件

真实缺陷不足、许可不可发布、效率审计无法受控、与 RFDD/DART 无法划界时：暂缓或降档，不并入 B。

## 7. A0 案头加厚（2026-09-24 晚 · 仍 IDLE）

- 近邻「已覆盖 / 未证实缺口 / A增量」见 `Literature/Literature_Matrix.md` §5。  
- A1 草稿（**不采集**）：`Writing/Taxonomy_Draft.md`、`Annotation_Timing_Protocol_D4_Draft.md`、`Synthetic_Disclosure_Checklist.md`、`Collection_Protocol_Draft.md`（FUTURE）、`SciData_Disclosure_Template_Stub.md`。  
- Taxonomy 注意：RFDD 扣件重叠 → **细类须超越扣件-only**。  
- Collection_Protocol 标 FUTURE，须 `Current_Stage` 书面授权后方可执行。


## 8. 主张梯子与 venue（不定死 · 2026-09-24）

| 档 | 工作/主张 | Venue |
|---|---|---|
| 强 | 多族 UAV + 真缺陷 + 双审计 | Sci Data 顺利；冲刺 NeurIPS D&B/E&D |
| **中（target）** | UAV×小部件×真缺陷 + 可审计效率/合成 | **主轨：数据刊 Sci Data** |
| 弱 fallback | 按采集难度收缩部件族；审计变薄但仍有协议/基线 | **相关** 方法/应用 **JCR Q2 或 Q3（floor）** |

- 部件族**可按采集难度增减**（见 `Writing/Taxonomy_Draft.md` §7 与 PartFamily 分析）。  
- Sci Data 未达时，**不**并入 B；改投 JCR Q2/Q3 related 或暂缓。
