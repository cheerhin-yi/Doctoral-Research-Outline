# Paper 1论文提纲

**状态**：结构占位；阶段6核心实验冻结前不写结果性文字。

## 暂定题目

Railway-Context-Aware Open-World Hazard Screening for UAV Inspection

题目在阶段2新颖性审计和阶段6结果后调整。

## 结构

1. **Introduction**
   - 铁路UAV小目标和类别不完备问题；
   - 仅检测对象不能直接支持风险告警；
   - 最近工作缺口；
   - 不超过两条贡献。
2. **Related Work**
   - 铁路UAV危险检测；
   - 开放集/开放词汇目标检测；
   - 轨道侵界和风险告警。
3. **Method**
   - 问题定义和Known/Unknown协议；
   - YOLO已知检测；
   - 未知候选；
   - 轨道上下文风险排序。
4. **Experiments**
   - 数据、split和指标；
   - 强基线；
   - C1主结果；
   - C2主结果；
   - 删除研究、效率和鲁棒性。
5. **Discussion**
   - 适用条件；
   - 未知误报、轨道解析错误和数据局限；
   - 对Paper 2/3/5/6的接口。
6. **Conclusion**

## 写作纪律

- 不把YOLO、开放集、中心线、距离规则或校准单独写成首次提出；
- 无稳定实验增量的组件不进入贡献列表；
- 结论只覆盖实际测试的场景、类别和飞行条件；
- 每张表和图都能回链到Run ID。
