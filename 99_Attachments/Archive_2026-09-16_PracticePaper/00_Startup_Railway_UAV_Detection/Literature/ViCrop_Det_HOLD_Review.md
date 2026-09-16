# ViCrop-Det直接近邻补查：HOLD

日期／批次：2026-09-12 / `2026-09-12-N1`。注册表／各矩阵／阅读记录及PDF文件名去重未发现既有工作；未分配Work ID、未归档PDF，不计PASS或精读完成。

[arXiv身份页](https://arxiv.org/abs/2604.26806)核实题名ViCrop-Det: Spatial Attention Entropy Guided Cropping for Training-Free Small-Object Detection，作者Hui Wang、Hongze Li、Wei Chen、Xiaojin Zhang；v1于2026-04-29提交，DOI `10.48550/arxiv.2604.26806`，preprint，未核得正式发表。检查了[公开HTML](https://arxiv.org/html/2604.26806v1)方法§3、实验§4、限制§5及附录A–E相关协议；PDF访问失败，未完成版本逐项对照。HTML标注compiled August 24, 2026与v1提交日期并列出现，二者关系Unknown，不能擅自改写版本时间。

**有原文支持的机制重合**：§3聚合解码器cross-attention，按注意强度与空间熵评分，门控、多尺度窗口、Top-K、局部重检与融合；不需要重新训练检测器。故“使用内部信号、免训练、有限裁片预算”必须视为已有近邻主张，不能因本文HOLD而当成空白。

**HOLD原因**：§4.1把VisDrone test-dev写成5240，与既有官方审计1610不符；表5的K对应FPS与§4.3文字序列不一致；版本日期与PDF对照未解决。表2报告RT-DETR-R50在VisDrone AP50 37.0→38.9、FPS47.5→38.6，仅登记为作者报告，不能作本项目可复现性能证据。附录A称val调参并报告val，B给出RTX4090、batch1、20次预热和200次计时；真实范围／复现代码本批未核得。

§5承认零注意响应目标仍可能漏掉。作者的固定阈值、Top-K与吞吐并非硬实时保证。不能把Transformer信号换成YOLO信号就认定创新，也不能通过质疑本文实验消除其方法先例。

拟主归属P0，直接关系P0-A-C1/C2；阅读Must Read线索、技术身份审查HOLD。再查条件为版本可对照及关键协议说明／代码可核验；本轮不以补齐这篇所有疑点无限延长候选审查。冲突与缺口已写入[候选报告](Weak_Response_Candidate_Review.md)、台账和周报，不改变模型阶段门或其他论文。
