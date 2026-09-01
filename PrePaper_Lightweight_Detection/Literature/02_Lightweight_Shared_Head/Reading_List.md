# L2：轻量共享检测头阅读清单

## 本主题要回答

- 跨尺度参数共享是否已有同构方法？
- 参数减少是否同时减少计算和访存开销？
- 哪些轻量算子便于导出且不引入额外模块？

## 阅读清单

| ID | 论文 | 优先级 | 状态 | 重点阅读 | 笔记 |
|---|---|---|---|---|---|
| L2-01 | [Searching for MobileNetV3](Searching%20for%20MobileNetV3.pdf) | SHOULD | SCREENED | 硬件感知搜索、NetAdapt、延迟意识 | 待创建 |
| L2-02 | [YOLOv9](YOLOv9%20-%20Learning%20What%20You%20Want%20to%20Learn%20Using%20Programmable%20Gradient%20Information.pdf) | SHOULD | SCREENED | GELAN、参数利用、模型规模与速度 | 待创建 |
| L2-03 | [GlimmerNet](GlimmerNet%20-%20A%20Lightweight%20Grouped%20Dilated%20Depthwise%20Convolutions%20for%20UAV-Based%20Emergency%20Monitoring.pdf) | SHOULD | SCREENED | 分组空洞深度卷积、参数量、分类任务边界 | 待创建 |
| L2-04 | [EADI-YOLO](EADI-YOLO%20-%20A%20Lightweight%20and%20Efficient%20Model%20for%20Rail%20Surface%20Defect%20Detection.pdf) | MUST | SCREENED | 轻量模块、消融、铁路域差异、结构冲突 | 待创建 |
| L2-05 | 共享检测头直接近邻 | MUST | TODO | 共享范围、算子、消融、冲突 | 待检索 |

## 本主题完成门

- [ ] 至少3篇直接相关论文完成精读；
- [ ] 完成与LSM-Head的结构冲突表；
- [ ] 明确B2到M唯一改变的变量。
