# Paper 1前置论文与桥接模块实施入口

更新日期：2026-08-28

本实施包把“两篇Paper 1前置练手论文＋两个桥接模块”落为可执行、可验收的研究任务。它不改变现有七篇论文的核心边界；发生冲突时，以本实施包中的边界表和各任务章程为准，并在下一次项目评审时同步回主框架文档。

## 当前唯一活动任务

**前置论文A：飞行条件感知风险校准。**

前置论文B必须等A的校准接口冻结后才能启动。桥接M1必须等Paper 1输出接口稳定后启动。桥接M2必须等Paper 1和M1均稳定后启动。任一时刻只能有一个活动研究任务。

## 文件导航

- [总体实施路线](./PrePaper_Bridge_Master_Plan.md)
- [前置论文A章程](./PrePaper_A_Viewpoint_Calibration_Charter.md)
- [前置论文B章程](./PrePaper_B_TwoPass_Verification_Charter.md)
- [桥接M1章程](./Bridge_M1_Encroachment_Measurement_Charter.md)
- [桥接M2章程](./Bridge_M2_Reinspection_Trigger_Charter.md)
- [共享数据与接口契约](./PrePaper_Shared_Data_Contract.md)
- [封闭线路实飞采集规范](./PrePaper_Field_Collection_Protocol.md)
- [20周执行清单](./PrePaper_20_Week_Execution_Backlog.md)
- [实验注册表](./PrePaper_Experiment_Registry.csv)

## 完成定义

一项研究只有同时满足以下条件才算完成：

1. 数据划分冻结且不存在同场景、相邻帧或增强同源泄漏；
2. 主基线、所提方法、消融和失败案例全部完成；
3. 验收指标在独立物理场景测试集上计算；
4. 代码配置、随机种子、模型权重和输出表可追溯；
5. 论文或模块报告明确区分支持与不支持的结论；
6. 投稿前重新核验IF、SCIE、中科院大小类分区和历年预警状态。

## 暂不实施

未知目标算法、稠密三维重建、SLAM、点云融合、多时相变化、NBV、路径规划、强化学习和多无人机协同不属于两篇前置论文。它们分别保留给Paper 1、Paper 2和Paper 6。
