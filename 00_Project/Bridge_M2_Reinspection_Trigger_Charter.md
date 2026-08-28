# 桥接M2研究章程：风险与测量不确定性驱动的复检触发

**状态**：BLOCKED；Paper 1和M1接口稳定前只保留边界，不开展学习或实验。

## 1. 角色

M2接收Paper 1开放世界风险和M1物理测量不确定性，回答“是否值得获取一次固定复检观测”。它不回答“去哪里看”和“如何到达”。

## 2. 输入契约

- Paper 1：`semantic_status, risk_probability, epistemic_uncertainty`
- M1：`intrusion_probability, clearance_interval_width, measurement_valid`
- 任务：`reinspection_time_s, reinspection_energy_wh`
- 历史配对观测：首次和复检后的实际风险损失。

## 3. 正式观测价值

`VoI = expected_loss_reduction - lambda_time * time_cost - lambda_energy * energy_cost`

当`VoI > 0`且任务预算允许时触发复检。危险漏判损失必须高于普通误报损失，权重在实验前冻结。

## 4. 输出契约

- `object_id`
- `expected_risk_reduction`
- `reinspection_priority`
- `trigger_reinspection`
- `stop_reason`

## 5. 基线与指标

基线：从不、全部、随机、置信度、风险、测量区间单变量触发。

指标：危险FNR、未知候选验证率、复检比例、单位时间/能耗风险下降、不同预算下的效用曲线。

## 6. 模块验收

- 复检比例不超过50%时达到全部复检至少95%的危险Recall；
- 同预算下优于三个单变量触发器；
- 已知、未知和测量无效三类场景均有单独结果；
- 输出可直接作为Paper 6的触发基线。

## 7. 独立论文门槛

只有在真实时间/能耗成本下仍有稳定收益、且新增开放世界和物理测量证据时才升级。若达不到门槛，M2作为Paper 6模块，不增加论文数量。

## 8. 不得侵入Paper 6的内容

候选视点搜索、最优高度/角度、航迹规划、避障、强化学习、多无人机任务分配和长期序列决策。
