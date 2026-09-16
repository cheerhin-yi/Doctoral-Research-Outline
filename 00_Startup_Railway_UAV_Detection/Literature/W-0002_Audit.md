# 单篇论文审计：Slicing Aided Hyper Inference and Fine-tuning for Small Object Detection

- Work ID / Legacy ID / Batch ID：W-0002 / N/A（既有索引无匹配）/ 2026-09-10-Mainline-A
- Audit Date / Auditor：2026-09-10 / Codex独立证据审查
- Audit Status：PASS
- Reading Status：SCREENED（已定向核验方法、结果和局限，未登记为精读DONE）
- Sync Status：COMPLETE（注册表、矩阵、台账和本批周报已联动）
- 输入来源与定位：用户批准主线A后的直接近邻审计；指定arXiv:2202.06934。

## 身份、出版与来源

本页全部URL访问日期为2026-09-10；页码为PDF顺序页码。

| 字段 | 值 | 一手来源URL、访问日期、页/节 |
|---|---|---|
| Title / Authors | Slicing Aided Hyper Inference and Fine-tuning for Small Object Detection；Fatih Cagatay Akyon、Sinan Onur Altinuc、Alptekin Temizel | [arXiv身份页](https://arxiv.org/abs/2202.06934) |
| DOI / arXiv base ID / version | 10.1109/icip46576.2022.9897990；2202.06934；v5 | [IEEE出版页](https://doi.org/10.1109/ICIP46576.2022.9897990)及arXiv身份页 |
| Year / Venue / Publication Status | 2022；IEEE ICIP；published；技术审计副本为arXiv v5，不冒称逐字核对过IEEE最终版 | IEEE出版页；[当前全文](https://arxiv.org/pdf/2202.06934v5) |
| First Preprint / Version Online Date | 2022-02-14 / 2022-10-24 | arXiv Submission history；中间版本未逐版技术比较 |
| Early Access / Published Date | N/A（会议论文）/ IEEE Xplore上线2022-10-18；会议2022-10-16至19 | IEEE出版页；上线日与会议日期分别记录 |
| 载体A–D / 正式等级体系与年份 | A（仓库内部会议载体等级）；中科院/JCR/学校等级Unknown，本审计未核验 | [项目等级规则](../../00_Overview/Paper_Reading_Guide.md) |
| 更正、撤回、撤稿状态 | 所访问身份页未显示撤回标记；未完成独立全量更正排查 | arXiv身份页；不作“绝无更正”保证 |
| 已有工作匹配 / 版本关系 | 注册表、全仓库Markdown及PDF文件名未发现同题、SAHI或标识符匹配；arXiv直接关联ICIP DOI，为同工作 | 2026-09-10仓库去重；arXiv Related DOI |

## 技术证据

| 字段 | 作者报告的内容与原文定位 | 审计判断及证据局限 |
|---|---|---|
| Problem | 小目标在整图缩放后像素不足；§3 | 与主线A的分辨率问题直接相邻；没有铁路专属论证 |
| Dataset（版本、规模、划分、预训练/泄漏） | VisDrone2019-DET：训练6471、验证548，表1评测test-dev；xView按75%/25%随机划分训练/验证；§4、PDF第3页。框架预训练和切片微调见§3 | 不把VisDrone验证集与表1 test-dev混同；xView未给可独立复核的地理分组清单，本次未审查数据文件或权重 |
| Method（核心机制、输入输出、比较对象） | 原图重叠切片、放大后逐片检测、坐标回映与NMS；可加入整图预测，也可切片微调；§3、图2。区域来自均匀网格，不依赖目标标注生成测试ROI | 每片均有前向开销；整图分支、重叠和融合也有成本。它是主线A必须比较的切片基线 |
| Contribution（作者创新主张） | 通用切片推理及微调流程；§3 | 不接受“局部放大＋融合”作为主线A的新颖性依据 |
| Metrics（数值、协议、表号） | 表1：TOOD+FI为AP50=29.4、AP50-small=18.1；+SAHI+FI+PO为34.7、23.8；再有SF为43.5、31.7。§4明确IoU=0.5、maxDets=500；VisDrone推理切片640×640、PO=25% | 前一对照AP50增加5.3个百分点，不是AP50–95；含SF的一行改变训练，不能把全部增益归因于推理策略。未报告可复核硬件FPS、计时起止或固定延迟预算 |
| Limitations（作者与审计分开） | 作者§3/§5：切片可能截断大目标，计算时间随切片增加；审计：未验证铁路数据或硬预算 | 摘要中的FCOS“+6.8”与v5表1所列25.8→31.0并不对应；本审计只采用逐行可核对的TOOD值，不能盲抄摘要提升 |

全文证据：[arXiv v5 PDF](https://arxiv.org/pdf/2202.06934v5)，§3–5、表1–2；[对应HTML](https://arxiv.org/html/2202.06934v5)。以上为作者报告，不是本项目复现结果。

## 项目判断

- Related Paper：主P0；无必须新增的次方向。向Paper 1交付已知检测基线是项目接口，不构成开放世界或风险排序证据。
- Closest Innovation：P0-A-C1、P0-A-C2（均待验证），见[创新台账](../../00_Overview/Innovation_Ledger.md)。
- Novelty Conflict：Partial；“切片放大＋整图/局部融合”已覆盖；本文未给轨道走廊先验与固定端到端预算的实证，但本次未检出不等于不存在。
- Reading Priority：Must Read；用户本批次已授权定向审计；不因此解除模型与实验阶段门。
- 边界影响：主线A必须承认SAHI为直接基线，不恢复旧LSM-Head；不增加模型模块。
- 创新影响ID与台账链接：I-2026-09-10-Mainline-A-02；对应P0-A-C1/C2，已同步。
- 后续最小验证：唯一变量为区域选择，检测器和训练固定；比较完整网格与候选区域策略的AP50–95、Recall-small、端到端p50/p95、区域漏检及实际切片数。若完整计时后候选不能形成更优折中，停止该策略；本页只提议，运行继续受[实验计划](../Experiments/Experiment_Plan.md)阶段门约束。
- 决策及证据缺口：PASS，身份与技术证据足以确立直接相关性；尚缺同预算复现、代码版本冻结和铁路适用性。PASS不证明作者每个数字一致或主线A创新成立。
- Local Path/Reference：[唯一当前全文参考：arXiv v5](https://arxiv.org/pdf/2202.06934v5)；未在项目新增PDF。
- Date Added / Last Audited：2026-09-10 / 2026-09-10。

## 同步检查

- [x] 旧ID、正文文件名和全仓库Markdown已搜索。
- [x] 全局注册表和版本历史已更新。
- [x] 主Literature Matrix必填字段已同步。
- [x] 次方向交叉引用已核对（本篇无必须新增次方向）。
- [x] P0-A-C1/C2四字段及影响记录已同步。
- [x] 周报已记录；全部完成后再改Sync Status为COMPLETE。
