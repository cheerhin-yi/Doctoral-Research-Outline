# 练手论文实验跟踪表


## P0 Benchmark Stage B (P0-BENCH-B-TIMING-20260917-01) — READY

| Run ID | Stage | Goal | Hardware | Env | Status | Artifacts |
|---|---|---|---|---|---|---|
| P0-BENCH-B-TIMING-20260917-01 | B | cal48 x 5 methods x 3 timing (pipeline bring-up) | GTX 1660 SUPER | H:/Conda/envs/UAV_BT1 | READY | P0_Benchmark/stage_b/P0-BENCH-B-TIMING-20260917-01/ |

Hypothesis: bring up end-to-end timing path on local GPU; formal 4090 table deferred.
Frozen: weight SHA bc42d54e..., cal48, conf=0.25, DensK1 from BTD8, SAHI 640/0.25.
Stopping: finish 48 images x methods x 3 or FAILED.

---


## P0 Benchmark Stage A (P0-BENCH-A-ENV-20260917-01)

| Run ID | Stage | Goal | Hardware | Env | Status | Artifacts |
|---|---|---|---|---|---|---|
| P0-BENCH-A-ENV-20260917-01 | A | Env & SHA freeze for P0 five-method benchmark | GTX 1660 SUPER | H:/Conda/envs/UAV_BT1 | DONE / PASS | [Freeze report](P0_Benchmark_Environment_Freeze.md); `P0_Benchmark/stage_a/` |

Notes: weight SHA match; cal48 n=48 frozen; sahi missing (M5 blocker); 4090 not present (B–D unified latency blocker on this host). No training. Stage B not started.

---

正式实验当前全部`BLOCKED`。2026-09-10切换主线A：下表为未运行的LSM-Head历史预案，**不再作为当前执行方案**；旧阶段号和B模型定义不触发执行，不复用旧Run ID。A0-01未产生任何训练或检测推理运行记录。新增运行前必须通过主线A阶段门并填写假设、唯一变量、数据版本、seed、硬件和停止条件。

| Run ID | 阶段 | 模型 | 目的 | 数据/版本 | Seed | 主要指标 | 状态 | 结果位置/备注 |
|---|---|---|---|---|---:|---|---|---|
| P000 | M0 | B0 | 官方小样例推理与验证 | 框架样例 |  | 输出完整性 | BLOCKED | 未运行；原阶段3预案已退出执行 |
| P001 | M0 | B1 | 普通P2结构与张量检查 | 极小样例 |  | shape/参数量 | BLOCKED | 未运行；原阶段3预案已退出执行 |
| P010 | M1 | B0 | 正式基线 | 待冻结 |  | mAP/AP_small/延迟 | BLOCKED | 未运行；原阶段4预案已退出执行 |
| P011 | M1 | B1 | P2收益和代价 | 待冻结 |  | mAP/AP_small/延迟 | BLOCKED | 未运行；原阶段4预案已退出执行 |
| P020 | M2 | B2 | P2–P4消融 | 待冻结 |  | AP_small/GFLOPs | BLOCKED | 未运行；原阶段5预案已退出执行 |
| P021 | M2 | M | 共享轻量头 | 待冻结 |  | AP_small/延迟 | BLOCKED | 未运行；原阶段5预案已退出执行 |

状态使用：`BLOCKED`、`READY`、`RUNNING`、`DONE`、`FAILED`、`EXCLUDED`。

## BT-1批准后的实际执行记录

用户于2026-09-12批准Conda本机小参数预检后转云端；以下不使用旧P编号。普通基线与创新对照分开，预检不产生可报告的准确率提升。

| Run ID | 假设／目的与唯一范围 | 数据与配置 | Seed／硬件 | 状态 | 结果与停止条件 |
|---|---|---|---|---|---|
| BT1-SMOKE-20260912-01 | 检查训练、保存、重载和P3/P4读取链；不检验创新 | 固定ZIP派生train前4图／cal48前4图验证；YOLO11n，640，batch1，FP32，1轮 | 0；GTX1660SUPER 6GiB；独立Conda UAV_BT1 | DONE | 148.75秒；1轮4batch通过，末轮重载及P3/P4响应有限；产物11_Datasets/processed/VisDrone/BT1/BT1-SMOKE-20260912-01；baseline_eligible=false |

云端已连接并导入Notebook；Kaggle仍受手机验证限制，只有CPU草稿会话，训练单元未执行。Colab仅发生安装前Python版本检查失败，不构成模型运行。当前只使用Kaggle，真实训练Run ID尚未产生。断点序列化构造检查通过，真实恢复与平台输出备份未验证；详见[交接报告](BT1_Local_Smoke_and_Cloud_Handoff.md)。

## 2026-09-12本地首段授权

用户因Kaggle手机验证暂不可用改为本地初步训练。BT1-LOCAL-20260912-01：PAUSED（已完成3轮）；普通YOLO11n，6471张train/cal48，seed0，640，batch4，FP32，GTX1660SUPER；100轮日程先运行约15分钟于轮末保存，不代表完成100轮。来源与ignore局限继续保留，无云端或候选模块训练。

2026-09-12结果：BT1-LOCAL-20260912-01完成3轮、正常暂停，1121.17秒；cal48原生mAP50=0.16299、mAP50–95=0.08259、Recall=0.21021。固定6图预览及恢复包核验完成，实际续训尚未验证。详情见BT1_Local_First_Segment_Result.md；没有正式测试或创新效果结论。

## BT1-LOCAL-20260912-02：第4轮续训核验

DONE（核验完成；训练PAUSED在第4轮）；从01号第3轮恢复包读取，独立输出目录，原100轮日程、batch4、640、FP32不变。训练前9项状态比对PASS；第4轮首批学习率0.009703，与期望一致，损失有限。设置第4轮末停止；完成保存后再报告本轮通过，不重跑第1–3轮。

02号结果：实际完成第4轮，378.20秒，新CSV只有第4轮，恢复包完整性与SHA通过；原生mAP50=0.16344、Recall=0.19320。详细证据见[第4轮核验](BT1_Epoch4_Resume_Verification.md)。

## BT1-LOCAL-20260913-01：连续完成基线

DONE；从02号第4轮恢复包完成第5–100轮，累计100轮，末轮状态PASS，权重SHA为bc42d54e37acaf1f698af487439dc222fa86fb4498623e8cf954df14e0aa5533。640/batch4/FP32/seed0不变；没有重新训练第1–4轮，未启动云端。日志与进程号在同名-launch目录。后续归档与分析见本节以下新运行。

## BTD1-CAL48-20260913-01：基线归档及可恢复漏检诊断

READY → RUNNING → DONE（2026-09-13，先登记后启动；运行38.11秒含归档）。用户明确要求归档及机制支持分析；固定末轮权重、cal48全48图、seed0训练来源、GTX1660SUPER、640/batch1/FP32。唯一比较变量为选区评分，K≤2、相同局部池与融合；F640/Tall作诊断参考。假设：跨层同类支持较低阈值/P3-only更能定位可恢复小GT。完整预登记、阈值、匹配、2小时/10GiB上限及失败条件见[协议](BT1_Baseline_Diagnostic_Protocol.md)。输出11_Datasets/processed/VisDrone/BT1/BTD1-CAL48-20260913-01。无新训练、网络修改、diag500或test-dev访问；缓存计时不作端到端速度。

结果：有效小GT2720，可恢复558；候选恢复336、P3-only338、密度429，当前v0.1转HOLD，不继续调参。归档与诊断检查PASS，不等于创新通过。见[100轮归档](BT1_100_Epoch_Archive.md)与[漏检分析](BT1_Cal48_Miss_Diagnosis.md)。下一项仅从缓存归因密度遗漏的129个可恢复GT，不重跑模型。

## BTD2-DENSITY-20260913-01：密度残差缓存归因

READY→RUNNING→DONE，2026-09-13。用户明确要求分析129个残差；复用BTD1预测，唯一范围为失败归因与信息缺口分析，没有新的模型Run。基线seed0来源/权重/数据身份不变；本次CPU NumPy计算。先登记[协议](BTD2_Density_Miss_Protocol.md)，再核验129个目标身份、所选视图独立匹配/覆盖/融合，并检查粗预测重复计数及现有评分增减收益。输出`11_Datasets/processed/VisDrone/BT1/BTD2-DENSITY-20260913-01`；身份或缓存错误立即停止，不重训、不重推理、不改候选。

结果：77未覆盖中心、42覆盖但局部未检出、10融合/匹配变化；77中66存在新增粗中心更多的未选恢复窗口，但零新增粗中心的第二片在11图仍找回19个第一片未找回目标。支持检验条件新增收益，尚不支持新机制。下一项仅简单去重密度缓存对照，尚未运行。见[分析报告](BTD2_Density_Miss_Analysis.md)。

## BTD3-DEDUP-20260913-01：简单去重密度缓存对照

READY→RUNNING→DONE，2026-09-13，用户明确要求继续该对照。预先固定：复用BTD1 cal48全部48图/240窗口，第一片等于原密度Top1；第二片按粗预测中心集合减去第一片覆盖集合后的数量排序，排除第一片自身；同分按原窗口索引，零分仍补足第二片。粗框conf≥.25不变，不读GT选区。原权重/预测、全图结果、K=2、NMS=.5/max500、诊断conf=.25/IoU=.5、ignore及小目标定义全部不变。CPU缓存计算，不加载模型、不重推理、不打开diag500/test-dev、不改弱响应公式。

验收预先要求：48图/96片及选择规则核验；全部2720小GT的TP/FP与Recall，558可恢复集合内补回/丢失相对密度的配对关系，129个原残差去向，各类及逐图结果。不按局部成功案例选择阈值。若整体不优或交换代价抵消收益，保留负结果，不自动再加一个评分项。缓存身份/分母不符立即停止；输出`11_Datasets/processed/VisDrone/BT1/BTD3-DEDUP-20260913-01`。

结果PASS：小GT1259→1282（补54、丢31），Recall46.29%→47.13%；可恢复GT429→453，全尺寸FP1233→1249。逐图7胜/34平/7负，开发图自助差区间跨0，未确认稳定收益。见[结果报告](BTD3_Dedup_Density_Result.md)。下一项为冻结两个简单规则在diag500配对验证及完整计时，尚未运行；不调当前候选。

## BTD4-DIAG500-20260913-01：两简单规则配对验证及实测速

READY→RUNNING→DONE，2026-09-13。用户明确授权继续；执行前固定[协议](BTD4_Diag500_Protocol.md)。末轮权重、原val划出的diag500，YOLO11n/640/batch1/FP32/GTX1660SUPER；唯一变量为第二片选区，原密度对去重密度。两方法各500图×3次真实运行；cal48校准与F1280时间参考不参与diag500准确率。指标固定小目标Recall/TP/FP及完整时延分布和相对预算超限率。首次输出作准确率，重复仅计时，不以缓存测速。2小时/10GiB上限；错误即停，不改参数。输出`11_Datasets/processed/VisDrone/BT1/BTD4-DIAG500-20260913-01`。未训练、未改网络、不访问test-dev。

结果PASS：500图、3000计时齐全，重复输出无不一致；23708小GT，原密度11129、去重11402（补644、丢371、净+273，Recall+1.15pp）。两方法平均90.89/90.21ms，p95 128.93/127.10ms，超过参考61ms的帧次89.80%/89.00%，预算未通过。执行501.91秒；启动低内存需披露。去重保留强简单对照，非创新。见[完整报告](BTD4_Diag500_Result.md)。下一项仅公共后处理等价性与计时校核，不改规则、不重训。

## BTD5-NMS-20260913-01：公共NMS等价性及CPU耗时

READY→RUNNING→DONE（等价与计时PASS，资源协议存在偏差），2026-09-13。用户明确要求继续；范围按[协议](BTD5_NMS_Protocol.md)。使用既有cal48缓存及人工构造输入，对比原float64稳定NMS和现有torchvision CPU编译算子，单变量为公共实现。先逐行精确等价，再432组×11次/实现交替计时；不加载模型、不推理、不修改历史选区/预测。任一有效域不等价停止，10分钟/1GiB上限。输出`11_Datasets/processed/VisDrone/BT1/BTD5-NMS-20260913-01`；代码加速不计创新。

结果：115组构造及432组缓存逐行完全一致，9504次计时无输出差异，耗时222.08秒；密度/去重合并的每数组中位数均值27.034/26.954→6.275/6.573ms。9张全图及其合并走几何回退。未加载模型、无训练或推理，缓存SHA不变。内存上限未实现强制守卫，单次私有内存1.089GiB超过协议1GiB，峰值未知；不宣称全部协议合规。见[报告](BTD5_NMS_Result.md)。下一项BTD6真实流程等价与完整计时，同时重校参考T；尚未启动。

## BTD6-PIPELINE-20260913-01：共用新NMS的完整流程复测

READY→RUNNING→DONE（运行9月13日完成，9月14日核验；实现PASS、预算未通过），2026-09-13，用户明确要求继续。先登记[协议](BTD6_Pipeline_Protocol.md)，cal48实际NMS输入新旧精确等价后，两方法各500图×3次真实计时，重校F1280参考T；全部选区、预测和逐图统计对照BTD4，容差外差异即停。无训练、规则调整或test-dev；权重和参数不变。30分钟、目录1GiB、磁盘余量5GiB；每帧外采样RSS3GiB/私有4GiB/系统余量256MiB守卫，不是连续硬上限。输出`11_Datasets/processed/VisDrone/BT1/BTD6-PIPELINE-20260913-01`。

结果：240次NMS精确一致、diag500全部3000次输出与BTD4逐值相同（最大差0）；全部统计保持。均值51.23/51.25ms、p95 82.63/82.90ms，新F1280参考T=40ms，帧次超限98.80%/99.07%。3636次资源采样通过，运行224.47秒，输入SHA未变，无训练/test-dev访问。完整校核及[报告](BTD6_Pipeline_Result.md)已归档。下一项BTD7只读cal48去重105残差及全窗口条件新增价值，尚未启动。

## BTD7-RESIDUAL-20260914-01：去重残差及条件新增检出价值

READY→RUNNING→FAILED（归档整数格式错误；已保存计算结果），2026-09-14。用户要求继续，先登记[协议](BTD7_Residual_Protocol.md)。仅cal48既有全图/240局部和去重缓存；核验105残差，固定第一片逐个审计第二片的新增/丢失、误检、GT事后上界与推理可得信号排序关系。GT不用于实际方法，不拟合或调参，不读diag500/test-dev新数据，不加载模型。CPU15分钟/RSS2GiB/输出256MiB，系统余量256MiB、磁盘2GiB；逐图守卫。输出`11_Datasets/processed/VisDrone/BT1/BTD7-RESIDUAL-20260914-01`。

BTD7-01归档失败：48图条件匹配与105例CSV已完成，但NumPy int64未转换导致JSON序列化失败；保留原status=FAILED、failure.txt及48份逐图集合。BTD7-RESIDUAL-20260914-02仅接续归档：复用01逐图集合/105例，重建未写出的窗口信号表，补算缺失的窗口FP并核对已存匹配集合；不重做残差分类/oracle搜索，不加载模型。修复整数标准化，资源规则同01；01不覆盖。

## BTD7-RESIDUAL-20260914-02：中间集合接续归档

READY→RUNNING→DONE，2026-09-14，接续约6.20秒。105例/240窗口/48图及输入身份、集合守恒核验PASS；01原失败文件保持。残差26未覆盖、67覆盖未检出、12合并/匹配变化；固定第一片的GT最佳第二片小TP1308，对去重1282补47/丢21/净26。所查弱响应及第一片反馈计数没有超越密度的方向一致性证据；暂缓第二片重排为唯一创新。01资源样本未落盘、峰值未知；02离散样本保存。无模型加载、训练、推理。见[完整报告](BTD7_Conditional_Recovery_Result.md)。下一项BTD8单片预算和选择上界检查，尚未启动。

## BTD8-SINGLE-20260914-01：单片预算与选择上界

READY→RUNNING→DONE（执行校核PASS，尾部预算未通过），2026-09-14，用户要求继续，先登记[协议](BTD8_Single_Crop_Protocol.md)。两阶段独立落盘：cal48缓存240个单片组合、密度第一片与GT最佳单片（仅诊断）；随后密度K1与F1280各48图×3次真实完整计时，交替先后、重校T。固定末轮权重、GTX1660SUPER/FP32/batch1，无训练/评分拟合/diag500/test-dev新访问。资源逐图或帧前守卫，样本立即追加；各阶段15分钟、RSS3GiB/私有4GiB、输出256MiB。输出`11_Datasets/processed/VisDrone/BT1/BTD8-SINGLE-20260914-01`。

结果：缓存48图/240组合通过，密度单片1172、GT最佳1223（补97/丢46/净51）；288次计时，K1平均37.36ms/p95 64.51ms，重校T=40ms，30/144帧次超参考；F1280平均27.33ms。144次K1、96次F1280重复比较精确一致；382资源样本、输入SHA及守恒核验PASS，阶段未重跑，无训练。见[报告](BTD8_Single_Crop_Result.md)。下一项BTD9仅用保存F1280预测核对强基线效果，不新推理；尚未启动。

## BTD9-F1280-20260914-01：整图1280强基线缓存效果

READY→RUNNING→DONE，2026-09-14，用户要求继续，先登记[协议](BTD9_F1280_Protocol.md)。仅48张cal48已保存F1280预测与F640/K1/GT最佳单片对照，原阈值/ignore/小目标定义保持；逐图/逐类补回丢失，GT和集合并集仅诊断。无模型加载、推理、训练或新测试数据。CPU10分钟/RSS2GiB/系统余量256MiB/输出128MiB，逐图样本立即落盘。输出`11_Datasets/processed/VisDrone/BT1/BTD9-F1280-20260914-01`。

结果PASS：48图/四配置，F1280小TP1312、FP839；对密度单片1172/1051、GT最佳1223/1038均更优，总量并非完全包含。F1280相对密度补287丢147，GT最佳独有169；GT逐图切换上界1345仅比F1280多33。现有实际时延F1280亦更快。1461条跨对照变化及输入/集合/类别核验通过，分析1.47秒，无新模型调用。见[报告](BTD9_F1280_Result.md)。暂缓当前区域排序机制，下一项BTD10仅研究问题重审，不继续自动扩展实验。

## BTD10：书面研究重审（2026-09-14，非实验运行）

书面任务DONE，见[报告](../Research_Question_Reassessment_BTD10.md)。W-0010–W-0012新增审计；当前区域机制HOLD；定位／分数失配优先筛查、密集后处理备用，均非成立创新。没有模型加载、训练、推理或实验Run ID；不复用旧运行编号。下一项BTD11仅合并缓存审计，尚未运行。

## BTD11-ERROR-20260914-01：整图1280错误结构

READY，2026-09-14，用户续接未完成任务；[协议](BTD11_Error_Structure_Protocol.md)已登记。仅cal48已存预测和标注，CPU诊断、无模型调用。先人工语义校核，再实际缓存审计；结果未产生前不标DONE。输出目录使用新编号，不覆盖BTD1–BTD9。

BTD11-ERROR-20260914-01结果：READY→RUNNING→DONE，缓存审计及独立校核PASS，见[报告](BTD11_Error_Structure_Result.md)。48图1408小FN／839FP，conf.10小TP1624、FP2170；分数GT修复补559、定位142、分类198，均丢0，不能称实际方法增益。35图截断至500。分析5.23秒；247输入SHA／399初始产物SHA、144最大匹配证书／修复重评及96资源样本通过，无模型调用。下一项BTD12只单机制方案与否决审查，不继续扩大缓存诊断，不自动新训练。

## BTD12：单机制方案与否决审查（2026-09-14，非实验运行）

书面任务DONE；[报告](../Literature/reviews/BTD12_Low_Score_Candidate_Review.md)。RQ-BTD12-1尺度条件DFL分布重评分DISMISSED，原因是独立新颖性依据不足，非实测失败。静态核查已有源文件及公开文献，W-0013/14审计联动完成；无模型加载／训练／推理，无新增实验Run ID。100轮及BTD1–BTD11不重跑，下一项为论文主张与投入方向决策，不自动创建BTD13或执行报告中的条件性工程验证。
