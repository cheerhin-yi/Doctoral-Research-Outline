# Paper 1到桥接模块M1的接口

## 输入契约

M1从Paper 1接收：

| 字段 | 含义 | 必需 |
|---|---|---|
| `scene_id` | 独立物理场景ID | 是 |
| `flight_id` | 航次ID | 是 |
| `object_id` | 跨帧/跨视角目标ID | 是 |
| `timestamp` | 图像时间 | 是 |
| `known_or_unknown` | 已知或未知候选标志 | 是 |
| `class_probability` | 已知类概率；未知时可为空 | 否 |
| `open_world_risk` | Paper 1风险输出 | 是 |
| `epistemic_uncertainty` | 认知不确定性 | 是 |
| `box_or_mask` | 目标框或轮廓 | 是 |
| `track_region_id` | 轨道区域ID | 是 |
| `image_reference` | 原图或裁剪索引 | 是 |

相机内参、姿态、RTK、轨道边界与地面控制点由M1的数据层补充，不归Paper 1负责。

## M1输出契约

`object_id, longitudinal_position, lateral_offset, clearance_distance, clearance_interval, encroachment_probability, measurement_valid`

## 版本门槛

在Paper 1字段定义、单位、缺失值规则和坐标约定冻结以前，M1只允许做纸面设计，不允许启动正式实验。
