# 单篇论文审计：AutoFocus

- Work ID：W-0009；原周报线索A10，无旧论文ID；批次`2026-09-12-N1`。
- Date Added / Last Audited：2026-09-12；Audit PASS；Reading SCREENED，非本人精读DONE；Sync COMPLETE。
- 用途：直接反驳“粗尺度尚未识别时预测哪里值得放大就是新机制”的宽泛主张。PASS只表示身份和技术证据足以支持相关性判断，不是复现通过。

## 身份与版本

Title：AutoFocus: Efficient Multi-Scale Inference。Authors：Mahyar Najibi、Bharat Singh、Larry S. Davis。[CVF正式页](https://openaccess.thecvf.com/content_ICCV_2019/html/Najibi_AutoFocus_Efficient_Multi-Scale_Inference_ICCV_2019_paper.html)核实ICCV 2019、pp.9745–9755、October 2019，published；精确出版日Unknown。网页工具访问失败，普通HTTPS访问成功核得题名／作者／会议信息。

唯一技术正文：[arXiv 1812.01600v2 PDF](https://arxiv.org/pdf/1812.01600v2)，11页；已检查正文方法、实验、表1–2与后续方向。版本来源：[arXiv记录](https://arxiv.org/abs/1812.01600)，v1=2018-12-04、v2=2019-08-01；arXiv DOI `10.48550/arxiv.1812.01600`。会议DOI本批未核实，Unknown；未逐字比较会议PDF与v2，不作为两个工作。

载体：正式视觉会议、直接机制近邻，阅读优先级Must Read；国奖／中科院期刊等级N/A（会议不是当前拟投期刊），不用于投稿资格承诺。上述页面未显示撤回／更正提示，未作完整撤稿库检索。

去重：注册表、项目／旧项目矩阵、阅读记录和保护PDF文件名核查后，只有既有HOLD线索，未发现已分配Work ID或同题PDF。原线索保留历史，正文仅登记稳定链接，无新增本地PDF。

## 技术证据与限制

| 项目 | 原文证据 | 对本项目的含义 |
|---|---|---|
| 输入与机制 | §4.1–4.3，PDF pp.3–5：粗尺度特征预测类别无关FocusPixels，阈值／膨胀／连通分量产生FocusChips，处理放大片并清理边界截断预测 | 不以最终检测框作为唯一选区来源早已有先例；增加两个卷积层预测FocusPixels，需要训练 |
| 监督 | §4.1：按当前尺度GT尺寸定义正／负／忽略像素 | 是小目标存在监督，不等于本候选的既有类别logit统计；“先定位再识别”不能独占 |
| 可恢复性 | §5.2–5.3，pp.6：除全GT外，还对高置信检测覆盖的GT统计FocusPixels／Chips召回 | 只统计可被细检测恢复的目标也已有诊断先例，不能单独命名为创新 |
| 数据与选择 | §5：COCO train-2017训练、val-2017分析／100图调参，test-dev报告；VOC2007 test、VOC2012 trainval＋VOC2007 trainval训练 | 没有VisDrone或本项目来源独立组证据；不同检测器／数据不能直接迁移FPS |
| 主结果 | 表1及§5.4，p.7：COCO test-dev AP47.9、AP50 68.3，Titan X Pascal 6.4图/s；SNIPER同AP、2.5图/s | 作者报告；像素节省与相对多尺度基线加速，不是同毫秒预算本项目效果 |
| 成本口径 | §5描述相似尺寸／长宽比分组批处理；报告平均像素和吞吐 | 完整端到端分项、p95和超预算比例Not reported；不是硬截止证明 |
| 边界 | §4.3处理切片边界错误；§6提出迁移其他检测器／视频 | “换YOLO”本身亦不是充分差异；本轮未运行源码或复现数字 |

Related Paper：P0；无必要P1／暂停方向交叉索引。Closest Innovation：P0-A-C1/C2。Novelty Conflict：广义低响应区域引导高分辨率计算为Direct；对[当前具体跨尺度弱响应候选](Weak_Response_Candidate_Review.md)为Partial，精确统计机制的覆盖性尚未证明。Novelty Risk保持High。

I-2026-09-12-N1-01回链[创新台账](../../00_Overview/Innovation_Ledger.md)。最小验证为固定检测器和裁片，只比较响应信号；不得把新增检测头的收益或更多裁片归因于选区。目标[实验预案](../Experiments/Experiment_Plan.md)，运行BLOCKED、Run ID=N/A。

已同步注册表／版本表、主矩阵、近邻入口、创新四字段、检索日志与周报；无次方向变更，七篇路线不变。
