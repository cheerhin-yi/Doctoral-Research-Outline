# Learning_Notes（练手稿）

按 **P0 EI 对比／协议路线**分块学习。除 `01` 外，主题笔记采用两部分：

1. **第一部分：必须掌握** — 学习目标、知识链、链上说明、练习、必答  
2. **第二部分：我的记录** — 按同一条链填写理解／证据／必答；**过关只查这里**

| 文件 | 用途 |
|---|---|
| [`../Learning_Check_Baseline.md`](../Learning_Check_Baseline.md) | 助手维护的检查基准 |
| [`../Completion_Metrics.md`](../Completion_Metrics.md) | 关卡总门 L0–L4 |
| `00_Unified_Core_Knowledge_Map.md` | 全局导航（不过关） |
| `01_YOLO_Research_Core.md` | L0；**暂保持单部** |
| `02_PyTorch_and_Reproducibility.md` | L1；双部样板 |
| `03_Experiment_Design_and_Uncertainty.md` | L1；主张→实验卡 |
| `04_Small_Object_and_Multiscale.md` | L2；小目标／分辨率轴 |
| `06_Efficiency_and_Deployment.md` | L2；时间预算／计时 |
| `05_Lightweight_Shared_Head.md` | L2 历史候选 |
| `07_Mainline_A_Knowledge_Chain.md` | L3；五方法主链（含 E 已 PASS 口径） |
| `08_Image_Level_Paired_Inference.md` | L3；Stage F 图级配对 |
| `09_Cross_Set_UAVDT_Mapping_and_Related_Tech.md` | L3/L4；跨集映射＋近邻技术词表 |
| `11_EI_Packaging_Neighbor_Failure_Repro.md` | L4；近邻表／失败例／复现附录 |
| `10_ResNet_Core.md` | L0 可选 |
| `Learning_Record_Template.md` | 可选当日备忘 |

## 顺序（写 EI 稿时可并行科研）

1. 读检查基准与 `Current_Stage`  
2. 基础：`01`（单部自检）→ `02`  
3. **P0 优先：** `03` → `04` → `06` → `07` → `08` → **`09` → `11`**  
4. 每块第二部分自评后交给助手检查；`PASSED` 再进下一块  

样板：`02`。`01` 仍单部，待你确认后再改双部。

## 与当前 EI 架构的对齐（2026-09-23）

| EI 稿块 | 主要笔记 |
|---|---|
| 主张／实验卡 | `03` |
| 小目标与分辨率／切片族 | `04`、`07`、`09` 词表 |
| 时序与预算 | `06`、`11`（4090 分列） |
| 图级配对 | `08` |
| 跨集外推与映射冻结 | `09` |
| 近邻表＋失败边界＋复现附录 | `11` |

实验主线下一可检查事项仍是 **EI 包装增量**（见 `Current_Stage`）；学习关卡 **不**替代实验门禁，也 **不**因补笔记而解锁训练。
