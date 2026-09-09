# 候选创新台账

本台账用于[每周文献审计](Literature_Tracking_Workflow.md)的证据联动，不替代研究计划，不确认创新成立，不增加主张。初始化日期2026-09-07；下列已有工作判断仅转录当前仓库矩阵，未在本轮重新核验原文。新论文通过审计后，所有直接受影响条目必须更新四个英文命名字段并追加变化记录。

## 候选创新与来源

| Innovation ID | Related Paper | 候选主张/范围 | 原始依据 | 状态 |
|---|---|---|---|---|
| P0-C0-1 | P0 | 共享轻量P2–P4检测头的精度—计算折中 | [研究计划](../00_PrePaper_Lightweight_Detection/Research_Plan.md) C0-1 | 暂定，等待阶段2查新 |
| P0-C0-2 | P0 | 理论轻量化转化为真实推理速度 | [研究计划](../00_PrePaper_Lightweight_Detection/Research_Plan.md) C0-2 | 暂定，同一个检测头，不是第二个模块 |
| P1-C1 | P1 | 已知＋未知双路径在固定告警预算下提高危险召回 | [研究计划](../01_Paper1_OpenWorld_Risk/Research_Plan.md) C1 | 暂定，执行等待练手论文 |
| P1-C2 | P1 | 轨道上下文风险排序提高告警决策价值 | [研究计划](../01_Paper1_OpenWorld_Risk/Research_Plan.md) C2 | 暂定，执行等待练手论文 |

## 创新证据与风险

| Innovation ID | Closest Prior Work | Existing Work | Remaining Gap | Novelty Risk | Evidence / Last Updated |
|---|---|---|---|---|---|
| P0-C0-1 | L1-01 LUD-YOLO；L1-02 BPD-YOLO；共享头直接近邻仍待补 | 已有UAV轻量化和高分辨率检测；精确共享范围未核验 | 待确认是否已有同构共享P2–P4头；B1→B2→M能否隔离收益 | Unknown；不能因尚未查到而判断低风险 | [练手矩阵](../00_PrePaper_Lightweight_Detection/Literature/Literature_Matrix.md)；2026-09-07，仓库转录 |
| P0-C0-2 | L3-02 EUAVDet；真实速度规范待补 | 已有边缘设备FPS证据，不能只比GFLOPs | 固定硬件、输入、batch和计时边界下，共享头是否改善延迟仍待验证 | Unknown；部署测速本身不是默认创新 | [练手矩阵](../00_PrePaper_Lightweight_Detection/Literature/Literature_Matrix.md)；2026-09-07，仓库转录 |
| P1-C1 | T2-01 ROSD；T2-02/T2-03强基线；T2-07未知路径候选 | 铁路开放集检测、通用开放世界及VLM OOD已有工作 | 固定告警预算下铁路危险召回的真实缺口仍待核验 | High（沿用矩阵风险，非本轮查新结论） | [Paper 1矩阵](../01_Paper1_OpenWorld_Risk/Literature/Literature_Matrix.md)；2026-09-07，仓库转录 |
| P1-C2 | T1-01、T3-02、T3-03 | 轨道距离、边界、危险分级和风险量化已有直接工作 | 未知候选＋轨道上下文＋告警排序是否存在可检验增量仍待核验 | High（沿用矩阵风险，非本轮查新结论） | [Paper 1矩阵](../01_Paper1_OpenWorld_Risk/Literature/Literature_Matrix.md)；2026-09-07，仓库转录 |

Novelty Risk统一用 `Low / Medium / High / Unknown`，附理由、证据及核验日期；新版本不得静默抹掉旧风险结论。Closest Prior Work可以列多个工作ID；旧ID需带方向，不能跨矩阵裸引用。Remaining Gap要写可被证伪的差异，不写笼统的“效果更好”。

## 暂停方向边界观察

下列ID只是边界观察项，不是候选创新；Closest Innovation应写 `N/A（尚未定义候选创新；观察P2-SCOPE等）`。若新文献影响其方向，更新对应行；正式启动且用户确定主张后才创建创新ID，每篇最多两项。

| Scope ID | 方向依据 | Closest Prior Work | Existing Work | Remaining Gap | Novelty Risk |
|---|---|---|---|---|---|
| P2-SCOPE | [P2三维灾害定量](../02_Paper2_3D_Disaster/README.md) | 未审计 | 已存损伤分割/三维分割背景，非定量测量证据 | 尚未定义候选创新 | Unknown；PAUSED |
| P3-SCOPE | [P3通信受限感知](../03_Paper3_Comm_Perception/README.md) | 未审计 | 已存通信综述/边缘传输背景 | 尚未定义候选创新 | Unknown；PAUSED |
| P4-SCOPE | [P4风险ISAC](../04_Paper4_Risk_ISAC/README.md) | 未审计 | 已存定位通信/RIS背景，非风险驱动证明 | 尚未定义候选创新 | Unknown；PAUSED |
| P5-SCOPE | [P5多模态风险](../05_Paper5_Multimodal_Risk/README.md) | 未审计 | 已存视觉退化背景，非多模态证据 | 尚未定义候选创新 | Unknown；PAUSED |
| P6-SCOPE | [P6主动巡检](../06_Paper6_Active_Inspection/README.md) | 未审计 | 已存UAV-ITS/航迹背景，非风险复检证据 | 尚未定义候选创新 | Unknown；PAUSED |
| P7-SCOPE | [P7多机决策](../07_Paper7_MultiUAV_Decision/README.md) | 未审计 | 已存Agentic/网络背景，非任务分配直接证据 | 尚未定义候选创新 | Unknown；PAUSED |

## 文献影响与待决动作

尚无本流程产生的真实影响记录。每个影响ID一行；后续更新执行状态和结果链接，保留原建议与决定依据。

| Impact ID / Batch | Work ID / Audit | Innovation or Scope ID | Changed Fields / Risk Before → After | 边界原条款与建议 | 最小验证：假设、唯一变量、指标、停止条件 | Target Experiment Plan / Entry | Status / Stage Gate | Decision / Run ID / Outcome |
|---|---|---|---|---|---|---|---|---|

状态：`PROPOSED / BLOCKED / READY / IMPLEMENTED / DISMISSED`。只有阶段允许且方案决定明确时才更新实验计划；只有真实运行才填写Run ID。High风险必须提出核验或主张收缩建议，不能通过自动增加模块规避。
