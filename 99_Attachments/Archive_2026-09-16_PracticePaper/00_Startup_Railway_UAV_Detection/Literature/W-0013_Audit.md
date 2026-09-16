# W-0013：GFLV2

- Title：Generalized Focal Loss V2: Learning Reliable Localization Quality Estimation for Dense Object Detection
- Authors：Xiang Li; Wenhai Wang; Xiaolin Hu; Jun Li; Jinhui Tang; Jian Yang
- Batch：2026-09-14-BTD12；Audit Date / Date Added：2026-09-14；Auditor：Codex
- Audit Status：PASS；Reading Status：SCREENED；Sync Status：COMPLETE
- 唯一技术正文：[arXiv v1，10页](https://arxiv.org/pdf/2011.12885v1)；[身份页](https://arxiv.org/abs/2011.12885)。

## 身份与版本

arXiv 2011.12885v1首次／版本日期2020-11-25，DOI 10.48550/arxiv.2011.12885，正式DOI Unknown。[CVF身份](https://openaccess.thecvf.com/content/CVPR2021/html/Li_Generalized_Focal_Loss_V2_Learning_Reliable_Localization_Quality_Estimation_for_CVPR_2021_paper.html)核对CVPR2021、pp11632–11641，published；会议2021-06（月级），精确上线日Unknown，early access N/A。本日CVF PDF直访403，采用公开arXiv正文，未逐字比对正式稿。内部载体C（技术参考副本），官方等级Unknown；撤稿库未独立核查。

去重：题名、GFLV2/DGQP、基础ID及既有PDF文件名无既有登记；GFLv1为不同工作线索，未合并。无旧ID。

## 技术证据

§3.2及式3：四边分布Top-k概率及均值输入轻量DGQP，估计定位质量参与排序；表4也比较直接联合评分。表2/4的COCO minival 5K、R50/12轮消融，GFLv1 AP40.2→41.1，表4均19.4FPS；勿将摘要对ATSS的差额全归因本模块。主实验训练trainval35k，COCO test-dev；硬件单2080Ti、batch1等见§4，完整I/O和整帧p95未明。不直接外推本机VisDrone。

## 项目判断

P0；次方向N/A。Must Read，SCREENED非DONE。Closest Innovation=N/A（RQ-BTD12-1方案观察，影响P0-A-C1）。Novelty Conflict=Direct：分布统计→质量→排序已覆盖；具体熵＋尺度公式仅Partial，未认定同构。冻结检测器适配与重新拟合的收益未知。

I-2026-09-14-BTD12-01 → [台账](../../00_Overview/Innovation_Ledger.md) → [候选审查](BTD12_Low_Score_Candidate_Review.md)。当前候选DISMISSED，不执行验证；若未来工程任务另行启动，唯一变量为评分信息组，固定框池比较现成统计质量与简单校准，无法独立解释收益则停止。Run ID=N/A。

PASS表示身份／正文足以支持重合判断，非复现或用户精读完成。注册表／主矩阵／四字段／周报同步，无必要次矩阵和Reading_List，无新增PDF。
