> **2026-09-16 学习框架调整：** 本目录现为练手文**统一学习枢纽**（LEARNING-CORE）。先完成约三周核心学习，再讨论三个月实验。已有实验/代码/结果**不删除**；副本见 [`99_Attachments/Archive_2026-09-16_PracticePaper/`](../99_Attachments/Archive_2026-09-16_PracticePaper/)。当前入口：[LEARNING_CORE.md](LEARNING_CORE.md) · [三周计划](Learning_Plan_3_Weeks.md) · [验收协议](ASSESSMENT_PROTOCOL.md) · [英语并行](English_Parallel_Plan_CET4.md)。三周内默认不新训模型。下方旧科研入口仍有效，作归档证据索引，不触发重跑。

# 主线A启动项目：无人机航拍时间预算约束小目标检测

更新：2026-09-14。BTD12单机制审查已完成：尺度条件DFL分布统计重评分候选DISMISSED，GFLV2与多变量校准已覆盖核心关系，尚无独立机制差异；这是书面否决，非实测失败。100轮及BTD1–BTD11完成且不重跑。当前返回论文主张与投入方向决策，停止自动候选开发／新模型运行，不创建BTD13。旧区域机制及A0整体HOLD。 见[BTD12审查](Literature/BTD12_Low_Score_Candidate_Review.md)。

详细证据以[当前阶段](../00_Overview/Current_Stage.md)为准；下方未同步的旧准入措辞只记录历史前提，不触发重复执行。

2026-09-12历史平台约定（已由本机执行及100轮完成状态替代）：只先用Kaggle，每轮保存恢复包、每5轮保留副本、默认约60分钟轮末暂停并封存平台输出；Kaggle额度耗尽且旧会话停止后才转Colab续训。目前Kaggle手机验证未完成，尚无云端模型训练。此约定替代旧“二选一／不允许恢复”描述；本机完成项不重跑，详见当前阶段与BT1交接报告。
本目录独立存放主线A研究计划、文献审查、数据审计、学习记录和写作材料。原`00_PrePaper_Lightweight_Detection/`恢复并保留原有学习笔记、文献及历史计划，不再接收本项目交付物；其LSM-Head及旧阶段要求不适用于当前主线A。旧笔记只作学习参考，新学习内容写入本目录的`Learning_Notes/`。

当前已按用户决定弱化铁路场景，保留无人机、实时性和小目标。[100轮基线归档](Experiments/BT1_100_Epoch_Archive.md)及[cal48漏检诊断](Experiments/BT1_Cal48_Miss_Diagnosis.md)已完成；当前弱响应v0.1转HOLD，旧熵反馈候选仍DISMISSED。单片预算/上界及F1280强基线对照均已完成；当前区域排序机制暂缓，BTD10重审及BTD11筛查已完成；BTD12已完成并否决本候选；下一项为论文主张与投入方向决策；学习独立后续完成。

| 入口 | 用途 |
|---|---|
| [当前阶段](../00_Overview/Current_Stage.md) | 唯一任务、结果与阶段门 |
| [研究计划](Research_Plan.md) | 问题、两项候选、范围及停止条件 |
| [阶段指南](Stage_Guide.md) | A0至写作的完成门 |
| [VisDrone完整审计](Experiments/A0-05_VisDrone_File_Audit.md)／[来源预审](Experiments/VisDrone_Feasibility_Audit.md) | 文件、标注、小目标、重复及待确认协议 |
| [A0-06评测与数据用途草案](Experiments/A0-06_Evaluation_Protocol_Draft.md) | 数据用途、共享场景限制、异常与指标规则；尚未冻结 |
| [A0-07评价语义核验](Experiments/A0-07_Evaluator_Semantics_Check.md) | 24个构造样例及手算对照；原版运行仍待补证 |
| [A0-08可行性决策](Experiments/A0-08_Feasibility_Decision.md) | 评测框架、剩余门、继续／暂缓和下一任务止损 |
| [A0-09候选审查](Literature/A0-09_Candidate_Review.md) | 单候选卡、已有覆盖、当前否决与方向决策 |
| [研究问题重新界定](Research_Question_Reframing.md) | 三条路径、推荐诊断问题、待审阶段门与停止规则 |
| [诊断准入与最小协议](Experiments/Diagnostic_Admission_Review.md) | 本机核查、已选路径、六个配置、运行门与实际补证任务 |
| [原版代码兼容交叉核验](Experiments/Official_Runtime_Crosscheck.md) | Octave实跑24/24、差异0、运行环境与局限 |
| [权重来源与十类映射](Experiments/Weight_Source_Audit.md) | 两个公开候选、身份缺口、索引映射与自训准备依据 |
| [训练接口静态核查](Experiments/Training_Interface_Audit.md) | 固定源码、训练ignore偏差、逐行转换规则 |
| [最小标签转换器与核验](Experiments/Label_Adapter_Check.md) | 单文件适配器、50/50人工检查、文件保护与下一学习节点 |
| [W-0008全文审计](Literature/W-0008_Audit.md) | 顺序收益选区、成本和熵／贪心近邻证据 |
| [UAV-RSOD历史审计](Experiments/Data_Feasibility_Audit.md) | 旧候选数据证据，HOLD保留 |
| [A0-02补证结果](Experiments/A0-02_Data_Gap_Followup.md)／[作者询问信草稿](Experiments/A0-03_Author_Data_Request_Draft.md) | 历史补证；询问信未发送，退出当前关键路径 |
| [近邻比较](Literature/Mainline_A_Prior_Work_Comparison.md) | 已有机制与候选差异 |
| [文献矩阵](Literature/Literature_Matrix.md)／[检索日志](Literature/Search_Log.md) | 审计、优先级与检索范围 |
| [按需学习](Learning_Notes/07_Mainline_A_Knowledge_Chain.md) | 检测链、切片、划分、端到端测速 |
| [实验计划](Experiments/Experiment_Plan.md)／[实验跟踪](Experiments/Experiment_Tracker.md) | 当前BLOCKED预案与真实运行记录 |
| [写作提纲](Writing/Paper_Outline.md)／[投稿适用性](Writing/Journal_Eligibility_Check.md) | 证据组织与国奖／分区待核验项 |

LSM-Head已退出当前执行方案；历史研究理由、文献、学习初稿和旧实验编号保留。单目RGB、无人机视角、已知类别二维检测是硬边界，轨道走廊已退出当前方法前提。Paper 1及七篇论文规划保持不变。
