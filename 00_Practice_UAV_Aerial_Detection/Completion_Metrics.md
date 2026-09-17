# 练手文掌握与完成指标

本文件是**关卡总门**：某一关全部达标后，才开始下一关。不按「每天做完多少任务」推进。

**块内笔记写法与过关检查**见 [`Learning_Check_Baseline.md`](Learning_Check_Baseline.md)（查笔记**第二部分**；`01` 为单部例外）。

验收：闭卷复述／手算／必答证据；**不得代填**。状态：`TODO` → `LEARNING` → `REVIEWING` → `PASSED`／`REPEAT`。

总入口：[`00_Overview/Current_Stage.md`](../00_Overview/Current_Stage.md)。  
英语并行：[`90_English_Learning/README.md`](../90_English_Learning/README.md)。  
未授权前不新训模型。

---

## 关卡总表

| 关卡 | 名称 | 通过后才能做什么 | 状态 |
|---|---|---|---|
| L0 | 检测链与指标 | 进入 L1 | TODO |
| L1 | 可复现与实验设计 | 进入 L2 | TODO |
| L2 | 小目标／多尺度／时间预算口径 | 进入 L3 | TODO |
| L3 | 主线协议链 + 图级配对推断 | 进入 L4 | TODO |
| L4 | 文献边界与可证伪实验卡 | 讨论主张措辞；可改 Current_Stage 学习相关项 | TODO |

---

## L0 · 检测链与指标

**学习块：** [`Learning_Notes/01_YOLO_Research_Core.md`](Learning_Notes/01_YOLO_Research_Core.md)；按需 [`10_ResNet_Core.md`](Learning_Notes/10_ResNet_Core.md)。

**完成指标：** 见 `01` 与基准 §2.1。

---

## L1 · 可复现与实验设计

**学习块：** `02_PyTorch_and_Reproducibility.md`、`03_Experiment_Design_and_Uncertainty.md`。

**完成指标：** 二者均 PASSED（复现清单、泄漏、**P0 实验卡**、必答）。

---

## L2 · 小目标与时间预算

**学习块：** `04_Small_Object_and_Multiscale.md`、`06_Efficiency_and_Deployment.md`；`05` 历史可选。

**完成指标：** 原图小目标阈值、四手段区分、计时边界、超时率口径；见基准 §2.4–2.5。

---

## L3 · 协议主链与图级统计

**学习块：** `07_Mainline_A_Knowledge_Chain.md`、`08_Image_Level_Paired_Inference.md`。

**完成指标：** 五方法流图、Stage 纪律、能解读 Stage F 主比较 CI／Wilcoxon；见基准 §2.7–2.8。

---

## L4 · 文献边界与可证伪实验卡

近邻边界 + C1/C2 可证伪卡；不强制单文件双部。

---

## 与实验阶段

学习关卡**不替代**实验门；实验是否启动只写在 `Current_Stage`。  
P0 Benchmark A–D/F 已 PASS；E 阻塞；4090 时序未跑。已有 BT／BTD 默认不重跑。
