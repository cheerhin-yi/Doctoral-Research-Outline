# 主线A检索记录

检索日2026-09-10；本批为定向审查。

## 主线A批次 2026-09-10-Mainline-A

| ID | 来源／检索式 | 范围与实际处置 |
|---|---|---|
| A-S01 | 指定六入口题名及DOI/arXiv，出版社、arXiv、Crossref、Europe PMC、Zenodo/DataCite | 首批六篇定向全文审计；未统计数据库总命中数，不能填伪精确返回数 |
| A-S02 | `"aerial" "object detection" "adaptive" "slicing" 2025 2026` | 搜索引擎→一手来源；发现MRU-YOLO、GOIS、ASAI、ASAHI及高度引导切片等线索；身份与全文状态见周报 |
| A-S03 | `"railway" "corridor" "object detection" "UAV" slicing` | 未得到足以确认完整同构铁路毫秒预算方法的证据；不能据此声称不存在 |
| A-S04 | `"ClusDet" "DMNet" "AutoFocus" detection` | 聚类／密度／Focus方法作为继续查新的追溯方向，本批不宣称已全文审计这些经典工作 |
| A-S05 | `"time budget" "aerial" "object detection" slicing`；`"railway" "adaptive slicing" detection UAV` | 部分返回偏离任务；不以无相关结果推断新颖性 |
| A-S06 | `"UAV-RSOD" "Zenodo"`及官方记录API | 记录12606374；许可CC BY 4.0；上午多次超时，下午恢复后下载原包并校验 |

检索局限：非系统综述，未覆盖付费数据库完整索引、所有非英文工作和所有版本；截至执行日的新颖性结论为High风险／差异待验证。相似缩写ASAHI的不同题名／作者条目不未经核实合并。PASS、HOLD和重复数量以[本批周报](../../00_Overview/Weekly_Literature_Audits/Weekly_Literature_Audit_2026-09-10.md)为准。

## 2026-09-10-A0-02：既有数据来源补证

沿用W-0001，未新增论文或正文。检索式、官方版本与代码入口、访问失败及停止范围见[A0-02](../Experiments/A0-02_Data_Gap_Followup.md)。当前检查范围未补齐原图框、派生映射或独立分组，维持HOLD；不将未命中解释为资料绝不存在。

## 2026-09-10-A0-04：范围调整与数据官方入口预审

仅核查VisDrone官方数据仓库、下载页和DET工具包，补查学术用途说明。未开展新增论文全文审计，新增Work ID/PASS/PDF均0。用户接受弱化铁路场景；当前下一项A0-05文件审计。见[VisDrone预审](../Experiments/VisDrone_Feasibility_Audit.md)。

## 2026-09-11-A0-09：单候选定向补证

本批只审查检测反馈／顺序选区／剩余预算，复用既有全文审计；不是系统综述。实际执行六条检索式：

1. `object detection sequential zoom selection feedback remaining time budget marginal utility image regions`
2. `"MRU-YOLO" "conditional" oracle`
3. `"object detection" "adaptive" "zoom" "sequential" budget`
4. `"Dynamic Zoom-in Network" CVPR 2018 Gao`
5. `"object detection" "remaining budget" "region" sequential`
6. `"object detection" "feedback" "region selection" time budget`

选入处置的3项：新增PASS 1（W-0008 Dynamic Zoom-in Network，正式CVF全文10页）；新增HOLD线索1（SRENet）；既有重复／复用1（W-0007 MRU）。版本更新0，仓库新增PDF 0；不把一般噪声计为已审论文，也未统计全库总命中数。先查题名、DOI、arXiv与既有PDF文件名去重，再核验全文。

W-0008的CVF网页工具访问失败后，经普通HTTPS读取正式PDF，并以arXiv、Crossref核对身份；正文只登记稳定CVF链接。MRU本轮HTML限流，复用既有审计，不宣称新版本补审。SRENet：Selective region enlargement network for fast object detection in high resolution images，Neurocomputing 462:402–411（2021），DOI 10.1016/j.neucom.2021.08.015；[出版社入口](https://www.sciencedirect.com/science/article/pii/S0925231221011991)摘要显示顺序放大关系，全文实验未核验，作者信息本批Unknown，保留HOLD且不分配Work ID。

已存在的ClusDet／DMNet／AutoFocus／GOIS／ASAHI等HOLD未重开。未穷尽付费库、非英文和引用网络；当前候选差异不足，不等于证明完全同构或无人做过。见[候选结论](../reviews/A0-09_Candidate_Review.md)、[W-0008审计](../audits/W-0008_Audit.md)和[周报](../../00_Overview/Weekly_Literature_Audits/Weekly_Literature_Audit_2026-09-10.md)。本批止损，返回用户方向决策。

## 2026-09-12-N1：创新候选定向查新

实际检索跨2026-09-11至09-12（北京时间）；下列为主任务实际执行的17条查询，不是数据库完整覆盖记录。使用网页检索及arXiv／CVF原文跟进，复用已审计近邻；近期检索窗口并非所有查询统一的筛选条件，也没有独立完成Google Scholar／Semantic Scholar全库或引用链穷举。定向批次不推进七方向每周检索的成功覆盖日期。

| 序号 | 实际检索式 |
|---|---|
| N1-01 | `small object detection adaptive zoom missed detections regions no coarse detection risk calibration conformal budget` |
| N1-02 | `object detection selective zoom low confidence dense predictions small objects adaptive slicing recovery utility` |
| N1-03 | `"small object detection" "overlap" "marginal" "regions"` |
| N1-04 | `"zoom" "detection" "submodular" selection` |
| N1-05 | `"adaptive slicing" "redundancy" "2026" detection` |
| N1-06 | `site:arxiv.org 2026 "adaptive" "slicing" "confidence" detection` |
| N1-07 | `site:arxiv.org 2025 2026 "small object" "missed" "region selection"` |
| N1-08 | `site:openreview.net 2025 2026 "object detection" "zoom"` |
| N1-09 | `site:arxiv.org "small object detection" "response" "slicing" 2026` |
| N1-10 | `"object detection" "pre-NMS" "region" "zoom"` |
| N1-11 | `"small object" "scale sensitivity" "inference"` |
| N1-12 | `"object detection" "cross-scale consistency" "region selection"` |
| N1-13 | `"small object detection" "local contrast" "inference" "slicing"` |
| N1-14 | `site:arxiv.org "adaptive" "slicing" detection after:2026-03-12 before:2026-09-13` |
| N1-15 | `"AutoFocus: Efficient Multi-Scale Inference" "2019" "9749"` |
| N1-16 | `"ViCrop-Det" "github"` |
| N1-17 | `"object detection" "weak responses" "cross-scale" "inference"` |

第15条页码为检索提示，后续CVF正式页核得9745–9755，以原文为准。风险校准／子模等查询仅为排除已有覆盖，没有采纳为新机制或增加研究方向。

工作级处置：AutoFocus原A10 HOLD完成全文补审后首次PASS为W-0009（唯一arXiv v2正文）；ViCrop-Det新增HOLD线索（公开HTML已读，版本／数据与FPS口径待澄清）；ASAHI2026原A14仅复核arXiv身份，继续HOLD，不与2023 ASAHI按缩写合并。其他返回结果未作为有效近邻进入审计，不由搜索噪声产生Work ID。

直接访问证据与段落定位见[W-0009](../audits/W-0009_Audit.md)、[ViCrop-Det HOLD](../reviews/ViCrop_Det_HOLD_Review.md)。既有SAHI／QueryDet／ESOD／ROI-Gated／MRU／DZN证据用于比较，不记新论文或新版本。没有新增PDF、模型运行或效果结果。

novelty-check要求的独立反驳子任务因额度失败，没有取得结果或重试；不能声称外部／跨模型复核通过。该限制连同近期工作未穷尽的限制保留在[候选报告](../reviews/Weak_Response_Candidate_Review.md)中。


## 2026-09-14-BTD10：强基线后的问题重审

定向查新截止实际执行日2026-09-14。先搜索全仓Markdown、既有矩阵／阅读单和PDF文件名中的TIDE、Wasserstein/NWD、Adaptive NMS/Soft-NMS及基础ID，三项无旧工作命中，最大既有编号W-0009。初轮查询的完整逐字日志未保留，不能声称检索可完全重放；保留如下可回读的实际查询及全部进入处置的来源：

1. `site:arxiv.org "2025" "2026" "tiny object" "localization" "NMS"`
2. `site:mdpi.com "Tiny Object Detection via Normalized Gaussian Label Assignment and Multi-Scale Hybrid Attention"`

随后直接核验arXiv 2008.08115、2110.13389、1904.03629及作者／CVF来源，正文定位见W-0010–W-0012。CVF直接页/PDF出现Internal Error，Adaptive NMS改读arXiv v1，未宣称正式稿逐字一致。NWD扩展工作2206.13996不直接合并或新分ID。TIDE同缩写few-shot工作不与2008.08115合并。

工作级处置8项：新增PASS3、HOLD5、重复0、版本更新0、REJECT0；一般搜索噪声和复用既有审计不计本批新输入。BCDet、ContextTiny-Net、机场YOLOv7、NWD扩展和Soft-NMS各自缺口见[本批周报](../../00_Overview/Weekly_Literature_Audits/Weekly_Literature_Audit_2026-09-14.md)。近期工作未穷尽，不声称新颖性查清。无新增PDF、代码下载或模型运行；不推进七方向周检索成功覆盖日期。

## 2026-09-14-BTD12：低分单机制直接近邻

实际执行日期2026-09-14，Asia/Shanghai；定向审查，非全领域穷尽检索，不推进七方向周检成功覆盖日期。先查注册表、全库Markdown／旧矩阵／阅读单及保护目录PDF文件名；GFLV2、DGQP、Multivariate Confidence Calibration、Küppers、2011.12885、2004.13546及DOI无既有工作命中。

实际检索式：

- `site:openaccess.thecvf.com "Generalized Focal Loss V2"`
- `site:openaccess.thecvf.com "Multivariate Confidence Calibration" object detection`
- `site:arxiv.org 2025 2026 tiny object distribution focal quality confidence calibration`
- `site:arxiv.org "Multivariate Confidence Calibration for Object Detection"`

CVF身份页与arXiv身份、全文交叉核验；CVF两项PDF直访403，改用公开arXiv v1，不绕过限制。全文定位及实验口径见W-0013/14审计。近期检索不足以排除全部近邻；已有BTD10 BCDet等HOLD不重复计入新增。

本批4工作线索：W-0013/14新PASS；GFLv1 2006.04388和校准扩展2202.12785 HOLD，未独立全文／版本关系审完。普通focal-loss搜索噪声不计工作候选。没有新增PDF、用户精读DONE、模型或论文复现运行。处置与联动见本日周报BTD12批次。
