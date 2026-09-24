# 文献矩阵增补（2026-09-24 · B 划界加厚）

> 增补条目来自 `AB_Direction_Judgment_With_Literature_2026-09-24.md` 及附录；写入本增补以免覆盖既有 `Literature_Matrix.md` 手工表。精读后合并回主矩阵。  
> **列式对齐 Practice：** 已覆盖 / 未证实缺口 / 本篇增量 / 会议期刊 / 年。不确定处标 **Unknown**。  
> **禁止：** 虚构 DOI、虚构指标数值。  
> 更新：2026-09-24 晚（案头预备）。

## 1. 划界优先阅读队列（加厚）

| ID | 工作 | 年 | 会议/期刊 | 已覆盖 | 未证实缺口（相对本篇） | 本篇增量（C1/C2） | 状态 | 定位 |
|---|---|---:|---|---|---|---|---|---|
| T3-CAO | Cao 等 Railway Intrusion Detection Survey | 2024 | IEEE TITS | 侵界视觉综述；地面/车载/UAV 分景；挑战清单 | 无固定告警预算系统评测；无双路径+派单协议 | 场景合法性背书；Related Work 挑战条目对表（**非方法贡献**） | SCREENED | 场景合法性 |
| T3-TIM | TIM OID Comprehensive Review | 2025 | IEEE TIM | 障碍物侵界 OID 综合；传感+AI | Unknown：是否含 UAV 告警预算实验 | 投 TIM/应用刊背书；与 C2「可派发」叙事对齐 | SCREENED | 投 TIM 背书 |
| T2-OWOD | Li 等 Open World Object Detection: A Survey | 2024 | IEEE TCSVT | OWOD 定义/基准/指标综述 | 铁路UAV专用协议 Unknown | 术语精确；禁止把一次 open-set 测试写成完整 open-world | SCREENED | 术语 |
| T2-OSOD | Rethinking Open-Set Object Detection | 2025 | IJCV | OSOD 评测偏差与协议反思 | 告警预算轴 Unknown | **支持**用危险召回/预算，而非只报 unknown AP | SCREENED | 指标正当性 |
| T2-SRLF | SRLF | 2025 | IEEE TITS | UAV 铁路稀疏/未知相关检出（同场景近邻） | 是否含固定告警预算曲线、可派发排序 Unknown（精读确认） | **必须多出：** 固定告警预算 + 可派发 + 轨道上下文排序（非同构稀疏未知检出） | SCREENED | **最近邻** |
| T2-MENG | Meng 等 UAV 未知风险 | 2024+ | Unknown（精读核验 venue） | UAV 未知风险检出取向 | 告警决策层与预算曲线是否缺失（待精读） | 告警层对照；删除未知支路实验 | SCREENED | 偏检出对照 |
| T4-CRC | Conformal OD / Conformal Risk Control 谱系 | 2023+ | arXiv:2304.06052 及后续 | 覆盖保证/风险控制校准 | 铁路双路径+派单 Unknown | 钉死「双路径 × 固定配额 × 可派单」，避免被校准文献稀释 | SCREENED | 预算邻域 |
| T4-FNB | Three-way open-set + false-novelty budget | — | arXiv:2511.15343 | 抽象 false-novelty 预算（如 q≈20%） | 轨旁风险排序 Unknown | 补轨道上下文与派单；否则 C1 抽象新颖性被压 | SCREENED | 压缩抽象新颖性 |
| T2-OOD | PCA-HBOS 等 UAV OOD | — | Drones 等 | 航拍 OOD 滤波 | 危险召回–预算曲线 Unknown | 与纯 OOD 滤波划界；强调可派发危险告警 | SCREENED | 下位拥挤 |
| T3-SENS | Sensors 等风险量化 / 侵界多传感 | 2023–2025 | Sensors 等 | 风险量化、多传感周界 | 单目 UAV + 未知候选 + 预算 Unknown | 支持 C2 几何/分级动机；划界单视觉范围 | SCREENED | C2 动机 |
| T2-YW | YOLO-World | 2024 | CVPR 等 | 实时开放词汇检测 | — | **基线非贡献**；公平报告预训练与提示 | SCREENED | 基线 |
| T2-CAST | CastDet | 2024–2025 | Unknown | 开放词汇/航拍相关检测（待精读确认贡献点） | Unknown | **基线非贡献** | SCREENED | 基线 |
| T2-UOVD | UAV-OVD / OW-OVD 等 | 2024–2025 | CVPR/ECCV 等 | UAV/统一开放词汇与开放世界 | — | **基线非贡献**；不写成本篇方法 | SCREENED | 基线 |

## 2. 与 C1/C2 证据链（增补视角）

### C1

| 链条 | 增补后状态 | 仍需精读确认 |
|---|---|---|
| 最近邻 | SRLF + Meng + false-novelty budget + conformal 谱系 | SRLF 是否已含预算曲线；Meng venue/协议 |
| 尚存缺口（主张级） | 「固定告警预算下的铁路危险召回 + 双路径」仍为待证实组合缺口 | 原文表号与指标定义 |
| 基线菜单 | YOLO-World / CastDet / UAV-OVD / NegAS 等 | 投稿前冻结**一个**主强基线 |

### C2

| 链条 | 增补后状态 | 仍需精读确认 |
|---|---|---|
| 最近邻 | 主矩阵 T3-02/T3-03 距离风险 + Sensors 风险量化 + Cao/TIM 综述 | 是否已有「未知候选 + 轨道排序」组合 |
| 尚存缺口（主张级） | 「未知候选 × 轨道上下文 × 告警排序」组合待证实 | 风险标签是否类别捷径 |
| 方法下限 | 最简单 track-zone / boundary | 复杂网络默认不采用 |

## 3. 阅读优先级（案头）

1. MUST 精读：SRLF；Cao TITS；OSOD IJCV；Conformal 谱系综述/代表作；false-novelty budget。  
2. SHOULD：Meng；TIM OID；OWOD Survey；PCA-HBOS；Sensors 风险量化。  
3. 基线说明书级：YOLO-World / CastDet / UAV-OVD（只记协议与预训练，不记「贡献」）。

## 4. 主矩阵关系

主矩阵 `Literature_Matrix.md` 原表仍有效；本表为划界优先队列与 Practice 风格缺口列。精读完成后：合并 ID、回链单篇笔记、把 Unknown 改写为有原文定位的句子。
