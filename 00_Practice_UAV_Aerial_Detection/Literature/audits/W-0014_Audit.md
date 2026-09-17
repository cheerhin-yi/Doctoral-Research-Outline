# W-0014：检测多变量置信度校准

- Title：Multivariate Confidence Calibration for Object Detection
- Authors：Fabian Küppers; Jan Kronenberger; Amirhossein Shantia; Anselm Haselhoff
- Batch：2026-09-14-BTD12；Audit Date / Date Added：2026-09-14；Auditor：Codex
- Audit Status：PASS；Reading Status：SCREENED；Sync Status：COMPLETE
- 唯一技术正文：[arXiv v1，9页](https://arxiv.org/pdf/2004.13546v1)；[身份页](https://arxiv.org/abs/2004.13546)。

## 身份与版本

arXiv 2004.13546v1首次／版本日期2020-04-28，相关正式DOI 10.1109/cvprw50498.2020.00171。[CVF身份](https://openaccess.thecvf.com/content_CVPRW_2020/html/w20/Kuppers_Multivariate_Confidence_Calibration_for_Object_Detection_CVPRW_2020_paper.html)：CVPR2020 Workshops，SAIAD，published，元数据pp326–327。2020-06（月级），精确上线日Unknown，early access N/A。CVF PDF直访403，公开arXiv为本次技术正文；未认定9页版与两页会议记录逐字相同。内部载体D（Workshop），官方等级Unknown；撤稿库未独立核查。

去重：题名、作者、基础ID／DOI与既有PDF文件名无已登记工作。2202.12785后续章节的关系未审清，HOLD，不另分Work ID。无旧ID。

## 技术证据

§3–4将分数和框位置／尺度联合校准，提出D-ECE；不同维度／分箱的D-ECE不可直接互比。§5.1用COCO val2017许可筛选子集，70/30随机图像校准／评估、20次；三种预训练检测器；保留分数≥.3、NMS IoU.6，评价IoU.6/.75。表1c固定5维D-ECE、SSD、IoU.6：仅分数逻辑校准7.575%，多变量相关逻辑校准5.111%；这是校准误差，不是AP。§5.2讨论高维稀疏与过拟合。未提供本项目整帧时延，也未验证低于.25的无人机小目标恢复。

## 项目判断

P0；次方向N/A。Must Read，SCREENED非DONE。Closest Innovation=N/A（RQ-BTD12-1，影响P0-A-C1）。Novelty Conflict=Direct：尺寸条件校准已有；与分布统计组合的精确公式未认定相同。不能将校准改善等同检出改善。

I-2026-09-14-BTD12-02 → [台账](../../00_Overview/Innovation_Ledger.md) → [候选审查](BTD12_Low_Score_Candidate_Review.md)。当前DISMISSED，无实验；若以后工程验证，冻结同框池先比较无分布的类别／尺寸校准，隔离拟合和评价，以固定FP召回、AP和完整耗时判断，简单条件校准解释收益则停止新机制主张。Run ID=N/A。

PASS为技术审计，不代表复现或用户精读完成。注册表／主矩阵／四字段／周报同步，无必要次矩阵和Reading_List，无新增PDF。
