# RailUAV-SOD 阶段指南（预备 · 无冲突干净稿）

> **2026-09-24：** 本文件为 Post-EI **预备包**阶段门。全文状态默认 **IDLE**。  
> **不**授权采集/训练；**不**覆盖 [`../00_Overview/Current_Stage.md`](../00_Overview/Current_Stage.md) 中唯一 ACTIVE=P0_EI。  
> 再授权后，以 `Current_Stage` + 本指南同步推进。

更新：2026-09-24（Asia/Shanghai）。

## 总状态

| 阶段 | 名称 | 状态 |
|---|---|---|
| A0 | 可行性与近邻划界 | IDLE（预备材料可读） |
| A1 | 协议与 taxonomy 冻结 | IDLE |
| A2 | 采集与许可落地 | IDLE · **禁提前采集** |
| A3 | 双引擎预标注 + D4 计时审计 | IDLE |
| A4 | 合成审计 + 封闭集基线 | IDLE |
| A5 | 写作与投稿（Sci Data 取向） | IDLE |

## A0：可行性审查（再授权后首项）

**授权后允许：** 研究计划收窄；近邻全文审计（UAV-RSOD / RailFOD23 / RFDD / DART / RSD_UAV 等）；许可与发布条件核验；taxonomy 草案；公开代理数据**只读**审计（披露使用）。  
**禁止：** 正式 UAV 采集、外包大规模标注、模型训练、把代理结果写成基准主表。

**完成交付：**
- README / Research_Plan / Literature_Matrix / Writing outline 主张一致；
- 与 RFDD、DART、UAV-RSOD、RailFOD23 的「已覆盖 / 未证实差异」有原文定位；
- 给出继续 / 降档 / 暂缓结论与单一后续任务。

**交付完整 ≠ 可行性通过。** 缺真实缺陷路径或许可证据则保持 HOLD。

## A1：协议与 taxonomy（A0 通过后）

冻结：类目树、尺度定义、split 原则（场景/航次隔离）、OVD 引擎候选、D4 计时协议草稿、合成披露清单。  
学习支持见 `Learning_Notes/`。不启动采集。

## A2：采集与许可（未开放）

仅在 A1 冻结且 `Current_Stage` 书面授权后开放。完成门：许可明确、场景清单与哈希方案就绪、缺陷稀缺披露句可写进数据文。

## A3：预标注与效率审计（未开放）

双引擎跑通；受控人时（建议 D4 量级）；加速比 / 修错率 / Kappa；误差模式表。  
OVD = **预标注工具**，不是告警系统组件（后者属 B）。

## A4：合成审计与封闭集基线（未开放）

合成比例–性能曲线；YOLO / RT-DETR 等同协议基线；失败边界。所有数字回链 Run ID。

## A5：写作与投稿（未开放）

先冻主表与披露附录，再写 Methods；摘要禁止「首个 UAV 铁路数据集」。Venue 按中位 Sci Data 准备，上限/下限见 Research_Plan。

## 与全局纪律

- 学习关卡**不替代**实验门；实验是否启动只写在 `Current_Stage`。
- 本指南与其他目录若有历史合并冲突，**以本干净稿为准**（本包新建，无 marker）。
