# 练手文掌握与完成指标

本文件是**学习推进的唯一指标表**：某一关全部达标后，才开始下一关。不按「每天做完多少任务」推进。

验收由助手按闭卷复述／手算／必答证据判定；**不得代填**。状态：`TODO` → `LEARNING` → `REVIEWING` → `PASSED` / `REPEAT`。

总入口仍是 [`00_Overview/Current_Stage.md`](../00_Overview/Current_Stage.md)（学习＋实验统一在那里更新）。

每日记录：复制 [`Learning_Notes/Learning_Record_Template.md`](Learning_Notes/Learning_Record_Template.md) 为 `LR_日期_主题.md`。

英语并行：见 [`90_English_Learning/README.md`](../90_English_Learning/README.md)（约 1h／日，对齐当前关卡主题；12 月 CET-4 日期待确认）。

三周量级为目标节奏，**以本表通过为准**，可快可慢。未授权前不新训模型。

---

## 关卡总表

| 关卡 | 名称 | 通过后才能做什么 | 状态 |
|---|---|---|---|
| L0 | 检测链与指标（原 S0-01 核心） | 进入 L1 | TODO |
| L1 | 可复现与实验设计 | 进入 L2 | TODO |
| L2 | 小目标／多尺度／轻量结构（历史候选知识） | 进入 L3 | TODO |
| L3 | 切片／时间预算／数据与评价纪律 | 进入 L4 | TODO |
| L4 | 文献边界与可证伪实验卡 | 讨论三个月实验与主张更新；可改 Current_Stage | TODO |

---

## L0 · 检测链与指标

**学习内容（用这些笔记）：**
- [`Learning_Notes/01_YOLO_Research_Core.md`](Learning_Notes/01_YOLO_Research_Core.md)
- [`Learning_Notes/00_ResNet_Core.md`](Learning_Notes/00_ResNet_Core.md)（按需）
- [`Learning_Notes/07_Mainline_A_Knowledge_Chain.md`](Learning_Notes/07_Mainline_A_Knowledge_Chain.md) 第 1 条链

**完成指标（须全部满足）：**
1. 闭卷讲清：输入→Backbone→Neck→Head→训练分支／推理分支→评价。
2. 自绘结构图，每节点有输入／处理／输出。
3. 独立完成一组 IoU、Precision／Recall、简化 NMS 手算，步骤可复查。
4. 能区分漏检／误检／定位偏差／重复框，并各举一例映射到结构环节。
5. 必答（书面）：①训练时为何通常不做 NMS？②P3 与 P5 更适合什么尺度？③「能跑 predict」为何不等于懂检测链？

**英语对齐：** EL 检测链＋指标术语（见英语 README 当前模块）。

---

## L1 · 可复现与实验设计

**学习内容：**
- [`Learning_Notes/02_PyTorch_and_Reproducibility.md`](Learning_Notes/02_PyTorch_and_Reproducibility.md)
- [`Learning_Notes/03_Experiment_Design_and_Uncertainty.md`](Learning_Notes/03_Experiment_Design_and_Uncertainty.md)

**完成指标：**
1. 闭卷复述训练环：data→forward→loss→backward→optimizer→validation→checkpoint。
2. 写出最小复现清单（环境、seed、配置、数据版本、Run ID、日志）。
3. 能说明至少一种来源／增强／邻帧泄漏，并给出不泄漏划分规则。
4. 能写一张「主张→假设→唯一变量→停止条件」空白实验卡（不要求已跑实验）。
5. 必答：①验证为何不 backward？②测试集调阈值破坏了什么？③增强图为何不一定是独立样本？

---

## L2 · 小目标／多尺度／轻量结构（历史候选）

**学习内容：**
- [`Learning_Notes/04_Small_Object_and_Multiscale.md`](Learning_Notes/04_Small_Object_and_Multiscale.md)
- [`Learning_Notes/05_Lightweight_Shared_Head.md`](Learning_Notes/05_Lightweight_Shared_Head.md)（**历史候选，非已定创新**）
- [`Learning_Notes/06_Efficiency_and_Deployment.md`](Learning_Notes/06_Efficiency_and_Deployment.md)

**完成指标：**
1. 给定 640 输入，能估算 P2–P5 特征图尺寸与小框覆盖。
2. 能说明共享头 vs 独立头的边界，并明确表述「LSM-Head＝历史候选，不是当前必须实现」。
3. 能解释 Params／GFLOPs／延迟／p95／超时率差别；写出整帧测速应包含的环节清单。
4. 必答：①只提高输入分辨率与增加 P2 有何不同？②为何不能用 GFLOPs 代替端到端延迟？③学习轻量结构的目的是什么（权衡理解，不是默认采用）？

---

## L3 · 切片／时间预算／数据与评价纪律

**学习内容：**
- [`Learning_Notes/07_Mainline_A_Knowledge_Chain.md`](Learning_Notes/07_Mainline_A_Knowledge_Chain.md)（切片、选区、ignore、计时）
- 按需查阅归档实验报告（只读）：`99_Attachments/Archive_2026-09-16_PracticePaper/`

**完成指标：**
1. 完成 07 中三道坐标／ignore／oracle 练习（本人作答）。
2. 闭卷说明：GT-oracle 选区为何不能当部署效果；删除 ignore 正标签≠区域被忽略。
3. 能画出／写出全流水线计时边界，并解释 mean vs p95 vs 超时率。
4. 能用自己的话复述：F1280 强简单基线对「区域机制」主张的压力（引用归档证据口径，不编数字）。
5. 必答：①切片框还原顺序错了会出现什么？②diag／cal 开发集为何不能冒充独立测试？③当前负结果对下一阶段实验意味着什么？

---

## L4 · 文献边界与可证伪实验卡

**学习内容：**
- [`Literature/Literature_Matrix.md`](Literature/Literature_Matrix.md)（已有近邻）
- [`Literature/Mainline_A_Prior_Work_Comparison.md`](Literature/Mainline_A_Prior_Work_Comparison.md)
- [`Research_Plan.md`](Research_Plan.md)

**完成指标：**
1. 用自己的话写出练手文当前边界（单目 RGB、已知类、时间预算；轨道走廊退出方法前提）。
2. 列出至少 3 个直接近邻及「已被覆盖／仍可能缺口」（不要求新审计 PASS）。
3. 提交 1 份可证伪实验卡：主张一句、对照、唯一变量、成功／失败标准、与近邻差异。
4. 明确两条线索：轻量共享头＝历史候选；时间预算局部高分辨率＝待重设计实验的主线语境。
5. 与助手讨论后，才能更新 `Current_Stage` 进入「三个月实验」相关事项。

---

## 与实验阶段的关系

- 学习关卡 **不替代** 实验门；实验是否启动只写在 `Current_Stage`。
- 已有 BT1／BTD 等结果在归档与本目录 `Experiments/` 中保留，**默认不重跑**。
- L4 通过后：再定主张×投入方向，并规划三个月实验（另开阶段条目）。
