# 2026-09-14：BTD10定向审计

- Batch ID：2026-09-14-BTD10；日期／时区：2026-09-14，Asia/Shanghai。
- 输入：BTD9后的研究问题重审；检索可追溯范围见[Search Log](../../00_Startup_Railway_UAV_Detection/Literature/Search_Log.md)。非七方向每周全量检索，不推进其成功覆盖日期。
- Batch Status：COMPLETE（本批处置与联动完成，不代表HOLD证据补齐）。
- 工作级候选8项：新增PASS 3，版本更新0，重复0，HOLD 5，REJECT 0；合计8。既有W-0002–W-0009仅复用，不计新增输入；一般检索噪声不计审计论文。

| 输入 | 工作／来源 | Work ID | 处置与原因 | 归属／后续条件 |
|---|---|---|---|---|
| BTD10-01 | TIDE，2008.08115 | W-0010 | PASS；[审计](../../00_Startup_Railway_UAV_Detection/Literature/W-0010_Audit.md) | P0；错误分解参考，SCREENED |
| BTD10-02 | NWD，2110.13389v2 | W-0011 | PASS；[审计](../../00_Startup_Railway_UAV_Detection/Literature/W-0011_Audit.md) | P0；小框度量直接近邻，SCREENED |
| BTD10-03 | Adaptive NMS，1904.03629v1 | W-0012 | PASS；[审计](../../00_Startup_Railway_UAV_Detection/Literature/W-0012_Audit.md) | P0；密度抑制直接近邻，SCREENED |
| BTD10-04 | [Detecting tiny objects in aerial images: A normalized Wasserstein distance and a new benchmark](https://arxiv.org/abs/2206.13996) | N/A | HOLD；NWD身份页明确扩展关系，但扩展贡献及是否独立工作未审清 | 不拆分计数／拼接结果；若选定位路线再审全文与版本 |
| BTD10-05 | [Tiny Object Detection via Normalized Gaussian Label Assignment and Multi-Scale Hybrid Attention](https://www.mdpi.com/2072-4292/18/3/396)，10.3390/rs18030396 | N/A | HOLD；官方身份及方法片段已核，2026-01-24；完整实验／消融／计时未审完 | 分类定位联合筛选的近期挑战；选路线一前必须补审，不能称未有近邻 |
| BTD10-06 | [ContextTiny-Net: An Ultra-Tiny Object Detection Network for UAV Aerial Images in Urban Scenarios](https://www.mdpi.com/2073-8994/18/7/1145) | N/A | HOLD；仅检索线索，元数据／全文未核 | 仅在与确定机制直接相关时补审，不用搜索摘要归因提升 |
| BTD10-07 | [Improved YOLOv7 for small object detection in airports: Task-oriented feature learning with Gaussian Wasserstein loss and attention mechanisms](https://www.sciencedirect.com/science/article/pii/S0925231225005168) | N/A | HOLD；仅检索线索，版本／全文实验未核 | 不把机场场景或多模块成绩作为本项目支持 |
| BTD10-08 | Soft-NMS: Improving Object Detection With One Line of Code（W-0012参考文献[1]及对照） | N/A | HOLD；本轮只核其在Adaptive NMS中的对照，未独立全文审计 | 若开发后处理需独立审计／复现；不新建PASS记录 |

同缩写TIDE的few-shot检测工作与2008.08115不是同一工作；搜索噪声未登记为新论文。去重覆盖现有Markdown、旧矩阵／阅读单、PDF文件名和基础ID；三项首次登记，无新增正文PDF，均用一个稳定全文链接。

## 研究影响

I-2026-09-14-BTD10-01/02/03已回链[台账](../Innovation_Ledger.md)与[预案](../../00_Startup_Railway_UAV_Detection/Experiments/Experiment_Plan.md)。P0-A-C1/C2旧机制继续HOLD、风险High；修正主表仍写PROPOSED／未测的过时表述，历史不删除。TIDE仅指导证据归因；NWD与Adaptive NMS分别否定“简单换距离”和“密度调抑制即可算新颖”的写法。两项新切入点仍是问题观察，未新增论文创新主张。

主归属全部P0，无必要P1–P7次索引或既有主题Reading_List变更。Must Read只是与当前问题直接有关，不要求用户先完成学习。

局限：本轮经典近邻为主，近期补查非穷尽；BCDet等仍HOLD，不宣布完成全部新颖性排除。CVF直接访问失败的记录已在W-0012注明；三项均未本机复现实验。期刊分区／国奖适用性未做新的核验。

## 联动检查与下一步

- [x] 八项输入均有处置，HOLD未计为新增；预印本未冒充正式期刊版。
- [x] 三项PASS各有一个主正文参考、审计、注册表／版本历史和19字段主矩阵记录。
- [x] 受影响创新四字段、影响行、研究重审报告与入口同步。
- [x] 无必要次方向变更；无保护附件／旧学习稿修改；没有模型运行。
- [x] 本地文档链接与编号唯一性完成核验；既有未提交内容保留，不提交／推送。

交付：[BTD10重审](../../00_Startup_Railway_UAV_Detection/Research_Question_Reassessment_BTD10.md)。下一项唯一任务BTD11：只用现有cal48 F1280缓存，合并检查剩余错误类型、可观察改善空间和证据缺口；交付明确继续／停止建议。无具体机制差异时停止方法开发，不自动再训练或扩展诊断。

## 2026-09-14-BTD12：单机制直接近邻审查

- Batch ID：2026-09-14-BTD12；2026-09-14，Asia/Shanghai；Batch Status：COMPLETE。
- 输入：BTD11后一个低分机制审查；[实际检索日志](../../00_Startup_Railway_UAV_Detection/Literature/Search_Log.md)。非全领域穷尽检索，不更新七方向覆盖日期。
- 工作级候选4项：新PASS 2、HOLD 2、版本更新0、重复0、REJECT 0。既有文献复用和搜索噪声不计输入。

| 输入 | 工作／来源 | Work ID | 处置与原因 | 用途／后续条件 |
|---|---|---|---|---|
| BTD12-01 | GFLV2，2011.12885v1 | W-0013 | PASS；[审计](../../00_Startup_Railway_UAV_Detection/Literature/W-0013_Audit.md) | P0，分布质量评分直接近邻，SCREENED |
| BTD12-02 | Multivariate Confidence Calibration，2004.13546v1 | W-0014 | PASS；[审计](../../00_Startup_Railway_UAV_Detection/Literature/W-0014_Audit.md) | P0，框尺寸条件校准直接近邻，SCREENED |
| BTD12-03 | [Generalized Focal Loss: Learning Qualified and Distributed Bounding Boxes for Dense Object Detection](https://arxiv.org/abs/2006.04388) | N/A | HOLD；源码引用／GFLV2前作线索，未独立全文审计 | 若另行实施分布质量方法，再核版本和完整协议；非新PASS |
| BTD12-04 | [Confidence Calibration for Object Detection and Segmentation](https://arxiv.org/abs/2202.12785) | N/A | HOLD；后续章节与W-0014的扩展／独立关系未审清 | 不自动分配新ID或拼接结果；如选工程校准路线再审 |

去重覆盖注册表、旧矩阵／阅读单、Markdown与PDF文件名。两项新PASS使用各自一个arXiv v1正文；CVF身份已核，PDF直访403，未逐字比较正式版本。没有新增PDF。

研究影响：I-2026-09-14-BTD12-01/02已更新[台账](../Innovation_Ledger.md)中P0-A-C1的Closest Prior Work、Existing Work、Remaining Gap、Novelty Risk，并回链实验计划。RQ-BTD12-1 DISMISSED，因为具体评分式暂无近邻外独立机制依据；不是已实测失败。旧区域机制保持HOLD，无必要次方向或Reading_List改动。

联动核验：两项各有唯一工作／版本参考、审计、19字段主矩阵和影响记录；PASS与SCREENED分开；本地链接及编号检查通过。HOLD未计新增，未虚报用户阅读完成。无模型训练／推理、保护附件或旧学习目录修改，无提交／推送。

交付：[BTD12报告](../../00_Startup_Railway_UAV_Detection/Literature/BTD12_Low_Score_Candidate_Review.md)。下一项为论文主张与投入方向决策；本批已触发停止条件，不自动创建BTD13或新机制实验。
