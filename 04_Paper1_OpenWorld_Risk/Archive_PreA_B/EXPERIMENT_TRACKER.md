# Paper 1 Experiment Tracker

> **PAUSED（2026-08-28）**：不得把本表任何Run改为READY/RUNNING。当前实验状态只在`../00_Project/PrePaper_Experiment_Registry.csv`维护；Paper 1恢复前需重新审计并重编号必要Run。

状态只使用：TODO、READY、RUNNING、FAILED、COMPLETE、CUT。任何COMPLETE必须有配置、日志和原始指标位置。

| Run ID | Milestone | Purpose | System / Variant | Split | Primary Metrics | Priority | Status | Config/Log/Result | Notes |
|---|---|---|---|---|---|---|---|---|---|
| R000 | M0 | 数据审计与哈希泄漏检查 | Audit | A/B/C | overlap count | MUST | TODO |  |  |
| R001 | M0 | 标签/可视化检查 | Data pipeline | toy | manual QA | MUST | TODO |  |  |
| R002 | M0 | 指标手算与小样本过拟合 | Evaluator + toy model | toy | exact match/loss | MUST | TODO |  |  |
| R003 | M1 | YOLO主基线 | YOLO11n | main | mAP50–95, size-stratified Recall, FPS | MUST | TODO |  |  |
| R004 | M1 | YOLO规模对照 | YOLO11s/m | main | accuracy-speed-memory | MUST | TODO |  | 选择一个后续固定规模 |
| R005 | M1 | 第二家族参考 | RT-DETR | main | mAP50–95, Recall, FPS | SHOULD | TODO |  | 仅交叉验证，不决定主线 |
| R006 | M1 | YOLO开放词汇参考 | YOLO-World | A/B/C | known/unknown detection | MUST | TODO |  | 与闭集YOLO分开解释预训练差异 |
| R007 | M1 | YOLO失败分层 | frozen YOLO baseline | main | size/height/occlusion/background errors | MUST | TODO |  | 决定R008唯一候选改动 |
| R008 | M2 | YOLO最小铁路适配 | one preregistered change | main | small/hazard Recall + efficiency | MUST | TODO |  | 只能选择一个改动方向 |
| R009 | M2 | YOLO改动反解释 | original/equal-compute/control | main | effect vs cost | MUST | TODO |  | 排除尺寸/epoch/参数扩张 |
| R010 | M2 | YOLO关键重复 | retained variants seeds 2/3 | main | mean/std | MUST | TODO |  | 无稳定收益则CUT改动 |
| R011 | M3 | 开放集/异常候选基线 | one verified baseline | A/B/C | Unknown Recall, FPR | MUST | TODO |  |  |
| R012 | M3 | 开放环境增量 | closed YOLO vs candidate supplement | A/B/C | known/unknown + candidate load | MUST | TODO |  |  |
| R013 | M3 | 轨道解析/运行区域 | one frozen parser | main | mIoU/Dice/zone quality | MUST | TODO |  | 只服务风险告警 |
| R014 | M3 | 风险告警增量 | detection/category/zone/distance | A/B/C | high-risk AUPRC/Recall, alarms/image | MUST | TODO |  | 几何表示为支撑消融 |
| R015 | M3 | 风险校准/复检 | before/after TS | A/B/C | ECE/Brier/NLL/top-k hit | SHOULD | TODO |  | 无实际收益则CUT |
| R016 | M3 | 重复性 | Key variants seed 2 | main | mean/std | MUST | TODO |  |  |
| R017 | M3 | 重复性 | Key variants seed 3 | main | mean/std | MUST | TODO |  |  |
| R018 | M4 | 模糊/亮度 | Full + baselines | main | degradation curves | MUST | TODO |  |  |
| R019 | M4 | 尺寸/高度/分辨率/视角变化 | YOLO + retained modules | stratified scenes | detection/open/risk degradation | MUST | TODO |  | 几何稳定性只作风险诊断 |
| R020 | M4 | 效率 | Key systems | main | FPS/latency/memory | MUST | TODO |  |  |
| R021 | M4 | 失败分析 | Key systems | main | error taxonomy | MUST | TODO |  |  |
| R022 | M4 | 跨数据集 | Full + baseline | external | task metrics | NICE | TODO |  | 仅许可与映射完成后 |
| R023 | M4 | 额外提示词/阈值敏感性 | OV baselines | appendix | sensitivity | NICE | TODO |  |  |
