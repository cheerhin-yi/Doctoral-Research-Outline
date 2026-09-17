# W-0011：NWD

- Title：A Normalized Gaussian Wasserstein Distance for Tiny Object Detection
- Authors：Jinwang Wang; Chang Xu; Wen Yang; Lei Yu
- Batch：2026-09-14-BTD10；Audit Date / Date Added：2026-09-14；Auditor：Codex
- Audit Status：PASS；Reading Status：SCREENED；Sync Status：COMPLETE
- 唯一技术正文：[arXiv v2，12页](https://arxiv.org/pdf/2110.13389v2)；[身份页](https://arxiv.org/abs/2110.13389)，本日访问。

## 身份与版本

arXiv 2110.13389；v1 2021-10-26、v2 2022-06-14；引用年2022；DOI 10.48550/arxiv.2110.13389；当前副本preprint（页1标Under review）。内部载体C，正式等级Unknown，正式出版／early access N/A（不将扩展版等同本副本）。身份页声明存在ISPRS扩展工作；2206.13996的独立贡献与合并关系待审，HOLD，不分配第二Work ID、不把两版结果拼接。撤稿数据库未独立核验，Unknown。

去重：仓库题名、NWD、Wasserstein、基础ID及PDF文件名无已有工作命中；无旧ID。作者仓库为身份页所链jwwangchn/NWD，本轮不下载代码。

## 技术证据

| 项 | 原文定位及审计摘要 |
|---|---|
| 问题／方法 | §3、式4/8/9：框高斯化，以归一化Wasserstein相似度替换分配、NMS、回归损失中的IoU |
| 数据／训练 | §4：AI-TOD八类28036图、700621实例；另有VisDrone；ImageNet预训练R50/FPN，SGD12轮，batch8、4×Titan X。表4是AI-TOD test、表5是VisDrone val；来源级隔离未核验 |
| 指标 | 表4 Faster R-CNN AP11.1→17.8，+6.7个百分点；表5 VisDrone AP50 38.0→38.5，不能把AI-TOD增量搬至VisDrone |
| 贡献／局限 | 小框度量敏感性及分配改进已覆盖。§4.2单独替换R-CNN NMS反降，全部替换不优于仅RPN；不支持任意替换保证收益。当前anchor-free YOLO11n适用性需另证；完整端到端时延Not reported |

## 项目判断与同步

主方向P0；次方向N/A。Closest Innovation=N/A（BTD10切入点一尚未形成新主张）；影响P0-A-C1/C2的主张收缩。Novelty Conflict=Direct（若仅提出“小框敏感，换距离／损失”）；不声称其直接覆盖旧弱响应实现。Reading Priority=Must Read。

I-2026-09-14-BTD10-02 → [台账](../../00_Overview/Innovation_Ledger.md) → [实验预案](../Experiments/Experiment_Plan.md)。后续先以现有预测区分定位／低分与未观察到输出；只改变诊断修复类型。无定位瓶颈则不提出新损失；有空间也不自动采用NWD。边界调整仅建议，训练／结构改动未开放；Run ID=N/A。

PASS是冲突证据审计，不等于同行评审或本机复现。注册表含版本关系，主矩阵、影响四字段和[周报](../../00_Overview/Weekly_Literature_Audits/Weekly_Literature_Audit_2026-09-14.md)已同步。无必要次方向／主题Reading_List，无新增PDF。
