# 前置论文文献与期刊矩阵

## 1. 使用方法

第1周只回答四个问题：已有工作做了什么、没有做什么、我们最小新增什么证据、该证据适合哪个期刊。每读一篇文献增加一行，不写与两个前置研究问题无关的长篇综述。

## 2. 种子文献

| 主题 | 文献/资源 | 已有内容 | 对本项目的约束 |
|---|---|---|---|
| 公共数据 | UAV-RSOD, Scientific Data, 2024 | 315幅原图、轨道掩膜、六类障碍及增强数据 | 只用原始谱系做划分；增强同源样本不得跨集合 |
| 轨道距离 | Lightweight railroad semantic segmentation network and distance estimation for railroad UAV images, 2024 | 轨道分割和点到线距离 | 距离计算本身不能作为前置A创新 |
| 风险量化 | Railway Intrusion Risk Quantification with Track Semantic Segmentation and Spatiotemporal Features, 2025 | 标准轨距换算、横向距离和时空风险 | 前置A必须突出视角条件校准而非简单轨距风险 |
| 多高度筛查 | Decision-oriented multi-altitude UAV-based deep learning framework for railway track and ballast anomaly screening, 2026 | 多高度训练和决策筛查 | 多高度本身不能作为创新；高度只作为可靠性条件变量 |
| UAV不确定性 | Active Learning for Single-Stage Object Detection in UAV Images, WACV 2024 | UAV图像不确定性聚合与样本选择 | 区分主动学习与本项目的部署概率校准 |
| 主动视点 | NeU-NBV, 2023；NBV综述, 2025 | 不确定性驱动的候选视点选择 | 前置B和M2均不得进入候选视点搜索，保留给Paper 6 |

## 3. 必须补齐的文献组

### 前置A

- 目标检测概率校准：temperature scaling、isotonic、classwise calibration；
- 条件/群组校准：domain-conditional、worst-group calibration；
- UAV高度、倾斜角、小目标尺度对置信度可靠性的影响；
- 铁路侵限风险与轨道相对位置建模。

### 前置B

- 多视角目标对应与置信度融合；
- 几何坐标约束的一致性检验；
- 不确定性加权的证据融合；
- 固定二次观测或双航次铁路/UAV验证。

### 桥接M1/M2

- 相机测量误差传播和区间校准；
- 风险敏感选择性预测；
- value of information与成本敏感复检；
- 主动感知与NBV边界。

## 4. 每篇文献的记录字段

| 字段 | 内容 |
|---|---|
| Citation | 作者、题目、期刊、年份、DOI |
| Task | 校准/多视角/测量/复检 |
| Data | 数据规模、视角、是否真实飞行 |
| Method | 方法和输入输出 |
| Split | 是否按场景或航次隔离 |
| Metrics | 主指标与统计方法 |
| Limitation | 作者承认和我们识别的局限 |
| Collision | 与A/B/M1/M2哪一项重叠 |
| Reusable | 可复用基线、指标或实验设计 |

## 5. 期刊候选状态

| 工作 | 当前首选 | 投稿当日硬检查 | 状态 |
|---|---|---|---|
| 前置A | Drones | JIF>2、SCIE、大小类≤3、2020–2025无预警、范围匹配 | 条件候选 |
| 前置B | International Journal of Rail Transportation | 同上 | 条件候选 |
| M1 | 暂不指定 | 模块达到独立论文门槛后再检索 | 不启动期刊选择 |
| M2 | 暂不指定 | 模块达到独立论文门槛后再检索 | 不启动期刊选择 |

中科院分区和预警记录以投稿当日学校正式数据库为准，不以商业聚合网站截图作为最终证明。
