# 单篇论文审计：ESOD: Efficient Small Object Detection on High-Resolution Images

- Work ID / Legacy ID / Batch ID：W-0004 / N/A（既有索引无匹配）/ 2026-09-10-Mainline-A
- Audit Date / Auditor：2026-09-10 / Codex独立证据审查
- Audit Status：PASS
- Reading Status：SCREENED（定向核验，未登记为精读DONE）
- Sync Status：COMPLETE（注册表、矩阵、台账和本批周报已联动）
- 输入来源与定位：用户批准主线A后的指定直接近邻arXiv:2407.16424。

## 身份、出版与来源

本页全部URL访问日期为2026-09-10；页码为PDF顺序页码。

| 字段 | 值 | 一手来源URL、访问日期、页/节 |
|---|---|---|
| Title / Authors | ESOD: Efficient Small Object Detection on High-Resolution Images；Kai Liu、Zhihang Fu、Sheng Jin、Ze Chen、Fan Zhou、Rongxin Jiang、Yaowu Chen、Jieping Ye | [arXiv身份页](https://arxiv.org/abs/2407.16424) |
| DOI / arXiv base ID / version | 10.1109/tip.2024.3501853；2407.16424；v2 | [全文第1页](https://arxiv.org/pdf/2407.16424v2)明确印有正式DOI；[出版社提交的Crossref记录](https://api.crossref.org/works/10.1109/TIP.2024.3501853) |
| Year / Venue / Publication Status | 当前技术参考2024（arXiv v2）；正式论文IEEE Transactions on Image Processing 34:183–195（2025）；工作状态published | 不混同作者版本上线年与正式卷年；正式版正文未逐字比较 |
| First Preprint / Version Online Date | 2024-07-23 / 2024-12-17 | arXiv Submission history |
| Accepted / Early Access / Published Date | 接受2024-11-06；Early Access精确日未获出版社页面直接核验；正式卷年2025（月日Unknown） | PDF第1页接受日期；Crossref published-print=[2025]。Crossref created=2024-11-25不擅自充当Early Access日期 |
| 载体A–D / 正式等级体系与年份 | A（内部正式期刊级）；中科院/JCR/学校等级Unknown，本审计未查 | [项目等级规则](../../00_Overview/Paper_Reading_Guide.md) |
| 更正、撤回、撤稿状态 | arXiv未显示撤回标记；未完成独立全量更正排查 | arXiv身份页 |
| 已有工作匹配 / 版本关系 | 全仓库Markdown、注册表、PDF文件名无ESOD/同题/标识符匹配；v2全文中的DOI连接正式出版记录 | 仓库去重和上述一手证据；v1未逐版比较 |

## 技术证据

| 字段 | 作者报告的内容与原文定位 | 审计判断及证据局限 |
|---|---|---|
| Problem | 高分辨率小目标稀疏聚集，背景特征提取冗余；§I、图1 | 与主线A的核心动机直接重合，不能再把“避免背景计算”作为新发现 |
| Dataset（版本、规模、划分、预训练/泄漏） | §IV-A：VisDrone训练6471、验证548（用于评价）；UAVDT训练30视频23258帧、测试20视频15069帧；TinyPerson训练794/测试816 | 本次未核验具体文件、权重和视频清单；不推定其来源分组适用于铁路数据。没有UAV-RSOD结果 |
| Method（核心机制、区域来源、额外计算） | §III：复用早期特征，ObjSeeker预测前景掩码，AdaSlicer选择特征块，SparseHead进一步稀疏检测；训练掩码来自框生成Gaussian并结合SAM；推理使用预测掩码。ObjSeeker额外约1.2 GFLOPs（图3、表VI） | 不依赖测试真值框；SAM属训练监督来源，不能说推理零成本或完全无额外先验。特征切片与图像走廊裁剪不同，但机制冲突强 |
| Contribution（作者主张） | 联合复用特征、区域切片和稀疏头实现高分辨率检测；§III | 不将作者SOTA表述视为全领域核实结论 |
| Metrics（数值、表号、协议） | §IV-B/C：V100、测试batch=1；VisDrone输入长边1536。表III同YOLOv5路线：基线36.2 AP/264.9 GFLOPs/26.1 FPS；ESOD 36.0/119.5/36.4；输入×1.25后37.9/180.6/28.6 | 基线与ESOD同分辨率时并非AP提高；收益是节省开销后提高分辨率的折中。表IV同基线列30.5 FPS，与表III的26.1不同，原因未解释，不混表计算加速比 |
| 计时与预算 | §IV-B给同设备、batch；图10按保留块比例统计总延迟；§III-C承认迭代切片可能有额外延迟，提供并行简化版 | 未找到完整解码/预处理/NMS起止、预热和同步协议；平均FPS不证明硬截止时间。图10已有“块比例—延迟”分析，该分析形式本身不是新颖点 |
| Limitations（作者与审计分开） | 作者§IV-E：切片过小会截断目标，算法工程实现影响时延；审计：场景密度、区域漏检和额外监督影响可迁移性 | 表IV已有均匀/自适应/简化切片对照；只把均匀切片改成自适应不能默认算新贡献 |

证据：[arXiv v2全文](https://arxiv.org/pdf/2407.16424v2)，图2–5、10、§III–IV、表III–IV/VI；[对应HTML](https://arxiv.org/html/2407.16424v2)。所有数字为作者报告。

## 项目判断

- Related Paper：主P0；无必须新增次方向。类无关前景掩码不自动等于开放世界未知目标检测。
- Closest Innovation：P0-A-C1、P0-A-C2，见[创新台账](../../00_Overview/Innovation_Ledger.md)。
- Novelty Conflict：Direct（对“选择区域以节省背景计算，再支持更高分辨率”的广义机制）；具体铁路走廊与预算方案仅Partial重合，差异尚未验证。
- Reading Priority：Must Read；本批次授权定向核验，不自动复制其三模块设计或进入训练。
- 边界影响：主线A必须解释相对通用前景选择的增量；保持固定已知类别，不增加开放世界任务。
- 创新影响ID：I-2026-09-10-Mainline-A-04，已同步。
- 后续最小验证：先查候选方案是否重复其“区域覆盖—计算—召回”逻辑；若数据门通过，固定检测器与真实时间预算比较轨道先验、简单区域基线与通用区域选择，单独统计区域截断和区域漏检。候选仅因删掉更多目标而加速时停止。运行条目由[实验计划](../Experiments/Experiment_Plan.md)统一管理，本页未运行模型。
- 决策及证据缺口：PASS，技术足以识别高冲突；正式版逐字一致性、测速不一致原因和本地实现成本仍待核验。不得将“尚未铁路验证”写成新颖性已成立。
- Local Path/Reference：[唯一当前全文参考：arXiv v2](https://arxiv.org/pdf/2407.16424v2)。
- Date Added / Last Audited：2026-09-10 / 2026-09-10。

## 同步检查

- [x] 旧ID、注册表和正文名称已搜索。
- [x] 注册表与版本历史已更新，区分2024作者版本和2025正式卷年。
- [x] 主矩阵必填字段已同步。
- [x] 次方向入口已核对（本篇无必须新增次方向）。
- [x] P0-A-C1/C2四字段与影响已同步。
- [x] 周报已同步；全部完成后再改Sync Status为COMPLETE。
