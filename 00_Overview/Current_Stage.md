# 当前阶段：Paper 1知识补齐

- **状态**：ACTIVE
- **起点**：已学习深度学习中的卷积部分和YOLO基本内容。
- **当前目标**：从“知道YOLO是什么”提升到“能够解释、运行、评价并为论文设计YOLO实验”。
- **当前禁止**：收集项目数据、修改YOLO网络、训练开放世界模型、开始Paper 2–7。

## 现在只做这六项

按顺序完成，每次只推进一项：

1. **完整理解YOLO检测链**：阅读[YOLO研究核心](../01_Paper1_OpenWorld_Risk/Learning_Notes/01_YOLO_Research_Core.md)，画出`输入→Backbone→Neck→Head→候选框→NMS→最终预测`，写出每一步的输入输出。

2. **补齐评价指标**：手算一个包含TP、FP、FN的小例子，解释Precision、Recall、IoU、AP、mAP50和mAP50–95；说明Paper 1为什么优先关注危险目标Recall和告警负担。

3. **补齐科研代码能力**：阅读[PyTorch与可复现性](../01_Paper1_OpenWorld_Risk/Learning_Notes/02_PyTorch_and_Reproducibility.md)，能解释Dataset/DataLoader、train/eval、loss、optimizer、checkpoint、seed和AMP。

4. **建立开放世界概念边界**：阅读[开放世界感知](../01_Paper1_OpenWorld_Risk/Learning_Notes/03_Open_World_Perception.md)，用铁路例子区分closed-set、open-set、open-vocabulary、open-world和anomaly detection。

5. **建立论文实验意识**：阅读[实验设计与不确定性](../01_Paper1_OpenWorld_Risk/Learning_Notes/05_Experiment_Design_and_Uncertainty.md)，为“提高输入分辨率是否改善小目标检测”写一个完整对照实验。

6. **补齐练手论文专项知识**：依次填写[小目标与多尺度检测](../01_Paper1_OpenWorld_Risk/PrePaper_Lightweight_Detection/Learning_Notes/01_Small_Object_and_Multiscale.md)、[轻量共享检测头](../01_Paper1_OpenWorld_Risk/PrePaper_Lightweight_Detection/Learning_Notes/02_Lightweight_Shared_Head.md)和[速度评价与简单部署](../01_Paper1_OpenWorld_Risk/PrePaper_Lightweight_Detection/Learning_Notes/03_Efficiency_and_Deployment.md)；当前只画结构、手算参数量和写计时协议，不修改模型。

## 建议的前12次研究会话

每次约60–90分钟；时间不足时可拆分，不按自然日打卡。

| 会话 | 学习任务 | 必须留下的输出 |
|---|---|---|
| 1 | YOLO完整结构 | 一张结构图＋各阶段张量含义 |
| 2 | 多尺度检测 | 解释为什么小目标依赖高分辨率特征层 |
| 3 | IoU、Precision、Recall | 一组手算结果＋错误解释 |
| 4 | AP、mAP和阈值 | 一段“为什么不能只看mAP50”的说明 |
| 5 | 损失、标签匹配、NMS | 一张训练阶段与推理阶段差异表 |
| 6 | PyTorch数据与训练循环 | 用伪代码写出train/val流程 |
| 7 | seed、checkpoint、日志 | 一份最小复现清单 |
| 8 | 开放世界术语 | 一张五类概念对照表 |
| 9 | 铁路风险上下文 | 三个“同类别不同风险”例子 |
| 10 | 实验设计 | 一个包含假设、变量、对照、指标和失败解释的实验条目 |
| 11 | 小目标与多尺度 | P3–P5、P2–P5和P2–P4结构图 |
| 12 | 共享检测头与速度 | 参数量手算＋LSM-Head草图＋固定计时协议 |

## 阶段完成门

全部满足后才进入“Paper 1文献与问题冻结”：

- [ ] 不看资料画出YOLO完整推理流程；
- [ ] 能手算IoU、Precision和Recall，并解释AP的基本思想；
- [ ] 能说清YOLO11n/s/m公平比较需要固定什么；
- [ ] 能解释train/eval、checkpoint、seed和数据泄漏；
- [ ] 能区分五种开放环境概念；
- [ ] 能解释“检测到目标”为什么不等于“铁路高风险”；
- [ ] 能独立写出一个合格的对照实验；
- [ ] Paper 1五份共同笔记和练手论文三份专项笔记均留下自己的回答，而不是只复制资料。
- [ ] 完成检测尺度结构图、参数量手算、共享头草图和公平计时协议。

## 通过后做什么

先进入[实时轻量检测练手论文](../01_Paper1_OpenWorld_Risk/PrePaper_Lightweight_Detection/Stage_Guide.md)的文献与小样例阶段，完成投稿后再回到[Paper 1阶段任务指南](../01_Paper1_OpenWorld_Risk/Stage_Guide.md)的开放世界研究；仍然不立即收集数据。
