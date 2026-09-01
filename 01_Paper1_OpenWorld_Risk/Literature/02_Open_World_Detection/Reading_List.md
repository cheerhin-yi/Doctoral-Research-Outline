# T2：开放集、开放词汇与开放世界检测阅读清单

## 本主题要回答

- 铁路未知目标检测已经做到什么程度？
- open-set、open-vocabulary和open-world实验协议有什么不同？
- 哪个未知候选基线最适合Paper 1？
- 如何同时报告Unknown Recall和误报/候选负担？

## 阅读清单

| ID | 论文 | 优先级 | 状态 | 重点阅读 | 笔记 |
|---|---|---|---|---|---|
| T2-01 | ROSD: Railway intrusion object generalized detection via Open-Set Detection | MUST | SCREENED | 铁路open-set问题、数据协议、评价与局限 | 待创建 |
| T2-02 | Towards Open World Object Detection | MUST | SCREENED | OWOD定义、A-OSE、Wilderness Impact | 待创建 |
| T2-03 | OW-OVD: Unified Open World and Open Vocabulary Object Detection | MUST | SCREENED | 现代开放方法、预训练知识和公平比较 | 待创建 |
| T2-04 | YOLO-World相关原始工作 | SHOULD | TODO | 提示词、预训练、开放词汇推理 | 待检索 |
| T2-05 | [YOLOE](YOLOE%20-%20Real-Time%20Seeing%20Anything.pdf) | MUST | SCREENED | 提示机制、预训练、开放词汇协议、实时性 | 待创建 |
| T2-06 | [YOLO-IOD](YOLO-IOD%20-%20Towards%20Real-Time%20Incremental%20Object%20Detection.pdf) | SHOULD | SCREENED | 增量协议、遗忘、旧类数据、与未知检测的边界 | 待创建 |
| T2-07 | [NegAS](NegAS%20-%20Negative%20Label%20Guided%20Attention%20and%20Scoring%20for%20Out-of-Distribution%20Object%20Detection%20with%20Vision-Language%20Models.pdf) | MUST | SCREENED | 负标签、OOD分数、未知召回、误报和铁路迁移风险 | 待创建 |

## 本主题完成门

- [ ] 至少5篇方法或铁路直接近邻完成精读；
- [ ] 冻结Known/Unknown类别轮换原则；
- [ ] 选择一个主要未知候选强基线；
- [ ] 明确预训练知识差异和误报评价方式。
