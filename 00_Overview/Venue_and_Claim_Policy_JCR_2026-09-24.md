# 发表档次与主张策略：JCR 主尺（2026-09-24）

> **效力：** 全局案头政策；编码 A/B 及概述文档中讨论 venue / claim 时的统一口径。  
> **不**授权新 ACTIVE 工作；**不**改变 `Current_Stage.md` 唯一 ACTIVE=**P0_EI**。  
> A/B 仍为 **IDLE / PREP**；A/B 独立发表边界不变。  
> 日期：2026-09-24（Asia/Shanghai）  
> 取代/上位：本文件为 **JCR-primary** 现行政策；旧 [`Venue_Quartile_Policy_2026-09-22.md`](Venue_Quartile_Policy_2026-09-22.md) 仍有效但以本文件为准并加厚 claim ladder。

---

## 1. 期刊分区主尺：JCR-primary

1. **主尺 = JCR 分区（Q1 / Q2 / Q3 / Q4）**。计划、判断、交接文档优先写「JCR Qx」。  
2. **不以 CAS / 中科院分区为主尺**；若导师/学院口径需要，可作**次要备注**，不得替代 JCR 表述。  
3. 旧文写「三区应用刊」而未标明体系时，统一改写为 **JCR Q3**（中位），并显式保留 **JCR Q2/Q3 相关论文为地板（floor）**。  
4. **不虚构具体影响因子**；分区以**当年 JCR 为准**。对 TITS / TIM 等精确当年 quartile 标 **Unknown**，写作时写「以当年 JCR 为准」。  
5. 会议：仍按投稿时 CCF 推荐目录；EI 索引是描述项，不替代 CCF/JCR。

---

## 2. 主张不定死：强 / 中 / 弱（fallback）梯子

| 档 | 含义 | 政策 |
|---|---|---|
| **强（upper）** | 冲刺主张与冲刺 venue | 允许规划，不当作唯一成功条件 |
| **中（mid / target）** | **计划锚**：主证据与主叙事对齐 | 默认按此设计实验与写作 |
| **弱（fallback）** | 证据不足时**有意收缩**的较弱主张 | 仍须支持 **相关论文** 发到 **JCR Q2 或 Q3（floor）** |

原则：

- 保留强中位主张，但**明确允许**较弱 fallback；**不定死**单一 claim。  
- Fallback 不是「随便降级」，而是预先设计的**可发表相关论文**（related papers），地板 = **JCR Q2/Q3**。  
- 弱主张仍须：可复现协议、诚实划界、删除/消融或等价证据；禁止把失败包装成强主张。

---

## 3. 论文 B（OpenWorld Risk）主张 × venue 梯子

| 档 | 主张范围（摘要） | Venue 带（JCR） | 备注 |
|---|---|---|---|
| **强** | C1 双路径×固定告警预算 + C2 轨旁风险排序齐全；删除实验显著；≥2 组 Unknown 轮换；相对 SRLF 增量可指认 | 上限：**IEEE TITS** / **IEEE TIM**（精确 quartile **Unknown**，以当年 JCR 为准；历史常讨论为 Q1/Q2 带） | 冲刺，非保底 |
| **中（target）** | 冻结卡 DESK-FROZEN 的 C1/C2 中位证据包：预算曲线 + 可派发 + 风险层 | **JCR Q2–Q3 应用刊**（TIM / Measurement / 同档应用向） | **计划锚** |
| **弱（fallback）** | 例：仅单路径+预算；或仅 Known 上风险排序；或协议/系统文而无完整双路径 | **相关论文**仍瞄准 **JCR Q2 或 Q3（floor）**；避免掉到无分区/弱开源叙事作为 Paper1 主成果 | 见 `01_Paper1_OpenWorld_Risk/Writing/Claim_Freeze_C1_C2.md` fallback 节 |

DESK-FROZEN 强/中措辞保留；fallback **不**覆盖冻结卡成功判据，而是「若不达标如何仍发相关 Q2/Q3」。

---

## 4. 论文 A（RailUAV-SOD）主张 × venue 梯子

| 档 | 工作/主张范围（摘要） | Venue 带 | 备注 |
|---|---|---|---|
| **强** | 多部件族 UAV + 真实缺陷 + 双审计（人时+合成）扎实；相对 RFDD/DART/UAV-RSOD 划界清楚 | *Scientific Data* 顺利 / 冲刺 NeurIPS D&B 或 E&D（不稳） | Sci Data = Nature portfolio **数据刊**，常与 JCR「应用刊」分轨讨论 |
| **中（target）** | UAV×小部件×真缺陷 + 受控效率/合成审计可复用 | **主轨：数据刊 Sci Data** | **计划锚** |
| **弱（fallback）** | 部件族收缩（如扣件为主）、审计变薄、真实缺陷不足但仍有协议/基线 | **方法/应用相关论文**瞄准 **JCR Q2 或 Q3（floor）**（如 Sensors / Electronics 同档应用向）；**禁止**把 A 贡献块并入 B | 见 `08_RailUAV_SOD/Writing/PartFamily_CollectionDifficulty_and_VenueBounds_2026-09-24.md` |

说明：A 的**主轨是数据刊 Sci Data**；若数据刊门槛未达，fallback 到 **JCR Q2/Q3 方法/应用相关论文**，而非「只能 Sci Data 或失败」。

---

## 5. 地板（Floor）

- **统一地板：** 较弱范围下仍应能支撑 **相关论文** 发表于 **JCR Q2 或 Q3**。  
- Floor ≠ 鼓励灌水；Floor = 预先设计的可辩护收缩路径。  
- 做差到「无预算曲线的未知检出 / 无审计的扣件小数据」仍可能低于 floor——政策要求**事前**把弱主张设计到仍可达 Q2/Q3 related。

---

## 6. 执行纪律（本文件不授权开工）

1. 唯一 ACTIVE 仍为 **P0_EI**（见 `Current_Stage.md`）。  
2. A / B = **IDLE / PREP**；采集、训练、主 Run 须书面再授权。  
3. A/B **独立发表**；可引用，不得互为必要条件。  
4. 本政策更新案头表述，**不**启动实验。

## 7. 指针

| 文档 | 角色 |
|---|---|
| `01_Paper1_OpenWorld_Risk/Writing/Claim_Freeze_C1_C2.md` | B 强/中冻结 + 弱 fallback |
| `01_Paper1_OpenWorld_Risk/AB_Direction_Judgment_With_Literature_2026-09-24.md` | A/B 上下限与文献界变（JCR 口径） |
| `08_RailUAV_SOD/Writing/PartFamily_CollectionDifficulty_and_VenueBounds_2026-09-24.md` | A 部件族采集难度 × 工作/发表界 |
| `POST_EI_HANDOFF_A_B_Packages.md` | 解锁纪律 |
