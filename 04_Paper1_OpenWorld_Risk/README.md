# Paper 1：以YOLO为核心的铁路UAV开放环境危险感知与风险告警

> **PAUSED（2026-08-28）**：本目录保留Paper 1未来恢复所需协议和实验设计。当前唯一活动任务为前置论文A，之后为前置论文B；不得依据本目录启动YOLO改进、开放世界或Paper 1正式实验。

暂定题目：**YOLO-Centered Open-Environment Hazard Perception and Risk Alarming for UAV Railway Inspection**。

恢复后的目标是在重新核验的16个弹性研究周内形成可复现的YOLO铁路危险检测主线和完整初稿。YOLO11负责已知危险实时检测及铁路小目标能力；YOLO-World/开放集基线用于补充未见危险候选；轨道解析与侵界关系用于风险告警。前置论文A已经独立承担条件校准，因此Paper 1只复用其接口或做必要开放世界扩展，不重复相同主张。

**贡献边界**：不把YOLO版本替换、轨道中心线/边界、标准轨距换算、距离风险分级、铁路开放集检测或风险校准单独宣称为创新。可能贡献来自铁路UAV数据/协议、YOLO错误驱动的最小适配、开放环境增量价值和完整风险告警证据。参见`../00_Project/Paper1_Research_Alignment.md`与`../01_Literature/Paper1_Novelty_Audit_2026-08-27.md`。

## 文件

- `Project_Charter.md`：范围、主张和完成标准。
- `Dataset_Audit.md`：数据来源、结构、许可和泄漏审计。
- `Known_Unknown_Protocol.md`：开放环境划分和评价规则。
- `Risk_Annotation_Protocol.md`：风险标签定义和复核。
- `EXPERIMENT_PLAN.md`：RQ1–RQ4及YOLO中心证据计划。
- `EXPERIMENT_TRACKER.md`：运行顺序和状态。
- `PAPER_OUTLINE.md`：论文写作骨架。
- `Interfaces/`：向Paper 2和Paper 3的接口。
