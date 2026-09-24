# RailUAV-SOD（论文 A · 数据/管线/协议预备包）

目录名：`08_RailUAV_SOD`  
论文代号：**A / RailUAV-SOD**（与 Paper1「B」独立发表；贡献与主结果互不绑定）

> **状态：PREP / IDLE** — Post-EI 预备包，**不是** Stage ④ / 采集 / 训练授权。  
> 当前全仓库唯一 ACTIVE 仍是 P0_EI（见 [`../00_Overview/Current_Stage.md`](../00_Overview/Current_Stage.md)）。  
> 解锁条件：P0_EI 收口后，由 `Current_Stage.md` **书面再授权**，本包才可从 IDLE → 执行。

## 你需要看的文件

| 文件 | 用途 |
|---|---|
| [`../00_Overview/Current_Stage.md`](../00_Overview/Current_Stage.md) | **唯一当前事项**（本包不得覆盖） |
| [`POST_EI_HANDOFF.md`](POST_EI_HANDOFF.md) | Post-EI 解锁说明与禁令 |
| [`Research_Plan.md`](Research_Plan.md) | 问题、主张、与 B 边界 |
| [`Stage_Guide.md`](Stage_Guide.md) | 阶段门（全部 IDLE，直至再授权） |
| [`Mainline_Current.md`](Mainline_Current.md) | 近/中/远与执行效力 |
| [`Completion_Metrics.md`](Completion_Metrics.md) | 学习关卡总门（轻量） |
| [`Literature/`](Literature/) | 主题矩阵与阅读清单 |
| [`Writing/`](Writing/) | Sci Data 取向提纲 |
| [`Experiments/`](Experiments/) | 实验槽位（空壳占位，禁跑） |
| [`Learning_Notes/`](Learning_Notes/) | 路线知识图 stub |

独立边界权威：[`../01_Paper1_OpenWorld_Risk/AB_Independent_Publication_Boundary.md`](../01_Paper1_OpenWorld_Risk/AB_Independent_Publication_Boundary.md)

## 硬边界（摘要）

- **卖点**：UAV 视角 × 铁路小部件 × 真实缺陷 + 双引擎 OVD 半自动标注的受控效率审计 + 合成 fidelity–utility 审计协议。
- **禁止**写「首个 UAV 铁路数据集」（UAV-RSOD / RailFOD23 / RFDD / RSD_UAV 已占坑）。
- **相对 RFDD**：硬切 UAV 视角 + 标注效率审计 + 合成审计；不得与 RFDD（高铁扣件全景）同质。
- **相对 DART**：不卖「又一条半自动管线」；只卖受控人时/质量曲线与误差模式。
- **不展开**告警预算 / 风险排序 / 可派发队列（属 B）。
- 未在 `Current_Stage` 授权前：**不采集、不新训、不建正式 Run ID 主证据**。

## 投稿锚（计划，非承诺）

| 档 | 目标 |
|---|---|
| 中位 | *Scientific Data* |
| 上限 | Sci Data 顺利 / NeurIPS Evaluations & Datasets（冲刺，须双审计写清） |
| 下限 | Electronics / Sensors（无审计或与 RFDD/UAV 扣件重叠时） |
