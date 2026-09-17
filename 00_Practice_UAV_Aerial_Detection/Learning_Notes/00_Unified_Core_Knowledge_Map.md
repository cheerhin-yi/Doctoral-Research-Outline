> **格式迁移（2026-09-17）：** 本文件尚未完全改写成「第一部分知识链＋第二部分记录」。学习本块前请先读 [`NOTE_FORMAT.md`](NOTE_FORMAT.md) 与 [`../Learning_Check_Baseline.md`](../Learning_Check_Baseline.md)。记录请仍按知识链节点整理；也可要求助手先把本文件改成与 `01`／`02` 相同结构再开始。
>

# 统一核心知识地图

更新日期：2026-09-16  
用途：把共同基础与两条创新线索收成一张图；标明**历史 / 候选 / 已验证证据**边界；映射旧笔记 00–07。  
本图是导航，不是已通过证明。

---

## 证据边界图例

| 标记 | 含义 |
|---|---|
| **FOUNDATION** | 研究共同基础；必须掌握，不构成论文 novelty |
| **HISTORICAL** | 曾作为方向或材料保留；可学，不作为当前执行前提 |
| **CANDIDATE** | 可讨论、可被实验证伪的结构或机制；**尚未成立** |
| **ARCHIVED_EVIDENCE** | 已完成运行/审查留下的事实（含负结果）；可引用为证据，**不等于**下一方法已成立 |
| **VALIDATED_PROTOCOL** | 已核验的程序/语义（如部分评价器构造样例）；仍可能有范围限制 |
| **BLOCKED / HOLD** | 未获准执行或整体暂缓；学习阶段不擅自解锁训练 |

---

## 总结构

```text
[FOUNDATION] 共同基础
  YOLO 训推链 · 指标手算 · PyTorch/复现 · 实验设计 · 失效分析 · 文献/novelty 审计
        │
        ├─► [HISTORICAL / CANDIDATE] 线索 A：轻量共享检测头知识（LSM-Head）
        │     小目标多尺度 · 共享vs独立 · DW/Group · Params/FLOPs/Mem/Latency · 部署
        │     ※ LSM-Head = 历史候选，非已建立创新
        │
        └─► [CANDIDATE context + ARCHIVED_EVIDENCE] 线索 B：时间预算局部高分辨率
              切片/坐标 · NMS/融合 · ROI/选区 · oracle vs 可部署
              全流水线预算 · mean/p95/超时 · F1280 强基线
              来源分组/泄漏 · ignore/评价
              ※ 当前负结果与书面否决 = 归档证据；实验待学习后重设计
```

---

## A. 共同基础（FOUNDATION）

| 节点 ID | 知识节点 | 最少复述 | 最小证据 | 旧笔记映射 |
|---|---|---|---|---|
| F1 | 完整 YOLO 检测链 | 输入→BB→Neck→Head→训/推分叉 | 结构图 + 闭卷口述 | `01_YOLO`；`07` 链1 |
| F2 | 多尺度特征与 stride | P2–P5 尺寸与职责 | 特征图尺寸手算 | `01`；`04` |
| F3 | 损失 / 解码 / NMS | 分配、解码、去重顺序 | IoU + NMS 手算 | `01` |
| F4 | 指标 | IoU、P/R、AP、mAP、错误类型 | 构造样例手算 | `01`；`07` |
| F5 | PyTorch 训练链 | DataLoader→…→checkpoint | 逐行标注最小循环 | `02` |
| F6 | 可复现 | seed/环境/配置/Run ID/ckpt | 复现清单 | `02` |
| F7 | 划分与泄漏 | 来源/邻帧/增强副本 | 泄漏案例 + 重划分规则 | `02`；`03`；`07` 链3 |
| F8 | 实验设计 | 主张→假设→唯一变量→门 | 一张实验卡 | `03` |
| F9 | 小目标失效分析 | 现象→证据→原因→是否改结构 | ≥2 案例判断链 | `04`；`01` |
| F10 | 文献与 novelty 审计 | 近邻覆盖、差异、可证伪点 | 迷你审计卡 | 方法论文 + Startup Literature |
| F11 | 残差/CBS 直觉（可选） | 残差为何利于训练 | 短复述即可 | `00_ResNet_Core` |

Week1 主打 F1–F7；Week2 强化 F2/F9 并接入线索 A；Week3 强化 F8/F10 并接入线索 B。

---

## B. 线索 A — 轻量共享检测头（HISTORICAL / CANDIDATE）

| 节点 ID | 知识节点 | 边界 | 旧笔记 |
|---|---|---|---|
| A1 | 小目标像素尺寸与覆盖 | FOUNDATION∩A | `04` |
| A2 | P2–P5 职责与加层代价 | FOUNDATION∩A | `04` |
| A3 | 独立头 vs 共享头边界 | **CANDIDATE 结构知识** | `05` |
| A4 | 通道对齐与尺度独立输出层 | CANDIDATE | `05` |
| A5 | 深度可分离 / 分组卷积 | CANDIDATE 工具 | `05` |
| A6 | 参数量 / FLOPs 手算 | FOUNDATION∩A | `05`；`06` |
| A7 | 延迟 / 显存 / 部署协议 | FOUNDATION∩A | `06` |
| A8 | LSM-Head 历史方案记忆 | **HISTORICAL CANDIDATE**；非当前执行 novelty | `05`；PrePaper Research_Plan |

**明确声明**：学习 A3–A8 是为了具备结构与效率判断力，以及阅读相关文献；**不**把 LSM-Head 设为已定未来方向，也**不**在 LEARNING-CORE 阶段实现/训练该头。

---

## C. 线索 B — 时间预算局部高分辨率（当前语境 + 归档证据）

| 节点 ID | 知识节点 | 边界 | 旧笔记 / 材料 |
|---|---|---|---|
| B1 | 切片、重叠、边界截断 | FOUNDATION∩B | `07` 链2；`04` |
| B2 | 坐标恢复与缩放顺序 | FOUNDATION∩B | `07` 练习2 |
| B3 | 分片合并 / NMS / 融合 | FOUNDATION∩B | `07`；效率笔记 |
| B4 | ROI / 选区策略 | CANDIDATE 问题设定 | `07` 链5 |
| B5 | Oracle vs 可部署信号 | **硬边界**（概念必须过） | `07` 练习3 |
| B6 | 端到端时间预算链 | FOUNDATION∩B | `07` 链4；`06` |
| B7 | mean / p95 / 超时率 | FOUNDATION∩B | `06`；`07` |
| B8 | 强 F1280 基线角色 | **ARCHIVED_EVIDENCE**（对照事实） | BTD9 等实验记录 |
| B9 | 来源分组与泄漏 | FOUNDATION∩B | `03`；`07` 链3 |
| B10 | Ignore / others / 有效真值 | FOUNDATION∩B；（部分）VALIDATED_PROTOCOL | `07` 练习1；A0-07 等 |
| B11 | 已归档诊断与负结果 | **ARCHIVED_EVIDENCE**；学习后重设计 | BTD1–12、BT1 归档 |

**明确声明**：B8/B11 的数字与结论保持原实验记录口径；学习阶段只用于理解失败模式与评价纪律，**不重跑、不把负结果改写成正 novelty**。

---

## D. 旧笔记 00–07 → 新结构映射

| 旧文件 | 主要进入 | 学习阶段使用方式 |
|---|---|---|
| `00_ResNet_Core.md` | F11 | 可选补残差直觉 |
| `01_YOLO_Research_Core.md` | F1–F4 | Week1 主教材；S0-01 类缺口在此补 |
| `02_PyTorch_and_Reproducibility.md` | F5–F7 | Week1；正式训练前必须过 |
| `03_Experiment_Design_and_Uncertainty.md` | F7–F8、B9 | Week1 末 + Week3 |
| `04_Small_Object_and_Multiscale.md` | F2、F9、A1–A2、B1 | Week2 核心 |
| `05_Lightweight_Shared_Head.md` | A3–A6、A8 | Week2；标 HISTORICAL/CANDIDATE |
| `06_Efficiency_and_Deployment.md` | A6–A7、B6–B7 | Week2 末 + Week3 |
| `07_Mainline_A_Knowledge_Chain.md` | B1–B7、B9–B10、F1/F4 | Week3 核心；练习题保留本人作答 |

用户机上 00–06 已复制进 Startup `Learning_Notes/` 与 07 并列；新作答用 `Learning_Record_Template`，不必删旧稿。

---

## E. 与阶段的耦合

| 阶段 | 知识焦点 | 禁止 |
|---|---|---|
| LEARNING-CORE（本 3 周） | F 全开；A 作历史候选理解；B 作主线概念与归档复盘 | 默认禁止新模型训练；禁止把 A8 写成既定方向 |
| 学习后讨论 | 用 F8+F10+B 综合产出 3 个月实验议程 | 讨论 ≠ 自动开工 |
| 未来实验期（待定） | 按新冻结协议执行；可重用归档证据作对照 | 不得静默删除失败 Run |

---

## F. 自检问题（地图级）

1. 我能否不看资料画出“基础 → 线索 A / B”分叉，并标对边界词？  
2. 我是否仍把 LSM-Head 说成“我们的创新”？（若是 → 纠正为历史候选）  
3. 我是否能指认至少一项 ARCHIVED_EVIDENCE 及其**不能**支持的主张？
