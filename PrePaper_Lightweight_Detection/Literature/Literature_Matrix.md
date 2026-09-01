# 练手论文文献矩阵

## 1. 论文索引

| ID | 主题 | 年份 | 论文 | 数据 | 核心改动 | 真实延迟 | 与本文关系 | 状态 | 笔记 |
|---|---|---:|---|---|---|---|---|---|---|
| L1-01 | 小目标/多尺度 | 2024 | LUD-YOLO | UAV航拍检测数据 | 轻量UAV检测结构 | 有速度结果，口径待精读 | 直接近邻，审计与LSM-Head同构性 | SCREENED | 待创建 |
| L1-02 | 小目标/多尺度 | 2025 | A Lightweight Small Object Detection Model for UAV Images Based on Deep Semantic Integration | VisDrone、TinyPerson | 高分辨率/P2与多尺度融合 | 待精读 | C0-1直接证据 | SCREENED | 待创建 |
| L2-01 | 轻量算子 | 2019 | Searching for MobileNetV3 | ImageNet等 | 硬件感知NAS与NetAdapt | 报告硬件延迟 | 轻量设计基础，不是检测头近邻 | SCREENED | 待创建 |
| L2-02 | 架构/训练 | 2024 | YOLOv9 | COCO等 | PGI与GELAN | 有模型效率结果 | 基线谱系，不直接支持唯一头改动 | SCREENED | 待创建 |
| L2-03 | 轻量算子 | 2025 | GlimmerNet | UAV应急图像分类 | 分组空洞深度卷积 | 缺少充分真实端侧检测评价 | 可借鉴算子，但任务不是检测 | SCREENED | 待创建 |
| L2-04 | 轻量YOLO | 2025 | EADI-YOLO | 铁路表面缺陷 | 轻量高效检测模块 | 有效率结果，口径待精读 | 铁路领域近邻，域与任务不一致 | SCREENED | 待创建 |
| L3-01 | 速度/部署 | 2025 | TakuNet | UAV应急图像分类 | 节能CNN与FP16部署 | Jetson/Raspberry Pi | 部署方法参考，不是检测基线 | SCREENED | 待创建 |
| L3-02 | 速度/部署 | 2024 | EUAVDet | VisDrone、UAVDT、SeaDronesSee | 轻量UAV检测器 | Jetson Nano实测 | C0-2直接近邻 | SCREENED | 待创建 |
| L4-01 | 训练效率/复现 | 2026 | Does YOLO Really Need to See Every Training Image in Every Epoch | YOLO训练实验 | 自适应训练样本选择 | 训练加速，不是推理延迟 | 训练成本与公平复现参考 | SCREENED | 待创建 |

状态：`TODO`未核验；`SCREENED`已核验摘要；`READING`精读中；`DONE`已形成证据；`EXCLUDED`已记录排除理由。

## 2. 新颖性冲突表

| ID | 使用P2 | 移除P5 | 跨尺度共享 | 轻量卷积 | 同时报告AP_small与延迟 | 冲突等级 | 决策 |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |

## 3. 方法冻结前必须回答

- [ ] 最近工作是否已有同构的共享P2–P4检测头？
- [ ] 普通P2的精度收益和速度代价分别多大？
- [ ] 移除P5在小目标数据上是否有充分依据？
- [ ] 参数共享是降低参数量，还是也能降低真实延迟？
- [ ] 哪些工作使用相同数据和YOLO版本，可作为直接对照？
- [ ] 如果方法差异很小，能否以精度—速度实证为主而不过度声称算法创新？
