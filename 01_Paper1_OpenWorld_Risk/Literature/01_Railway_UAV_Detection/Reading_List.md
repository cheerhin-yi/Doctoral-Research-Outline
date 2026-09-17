# T1：铁路UAV与小目标检测阅读清单

## 本主题要回答

- 铁路UAV图像中哪些失败是普通YOLO尚未解决的？
- 小目标、高度、遮挡和复杂背景如何评价？
- 一个YOLO改动需要什么证据才能进入Paper 1？
- 实时性和危险Recall怎样权衡？

## 阅读清单

| ID | 论文 | 优先级 | 状态 | 重点阅读 | 笔记 |
|---|---|---|---|---|---|
| T1-01 | UAV imagery based potential safety hazard evaluation for high-speed railroad using Real-time instance segmentation | MUST | SCREENED | 数据、铁路解析、危险评价和实时性 | 待创建 |
| T1-02 | 铁路UAV小目标检测最近工作 | MUST | TODO | 小目标定义、YOLO基线、分层评价 | 待检索 |
| T1-03 | YOLO11或同代检测器的官方/方法资料 | MUST | TODO | 结构、训练、规模与速度 | 待检索 |
| T1-04 | [CSEANet](CSEANet%20-%20Cross-Stage%20Enhanced%20Aggregation%20Network%20for%20Detecting%20Surface%20Bolt%20Defects%20in%20Railway%20Steel%20Truss%20Bridges.pdf) | MUST | SCREENED | UAV铁路桥螺栓、小目标、滑窗、聚合结构、消融和速度 | 待创建 |

## 本主题完成门

- [ ] 至少5篇直接相关论文完成精读；
- [ ] 能列出铁路UAV检测的主要失败类型；
- [ ] 明确YOLO改动是否真的需要；
- [ ] 提取可复用的数据划分、分层指标和效率报告方式。
## 主线A审计交叉入口（2026-09-10）

仅维护文献，不改变Paper 1阶段门或精读完成数，不复制正文。

- [W-0001 UAV-RSOD主审计](../../../00_Practice_UAV_Aerial_Detection/Literature/audits/W-0001_Audit.md)：Reference Only／SCREENED；原图框、来源组与分割用途需数据审计，不作为未知或风险标签。
- [W-0006 RVGC-YOLO主审计](../../../00_Practice_UAV_Aerial_Detection/Literature/audits/W-0006_Audit.md)：Reference Only／SCREENED；已知检测与端侧计时口径参考。

2026-09-10 W-0001来源补证：原图框／来源组仍Unknown；见[唯一补证记录](../../../00_Startup_Railway_UAV_Detection/Experiments/A0-02_Data_Gap_Followup.md)。不据此开启P1学习或实验。
