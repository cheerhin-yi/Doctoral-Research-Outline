# 练手论文实验跟踪表

正式实验当前全部`BLOCKED`。新增运行前必须填写假设、唯一变量、数据版本、seed、硬件和停止条件。

| Run ID | 阶段 | 模型 | 目的 | 数据/版本 | Seed | 主要指标 | 状态 | 结果位置/备注 |
|---|---|---|---|---|---:|---|---|---|
| P000 | M0 | B0 | 官方小样例推理与验证 | 框架样例 |  | 输出完整性 | BLOCKED | 阶段3启动 |
| P001 | M0 | B1 | 普通P2结构与张量检查 | 极小样例 |  | shape/参数量 | BLOCKED | 阶段3启动 |
| P010 | M1 | B0 | 正式基线 | 待冻结 |  | mAP/AP_small/延迟 | BLOCKED | 阶段4启动 |
| P011 | M1 | B1 | P2收益和代价 | 待冻结 |  | mAP/AP_small/延迟 | BLOCKED | 阶段4启动 |
| P020 | M2 | B2 | P2–P4消融 | 待冻结 |  | AP_small/GFLOPs | BLOCKED | 阶段5启动 |
| P021 | M2 | M | 共享轻量头 | 待冻结 |  | AP_small/延迟 | BLOCKED | 阶段5启动 |

状态使用：`BLOCKED`、`READY`、`RUNNING`、`DONE`、`FAILED`、`EXCLUDED`。
