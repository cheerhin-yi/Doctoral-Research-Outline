# Learning_Notes（A · RailUAV-SOD）

按 **数据文 + 双审计** 路线分块学习。面向**非铁路专家**：先打铁路可见结构基础，再学数据集论文工艺与审计。  
主题笔记统一两部分：

1. **第一部分：应知** — 学习目标、知识链、链上说明、练习、必答  
2. **第二部分：我的记录** — 按同一条链填写理解／证据／必答；**过关只查这里**

> **编号权威（已锁定 2026-09-24）：** [`_PLAN_Learning_Notes_Curriculum_2026-09-24.md`](_PLAN_Learning_Notes_Curriculum_2026-09-24.md)。本 README 与 `01`–`09` 文件名已与课表对齐；**应知已写成可自学正文；我的记录仍留空给你填。**编号/关卡/边界仍锁定；不以过程报告充数。
> **状态纪律：** 本目录学习 ≠ 授权采集/训练。包状态仍为 **PREP / IDLE**；全库唯一 ACTIVE 仍是 **P0_EI**（见 [`../../00_Overview/Current_Stage.md`](../../00_Overview/Current_Stage.md)）。
> **A/B 边界：** 笔记中不写告警预算、危情召回、可派发告警为主贡献（属 B）。见 [`../../01_Paper1_OpenWorld_Risk/AB_Independent_Publication_Boundary.md`](../../01_Paper1_OpenWorld_Risk/AB_Independent_Publication_Boundary.md)。

| 文件 | 用途 | 关卡 |
|---|---|---|
| [`../Learning_Check_Baseline.md`](../Learning_Check_Baseline.md) | 助手维护的检查基准 | — |
| [`../Completion_Metrics.md`](../Completion_Metrics.md) | 关卡总门 L0–L4 | — |
| `00_Knowledge_Map.md` | 统一核心知识地图（不过关） | 导航 |
| `01_Railway_Track_Structure_Basics.md` | 钢轨／轨枕／道床／轨距；UAV 能看见什么 | **L0 FOUNDATION** |
| `02_Fasteners_Joints_and_Visible_Parts.md` | 扣件系统、鱼尾板/接头、轨下可见件；对齐 Taxonomy；RFDD 重叠 | **L0 FOUNDATION** |
| `03_Defect_Types_and_Inspection_Language.md` | D0–D5 风格缺陷与巡检用语（非官方标准冒充） | **L0 FOUNDATION** |
| `04_UAV_Railway_Viewpoint_and_Visibility.md` | 航高/角度、遮挡、小部件尺度断崖 | **L1 FOUNDATION** |
| `05_Dataset_Paper_Craft_SciData.md` | Sci Data 逻辑与近邻划界；JCR Q2/Q3 fallback | **L1** |
| `06_OVD_AutoLabel_and_Timing_Audit.md` | OVD=预标注工具；D4 人时审计 | **L2** |
| `07_Synthetic_Audit_Fidelity_Utility.md` | 合成 fidelity–utility 与披露清单 | **L2** |
| `08_Aerial_SOD_Baselines_and_Metrics.md` | 航拍 SOD 封闭集基线与小目标指标 | **L3** |
| `09_Mainline_A_Knowledge_Chain.md` | A 端到端知识链（数据文主链） | **L3 / L4** |
| `Learning_Record_Template.md` | 可选当日备忘 | — |

## 推荐阅读顺序（完成门）

```text
00 地图（导航，不过关）
  → 01 轨道结构基础          【L0 门：闭卷串讲「看得见的轨」】
  → 02 扣件/接头/可见件      【L0 门：部件族表 + RFDD 重叠一句】
  → 03 缺陷与巡检用语        【L0 门：D0–D5 自洽 + 不冒充标准】
  → 04 UAV 视角与可见性      【L1 门：尺度断崖 + 与近景差异】
  → 05 数据集论文工艺        【L1 门：Sci Data vs Q2/Q3 fallback】
  → 06 OVD 预标注与计时      【L2 门：加速比/修错/Kappa；禁告警指标】
  → 07 合成审计              【L2 门：披露字段 + 曲线读法】
  → 08 航拍 SOD 基线         【L3 门：同协议基线表轴】
  → 09 主线知识链            【L3/L4 门：端到端串讲 + 主张自检】
```

### 完成门（摘要）

| 门 | 条件 | 才能做什么 |
|---|---|---|
| L0 | `01`+`02`+`03` 第二部分均 `PASSED` | 进入视角与数据文工艺 |
| L1 | `04`+`05` `PASSED` | 进入双审计主题 |
| L2 | `06`+`07` `PASSED` | 进入基线与主链 |
| L3 | `08` `PASSED` + `09` 主链练习完成 | 进入 L4 主张/划界自检 |
| L4 | `09` 必答与划界自检 `PASSED` | 讨论 A1 冻结措辞；**仍不**解锁采集/训练 |

1. 先读本 README、`Learning_Check_Baseline`、`Current_Stage`。  
2. 铁路 FOUNDATION 块（`01`→`03`）优先；用户不熟铁路域时**禁止跳过**。  
3. 每块第二部分自评后交给助手检查；`PASSED` 再进下一块。  
4. 学习关卡 **不**替代实验门，也 **不**因补笔记而授权采集/训练。

## 与案头材料对齐

| 写作/政策文件 | 主要笔记 |
|---|---|
| `Writing/Taxonomy_Draft.md` | `02`、`03`、`09` |
| `Writing/PartFamily_…VenueBounds….md` | `02`、`05` |
| `Writing/Annotation_Timing_Protocol_D4_Draft.md` | `06` |
| `Writing/Synthetic_Disclosure_Checklist.md` | `07` |
| `Writing/Collection_Protocol_Draft.md`（FUTURE） | `04`（可见性）；采集本身仍 FUTURE |
| `00_Overview/Venue_and_Claim_Policy_JCR_2026-09-24.md` | `05`、`09` |
| `AB_Independent_Publication_Boundary.md` | 全部笔记禁止泄漏 B 告警主张 |

样板结构对齐：[`00_Practice_UAV_Aerial_Detection/Learning_Notes/`](../../00_Practice_UAV_Aerial_Detection/Learning_Notes/README.md)（如 `04_Small_Object`、`07_Mainline`）。
