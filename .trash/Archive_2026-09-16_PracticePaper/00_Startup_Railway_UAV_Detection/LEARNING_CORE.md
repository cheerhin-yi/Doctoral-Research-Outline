# 合并学习框架：Startup 主线（LEARNING-CORE）

更新日期：2026-09-16（Asia/Shanghai）

本目录是写入用户本地仓库 `00_Startup_Railway_UAV_Detection/` 的**新合并学习枢纽**草案。目标：把原 `00_PrePaper_Lightweight_Detection` 与 `00_Startup_Railway_UAV_Detection` 的学习内容合并进后者，**不删除**现有实验、代码与结果。

## 当前阶段边界

| 项目 | 约定 |
|---|---|
| 当前阶段名 | **LEARNING-CORE**（约 3 周核心学习） |
| 每日投入 | 约 5 小时：默认 **4h 科研学习 + 1h 英语/CET-4** |
| 模型训练 | **三周内默认不做模型训练**；若需训练须单独授权 |
| 旧实验 | 已有 BT1 / BTD1–BTD12 等记录、代码与结果**保留不动**；当前负结果视为归档证据，学习后再讨论实验重设计 |
| 学习后 | 完成 3 周门禁后，再讨论约 **3 个月**实验设计与执行阶段 |
| 本草案作用 | 供复制进本地 Startup 仓库；**不**自动改写仓库其他文件 |

## 两条创新线索（统一学习，分开主张边界）

**线索 A（历史 / 候选）**：轻量共享检测头 / 轻量检测网络知识（LSM-Head）  
小目标与多尺度（P2–P5）、共享 vs 独立头、深度/分组卷积、参数量/FLOPs/显存/延迟、部署。**LSM-Head 本身是历史候选，不是已成立创新。**

**线索 B（当前主线语境）**：时间预算约束下的局部高分辨率分配 / 航拍小目标检测  
切片、坐标恢复、NMS/融合、ROI/选区、oracle vs 可部署信号、全流水线时间预算、均值/p95/超时、强 F1280 基线、数据泄漏与来源分组、忽略区域与评价。**当前负结果为归档证据；实验将在学习后重设计。**

**共同基础**：完整 YOLO 训练/推理链、指标与手算、可复现性、实验设计、小目标失效分析、文献阅读与 novelty 审计。

## 本目录文件

| 文件 | 用途 |
|---|---|
| [Learning_Plan_3_Weeks.md](Learning_Plan_3_Weeks.md) | 21 日日程（目标 / 内容 / 练习 / 必答题 / 验收） |
| [Learning_Notes/00_Unified_Core_Knowledge_Map.md](Learning_Notes/00_Unified_Core_Knowledge_Map.md) | 统一知识地图与旧笔记 00–07 映射 |
| [Learning_Notes/Learning_Record_Template.md](Learning_Notes/Learning_Record_Template.md) | 低负担单次学习记录模板 |
| [English_Parallel_Plan_CET4.md](English_Parallel_Plan_CET4.md) | 至 12 月 CET-4 的并行英语计划 |
| [ASSESSMENT_PROTOCOL.md](ASSESSMENT_PROTOCOL.md) | 助手评估协议（诚实门禁） |
| [ARCHIVE_MANIFEST.md](ARCHIVE_MANIFEST.md) | 归档清单（源未删除） |
| [90_English_Learning/README.md](90_English_Learning/README.md) | 英语支持线更新版入口 |
| [90_English_Learning/Progress_Log.md](90_English_Learning/Progress_Log.md) | 英语进度记录更新版 |

## 与现有仓库的关系

- **保留**：`00_Startup_Railway_UAV_Detection/Experiments/` 全部协议与结果；`11_Datasets` 下数据/权重（本归档默认不复制）。
- **学习笔记**：用户机上已将 PrePaper 笔记 00–06 复制到 Startup 的 `Learning_Notes/`，与 07 并列；本框架提供统一地图与记录模板，不要求删旧稿。
- **PrePaper 目录**：历史材料可保留查阅；LSM-Head 旧阶段要求退出执行，仅作线索 A 学习参考。
- **归档副本**：见 [ARCHIVE_MANIFEST.md](ARCHIVE_MANIFEST.md)；源目录**未被删除**。

## 使用顺序（建议）

1. 读本 README 与 ARCHIVE_MANIFEST，确认边界。  
2. 按 Learning_Plan 日推进；每节课用 Learning_Record_Template 留证。  
3. 对照 Knowledge Map 定位节点；对照 ASSESSMENT_PROTOCOL 接受日检/周门/三周门。  
4. 每天 1h 英语按 English_Parallel_Plan 与 `90_English_Learning/` 执行。  
5. 三周门通过后，再讨论 3 个月实验方案——**本框架不宣称用户已通过任何门。**

## 硬规则（LEARNING-CORE）

- 不以“看过 / AI 讲解过”代替闭卷复述与手算。  
- AI 可讲解与评分，**不得代填**用户答案。  
- 不把历史负结果说成已成立方法；不把 LSM-Head 标成既定未来方向。  
- 不启动新模型训练/正式实验，除非用户单独授权并改写阶段文件。
