# W-0010：TIDE

- Title：TIDE: A General Toolbox for Identifying Object Detection Errors
- Authors：Daniel Bolya; Sean Foley; James Hays; Judy Hoffman
- Batch：2026-09-14-BTD10；Audit Date / Date Added：2026-09-14；Auditor：Codex
- Audit Status：PASS；Reading Status：SCREENED（不代填用户精读）；Sync Status：COMPLETE
- 唯一技术正文：[作者全文，23页含更正附录](https://dbolya.github.io/tide/paper.pdf)。身份：[arXiv](https://arxiv.org/abs/2008.08115)、[作者项目](https://dbolya.github.io/tide/)，本日访问。

## 身份与版本

ECCV 2020，published；arXiv 2008.08115，v1 2020-08-18、v2 2020-08-31；DOI 10.48550/arxiv.2008.08115，会议DOI及精确出版日Unknown，未补造。作者正文未与arXiv逐字比较，不能声称二者字节相同。内部载体C（本批用作者副本、未存正式出版PDF）；官方等级／年度分区Unknown，非投稿推荐。附录E明确更正v1.0.0对ignored detections的处理；v1.0.1改变LVIS归因，不能沿用旧结论。撤稿状态未作独立数据库核验，Unknown。

去重：已搜索仓库Markdown、旧矩阵／阅读单、PDF文件名，未命中题名或2008.08115；同缩写的few-shot TIDE不是本工作，无旧ID。

## 技术证据

| 项 | 原文定位及审计摘要 |
|---|---|
| 问题／方法 | §2、图1、式2：分类、定位、两者兼有、重复、背景、漏检分解；各oracle从原预测独立计算ΔAP |
| 数据／协议 | §3及附录B.3：COCO、VOC、Cityscapes、LVIS；既有模型／预测，非统一预算重训比较；本批未复现其各来源划分 |
| 指标 | 附录表3：COCO Mask R-CNN，IoU阈值0.5时AP61.7、定位错误ΔAP6.2；阈值0.9时AP12.0、定位ΔAP55.1。均为作者结果，非本项目指标 |
| 贡献／局限 | 独立归因避免顺序修复偏差；附录A说明各ΔAP不具可加性。GT oracle不可部署，错误类别不等于网络因果。实时检测耗时不适用该工具贡献；本项目ignore适配未核验 |

## 项目判断与同步

主方向P0；次方向N/A（无必要交叉引用）。Closest Innovation=N/A（诊断工具），影响P0-A-C1/C2的证据解释与BTD11。Novelty Conflict=Partial：错误分解已存在，不是本项目创新；Reading Priority=Must Read，供AI诊断设计，不作为用户学习门。

I-2026-09-14-BTD10-01 → [创新台账](../../00_Overview/Innovation_Ledger.md) → [BTD11预案](../Experiments/Experiment_Plan.md)。唯一变量为错误修复类型；固定预测与评价，不能相加上界；语义不兼容则停止并报告Unknown，不冒充官方TIDE。边界无变更；Run ID=N/A。

PASS理由：公开全文与身份足以支持诊断方法及限制判断。技术实验未复现；出版细目Unknown不影响此用途。注册表、主矩阵、影响四字段和[周报](../../00_Overview/Weekly_Literature_Audits/Weekly_Literature_Audit_2026-09-14.md)已联动；无必要次方向／现有主题Reading_List。仅稳定链接，无新增PDF。
