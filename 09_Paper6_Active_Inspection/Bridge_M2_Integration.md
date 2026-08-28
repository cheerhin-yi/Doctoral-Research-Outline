# Paper 6与桥接模块M2的衔接说明

## 分工

M2只解决“当前候选是否值得额外复检”，Paper 6解决“去哪里看、如何到达、由哪架无人机执行”。

## M2向Paper 6输出

`object_id, reinspection_priority, expected_risk_reduction, trigger, stopping_reason, time_cost, energy_cost`

## Paper 6保留的核心研究

- 候选视点生成与评价；
- 最优飞行高度、角度或下一最佳视点；
- 航迹规划、避障与任务执行；
- 多无人机分配与协同；
- 必要时的长期序列决策。

## Paper 6启动门槛

1. M2能在固定复检协议下稳定输出触发决策；
2. 复检预算与时间/能耗计量方式已冻结；
3. 已确认Paper 6的评价指标集中于视点、路径和多机效用，而非重复M2触发准确率；
4. 具备可执行的候选视点和飞行安全约束。

M2未达到独立论文门槛时直接作为Paper 6的触发模块，不阻止Paper 6使用其接口。
