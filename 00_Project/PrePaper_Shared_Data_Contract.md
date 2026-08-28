# 前置论文与桥接模块共享数据契约

**状态**：ACTIVE GOVERNANCE；当前只冻结前置论文A必需字段，B/M1/M2字段不得反向扩大A的数据工作。

## 1. 数据单元

最小独立统计单元是`scene_id`，不是图像。一个场景包含一次物理布置在多个视角和重复航次中的全部观测。

建议层级：

`scene → placement → flight → observation → object`

## 2. 核心字段

| 字段 | 类型 | 生成阶段 | 说明 |
|---|---|---|---|
| `scene_id` | string | 采集 | 物理布置主键 |
| `flight_id` | string | 采集 | 完整航次主键 |
| `observation_id` | string | 采集 | 图像/关键帧主键 |
| `object_id` | string | 标注 | 跨视角稳定目标主键 |
| `timestamp_utc` | datetime | 采集 | 原始时间戳 |
| `camera_pose` | object | 采集 | RTK位置和相机姿态 |
| `class_label` | enum | 标注 | 六类已知障碍或unknown |
| `bbox_xyxy` | float[4] | 标注/模型 | 像素框 |
| `contact_point_xy` | float[2] | 标注 | 地面接触点 |
| `track_position_norm` | float | 前置A | 归一化横向位置 |
| `calibrated_risk` | float | 前置A/Paper 1 | 校准风险 |
| `epistemic_uncertainty` | float | Paper 1 | 认知不确定性 |
| `measurement_interval` | float[2] | M1 | 侵限距离区间 |
| `reinspection_result` | object | 前置B/M2 | 复检观测与决策 |

## 3. 数据划分规则

- 在抽帧和数据增强之前，按`scene_id`划分训练、校准、测试集；
- 推荐比例为6/3/3个场景，对应50%/25%/25%；
- 同一物体放置、同一航次、相邻帧和增强版本不得跨集合；
- 校准集只拟合校准器、区间和阈值，不参与主检测器选择；
- 测试集在所有方法和阈值冻结前保持不可见；
- 所有论文复用同一划分，禁止为了得到更好结果重新随机拆分。

## 4. 版本规则

数据版本格式：`rail-prepaper-vMAJOR.MINOR`。

- 修改标签或样本归属：增加MAJOR；
- 增加不影响既有样本的新字段：增加MINOR；
- 论文投稿时记录数据版本、配置版本、代码提交和模型权重校验值。

## 5. 统计规则

- 主结果运行3个随机种子；
- 置信区间按`scene_id`聚类Bootstrap；
- 同一场景的多视角和重复航次视为相关观测；
- 同时报告整体结果、最差视角、困难子集和失败案例；
- 不以单个最优随机种子作为论文主结果。
