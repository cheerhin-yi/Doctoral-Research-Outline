# Paper 1 Experiment Tracker

状态只使用：TODO、READY、RUNNING、FAILED、COMPLETE、CUT。任何COMPLETE必须有配置、日志和原始指标位置。

| Run ID | Milestone | Purpose | System / Variant | Split | Primary Metrics | Priority | Status | Config/Log/Result | Notes |
|---|---|---|---|---|---|---|---|---|---|
| R000 | M0 | 数据审计与哈希泄漏检查 | Audit | A/B/C | overlap count | MUST | TODO |  |  |
| R001 | M0 | 标签/可视化检查 | Data pipeline | toy | manual QA | MUST | TODO |  |  |
| R002 | M0 | 指标手算与小样本过拟合 | Evaluator + toy model | toy | exact match/loss | MUST | TODO |  |  |
| R003 | M1 | 闭集检测基线 | YOLO11 | main | mAP50–95, Recall | MUST | TODO |  |  |
| R004 | M1 | 第二检测基线 | RT-DETR | main | mAP50–95, Recall | MUST | TODO |  |  |
| R005 | M1 | 开放词汇基线 | YOLO-World | A/B/C | Unknown + detection | MUST | TODO |  |  |
| R006 | M1 | 开放词汇基线 | Grounding DINO | A/B/C | Unknown + detection | MUST | TODO |  |  |
| R007 | M2 | 铁路分割 | SegFormer或冻结备选 | main | mIoU, Dice | MUST | TODO |  |  |
| R008 | M2 | 中心线与铁路几何 | Pixel vs Railway | main | centerline/geometric error | MUST | TODO |  |  |
| R009 | M2 | 风险基线 | Semantic/Geometry/Fusion | A | Macro-F1, high-risk Recall | MUST | TODO |  |  |
| R010 | M2 | 风险校准 | Before/After TS | A | ECE, Brier | MUST | TODO |  |  |
| R011 | M3 | C1几何消融 | Pixel vs Railway | A/B/C | risk + stability | MUST | TODO |  |  |
| R012 | M3 | C2未知消融 | no Unknown | A/B/C | unknown-risk Recall | MUST | TODO |  |  |
| R013 | M3 | 额外特征反解释 | random Unknown | A/B/C | Macro-F1 | MUST | TODO |  |  |
| R014 | M3 | 不确定性消融 | no Calibration | A/B/C | ECE/Brier/Recall | MUST | TODO |  |  |
| R015 | M3 | 完整模型 | Full | A/B/C | all primary metrics | MUST | TODO |  |  |
| R016 | M3 | 重复性 | Key variants seed 2 | main | mean/std | MUST | TODO |  |  |
| R017 | M3 | 重复性 | Key variants seed 3 | main | mean/std | MUST | TODO |  |  |
| R018 | M4 | 模糊/亮度 | Full + baselines | main | degradation curves | MUST | TODO |  |  |
| R019 | M4 | 分辨率/尺度/高度样退化 | Full + baselines | main | degradation curves | MUST | TODO |  |  |
| R020 | M4 | 效率 | Key systems | main | FPS/latency/memory | MUST | TODO |  |  |
| R021 | M4 | 失败分析 | Key systems | main | error taxonomy | MUST | TODO |  |  |
| R022 | M4 | 跨数据集 | Full + baseline | external | task metrics | NICE | TODO |  | 仅许可与映射完成后 |
| R023 | M4 | 额外提示词/阈值敏感性 | OV baselines | appendix | sensitivity | NICE | TODO |  |  |
