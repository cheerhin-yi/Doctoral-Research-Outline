# 05 数据集论文工艺与 Sci Data（含 JCR fallback）

> 关卡：**L1**。过关只查**第二部分**。  
> 政策：[`../../00_Overview/Venue_and_Claim_Policy_JCR_2026-09-24.md`](../../00_Overview/Venue_and_Claim_Policy_JCR_2026-09-24.md)。  
> 近邻矩阵：[`../Literature/Literature_Matrix.md`](../Literature/Literature_Matrix.md)（若路径以仓库实际为准）。  
> PartFamily：[`../Writing/PartFamily_CollectionDifficulty_and_VenueBounds_2026-09-24.md`](../Writing/PartFamily_CollectionDifficulty_and_VenueBounds_2026-09-24.md)。  
> 模板桩：[`../Writing/SciData_Disclosure_Template_Stub.md`](../Writing/SciData_Disclosure_Template_Stub.md)。

---

## 第一部分：应知

### 学习目标

1. 能用自己的话说明 *Scientific Data* 类数据文审稿人主要看什么（可复用、披露、技术验证），与方法刊有何不同。  
2. 能默写近邻「已占坑」清单，并各给一句**增量落点**（禁「首个」）。  
3. 能解释主张梯子：强 / 中位 Sci Data / 弱 **JCR Q2 或 Q3 related** floor；以及「弱了也不并入 B」。  
4. 能写出合格 vs 不合格摘要贡献句各一句。

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

---

### 术语表（CN / EN）

| 中文 | English | 备注 |
|---|---|---|
| 数据记述 | Data Records | 数据如何组织、访问、字段 |
| 技术验证 | Technical Validation | 证明「用得起来」 |
| 主张梯子 | claim ladder | 强/中/弱预先设计的收缩路径 |
| 地板 | floor | 弱主张仍应可达的发表带 |
| 相关论文 | related paper | fallback 时的方法/应用文 |
| 划界 | positioning / demarcation | 相对近邻的增量说明 |

---

### 通俗讲解：数据文卖的是「别人能接着用的基础设施」

#### 1. Sci Data 审稿人在找什么

| 段落 | 他们问什么 | A 应准备什么意识 |
|---|---|---|
| Background | 为何需要这个基准？近邻差在哪？ | 近邻一句表 + 禁 first |
| Methods | 如何采集、标注、划分、许可？ | 协议可复现；未授权阶段只学结构 |
| Data Records | 下载什么、字段什么、如何引用？ | 披露完整；合成单独声明 |
| Technical Validation | 封闭集基线能否跑通？审计表是否诚实？ | YOLO/RT-DETR 是工具不是贡献（`08`） |

**不是**证明你发明了新检测头；**不是**证明固定告警预算下危险召回（那是 **B**）。

#### 2. 近邻一句表（必须会）

| 近邻 | 已占 | A 增量落点 |
|---|---|---|
| UAV-RSOD | 低空 UAV 铁路分割+异物 | 小部件×真缺陷 + 双审计；禁 first |
| RailFOD23 | 接触网异物+大量合成 | 合成走审计曲线，不堆生成 |
| RFDD | 高铁扣件全景+计量学缺陷 | UAV 硬切 + 超越扣件-only + 效率/合成审计 |
| RSD_UAV | UAV 轨面缺陷大规模 | 禁 first；细类+审计差异化 |
| DART | DreamBooth+Grounding DINO 管线 | **不卖管线发明**；卖受控人时审计 |
| Electronics 2024 UAV 扣件等 | 单点方法文 | 无审计 → 下限参照 |

DOI/指标以 Literature_Matrix 为准；**不虚构**。学习阶段会复述「已占/增量」即可。

#### 3. 主张梯子（不定死）

| 档 | 工作直觉 | Venue 带 |
|---|---|---|
| 强 | 多族 + 真缺陷 + 双审计扎实 | Sci Data 顺利 / 冲刺 D&B（不稳） |
| 中（target） | UAV×小部件×真缺陷 + 可审计效率/合成 | **主轨 Sci Data** |
| 弱 | 缩族、审计变薄但仍有协议/基线 | **JCR Q2 或 Q3 related** floor |
| 停止 | 无真实缺陷硬称基准 / 不可发布 | **暂缓**；**禁止并入 B** |

CAS/中科院不作主尺；TITS/TIM 等精确 quartile 标 Unknown。

#### 4. 方法刊错位（禁止）

- 不要用「mAP 超 SOTA 3 点」冒充数据文主贡献。  
- 不要把 B 的告警预算曲线塞进 A 的 Technical Validation 主表。  
- 弱了改投 Q2/Q3 related 或暂缓，**不是**把 A 贡献块粘到 B 论文里凑篇幅。

---

### 常见错误 / 禁止说法

| 禁止 | 改法 |
|---|---|
| 「又一个 UAV 铁路数据集」无近邻 | 点名 ≥2 近邻 + 增量 |
| 「首个…」 | 删；改写硬切与审计 |
| 「我们提出更强检测器」作主贡献 | 基线工具化；贡献回到数据+审计 |
| 「Sci Data 未中就把 A 并进 B」 | 政策明确禁止 |

---

### 练习

1. 用 Sci Data 四段结构，各写一行「本文打算填什么」。  
2. 写一句合格摘要贡献句、一句不合格句（含「首个」或告警主张）并指出错在哪。  
3. 假设只能采到扣件+弱审计：venue/claim 落到梯子哪一档？下一步扩族还是降档？

### 必答题

1. 为什么不能只写「又一个 UAV 铁路数据集」？至少点名两个近邻。  
2. Sci Data 的 Technical Validation 与 TITS 类方法实验的核心差别是什么？  
3. Sci Data 中位未达时，为什么政策要求改投 Q2/Q3 related 或暂缓，而不是并入 B？

---

### 参考答案

#### 练习 1 参考

- Background：UAV 小部件×真缺陷基准缺口（相对 RFDD/UAV-RSOD…）。  
- Methods：视角/标注/划分/许可（授权后填实）。  
- Data Records：类目、split、合成字段、访问方式。  
- Technical Validation：同协议封闭集基线 + D4/合成审计表。

#### 练习 2 参考

- 合格：「We release a UAV-view multi-part railway fastener/joint appearance-defect benchmark with auditable labeling-time and synthetic-ratio protocols.」  
- 不合格：「We present the first fastener defect dataset and improve open-world alarm recall.」——「first」撞 RFDD；alarm recall 属 B。

#### 练习 3 参考

落到**弱档**（JCR Q2/Q3 related floor）。下一步优先：扩非扣件族或加厚审计以回到 Sci Data 中位；若不能，**降档诚实发表**，不并入 B。

#### 必答 1 参考

近邻已覆盖异物、扣件近景、轨面、合成管线等；不点名会被审稿人视为重复建设。至少如 UAV-RSOD 与 RFDD。

#### 必答 2 参考

Validation 证明数据可训练、可划分、可复现基线与审计；方法刊实验证明新算法相对 SOTA 的增益。A 主贡献在前者。

#### 必答 3 参考

A/B 独立发表边界：A 弱主张仍有 related Q2/Q3 路径；并入 B 会绑定告警主结果、破坏独立与划界，政策禁止。

---

### 当前边界

- 主轨/fallback 是计划锚，不是中稿承诺。  
- 学习本块 ≠ A0 可行性通过。

---


### 补充课：把「增量」写成审稿人能勾选的清单

写 Background / Related Data 时，用勾选而不是形容词：

- [ ] 点名 ≥2 近邻（如 UAV-RSOD、RFDD）  
- [ ] 各用一句写清「已占什么」  
- [ ] 各用一句写清「我们多什么」（UAV 视角 / 多部件 / 审计…）  
- [ ] 全文零「首个」  
- [ ] Technical Validation 主表无告警预算曲线  

### 补充课：弱档相关论文长什么样

当只能做扣件为主 + 审计偏薄时：

- 标题与摘要承认范围收缩；  
- venue 表述用 JCR Q2/Q3 related（不虚构 IF）；  
- 仍保留协议、划分、基线表；  
- **禁止**把未完成的数据文贡献粘进 B 当附录。


### 补充课：四段结构各写一行的合格示例

| 段 | 一行示例 |
|---|---|
| Background | UAV 视角下轨道小部件外观缺陷仍缺可审计公开基准。 |
| Methods | 类目两轴 + 划分隔离 + 预标注计时 + 合成披露协议。 |
| Data Records | 字段、split 哈希、合成占比、许可与访问方式。 |
| Technical Validation | 同协议封闭集基线 + D4 人时表 + 合成比例曲线。 |

## 第二部分：我的记录

### 元信息

| 字段 | 填写 |
|---|---|
| 日期 | |
| 目标（1–3 句） | |
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

### 自评

| 维度 | 1–5 | 备注 |
|---|---:|---|
| 近邻一句表能默写 | | |
| 梯子清晰 | | |
| 未把 A 并 B | | |

### 错误 / 不确定 / 助手检查

-


### 补充：Sci Data 四段 × A 材料对照清单

| Sci Data 段 | 你至少要能指向的学习笔记/草稿 | 常见空洞 |
|---|---|---|
| Background | `05` 近邻表 + `02` RFDD 句 | 只骂近邻「不够好」却说不清增量 |
| Methods | `04` 可见性 + `03` 两轴 + D4/合成草稿 | 把未授权采集写成已完成 |
| Data Records | Taxonomy + split 原则 + 合成字段 | 缺许可/缺合成声明 |
| Technical Validation | `06`/`07`/`08` | 把告警曲线塞进主表 |

### 补充：合格贡献句的「零件清单」

一句贡献里尽量同时出现（不必一次写全，但脑子里要有）：

1. **UAV 视角**（对 RFDD）  
2. **多部件或非扣件-only**（对扣件全景同质）  
3. **真实缺陷诚实披露**（对纯合成堆量）  
4. **可审计**（人时或合成比例至少其一扎实）  
5. **不出现** first / 告警召回 / 风险排序主结果

### 补充：弱档落地时的「相关论文」长什么样（意识）

- 仍有清晰协议与封闭集基线；  
- 部件族可以收缩，但划界诚实；  
- venue 表述用 JCR Q2/Q3 related，不虚构 IF；  
- 标题与摘要不要假装自己是 Sci Data 数据刊中位包。
