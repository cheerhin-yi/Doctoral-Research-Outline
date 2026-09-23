# 单篇论文审计：QueryDet: Cascaded Sparse Query for Accelerating High-Resolution Small Object Detection

- Work ID / Legacy ID / Batch ID：W-0003 / N/A（既有索引无匹配）/ 2026-09-10-Mainline-A
- Audit Date / Auditor：2026-09-10 / Codex独立证据审查
- Audit Status：PASS
- Reading Status：SCREENED（定向核验，未登记为精读DONE）
- Sync Status：COMPLETE（注册表、矩阵、台账和本批周报已联动）
- 输入来源与定位：用户批准主线A后的指定直接近邻QueryDet/CVPR2022。

## 身份、出版与来源

本页全部URL访问日期为2026-09-10；页码为PDF顺序页码。

| 字段 | 值 | 一手来源URL、访问日期、页/节 |
|---|---|---|
| Title / Authors | QueryDet: Cascaded Sparse Query for Accelerating High-Resolution Small Object Detection；Chenhongyi Yang、Zehao Huang、Naiyan Wang | [arXiv身份页](https://arxiv.org/abs/2103.09136)；[CVF记录](https://openaccess.thecvf.com/content/CVPR2022/html/Yang_QueryDet_Cascaded_Sparse_Query_for_Accelerating_High-Resolution_Small_Object_Detection_CVPR_2022_paper.html) |
| DOI / arXiv base ID / version | 10.1109/cvpr52688.2022.01330；2103.09136；v2 | [出版社提交的Crossref记录](https://api.crossref.org/works/10.1109/CVPR52688.2022.01330)；arXiv身份页 |
| Year / Venue / Publication Status | 2022；IEEE/CVF CVPR；published；当前技术参考为arXiv v2 | Crossref、CVF；[全文](https://arxiv.org/pdf/2103.09136v2) |
| First Preprint / Version Online Date | 2021-03-16 / 2022-03-24 | arXiv Submission history |
| Early Access / Published Date | Unknown / 2022-06（仅核实到月） | Crossref published-print；created不当作出版日 |
| 页码版本差异 | IEEE/Crossref为13658–13667；CVF页面为13668–13677 | 两个一手记录存在页码差异，不自行合并；本文技术定位使用arXiv PDF页/表 |
| 载体A–D / 正式等级体系与年份 | A（内部载体级）；中科院/JCR/学校等级Unknown，本批次未查 | [项目规则](../../00_Overview/Paper_Reading_Guide.md) |
| 更正、撤回、撤稿状态 | arXiv未显示撤回标记；未完成独立全量更正检索 | arXiv身份页 |
| 已有工作匹配 / 版本关系 | 全仓库Markdown、PDF文件名及注册表无题名/QueryDet/标识符匹配；CVF、arXiv与Crossref题名和作者一致 | 仓库去重及上述一手记录；未逐字比较最终版与v2 |

CVF页面可经搜索索引读取，但全文直链本次取回失败；arXiv v2全文可正常访问。未因此将摘要当作完整技术证据。

## 技术证据

| 字段 | 作者报告的内容与原文定位 | 审计判断及证据局限 |
|---|---|---|
| Problem | 高分辨率FPN检测头在背景位置耗费计算；§1、§3 | 与主线A减少背景计算的动机直接重合 |
| Dataset（版本、划分、预训练/泄漏） | COCO mini-val、VisDrone validation评测；VisDrone训练图分成4个无重叠块；§4.1、表1–2 | 本文给定训练/评测集合但本次未核查实际文件清单；不把训练切片视为测试ROI。精确数据发布版本、预训练权重哈希、来源分组无本次核验证据 |
| Method（区域来源、额外计算） | QueryHead在低分辨率特征预测小目标粗位置，CSQ逐级引导高分辨率稀疏卷积；§3、图1。位置来自模型预测，训练有额外监督；默认从P4查询、阈值0.15 | 不是轨道走廊图像裁剪；需要完整特征主干、查询及稀疏操作。不能把“粗定位→精检测”本身称为新方法 |
| Contribution（作者主张） | 利用查询减少高分辨率头的空间计算；§1/§3 | 只支持已有机制，作者泛化说法不代替部署实测 |
| Metrics（数值、表号、协议） | PDF第5页表1，COCO：RetinaNet 37.46 AP/13.60 FPS；高分辨率QueryDet无CSQ 38.53/4.85；有CSQ 38.36/14.88。表2，VisDrone相应为26.21/2.63、28.35/1.16、28.32/2.75 | “约3倍”主要相对高分辨率无CSQ，不是原始RetinaNet。§1标明2080Ti；训练用8卡不等于测速8卡。正文未提供足够计时起止、预热、I/O/NMS说明，端到端口径Unknown |
| Limitations（作者与审计分开） | 作者§4讨论查询阈值及上下文；审计：依赖查询召回、稀疏实现和场景密度，不能由平均FPS推出每帧预算保证 | 图4已有输入尺寸下的AP/FPS折中；本次未核验机载平台表现 |

全文证据：[arXiv v2](https://arxiv.org/pdf/2103.09136v2)，§3–4、表1–5、图4；[作者代码入口](https://github.com/ChenhongyiYang/QueryDet-PyTorch)可作后续实现核对，本次未运行。

## 项目判断

- Related Paper：主P0；无必须新增次方向。没有开放世界或风险排序实验。
- Closest Innovation：P0-A-C1、P0-A-C2，见[创新台账](../../00_Overview/Innovation_Ledger.md)。
- Novelty Conflict：Partial；低成本粗定位后对高分辨率位置选择性计算已覆盖；主线A的轨道先验和端到端预算必须另给实质证据。
- Reading Priority：Must Read；当前只进行用户已授权的定向审计，模型运行另受阶段门约束。
- 边界影响：将QueryDet列为机制近邻；不得为模仿它而自动引入稀疏头等第二模块。
- 创新影响ID：I-2026-09-10-Mainline-A-03，已同步。
- 后续最小验证：先核查主线A是否只是在图像空间重述已有粗到细流程；若可行性门通过，再固定检测器比较区域来源，测区域覆盖/漏检、实际端到端延迟和小目标召回。简单先验不能优于通用区域选择时，收缩轨道先验贡献；目标文件为[实验计划](../Experiments/Experiment_Plan.md)，本页不新建运行。
- 决策及证据缺口：PASS，全文足以确立机制重合与基线比较；测速全链路、版本逐字差异和数据清单仍待核验。论文速度不能直接移植到本项目。
- Local Path/Reference：[唯一当前全文参考：arXiv v2](https://arxiv.org/pdf/2103.09136v2)。
- Date Added / Last Audited：2026-09-10 / 2026-09-10。

## 同步检查

- [x] 全仓库旧ID与正文名称已搜索。
- [x] 注册表/版本历史已更新。
- [x] 主矩阵已更新。
- [x] 次方向入口已核对（本篇无必须新增次方向）。
- [x] P0-A-C1/C2四字段已更新。
- [x] 周报已同步；全部完成后再改Sync Status为COMPLETE。
