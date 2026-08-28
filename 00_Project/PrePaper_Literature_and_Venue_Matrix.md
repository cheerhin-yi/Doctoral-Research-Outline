# 前置论文文献与期刊矩阵

**当前只检索前置论文A。** 前置论文B在第13周开始定向检索；M1、M2和Paper 1当前只记录碰撞文献，不展开综述。

## 1. 第1周四个检索簇

| 簇 | 需要回答的问题 | 最低数量 | 当前状态 |
|---|---|---:|---|
| A-L1 检测概率校准 | 目标检测confidence如何校准，强基线是什么 | 5 | 待补齐 |
| A-L2 条件/分组校准 | 条件校准、worst-group或domain calibration如何定义与评价 | 5 | 待补齐 |
| A-L3 UAV视角退化 | 高度、倾角、目标尺寸和模糊如何影响可靠性 | 5 | 待补齐 |
| A-L4 铁路风险筛查 | 铁路障碍、轨道位置和危险筛查已有何种定义 | 5 | 待补齐 |

只有同时服务A1/A2或界定A—Paper 1—M1边界的文献才进入本表。

## 2. 已核验种子

| ID | 簇 | 文献/资源 | 已有内容 | 对A的约束 | 状态 |
|---|---|---|---|---|---|
| A-S01 | 数据 | UAV-RSOD, Scientific Data, 2024 | 315幅原图、轨道掩膜、六类障碍及增强数据 | 按原始物理场景划分；增强同源不得跨集合 | 待复核许可与原图谱系 |
| A-S02 | A-L4 | Lightweight railroad semantic segmentation network and distance estimation for railroad UAV images, 2024 | 轨道分割和点到线距离 | 距离计算不能作为A创新 | 初步核验 |
| A-S03 | A-L4 | Railway Intrusion Risk Quantification with Track Semantic Segmentation and Spatiotemporal Features, 2025 | 标准轨距、横向距离和时空风险 | A必须突出条件可靠性，不重复距离风险 | 初步核验 |
| A-S04 | A-L3 | Decision-oriented multi-altitude UAV-based deep learning framework for railway track and ballast anomaly screening, 2026 | 多高度训练和决策筛查 | 多高度不是创新，高度只作校准条件 | 初步核验 |
| A-S05 | A-L3 | Active Learning for Single-Stage Object Detection in UAV Images, WACV 2024 | UAV检测不确定性聚合与样本选择 | 区分主动学习与部署后概率校准 | 初步核验 |

## 3. 每篇论文记录字段

| 字段 | 必填内容 |
|---|---|
| Citation | 作者、题目、期刊、年份、DOI/官方链接 |
| Research question | 论文真正回答什么 |
| Data/Split | 数据规模、视角、scene/flight划分和泄漏控制 |
| Method | 输入、输出和核心机制 |
| Baselines | 最强基线及公平性 |
| Metrics | NLL/Brier/ECE、最差组或任务指标 |
| Finding | 作者有证据支持的结论 |
| Limitation | 作者承认和本项目识别的失效条件 |
| Collision | 与A1、A2、Paper 1或M1的重叠 |
| Reusable | 可复用基线、指标、代码或数据协议 |

## 4. 三张精读卡片

第1周只选择最接近A的三篇论文精读。每张卡片回答：

1. 它的主要主张和最强证据；
2. 它是否按物理场景隔离数据；
3. 它如何评价最差条件；
4. 它没有回答的铁路UAV可靠性问题；
5. A相对它只新增什么最小证据。

## 5. 后续文献停车场

- 前置B：多视角对应、轨道坐标一致性、不确定性融合；第13周再检索。
- Paper 1：开放集/开放世界铁路检测；A/B完成后再更新。
- M1：相机测量误差传播、区间校准；Paper 1接口稳定后再更新。
- M2/Paper 6：VoI、主动感知和NBV；M1完成后再更新。

停车场条目不计入当前20篇任务，也不安排代码复现。

## 6. 期刊候选

| 工作 | 工作候选 | 状态 |
|---|---|---|
| 前置A | Drones | 投稿当天按硬规则重新核验 |
| 前置B | International Journal of Rail Transportation | 第13周重新检索和核验 |

硬规则：当年JIF大于2.0、最新中科院大类及全部小类均为三区或以上、2020–2025各年度预警名单未出现、学校认可SCIE及分区、范围直接匹配。
