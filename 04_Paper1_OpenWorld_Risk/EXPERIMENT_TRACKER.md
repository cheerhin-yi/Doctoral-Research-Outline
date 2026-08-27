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
| R008 | M2 | 空间表示真值几何比较 | pixel/centerline/boundary/metric/local-width/BEV | matched scenes | variance, rank, monotonicity | MUST | TODO |  | 普通缩放不得冒充高度变化 |
| R009 | M2 | 轨道预测误差传播 | GT geometry vs predicted geometry | matched scenes | geometry error, risk degradation | MUST | TODO |  |  |
| R010 | M2 | H1风险预测比较 | all spatial representations | scene/height split | AUPRC, high-risk Recall, shift drop | MUST | TODO |  |  |
| R011 | M2 | H1重复与决策门 | strongest baselines | scene/height split | effect mean/std | MUST | TODO |  | H1无稳定信号则停止扩大H2/H3 |
| R012 | M3 | H2条件化融合 | unknown×clearance vs simple fusion | A/B/C | unknown high-risk AUPRC/Recall | MUST | TODO |  | 仅H1通过后运行 |
| R013 | M3 | H2反解释 | Unknown-only/Geometry-only/random Unknown | A/B/C | false alarms, AUPRC | MUST | TODO |  |  |
| R014 | M3 | H3风险事件校准 | before/after TS | A/B/C | ECE/Brier/NLL/top-k hit | MUST | TODO |  | 仅作辅助可靠性验证 |
| R015 | M3 | 最小通过系统 | 仅保留有效组件 | A/B/C | all retained metrics | MUST | TODO |  | 不默认存在Full Model |
| R016 | M3 | 重复性 | Key variants seed 2 | main | mean/std | MUST | TODO |  |  |
| R017 | M3 | 重复性 | Key variants seed 3 | main | mean/std | MUST | TODO |  |  |
| R018 | M4 | 模糊/亮度 | Full + baselines | main | degradation curves | MUST | TODO |  |  |
| R019 | M4 | 匹配高度/分辨率/轻度视角变化 | retained variants + all geometry baselines | matched scenes | stability and risk curves | MUST | TODO |  | 记录真实复采/重投影/仅图像退化的证据等级 |
| R020 | M4 | 效率 | Key systems | main | FPS/latency/memory | MUST | TODO |  |  |
| R021 | M4 | 失败分析 | Key systems | main | error taxonomy | MUST | TODO |  |  |
| R022 | M4 | 跨数据集 | Full + baseline | external | task metrics | NICE | TODO |  | 仅许可与映射完成后 |
| R023 | M4 | 额外提示词/阈值敏感性 | OV baselines | appendix | sensitivity | NICE | TODO |  |  |
