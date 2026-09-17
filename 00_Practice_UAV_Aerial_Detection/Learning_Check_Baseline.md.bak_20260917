# 练手文学习检查基准（助手维护）

路径：`00_Practice_UAV_Aerial_Detection/Learning_Check_Baseline.md`  
更新日期：2026-09-17。  
维护者：助手（Doctoral-Research-Outline）。用户完成某块笔记**第二部分**后提交检查；**未达标不得进入下一块／下一关**。

权威关系：
- 当前科研唯一事项仍以 `00_Overview/Current_Stage.md` 为准（EI 稿等）。
- 学习推进以本文件 + `Completion_Metrics.md` 为准。
- 笔记写法：每篇分「第一部分知识链教材」与「第二部分个人记录」；过关只查第二部分。

判定：`TODO` → `LEARNING` → `REVIEWING` → `PASSED` / `REPEAT`。  
助手**不得代填**用户作答；可只写「助手检查区」。

---

## 0. 总规则

1. 检查对象：对应主题笔记的**第二部分**（理解／证据／必答初稿）。
2. 第一部分是教材与标准，不把「抄写第一部分」当通过。
3. 必须能**沿知识链闭卷串讲**，知识点不能只会孤立名词。
4. 练习任务要有可复查证据（手算步骤、图、代码路径、输出摘要）。
5. 必答题：保留初稿；订正另写。初稿空白或明显代写 → `REPEAT`。
6. 同一关卡内多块笔记：**建议顺序**如下；写明「并行」的除外。关卡之间仍按 L0→L4。

---

## 1. 块顺序（练手文 Learning_Notes）

| 顺序 | 笔记 | 关卡 | 状态 |
|---|---|---|---|
| 1 | `01_YOLO_Research_Core.md` | L0 | TODO |
| 2 | `10_ResNet_Core.md`（按需，可与 01 并行） | L0 可选 | TODO |
| 3 | `02_PyTorch_and_Reproducibility.md` | L1 | TODO |
| 4 | `03_Experiment_Design_and_Uncertainty.md` | L1 | TODO |
| 5 | `04_Small_Object_and_Multiscale.md` | L2 | TODO |
| 6 | `06_Efficiency_and_Deployment.md` | L2 | TODO |
| 7 | `05_Lightweight_Shared_Head.md`（历史候选，非必须实现） | L2 | TODO |
| 8 | `07_Mainline_A_Knowledge_Chain.md` | L3 | TODO |
| — | 文献与实验卡（见 Completion_Metrics L4） | L4 | TODO |

`00_Unified_Core_Knowledge_Map.md` 为导航，**不做**单独过关笔记。

---

## 2. 分块检查清单

### 2.1 `01_YOLO_Research_Core`（L0）

**知识链：** 输入图 → Backbone → Neck(多尺度) → Head → 训练分支／推理分支 → IoU/P/R/NMS 评价 → 误差映射回结构  

| 检查项 | 通过标准 |
|---|---|
| 链串讲 | 闭卷按链讲清，不跳步、不把 NMS 说成训练损失 |
| 结构图 | 自绘；每节点有输入／处理／输出 |
| 手算 | 至少一组 IoU + P/R + 简化 NMS，步骤可复查 |
| 误差映射 | 漏检／误检／定位偏／重复框各一例，并指到链上环节 |
| 必答 | Completion_Metrics L0 三题有本人初稿且实质正确或订正到位 |

关卡 L0 还要求：若跳过 ResNet，须在 01 中能解释「残差／深层特征」到 YOLO backbone 的直觉（可短）。

### 2.2 `02_PyTorch_and_Reproducibility`（L1 块一）

**知识链：** 数据与标签 → Dataset/DataLoader → forward → loss → backward/optimizer → validation → checkpoint 与日志／seed  

| 检查项 | 通过标准 |
|---|---|
| 链串讲 | 闭卷讲清张量如何流过训练与验证 |
| 最小循环 | 对伪代码逐行标注 shape／是否产生梯度／train·eval 差异 |
| 复现清单 | 含环境、seed、配置、数据版本、Run ID、日志、权重路径 |
| 泄漏 | 至少一种来源／邻帧／增强泄漏 + 不泄漏划分规则 |
| 必答 | 见该笔记第一部分必答题；初稿完整 |

### 2.3 `03_Experiment_Design_and_Uncertainty`（L1 块二）

**知识链：** 主张 → 可证伪假设 → 唯一变量 → 对照 → 停止条件 → 不确定度／负结果  

| 检查项 | 通过标准 |
|---|---|
| 实验卡 | 一张空白卡字段齐全（不要求已跑） |
| 公平性 | 能指出「只加强新方法调参」为何不公平 |
| 必答 | 笔记内必答题通过 |

L1 关卡：`02` 与 `03` 均 `PASSED` 后，才把 `Completion_Metrics` 中 L1 标为可进入 L2。

### 2.4 L2 块（`04`／`06`／`05`）

按各笔记知识链检查；`05` 必须写明「历史候选、非当前必做」。指标见 `Completion_Metrics` L2。

### 2.5 L3 块（`07`）

切片坐标 → 融合／NMS → 选区 vs oracle → 整帧计时（mean／p95／超时）→ 开发集纪律。指标见 Completion_Metrics L3。

### 2.6 L4

不强制单文件笔记格式；以实验卡 + 近邻边界表述为准（Completion_Metrics L4）。

---

## 3. 检查记录（追加，勿删旧行）

| 日期 | 笔记 | 判定 | 主要缺口／补学指令 | 检查者 |
|---|---|---|---|---|
| （尚无） |  |  |  |  |

---

## 4. 变更规则

- 改知识链节点或通过标准：先改本文件，再改对应笔记第一部分，并在本表第 3 节留一行说明。
- 用户要求降低／提高标准：写入第 3 节并改状态，不静默放宽。
