# 学习检查基准（A · RailUAV-SOD · 助手维护）

路径：`08_RailUAV_SOD/Learning_Check_Baseline.md`  
更新日期：2026-09-24（Asia/Shanghai）。  
维护者：助手。用户完成某块笔记的**填写位**后提交检查；**未达标不得进入下一块／下一关**。

权威关系：
- 当前科研唯一事项：`00_Overview/Current_Stage.md`（**P0_EI**；A 包 IDLE/PREP）。
- 学习推进：本文件 + `Completion_Metrics.md`。
- 写法：笔记对齐 Practice `01_YOLO_Research_Core.md` 单文件骨架（必须掌握→知识链→按段拆解→必学问题）；**不是** Practice `02` 双部 R1–R6。
- 过关看填写：节点追问/要点、必学问题「我的回答」初稿、最小完成证据勾选、能闭卷串讲知识链。
- A/B：检查时若出现告警预算/风险排序当 A 主结果 → **REPEAT** 并指向 AB Boundary。

判定：`TODO` → `LEARNING` → `REVIEWING` → `PASSED` / `REPEAT`。  
助手**不得代填**用户作答。

---

## 0. 总规则

1. 检查对象：该笔记中的**用户填写位**（节点追问、必学问题、最小完成证据、完成评审），不是背诵教材正文。  
2. 教材讲解抄写不等于通过。  
3. 必须能**沿知识链闭卷串讲**。  
4. 节点追问/要点须有填写（允许「暂不清楚」）；必学问题须有初稿（允许「暂不能回答」）。  
5. 最小完成证据清单须勾选或标明缺口；空白或明显代写 → `REPEAT`。  
6. 关卡顺序 L0→L4；铁路 FOUNDATION（01–03）对非铁路背景用户**不可跳过**。  
7. 学习通过 **≠** 采集/训练授权；ACTIVE 仍为 **P0_EI**。

---

## 1. 块顺序

| 顺序 | 笔记 | 关卡 | 状态 |
|---|---|---|---|
| 0 | `00_Knowledge_Map.md` | 导航 | 不过关 |
| 1 | `01_Railway_Track_Structure_Basics.md` | L0 | TODO |
| 2 | `02_Fasteners_Joints_and_Visible_Parts.md` | L0 | TODO |
| 3 | `03_Defect_Types_and_Inspection_Language.md` | L0 | TODO |
| 4 | `04_UAV_Railway_Viewpoint_and_Visibility.md` | L1 | TODO |
| 5 | `05_Dataset_Paper_Craft_SciData.md` | L1 | TODO |
| 6 | `06_OVD_AutoLabel_and_Timing_Audit.md` | L2 | TODO |
| 7 | `07_Synthetic_Audit_Fidelity_Utility.md` | L2 | TODO |
| 8 | `08_Aerial_SOD_Baselines_and_Metrics.md` | L3 | TODO |
| 9 | `09_Mainline_A_Knowledge_Chain.md` | L3/L4 | TODO |

旧 stub 文件名（`01_Dataset_Paper_Craft` 等）已废弃，勿再检查。

---

## 2. 分块检查清单（对齐 YOLO01 填写位）

各块通用过关字段：
- [ ] 闭卷串讲主题知识链
- [ ] 各链节点「追问/要点」有填写（可写暂不清楚）
- [ ] 必学问题均有「我的回答」初稿（可写暂不能回答）
- [ ] 「最小完成证据」已勾选或标明缺口
- [ ] 无告警预算/危险召回当 A 主结果
- [ ] 无 Part1/Part2/R1–R6 残留依赖

### 2.1 `01`（L0）

知识链：轨→枕→道床→轨距→UAV 可见层→排除项。  
专题：横切草图、俯视指认、三类排除；不背未引标准数值充专家。

### 2.2 `02`（L0）

知识链：扣件→联结件→轨下可见件→可选/排除→RFDD 重叠→难度/发表地板。  
专题：部件族表、vs RFDD 一句（无「首个」）、Speculation 取舍。

### 2.3 `03`（L0）

知识链：part→defect→D0–D5→主 mAP vs 单独报。  
专题：弹条 D0/D1/D3 外观定义、D4 vs 脏污规则、不冒充国标声明。

### 2.4 `04`（L1）

知识链：航高→角度→GSD→像素覆盖→断崖→遮挡→vs 近景→隔离。  
专题：GSD 估算、vs 近景两句、D5 原因三条；不把笔记当飞行许可。

### 2.5 `05`（L1）

知识链：数据文卖点→Sci Data 结构→近邻增量→梯子→停止条件。  
专题：四段各一行、合格/不合格摘要句、弱档决策；venue 不虚构 IF。

### 2.6 `06`（L2）

知识链：预标注→双引擎→修正→计时→五类指标。  
专题：D4 流程图、误差模式字段、违规告警句改写；主指标无告警预算。

### 2.7 `07`（L2）

知识链：稀缺→合成诱惑→披露+曲线→混测纪律→收缩。  
专题：vs RailFOD23 句、曲线解读、刷分红旗。

### 2.8 `08`（L3）

知识链：冻结协议→同协议基线→指标/忽略区→Validation 写法。  
专题：空表表头、合规/违规句、稀缺 vs 合成并列披露意识；未跑训练亦可过概念关。

### 2.9 `09`（L3/L4）

知识链：端到端主链 + A/B 结果拆分 + BLOCKED 采集。  
专题：主链图、A/B 对照表、删 B 引用演练、自采受阻降档（不并入 B）；确认 ACTIVE 仍为 P0_EI。

---

## 3. 检查记录（追加，勿删旧行）

| 日期 | 笔记 | 判定 | 主要缺口／补学指令 | 检查者 |
|---|---|---|---|---|
| （尚无） |  |  |  |  |

---

## 4. 变更规则

- 改知识链或通过标准：先改本文件，再改对应笔记骨架/必学问题，并在第 3 节留行。  
- 2026-09-24：按 Practice 双部模式重建 A 侧 Learning_Notes（铁路 FOUNDATION + 双审计）；废弃旧四份 stub 文件名。  
- 2026-09-24（晚）：用户纠正——`01`–`09` 改对齐 Practice `01_YOLO_Research_Core.md` 单文件骨架；移除 Part1/Part2/R1–R6；过关字段改为节点追问 + 必学问题 + 最小完成证据 + 闭卷串讲。
