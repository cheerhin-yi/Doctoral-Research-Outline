# 论文 A（08_RailUAV_SOD）Learning_Notes 课程计划

> 日期：2026-09-24（Asia/Shanghai）  
> 对齐：[`../../00_Overview/Learning_Note_Method.md`](../../00_Overview/Learning_Note_Method.md) + Practice P0 双部模板  
> **编号权威：** 以本目录已落地的 Paper1 双部笔记文件名为准（见 §1.1）。本计划**只锁编号/关卡/过关门**，**不覆盖** `01`–`09` 正文。  
> 效力：案头预备。学习笔记 **不**解锁采集/训练；**不**改变 `Current_Stage.md` 唯一 ACTIVE=`P0_EI`。  
> 主张地板：[`../../00_Overview/Venue_and_Claim_Policy_JCR_2026-09-24.md`](../../00_Overview/Venue_and_Claim_Policy_JCR_2026-09-24.md)（A 主轨 Sci Data；fallback JCR Q2/Q3 related；不并入 B）  
> A/B 边界：[`../../01_Paper1_OpenWorld_Risk/AB_Independent_Publication_Boundary.md`](../../01_Paper1_OpenWorld_Risk/AB_Independent_Publication_Boundary.md)  
> 索引侧已推送：`a8a43f2`（discussion products index）

---

## 0. Paper1 四问摘要

| # | 问题 | 答案 |
|---|---|---|
| 1 | 编号列表 / 阅读顺序 / 过关门 | §1：`00` 导航 + `01`–`09`；顺序即块序；过关查第二部分；门控见 Baseline/Metrics |
| 2 | 铁路入门篇数与五节点 | **3 篇 L0 FOUNDATION**（`01`–`03`）+ **`04` 视角 FOUNDATION（L1）**；限界语境并入 `03` 巡检用语 + `04` 可见性；深法规=HISTORICAL |
| 3 | 终态如何成形 | 知识图 `00` → 双部笔记（应知/我的记录）→ Baseline 块门 → Metrics L0–L4；禁百科倾倒 |
| 4 | A vs B 笔记边界 | A 独占部件×缺陷/双审计/Sci Data；共享最小轨道词；告警预算/风险排序只在 B |

---

## 1. 编号文件列表 · 阅读顺序 · 过关门

### 1.1 总表（编号锁定 · 与目录文件名一致）

| 序 | 文件 | 关卡 | 角色 | 过关（PASSED）检查项 |
|---|---|---|---|---|
| — | `00_Knowledge_Map.md` | — | 导航 | 不过关 |
| 1 | `01_Railway_Track_Structure_Basics.md` | L0 | FOUNDATION·轨道结构 | ☐ 闭卷串讲 ☐ 横切草图 ☐ 俯视指认 ☐ 三类排除 ☐ 必答初稿 |
| 2 | `02_Fasteners_Joints_and_Visible_Parts.md` | L0 | FOUNDATION·扣件/接头/可见件 | ☐ 串讲 ☐ 部件族表≥5 ☐ vs RFDD 一句（无「首个」） ☐ 必答 |
| 3 | `03_Defect_Types_and_Inspection_Language.md` | L0 | FOUNDATION·缺陷×巡检用语 | ☐ 串讲 ☐ part×defect / D0–D5 自洽 ☐ 不冒充国标 ☐ 必答 |
| 4 | `04_UAV_Railway_Viewpoint_and_Visibility.md` | L1 | FOUNDATION·UAV 视角可见性 | ☐ 串讲 ☐ GSD/尺度断崖 ☐ vs 近景两句 ☐ 必答；不当事飞行许可 |
| 5 | `05_Dataset_Paper_Craft_SciData.md` | L1 | Sci Data 工艺+近邻 | ☐ 串讲 ☐ 四段各一行 ☐ 允许/禁止主张句 ☐ venue 梯子 ☐ 必答 |
| 6 | `06_OVD_AutoLabel_and_Timing_Audit.md` | L2 | OVD 预标注+D4 人时 | ☐ 串讲 ☐ D4 流程 ☐ 加速/修错/Kappa ☐ 禁告警主指标 ☐ 必答 |
| 7 | `07_Synthetic_Audit_Fidelity_Utility.md` | L2 | 合成 fidelity×utility | ☐ 串讲 ☐ 披露字段勾选 ☐ 曲线读法 ☐ 禁混 test ☐ 必答 |
| 8 | `08_Aerial_SOD_Baselines_and_Metrics.md` | L3 | 封闭集航拍 SOD 基线 | ☐ 串讲 ☐ 同协议表轴 ☐ 不做告警曲线 ☐ 必答 |
| 9 | `09_Mainline_A_Knowledge_Chain.md` | L3/L4 | A 端到端主链 | ☐ 主链图 ☐ A/B 结果对照 ☐ 删 B 引用后仍完整 ☐ L4 主张自检 ☐ 必答 |
| 选 | `Learning_Record_Template.md` | — | 可选日录 | 不过关 |

配套（包根，已由 Paper1 脚手架加厚，本计划不改其正文意图）：

- [`../Learning_Check_Baseline.md`](../Learning_Check_Baseline.md)
- [`../Completion_Metrics.md`](../Completion_Metrics.md)

> **勿覆盖纪律：** 若助手曾生成另一套 `01_Rail_Track_*` / `05_Dataset_Paper_Craft_and_Neighbors` 等文件名，**一律作废**；以本表与目录现有双部笔记为准。新增主题用 `10+`，**不重排 01–09**。

### 1.2 阅读顺序

```text
00 地图（不过关）
 → 01 轨道结构          【L0】
 → 02 扣件/接头/可见件  【L0】
 → 03 缺陷与巡检用语    【L0】
 → 04 UAV 视角可见性    【L1 FOUNDATION】
 → 05 Sci Data 工艺     【L1】
 → 06 OVD + D4 人时     【L2】
 → 07 合成审计          【L2】
 → 08 航拍 SOD 基线     【L3】
 → 09 A 主线知识链      【L3 → L4】
```

### 1.3 块解锁（与 P0 同构）

```text
TODO → LEARNING → REVIEWING → PASSED | REPEAT
```

1. 只查**第二部分：我的记录**。  
2. 须闭卷沿知识链串讲。  
3. 练习须有可复查证据。  
4. 必答保留初稿；空白/代写 → `REPEAT`。  
5. 未 PASSED 不得进下一块；铁路 `01`–`03` 对非铁路背景**不可跳过**。  
6. 出现告警预算/风险排序当 A 主结果 → `REPEAT`（属 B）。  
7. 学习 PASSED ≠ 采集/训练授权。

---

## 2. 铁路领域入门：篇数 · 五节点 · FOUNDATION vs HISTORICAL

### 2.1 篇数

- **铁路域入门 = 4 个 FOUNDATION 块**：`01`–`03`（L0）+ `04`（L1，视角可见性）。  
- 用户铁路知识少 → 目标是「能指认 + 能服务 taxonomy/采集字段案头」，不是工务百科。

### 2.2 五节点映射

| 必含节点 | 落点 | 标签 | HISTORICAL / 出界（不阻塞） |
|---|---|---|---|
| 轨道结构 | `01` | FOUNDATION | 纵断面/养护规程全书 |
| 扣件与接头 | `02` | FOUNDATION | 厂家型号全书；RFDD 计量学深读 |
| 缺陷类型 | `03` | FOUNDATION | 冒充国标条文；金相全谱 |
| 限界与巡检语境 | `03` 巡检用语 + `04` 取景/隔离字段 | FOUNDATION（最小） | 限界法规背诵；告警派发（→B） |
| UAV 视角可见性 | `04` | FOUNDATION | 飞控调参细则（授权采集后再学） |

### 2.3 标签纪律

| 标签 | 含义 |
|---|---|
| FOUNDATION | 过关必须 |
| HISTORICAL | 对照可读，不阻塞 |
| CANDIDATE | 待证据，未冻结进主 taxonomy |
| OUT_OF_SCOPE_A | 属 B 或出界 |

---

## 3. 终态成形（反百科）

```text
00 知识图（边界标签）
  → 双部笔记：应知（短链≤6步） / 我的记录
  → Learning_Check_Baseline 块门
  → Completion_Metrics L0–L4
  → 写作草稿只引用已 PASSED 链上的词与主张句
```

反百科三条：

1. 每块知识链短；链外进「暂不学 / HISTORICAL」。  
2. 铁路名词过滤器 = **图像上能不能稳定标**。  
3. A/B 不各写一套百科：共享只留最小轨道词，主张句分家（§4）。

---

## 4. A vs B Learning_Notes 边界

### 4.1 仅 A

- 部件×缺陷 taxonomy（超越扣件-only）与 UAV 可标性  
- 近邻缺口表（UAV-RSOD / RFDD / RailFOD23 / RSD_UAV / DART…）  
- OVD **预标注**人时、修错、Kappa（非告警召回）  
- 合成 fidelity×utility 与披露  
- Sci Data Data Records / Technical Validation 案头  
- 采集协议字段案头（FUTURE，未授权不执行）

### 4.2 共享（最小词）

| 词 | A 用法 | B 用法 |
|---|---|---|
| 轨道区域直觉 | 取景/标签空间 | 风险上下文 |
| 小目标尺度直觉 | 部件像素/基线协议 | 已知检测困难点 |
| 术语/Prompt 资产 | 报标注召回 | 仅旁证，不得当 C1/C2 主证据 |

### 4.3 仅 B（A 禁止当贡献展开）

固定告警预算下的危险召回；已知+未知双轨；风险排序；Detection-only vs Track-zone 消融。

### 4.4 自检

删掉对 B 的全部引用后，A 学习目标与主张句仍完整？→ 必须「是」。

---

## 5. 关卡总表（与 Completion_Metrics 对齐）

| 关卡 | 块 | 通过后 |
|---|---|---|
| L0 | `01`+`02`+`03` PASSED | 进 `04`/`05` |
| L1 | `04`+`05` PASSED | 进双审计 |
| L2 | `06`+`07` PASSED | 进基线/主链 |
| L3 | `08` PASSED + `09` 主链练习 | 进 L4 划界 |
| L4 | `09` 主张/划界自检 PASSED | 可讨论 A1 措辞；**仍不**解锁采集/训练 |

---

## 6. 本计划交付 / 明确不做

**本文件职责：** 锁定编号清单 + 关卡/过关门 + 四问答案。  

**明确不做：**

- 不覆盖 Paper1 已写的 `00`–`09` / README / Template 正文  
- 不改 `Current_Stage` ACTIVE=`P0_EI`  
- 不采集、不训练  
- 不把 B 风险笔记并入 A  

**可选后续（非本收口）：** Baseline §1 文件名若与目录有个别拼写差，仅做「对齐文件名」的最小修补，仍不改检查语义。
