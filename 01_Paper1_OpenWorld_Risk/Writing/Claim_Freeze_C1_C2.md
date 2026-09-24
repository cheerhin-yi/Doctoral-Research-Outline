# C1/C2 主张冻结卡（案头冻结 · 实验未授权）

> **效力：** 案头措辞冻结（DESK-FROZEN）。状态仍为 **PREP/IDLE**。  
> **不**授权 Stage ④ 采集 / 正式训练 / 主 Run。  
> **不**改变 `../../00_Overview/Current_Stage.md` 唯一 ACTIVE=P0_EI。  
> 日期：2026-09-24 晚（Asia/Shanghai）  
> 权威交叉：[`../Research_Plan.md`](../Research_Plan.md) · [`../AB_Independent_Publication_Boundary.md`](../AB_Independent_Publication_Boundary.md) · [`../AB_Direction_Judgment_With_Literature_2026-09-24.md`](../AB_Direction_Judgment_With_Literature_2026-09-24.md) · [`../../00_Overview/Venue_and_Claim_Policy_JCR_2026-09-24.md`](../../00_Overview/Venue_and_Claim_Policy_JCR_2026-09-24.md)
> **主张不定死：** 下文 C1/C2 为 **强/中（DESK-FROZEN mid）**；另见文末 **弱 fallback**，地板 = 相关论文 **JCR Q2/Q3**。

---

## C1（精确主张句）

**主张句：**  
在铁路 UAV 巡检场景中，以实时闭集检测器（YOLO 族）为**已知路径**，并并联一条**未知候选路径**（开放词汇 / 开放集 / 异常候选中择一强基线），在**固定告警预算**（每图或每航次可复核候选上限）下，相对「仅闭集 YOLO」以及「仅强未知基线」能提高**危险目标召回**，且不把 Known 类性能拖垮至不可接受。

**一句话口令：** 双路径 × 固定告警预算 × 危险召回（非 unknown AP 刷分）。

### C1 成功判据（最低可信证据）

1. 场景/航次隔离测试集；≥2 组 Known/Unknown 类别轮换。  
2. 主图：**危险召回–告警预算曲线**（横轴预算，纵轴危险 Recall）。  
3. 对照：闭集 YOLO；至少一个强未知候选基线（如 YOLO-World / NegAS 类，投稿前冻结选型）。  
4. 同时报告：Known 类性能、Unknown Recall、每图错误候选数 / FPR。  
5. 删除未知支路后，固定预算下危险召回应明显变弱（否则 C1 不成立）。

### C1 失败判据

- 未知误报在预算内不可控 → 删除「开放未知」主张，收缩为检测错误分析。  
- 收益仅来自更大输入/更多参数/测试集调阈 → 不保留方法主张。  
- 只提升 unknown AP / AUROC，无预算曲线 → **不算** C1 成功。

### C1 明确不包含（Out of Scope）

- 新建 UAV 铁路基准数据集（属 A）。  
- 持续类别增量学习完整 OWOD 流水线。  
- 纯 OOD 滤波、无告警预算的「又一未知检出」。  
- 告警决策层与轨道风险排序的主增量（属 C2）。

---

## C2（精确主张句）

**主张句：**  
在相同候选输入下，引入**轨道上下文**（轨道运行区域 / 边界 / 重叠或简单相对距离）的风险排序，相对 Detection-only、Unknown-only 与「无上下文的简单分数排序」，能提高**可派发危险告警**的价值：在固定高风险 Recall 下降低每图告警数，或在固定告警预算下提高高风险命中；删除风险层后该收益应消失或显著减弱。

**一句话口令：** 轨道上下文风险排序 × 可派发告警价值（非检测-only）。

### C2 成功判据

1. 相同上游候选；唯一自变量 = 是否使用轨道上下文风险层。  
2. 报告：高风险 Recall、AUPRC（或等价排序指标）、每图告警数；按 Known/Unknown 分组。  
3. 删除风险层应变弱；Detection-only / Unknown-only 不得已足够好到使 C2 冗余。  
4. 风险标签**不得**只编码目标类别（防类别捷径）。

### C2 失败判据

- 无稳定增量 → 只保留最简单区域规则作工程附录，**不称贡献**。  
- 增益只在单一场景或依赖错误轨道 Mask → 收缩适用范围或放弃。

### C2 明确不包含

- 稠密三维 / SLAM / 完整物理距离误差传播（属后续测量向论文）。  
- 告警系统整机产品化；多机协同；通信/ISAC。  
- A 的标注人时 / 合成 fidelity 曲线作为本主张主证据。

---

## 与近邻的差异化（Related Work 必写表）

| 近邻 | 他们已覆盖 | 本篇必须多出的增量 | 若无增量则 |
|---|---|---|---|
| **SRLF**（TITS 2025） | UAV 铁路稀疏/未知相关检出 | **固定告警预算** + **可派发** + 轨道上下文**排序**（非同构稀疏未知检出） | 难冲 TITS；改 TIM/Measurement 或收缩 |
| **Meng** 等 UAV 未知风险 | 未知风险检出取向 | **告警决策层**与**预算曲线**；删除实验 | 被写成「又一检出」 |
| **Conformal OD / Risk Control**（arXiv:2304.06052 谱系） | 覆盖保证 / 风险控制校准 | 钉死「**双路径 × 固定配额 × 可派单**」，避免被校准文献稀释 | 被审稿人归为 conformal 应用短文 |
| **Three-way open-set + false-novelty budget**（arXiv:2511.15343） | 抽象 false-novelty 预算（如 q≈20%） | 补 **轨旁风险层与派单**；铁路场景协议 | C1 抽象新颖性被压；上限下滑 |
| **PCA-HBOS UAV OOD** 等 | 航拍 OOD 滤波 | 与**纯 OOD 滤波**划界；强调危险召回–预算而非 anomaly score | 下限 Drones/Access |
| **Cao TITS 2024 / TIM OID 2025** | 侵界/障碍综述 | 场景合法性；挑战条目对表；**不是**方法贡献 | — |
| **OWOD TCSVT 2024 / IJCV OSOD 2025** | 术语与评测反思 | 用预算/危险召回，**拒绝**只报 unknown AP | 术语被挑错 |
| **YOLO-World / CastDet / UAV-OVD** | 开放词汇基线能力 | **基线非贡献**；公平报告预训练 | 被说成换皮 OVD |

---

## A/B 独立性自检（冻结时）

- [x] 删掉对 A 的全部引用后，C1/C2 句子与主表设计仍完整。  
- [x] C1/C2 **不**依赖 A 的效率表或合成曲线作必要条件。  
- [x] A 的 taxonomy / 人时审计 **不**写入本卡成功判据。



---

## 主张梯子与弱 Fallback（不定死 · 2026-09-24）

> **政策：** [`../../00_Overview/Venue_and_Claim_Policy_JCR_2026-09-24.md`](../../00_Overview/Venue_and_Claim_Policy_JCR_2026-09-24.md)  
> **口径：** 上表 C1/C2 保持 **DESK-FROZEN 中位/强主张**；若证据达不到，**允许**预先设计的较弱相关论文，仍瞄准 **JCR Q2 或 Q3（floor）**。Fallback **不**自动改写成功判据，须在写作时显式收缩贡献句。

### B Claim × JCR Venue 梯子

| 档 | 主张形态 | Venue（JCR 带） | 何时启用 |
|---|---|---|---|
| **强** | C1 双路径×预算 + C2 轨旁风险排序齐全；删除显著；Unknown 轮换扎实；相对 SRLF 增量可指认 | 上限 TITS / TIM（quartile **Unknown**，以当年 JCR 为准） | 冲刺，非唯一成功条件 |
| **中（target · 冻结卡默认）** | 本文件 C1/C2 全文 | **JCR Q2–Q3** 应用刊（TIM / Measurement / 同档） | **计划锚** |
| **弱 W1** | **单路径 + 固定告警预算**：仅闭集 YOLO（或仅一未知支路）+ 预算下危险召回曲线；不做完整双路径并联 | 相关论文 **JCR Q2/Q3** | 未知支路不可控或实现不过关 |
| **弱 W2** | **Known-only 轨旁风险排序**：候选仅 Known；C2 式轨道上下文排序 + 告警价值；弱化/不做开放未知 | 相关论文 **JCR Q2/Q3** | Unknown 协议泄漏风险高、正样本不足 |
| **弱 W3** | **协议/系统短文**：Known/Unknown 零泄漏协议 + 预算评测规范 + 基线对照，方法增量薄 | 相关协议/应用向 **JCR Q2/Q3**（或同档测量/传感应用刊） | 方法增益弱但协议贡献可辩护 |
| **不可接受（低于 floor）** | 无预算曲线的 unknown AP 刷分；与 SRLF 同构；堆 YOLO 模块冒充贡献 | 拒稿或弱开源刊——**不作 Paper1 主成果** | 禁止当作「弱成功」 |

### Fallback 写作纪律

1. 摘要/贡献列表必须改写为实际档位；不得仍写满血 C1+C2。  
2. Related Work 仍须划界 SRLF / Meng / conformal / OOD。  
3. A/B 独立性不变：弱 B **不得**靠并入 A 数据文贡献凑数。  
4. 状态机：fallback 启用仍须 **PREP→再授权**；本卡不授权实验。

## 状态机

| 字段 | 值 |
|---|---|
| 主张状态 | **DESK-FROZEN · IDLE**（中位 C1/C2；弱 fallback 已文档化，不定死） |
| 实验状态 | 未授权 |
| 下一步（解锁后） | Stage ② 精读合并矩阵 → Stage ③ 最小复现 → 再谈方法选型冻结 |
