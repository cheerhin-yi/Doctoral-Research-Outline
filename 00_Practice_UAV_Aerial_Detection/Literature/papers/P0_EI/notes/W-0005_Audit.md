# 单篇论文审计：ROI-Gated SAHI: Content-Adaptive Slicing-Based Inference for Efficient Object Detection

- Work ID / Legacy ID / Batch ID：W-0005 / N/A（既有索引无匹配）/ 2026-09-10-Mainline-A
- Audit Date / Auditor：2026-09-10 / Codex独立证据审查
- Audit Status：PASS（用于直接冲突与负面证据，不代表接受其全部效果主张）
- Reading Status：SCREENED（定向核验，未登记精读DONE）
- Sync Status：COMPLETE（注册表、矩阵、台账和本批周报已联动）
- 输入来源与定位：主线A直接近邻arXiv:2608.23923。

## 身份、出版与来源

本页全部URL访问日期为2026-09-10。

| 字段 | 值 | 一手来源URL、访问日期、页/节 |
|---|---|---|
| Title / Authors | ROI-Gated SAHI: Content-Adaptive Slicing-Based Inference for Efficient Object Detection；Rashid Riyadh、Abd Ullah Khan、Imad Gohar、Muzammil Behzad | [arXiv身份页](https://arxiv.org/abs/2608.23923) |
| DOI / arXiv base ID / version | 10.48550/arxiv.2608.23923（仓储DOI，不是期刊DOI）；2608.23923；v1 | arXiv身份页 |
| Year / Venue / Publication Status | 2026；arXiv；preprint（未核实同行评审发表） | arXiv身份页 |
| First Preprint / Version Online Date | 2026-08-25 / 2026-08-25 | arXiv Submission history |
| Early Access / Published Date | N/A / N/A（尚无正式发表证据） | 不把上传日期写成期刊发表日期 |
| 载体A–D / 正式等级体系与年份 | C（预印本）；中科院/JCR/学校等级N/A（非已核验期刊论文） | [项目等级规则](../../00_Overview/Paper_Reading_Guide.md) |
| 更正、撤回、撤稿状态 | 身份页仅v1，未显示撤回；未完成全量更正检索 | arXiv身份页 |
| 已有工作匹配 / 版本关系 | 注册表、全仓库Markdown和PDF文件名无同题/ROI-Gated/标识符匹配 | 2026-09-10仓库去重；不与SAHI原论文合并Work ID |

## 技术证据

| 字段 | 作者报告的内容与原文定位 | 审计判断及证据局限 |
|---|---|---|
| Problem | 全图SAHI对背景切片产生冗余；§III | 与主线A直接重合 |
| Dataset（版本、规模、划分、预训练/泄漏） | COCO128全128图；另选其中3图作案例；YOLOv8n/s均使用COCO预训练且不微调；§III-A/G、§IV-C | §III-D明确在同一COCO128全split校准τ，再在该split报告，缺独立调参/测试；本次未审查COCO预训练与这128图的重叠清单，不证明无泄漏 |
| Method（区域来源、额外计算） | YOLOv8n在416×416上生成框，扩边15%，ROI内640×640切片由YOLOv8s精检，合并预测并NMS；覆盖率≥0.40时回退Full SAHI；§III-B/D、Algorithm1 | ROI来自预测框，不是轨道先验；前置检测、框合并、路由、裁剪、精检和NMS都有成本。“区域选择＋密集时回退”已存在 |
| Contribution（作者主张） | 无需额外训练的区域门控及自适应路由；§III | 不把其平均加速理解为硬预算保证 |
| Metrics（数值、协议、表号） | 表I：Full SAHI为263.73 ms、mAP50=0.7569；静态ROI为298.24 ms、0.6602；τ=0.40混合路由为258.46 ms、0.7305，26/128图走ROI；表III三图平均比值3.41× | 静态方案平均更慢且更差；混合方案约1.02×同时有精度损失。三图结果不代表全体；Agreement F1/IoU只比较两模型输出一致性，不是对真值准确率 |
| 计时与预算 | §III-C模型显式包含额外常数开销C；实现节称测执行时间 | 全文未明确硬件型号、batch、预热、重复次数、GPU同步及计时起止；公式没有逐项证明实测包含所有预处理/NMS，因此端到端边界Unknown |
| Limitations（作者与审计分开） | 作者§IV-E承认proposal漏检不可恢复，阈值跨数据集泛化受限；审计：实验样本和调参隔离不足 | 式(5)以ROI面积求和，Algorithm1用并集面积，定义不一致；§IV-E局部概括与表I分组结果不完全一致，应以表I具体行作为证据 |

证据：[可访问的arXiv v1完整HTML](https://arxiv.org/html/2608.23923v1)，§III–IV、Algorithm1、表I–V。PDF直链本次取回失败，但HTML包含方法、表格、讨论和参考文献，不是摘要替代。

## 项目判断

- Related Paper：主P0；无必须新增次方向；与Paper 1未知检测/风险排序无直接证据关系。
- Closest Innovation：P0-A-C1、P0-A-C2，见[创新台账](../../00_Overview/Innovation_Ledger.md)。
- Novelty Conflict：Direct；ROI筛选、局部高分辨率精检、NMS融合、覆盖率阈值回退均已覆盖。轨道走廊来源和预先固定的端到端预算可能构成待检验差异，不能仅因换场景而认定创新。
- Reading Priority：Must Read，包含最直接反例；预印本身份不降低对新颖性风险的警示价值。
- 边界影响：不把简单ROI或fallback命名为新方法；不因本文效果有限就忽略其先例。
- 创新影响ID：I-2026-09-10-Mainline-A-05，已同步。
- 后续最小验证：只在训练/校准侧选阈值；对测试固定策略，分别报告区域来源、并集覆盖率、切片数、区域漏检、AP50–95和全链路p95。如果预算内增益不能超过简单裁剪或只来自测试调参，停止。目标为[实验计划](../Experiments/Experiment_Plan.md)，本页仅文献审计。
- 决策及证据缺口：PASS，身份和全文足以支持机制冲突/负面结果判断；不将硬件、完整计时和未见过测试集上的泛化标为已验证。正式复现前必须补齐这些条件。
- Local Path/Reference：[唯一当前全文参考：arXiv v1 HTML](https://arxiv.org/html/2608.23923v1)。
- Date Added / Last Audited：2026-09-10 / 2026-09-10。

## 同步检查

- [x] 全仓库旧记录和PDF文件名已搜索。
- [x] 注册表与版本历史已同步。
- [x] 主矩阵必填字段已同步。
- [x] 次方向已核对（本篇无必须新增次方向）。
- [x] P0-A-C1/C2四字段已同步。
- [x] 周报记录负面结果和技术缺口；全部完成后再改Sync Status为COMPLETE。
