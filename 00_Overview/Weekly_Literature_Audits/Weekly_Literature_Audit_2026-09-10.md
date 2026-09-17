# 主线A定向文献审计：2026-09-10

- 批次：2026-09-10-Mainline-A；时区Asia/Shanghai；输入为用户批准的A0-01计划及当日补充检索。
- 范围：指定六入口＋补查直接区域计算近邻，检索截至2026-09-10。不是全项目七方向的完整周检索，不推进该自动任务的成功覆盖日期。
- Batch Status：COMPLETE（审计归档联动完成；数据可行性HOLD，不解锁实验）。
- 计数：15个选入审查的唯一候选；7新增PASS、0已有工作新版本、0重复、8 HOLD、0 REJECT，合计15。搜索引擎全部返回数未统计；不把重复访问同一来源另算输入。

## 候选处置

| Input ID | 工作与一手入口 | Work ID | 处置 | 主／次方向 | 审计／正文 | 再查条件 |
|---|---|---|---|---|---|---|
| A01 | UAV-RSOD；10.1038/s41597-024-03952-3 | W-0001 | 新增PASS | P0／P1数据参考 | [主审计](../../00_Practice_UAV_Aerial_Detection/Literature/audits/W-0001_Audit.md) | 原图框、来源分组与数据独立性未通过，见数据报告 |
| A02 | SAHI；2202.06934v5 | W-0002 | 新增PASS | P0／无 | [主审计](../../00_Practice_UAV_Aerial_Detection/Literature/audits/W-0002_Audit.md) | 未来公平切片基线，当前不运行 |
| A03 | QueryDet；2103.09136v2 | W-0003 | 新增PASS | P0／无 | [主审计](../../00_Practice_UAV_Aerial_Detection/Literature/audits/W-0003_Audit.md) | 稀疏计算与完整计时边界 |
| A04 | ESOD；2407.16424v2 | W-0004 | 新增PASS | P0／无 | [主审计](../../00_Practice_UAV_Aerial_Detection/Literature/audits/W-0004_Audit.md) | 切片／前景计算直接冲突 |
| A05 | ROI-Gated SAHI；2608.23923v1 | W-0005 | 新增PASS，预印本 | P0／无 | [主审计](../../00_Practice_UAV_Aerial_Detection/Literature/audits/W-0005_Audit.md) | 保留全体COCO128负结果与校准问题 |
| A06 | RVGC-YOLO；10.1109/jsen.2026.3667586 | W-0006 | 新增PASS | P0／P1已知路径 | [主审计](../../00_Practice_UAV_Aerial_Detection/Literature/audits/W-0006_Audit.md) | 作者接受稿，非逐字确认VoR；速度排除NMS |
| A07 | MRU-YOLO；10.3390/rs18162680 | W-0007 | 新增PASS | P0／无 | [主审计](../../00_Practice_UAV_Aerial_Detection/Literature/audits/W-0007_Audit.md) | 固定K、效用排序与全局保护已有；毫秒保证未建立 |
| A08 | [ClusDet](https://arxiv.org/abs/1904.08008) | N/A | HOLD，未完成全文实验审计 | 拟P0 | 只留候选，无正文归档 | 补划分、计时与区域召回 |
| A09 | [DMNet](https://arxiv.org/abs/2004.05520) | N/A | HOLD，未完成全文实验审计 | 拟P0 | 同上 | 核验workshop版本与密度区域机制 |
| A10 | [AutoFocus](https://arxiv.org/abs/1812.01600) | N/A | HOLD，未完成全文实验审计 | 拟P0 | 同上 | 核验FocusPixels/Chips与合并失败 |
| A11 | [GOIS](https://www.sciencedirect.com/science/article/pii/S0925231225009993)；10.1016/j.neucom.2025.130327 | N/A | HOLD，出版社全文访问受限、版本关系未清 | 拟P0 | 摘要／作者代码线索未代替全文 | 取得合法全文，核验训练／评价集合及版本 |
| A12 | [ASAHI 2023](https://www.mdpi.com/2072-4292/15/5/1249)；10.3390/rs15051249 | N/A | HOLD，未完成全文核验 | 拟P0 | 出版年2023，HTML更新不变更论文年份 | 核验切片自适应与代价 |
| A13 | [ASAI](https://cjlcd.lightpublishing.cn/en/article/doi/10.37188/CJLCD.2024-0225/?viewType=HTML)；10.37188/CJLCD.2024-0225 | N/A | HOLD，已查一手摘要，未完成实验审计 | 拟P0 | 2025，窗口评分定位模糊目标；不归档正文 | 核验区域选择、二次推理与合并 |
| A14 | [ASAHI 2026线索](https://arxiv.org/abs/2604.19233) | N/A | HOLD，身份／版本与全文待核验 | 拟P0 | 不与2023 ASAHI凭缩写合并 | 核对题名作者、关系、全文与实际日期 |
| A15 | [Altitude-Aware Dynamic Tiling](https://arxiv.org/abs/2511.19728) | N/A | HOLD，已查作者版本身份，未全文审计 | 拟P0 | 作者列OCEANS2025，DOI10.1109/OCEANS58557.2025.11104659 | 核验高度信息成本及切片协议；不扩展救援任务 |

全部PASS主矩阵：[P0文献矩阵](../../00_Practice_UAV_Aerial_Detection/Literature/matrices/Literature_Matrix.md)；唯一正文及版本：[注册表](../Literature_Registry.md)。HOLD只有候选定位，不计新增正式记录。

## 本批结论与影响

W-0001至W-0007均Must Read，但Reading Status为SCREENED，未代替用户精读或S0-01验收。区域筛选、局部放大、阈值回退、固定K及效用选择已有先例；P0-A-C1/C2风险由未核验转为High。MRU相对同预算密度选择的AP差很小，必须保留简单基线；不能从局部回看总增益推断复杂排序有效。

影响链为I-2026-09-10-Mainline-A-01至07，见[创新台账](../Innovation_Ledger.md)。P1只新增W-0001/W-0006交叉参考，C1/C2主张不变，风险保持High；Paper 2–7保持PAUSED。

[数据审计](../../00_Startup_Railway_UAV_Detection/Experiments/Data_Feasibility_Audit.md)已发现原包train1611/test391、10组跨集合精确重复、原图小框不足及原图检测框映射未核实。**本批交付结论是暂缓方法实现**；这不等于已证明主线A理论无效。全部模型实验继续BLOCKED。

用户授权本批切换研究计划及A0阶段；不是文献审计自行放宽边界。旧LSM-Head及六个未运行P编号保留为历史。下一项唯一任务为A0-02补核原始数据证据，成功条件／止损见数据报告。国奖与分区[适用性仍待核验](../../00_Startup_Railway_UAV_Detection/Writing/Journal_Eligibility_Check.md)。

检索式与范围见[Search Log](../../00_Practice_UAV_Aerial_Detection/Literature/matrices/Search_Log.md)及[比较表](../../00_Practice_UAV_Aerial_Detection/Literature/matrices/Mainline_A_Prior_Work_Comparison.md)。未穷尽Web of Science/Scopus及引用网络，不作“无人做过”结论；暂不继续扩展检索，避免额外消耗。

## 联动验收

- [x] 15输入均已处置，7 PASS与8 HOLD分开统计。
- [x] 7个工作ID唯一；注册表／版本、主矩阵、7份审计与周报一致。
- [x] P1两条交叉索引及T1入口同步，未重复正文。
- [x] 受影响台账四字段和7条影响链同步。
- [x] 本地链接有效；保护附件、七篇路线、P1研究计划未改。
- [x] 模型运行记录未新增；静态审计不是训练或推理实验。

最终修改范围和验证结果见[验收记录](../../00_Startup_Railway_UAV_Detection/Experiments/A0-01_Verification.md)。

## 补充批次2026-09-10-A0-02

仅针对W-0001做数据来源补证，非全方向周扫描。新增论文0、论文版本更新0、既有工作补证1；未重新计数首批7 PASS/8 HOLD，未生成新Work ID或PDF。官方数据版本链仅1条记录，媒体未启用；XML未提供来源字段；论文代码链接为评价程序。原图框／派生映射／独立小目标证据仍未取得，维持HOLD。详见[A0-02报告](../../00_Startup_Railway_UAV_Detection/Experiments/A0-02_Data_Gap_Followup.md)。

联动已完成：W-0001审计、注册表、主矩阵、P1交叉矩阵／T1入口、创新台账四字段与影响记录、检索日志、当前阶段。作者询问信草稿已准备，未发送；下一项A0-03为用户审阅与确认外部求证方式。无模型运行、无正式数据划分、无原目录新增交付物。

## 范围更新2026-09-10-A0-04

用户接受弱化铁路专属场景，VisDrone-DET优先；官方来源／标注和评测入口预审完成，文件级审计尚未进行。无新增论文、Work ID或PDF；既有W-0001/W-0006在P0降为历史参考，原文PASS不撤销，P1交叉关系不变。计划、阶段、实验／学习／写作入口、主矩阵与创新台账已同步。轨道先验退出当前机制；风险High不变。下一项A0-05静态数据审计，无模型运行。见[VisDrone审计](../../00_Startup_Railway_UAV_Detection/Experiments/VisDrone_Feasibility_Audit.md)。

## 数据审计补充2026-09-10-A0-05

本轮仅做VisDrone文件级审计与官方评价代码静态读取，新增论文／Work ID／PDF为0。8,629张图全部解码并有对应标签，标签层小框284,915个；无跨split精确重复，34对近重复候选中有共享场景与误报，另3条train零高标注原样保留。支持继续VisDrone与协议审查，不开放模型。报告、当前阶段、计划、主矩阵及创新台账已联动。见[完整审计](../../00_Startup_Railway_UAV_Detection/Experiments/A0-05_VisDrone_File_Audit.md)。下一项A0-06，未提交／推送。

2026-09-11交付收尾：A0-05自9月10日启动，本日完成核对。已有9份统计产物校验值、汇总数字及253个本地链接通过检查，原学习目录与保护附件无内容差异。未重复下载或统计，未启动A0-06；详细核对记录见上述完整审计第9节。

## 协议补充2026-09-11-A0-06

[评测与数据用途草案](../../00_Startup_Railway_UAV_Detection/Experiments/A0-06_Evaluation_Protocol_Draft.md)已交付、未冻结；拟定train训练、val开发校准、test-dev最终评价，披露此前测试审计接触和共享场景限制。补充3条异常处理提案、原图小目标Recall诊断、时间边界及副本身份披露。官方源码新增定位行排序、重复类别汇总和ignore分母行为，待构造样例验证；没有评价运行结果。新增论文／Work ID／PDF为0，注册表及P1交叉索引无需改动，矩阵／台账／入口已同步。A0整体HOLD；下一项A0-07，无模型运行，未提交／推送。

## 评价语义补充2026-09-11-A0-07

[有限核验报告](../../00_Startup_Railway_UAV_Detection/Experiments/A0-07_Evaluator_Semantics_Check.md)交付：人工构造24个样例，最终Python语义对照24/24通过；MATLAB／Octave未在已检查位置发现，原版调用入口已生成但未执行。明确每图截断顺序、类别重复汇总、ignore分母与面积边界；未运行真实数据评价或模型。新增论文／Work ID／PDF为0，注册表及P1无需改动；主矩阵、台账和当前入口已同步。A0整体HOLD，下一项A0-08。无提交／推送。

## 决策补充2026-09-11-A0-08

[可行性决策](../../00_Startup_Railway_UAV_Detection/Experiments/A0-08_Feasibility_Decision.md)已交付：保留VisDrone，选择原版兼容结果＋小目标诊断的评价框架，正式协议未冻结。下一项A0-09仅审查一个可证伪候选，设置被已有方法覆盖或证据不足时的止损；来源独立性及原版运行门未放宽。复用现有审计，回查官方数据／代码入口，无新增论文、Work ID、PDF或模型运行，也未重跑数据与构造核验。当前入口、计划、矩阵和台账同步；注册表及P1无需变更。

## 候选审查批次2026-09-11-A0-09

[单候选审查](../../00_Practice_UAV_Aerial_Detection/Literature/reviews/A0-09_Candidate_Review.md)已交付。六条定向检索式见[日志](../../00_Practice_UAV_Aerial_Detection/Literature/matrices/Search_Log.md)，选入处置3项：新增PASS 1（W-0008 DZN）、新增HOLD线索1（SRENet，10.1016/j.neucom.2021.08.015，出版社摘要可访问、全文实验未审）、既有重复／复用1（W-0007 MRU）。新增版本0、仓库PDF 0；注册表当前累计8个PASS工作。此前HOLD不重开，不把本批数字冒充整个领域检索总数。

W-0008正式CVF全文10页核验完成；其顺序收益／成本选区、历史置零和熵／贪心对照已覆盖广义组件，但不能据此声称新检测结果重估所有剩余区域的精确形态已完全同构。当前候选仍不足以建立独立差异，状态DISMISSED，触发A0-08止损，暂缓方法实现。保留VisDrone及无人机／实时性／小目标范围，下一动作是用户审阅方向决策，不自动创建A0-10。

联动：W-0008审计、唯一正文链接、注册表／版本历史、主矩阵、创新四字段与I-2026-09-11-A0-09-01、检索日志、当前入口已同步。W-0008只属P0，无必要P1或暂停方向次矩阵更新；PASS为审计通过，阅读仍SCREENED。来源与原版运行门仍HOLD，S0-01未通过，国奖适用性待学院和年度信息核验。本轮未重跑数据／评价核验、未生成模型运行记录、未提交或推送。

## 候选审查补充批次2026-09-12-N1

本批接续未完成创新审查，检索跨09-11至09-12，北京时间；17条实际查询见[日志](../../00_Practice_UAV_Aerial_Detection/Literature/matrices/Search_Log.md)。复用已有审计，不重做数据、评价或接口检查；这是P0定向查新，不声明七方向本周全覆盖或推进其覆盖日期。

| 输入／身份 | 去重与处置 | 原文、缺口及再查条件 |
|---|---|---|
| A10 AutoFocus，1812.01600；Mahyar Najibi、Bharat Singh、Larry S. Davis | 旧HOLD首次PASS，新增W-0009；非新发表、非版本更新 | [全文审计](../../00_Practice_UAV_Aerial_Detection/Literature/audits/W-0009_Audit.md)，ICCV2019、arXiv v2唯一技术正文；粗响应选区和可恢复目标诊断已覆盖 |
| ViCrop-Det，2604.26806；Hui Wang、Hongze Li、Wei Chen、Xiaojin Zhang | 新增HOLD线索1，无Work ID、无正文归档 | [实名审查](../../00_Practice_UAV_Aerial_Detection/Literature/reviews/ViCrop_Det_HOLD_Review.md)：内部信号免训练裁剪已有；v1／HTML日期关系、VisDrone样本数、文表FPS不一致待官方版本或代码澄清，非认定虚假 |
| A14 ASAHI2026，2604.19233 | 既有HOLD身份页复核1，无Work ID | arXiv v1 2026-04-21；未完成方法与协议全文审计，继续HOLD；不得与2023 ASAHI合并 |
| W-0002/3/4/5/7/8 | 既有PASS证据复用，不计新增 | 对照已登记的切片、query、objectness、门控、收益与顺序成本机制；不刷新未重审工作的Last Audited |

计数：首次PASS 1（旧HOLD升级）；新HOLD线索1；既有HOLD身份复核1；论文版本更新0；新增本地PDF 0。注册表当前9项PASS，阅读均未因本批成为本人精读DONE。旧A10/A14处置行保留原批次历史，以本节为当前补充。

结论：[跨尺度同类弱响应候选](../../00_Practice_UAV_Aerial_Detection/Literature/reviews/Weak_Response_Candidate_Review.md)保留PROPOSED、High风险；通用免训练内部信号裁剪不是空白，精确跨层局部判据能否优于低阈值／P3-only尚无实证。旧A0-09保持DISMISSED。I-2026-09-12-N1-01联动P0-A-C1/C2四字段、固定评分对照及停止条件；没有新模块或性能承诺。

联动：W-0009审计／唯一正文／注册表与版本历史／主矩阵、HOLD审查、近邻比较、创新台账、检索日志、当前入口及实验预案已同步。无必要P1／暂停方向交叉更新，无新模型Run ID。独立反驳子任务因额度失败，未收到审查结果；主任务原文判断不冒充外部复核。

下一项唯一任务为受限普通YOLO11n基线训练执行方案，服务该候选的区分诊断；当前训练与检测推理未开放。学习作答不是科研前置，旧笔记及已完成证据保留；国奖适用性仍待学院／年份。未提交、未推送。
