# W-0012：Adaptive NMS

- Title：Adaptive NMS: Refining Pedestrian Detection in a Crowd
- Authors：Songtao Liu; Di Huang; Yunhong Wang
- Batch：2026-09-14-BTD10；Audit Date / Date Added：2026-09-14；Auditor：Codex
- Audit Status：PASS；Reading Status：SCREENED；Sync Status：COMPLETE
- 唯一技术正文：[arXiv v1，10页](https://arxiv.org/pdf/1904.03629v1)；[身份页](https://arxiv.org/abs/1904.03629)，本日访问。

## 身份与版本

arXiv 1904.03629v1，2019-04-07；DOI 10.48550/arxiv.1904.03629，会议DOI Unknown。CVPR2019，published，CVF检索元数据页码6459–6468；本日直接打开CVF页／PDF返回Internal Error，改核公开arXiv全文，其Comments注明CVPR2019 Oral。未与正式稿逐字核对；正式精确日期Unknown，early access N/A（未核得单列）。内部载体C（当前技术副本为arXiv），官方等级Unknown；撤稿数据库未独立核验。

去重：题名、Adaptive NMS、1904.03629及PDF文件名未命中已有工作；无旧ID。

## 技术证据

| 项 | 原文定位及审计摘要 |
|---|---|
| 问题／方法 | §3.2–3.3：以邻近GT最大IoU定义训练密度，三层子网预测密度并调NMS阈值；推理不直接用GT |
| 数据／协议 | §4：CityPersons train2975/val500/test1525，CrowdHuman train15000/val4370/test5000；各官方训练／验证，全身框；4×Titan X训练，CityPersons VGG16、CrowdHuman FPN R50等；来源隔离未额外审计 |
| 指标 | 表5 CrowdHuman val FPN的MR−2 52.35→49.73，降低2.62个百分点，AP83.07→84.71；不是VisDrone AP或本机速度 |
| 贡献／局限 | 按密度自适应抑制已覆盖；图6指出放宽阈值会保留不紧凑假框。密度子网有额外计算；正文未给本项目所需整帧p95／超预算率，不把作者效率描述当实测 |

## 项目判断与同步

主方向P0，次方向N/A。Closest Innovation=N/A（BTD10切入点二仅问题）；影响P0-A-C1/C2的剩余空间解释。Novelty Conflict=Direct（若仅用密度调抑制阈值），不等于覆盖旧裁剪选择器。Reading Priority=Must Read。

I-2026-09-14-BTD10-03 → [台账](../../00_Overview/Innovation_Ledger.md) → [预案](../Experiments/Experiment_Plan.md)。未来唯一变量为固定原候选上的抑制规则，统计补回／丢失／FP／完整时延；当前无F1280原始删除轨迹，因果归因Unknown，禁止凭最终框称NMS误删。仅有阈值放宽效应或无瓶颈则停止；本轮不取新模型输出。Run ID=N/A。

PASS理由：身份及公开技术正文足以确立重合风险，未完成本机复现。注册表、主矩阵、四字段和[周报](../../00_Overview/Weekly_Literature_Audits/Weekly_Literature_Audit_2026-09-14.md)同步；无必要次方向／主题Reading_List。仅稳定全文链接，无新增PDF。
