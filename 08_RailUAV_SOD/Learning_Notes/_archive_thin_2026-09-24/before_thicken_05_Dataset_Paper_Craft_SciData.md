# 05 数据集论文工艺与 Sci Data（含 JCR fallback）

> 关卡：**L1**。过关只查**第二部分**。  
> 政策：[`../../00_Overview/Venue_and_Claim_Policy_JCR_2026-09-24.md`](../../00_Overview/Venue_and_Claim_Policy_JCR_2026-09-24.md)。  
> 近邻矩阵：[`../Literature/Literature_Matrix.md`](../Literature/Literature_Matrix.md) §5。  
> 替旧 stub：`01_Dataset_Paper_Craft.md`。

---

## 第一部分：应知

### 学习目标

1. 能用自己的话说明 *Scientific Data* 类数据文审稿人主要看什么（可复用、披露、技术验证），与方法刊（如 TITS/TIM 取向）有何不同。  
2. 能默写近邻「已占坑」清单，并各给一句**增量落点**（禁「首个」）。  
3. 能解释主张梯子：强 / 中位 Sci Data / 弱 **JCR Q2 或 Q3 related** floor；以及「弱了也不并入 B」。

### 知识链

```text
数据文卖什么（基础设施，不是告警系统）
  → Sci Data：Background → Methods → Data Records → Technical Validation
  → 近邻已覆盖（UAV-RSOD / RailFOD23 / RFDD / RSD_UAV / DART…）
  → 未证实缺口 → A 增量
  → 主轨 Sci Data（中位）
  → 弱：部件族收缩/审计变薄 → JCR Q2/Q3 related（Sensors/Electronics 同档）
  → 停止：不可发布 / 无真实缺陷硬称基准 → 暂缓，不塞进 B
```

### 链上说明

1. **Sci Data 逻辑（工作摘要）**  
   - 价值：别人能否下载、理解标签、复现划分与基线。  
   - Technical Validation：证明数据「用得起来」（封闭集基线、审计表），**不是**证明你发明了新检测头。  
   - 模板桩：`Writing/SciData_Disclosure_Template_Stub.md`。

2. **近邻一句表（必须会）**

| 近邻 | 已占 | A 增量落点 |
|---|---|---|
| UAV-RSOD | 低空 UAV 铁路分割+异物 | 小部件×真缺陷 + 双审计；禁 first |
| RailFOD23 | 接触网异物+大量合成 | 合成走审计曲线，不堆生成 |
| RFDD | 高铁扣件全景+计量学缺陷 | UAV 硬切 + 超越扣件-only + 效率/合成审计 |
| RSD_UAV | UAV 轨面缺陷大规模 | 禁 first；细类+审计差异化 |
| DART | DreamBooth+Grounding DINO 管线 | **不卖管线发明**；卖受控人时审计 |
| Electronics 2024 UAV 扣件 | 单点方法文 | 无审计 → 下限参照 |

DOI 以 Literature_Matrix 为准；不虚构指标。

3. **主张梯子（不定死）**  
   - 强：多族 + 真缺陷 + 双审计扎实 → Sci Data 顺利 / 冲刺 D&B（不稳）。  
   - 中（target）：UAV×小部件×真缺陷 + 可审计效率/合成 → **主轨 Sci Data**。  
   - 弱：按采集难度缩族、审计变薄但仍有协议/基线 → **相关**方法/应用 **JCR Q2 或 Q3（floor）**。  
   - CAS/中科院不作主尺；不虚构当年 IF/quartile（TITS/TIM 等标 Unknown）。

4. **禁止的「方法刊错位」**  
   - 不要用「我们 mAP 超 SOTA 3 个点」冒充数据文主贡献。  
   - 不要把 B 的告警预算曲线塞进 A 的 Technical Validation 主表。

### 练习

1. 用 Sci Data 四段结构，各写一行「本文打算填什么」（可对照 Stub）。  
2. 写一句合格摘要贡献句、一句**不合格**（含「首个」或告警主张）并指出错在哪。  
3. 假设只能采到扣件+弱审计：你的 venue/claim 应落到梯子哪一档？下一步是扩族还是降档？

### 必答题

1. 为什么不能只写「又一个 UAV 铁路数据集」？至少点名两个近邻。  
2. Sci Data 的 Technical Validation 与 TITS 类方法实验的核心差别是什么？  
3. Sci Data 中位未达时，为什么政策要求改投 Q2/Q3 related 或暂缓，而不是并入 B？

### 当前边界

- 主轨/fallback 是计划锚，不是中稿承诺。  
- 学习本块 ≠ A0 可行性通过。

---

## 第二部分：我的记录

### 元信息

| 字段 | 填写 |
|---|---|
| 开始日期 | |
| 状态 | `TODO` / `LEARNING` / `REVIEWING` / `PASSED` / `REPEAT` |

### 闭卷复述

```text
数据文卖点 → Sci Data 结构 → 近邻增量 → 梯子强/中/弱 → 停止条件
```

- 我的复述：

### 练习证据

| 练习 | 证据 | 摘要 |
|---|---|---|
| 四段各一行 | | |
| 合格/不合格摘要句 | | |
| 弱档决策 | | |

### 必答作答

1.  
2.  
3.  

### 错误 / 不确定 / 助手检查

-
