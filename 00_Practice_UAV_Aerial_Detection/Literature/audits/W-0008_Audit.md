# 单篇审计：Dynamic Zoom-in Network for Fast Object Detection in Large Images

- Work ID / Legacy ID / Batch：W-0008 / N/A（无旧匹配）/ 2026-09-11-A0-09。
- Audit Date：2026-09-11；Audit Status：PASS；Reading Status：SCREENED，非用户精读DONE；Reading Priority：Must Read。
- Sync Status：COMPLETE；用途为候选冲突审查，不实施文中的强化学习或网络。

## 身份与唯一正文

| 字段 | 核验结果／证据 |
|---|---|
| Title / Authors | Dynamic Zoom-in Network for Fast Object Detection in Large Images；Mingfei Gao、Ruichi Yu、Ang Li、Vlad I. Morariu、Larry S. Davis；正式PDF首页、CVF与Crossref一致 |
| DOI / arXiv | 10.1109/cvpr.2018.00724；1711.05187，v1=2017-11-14、v2=2018-03-27；[arXiv记录](https://arxiv.org/abs/1711.05187) |
| Publication / Version | published，CVPR 2018，pp.6926–6935；主技术版本为CVF会议正式PDF；[会议入口](https://openaccess.thecvf.com/content_cvpr_2018/html/Gao_Dynamic_Zoom-In_Network_CVPR_2018_paper.html) |
| 日期 | 正式出版2018-06（月级，CVF／[Crossref](https://api.crossref.org/works/10.1109/CVPR.2018.00724)）；精确上线日Unknown；Early Access N/A（未核得单列）；不把Crossref created=2018-12-18当发表日 |
| 版本关系 | arXiv记录标注CVPR2018，题名作者与正式文一致；沿用一个Work ID，未声称v2与正式PDF逐字相同 |
| 载体 | 项目内部A级会议文献；中科院／国奖资格N/A，本条是机制近邻，不是拟投期刊 |
| 更正撤回 | 本次Crossref结果未返回update-to；未完成跨库撤稿核验，不保证不存在后续更正 |
| 去重 | 注册表、全仓库Markdown及Git跟踪PDF文件名按题名、1711.05187、Dynamic Zoom与DOI搜索，无既有工作；W-0008为当前首个未用编号 |

唯一Canonical Reference：[CVF正式全文](https://openaccess.thecvf.com/content_cvpr_2018/papers/Gao_Dynamic_Zoom-In_Network_CVPR_2018_paper.pdf)。网页工具直接打开CVF曾失败，普通HTTPS取得10页正式PDF并以pypdf提取全文；主正文仅保留稳定链接，不在仓库新增PDF。临时阅读文件与来源日志见被忽略的`11_Datasets/processed/VisDrone/A0-09/source_access.json`。初试PyMuPDF缺失，改用已有pypdf；一次终端编码输出失败不影响已保存文本。没有安装软件或运行作者代码。

## 技术证据：作者报告与项目推断分开

| 字段 | 原文定位及作者报告 | 审计判断／局限 |
|---|---|---|
| Problem | §1、§3：低分辨率粗检测后顺序选择高分辨率区域，兼顾准确率与计算成本 | 直接覆盖广义“收益＋顺序局部计算”；不是无人机专用结果 |
| Dataset | §4：CPD训练4321／测试4088，每30帧抽训练图，行人至少50px高；高分辨率短边600。WP为YFCC100M搜索所得100张测试图，行人宽至少16px、遮挡<50%，长边2000 | 检测器／R-net／Q-net在CPD训练；WP仅测试。来源泄漏、预训练重叠及单独调参隔离未独立验证；不等同VisDrone小目标分层 |
| Method | §3.1–3.3、图1–2：R-net从粗检测特征估计精细检测相对粗检测的准确率收益，Q-net顺序选位置和尺度；奖励包含像素比例成本λb/B | 增益预测、计算成本与历史动作选择已有；其Q学习超出本项目实施边界，但不能因此忽略先例 |
| 更新与停止 | §3.2末：已处理区域AG值置零；§3.3：用局部细检测替换该区域粗检测；§4.4：AG总和<0.1停止 | 没有证据证明它在线用新检测结果重估全部未选区效用；不能把“历史区域置零”夸写为完整检测反馈。也不是剩余毫秒硬截止约束 |
| 对照 | §4.1、图4–5：GS+Rnet按当前状态贪心选区，ER+Qnet用二元熵替代收益预测；§4.7含成本项消融 | “不用RL、改贪心”或“用置信度熵”本身不能构成充分差异；这些组件已有对照证据 |
| Metrics | §4.3定义Aperc、Pperc、Tperc均相对Fine-detection-all；不是百分点。表1：CPD APf=.493、304ms，WP APf=.407、1375ms；表2 CPD的Qnet*-CNN+Rnet在Pperc≤45%时Aperc=102%、Tperc=80%；WP同变体Pperc≤35%时Aperc=93%、Tperc=45% | 即相对细检测基线AP约保持／折中，不能读作102%绝对AP；表中已计入粗图25%像素开销。未把这些AP当COCO／VisDrone AP50:95，论文此处匹配阈值与积分细节未明确 |
| 硬件／时间 | §4.4 K-80 GPU；图6／表1–3报告平均检测时间 | 完整I/O、预热、同步、batch与p95／超时率范围Not reported；像素预算与真实毫秒约束不同，不能转用为本机FPS |
| 作者局限 | §4说明少数大目标场景收益低；§4.7讨论窗口大小、空间先验和成本惩罚对跨数据集表现的影响 | 非细粒度反馈闭环的完全同构证明，也未证明本候选有剩余创新；本项目未复现性能 |

## 项目映射与决定

- 主方向P0；次方向N/A：只用于图像内已知检测计算分配，不新增Paper 6航迹／主动巡检任务。
- 关联P0-A-C1/C2；Closest Prior Work加入W-0008；Existing Work新增顺序收益选区、历史抑制、像素成本与熵／贪心先例；Remaining Gap是当前具体反馈估计与毫秒准入是否有实质区别，尚未建立；Novelty Risk=High。
- Novelty Conflict：Direct（广义顺序收益／成本选区）；Partial/Unknown（新检测结果驱动全部剩余区重估＋完整毫秒控制的精确实现）。不把两者混写成已证明完全同构。
- PASS理由：身份、版本和完整技术／实验足以支持冲突判断；不代表认可全部作者效果，不代表本项目学习或实验通过。
- 最小后续验证提案：同候选、检测器、融合与时间准入，只比较初始排序、历史覆盖抑制、实际检测反馈重排；若优势只能来自片数／融合／成本门，否决反馈主张。当前候选不进入实现，见[A0-09候选卡](A0-09_Candidate_Review.md)；目标[实验预案](../Experiments/Experiment_Plan.md)，Run ID=N/A。
- Impact ID：I-2026-09-11-A0-09-01；Date Added / Last Audited：2026-09-11 / 2026-09-11。注册表、主矩阵、创新四字段和周报已联动；无必要P1交叉引用，无新增暂停方向工作。
