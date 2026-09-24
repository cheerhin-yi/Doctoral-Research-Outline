# 仓库文件总目录 / FILE_CATALOG

> **用途：** 维护型总目录，标明关键保险柜文件位置及其对应关系（尤其：近期 P0_EI 对照图的基准数据落点）。  
> **原则：** 只收录已扫描确认存在的路径；不枚举 `11_Datasets` 像素树 / Ultralytics 全量文件。  
> **更新：** 2026-09-24（Asia/Shanghai）

快速入口：[`README.md`](README.md) · [`00_Overview/Current_Stage.md`](00_Overview/Current_Stage.md) · [`00_Overview/INDEX_Discussion_Products_2026-09-24.md`](00_Overview/INDEX_Discussion_Products_2026-09-24.md)（当日政策/边界/A·B案头） · [`P0_EI/Run_Index.md`](00_Practice_UAV_Aerial_Detection/Experiments/papers/P0_EI/Run_Index.md) · [figures/](00_Practice_UAV_Aerial_Detection/Experiments/papers/P0_EI/05_packaging/figures/)

---

## 1. 维护说明

| 项 | 约定 |
|---|---|
| **谁更新** | 维护本仓库的执行代理 / 本人；重大证据变更后同步改本文件 |
| **何时更新** | 新 stage `PASS`、packaging 叙事变更、新增/再生对照图、顶层目录增减 |
| **如何再生图** | 见 `00_Practice_UAV_Aerial_Detection/Experiments/papers/P0_EI/05_packaging/figures/FIGURES.md`；运行同目录 `generate_plots.py`（`H:\Conda\envs\UAV_BT1\python.exe`） |
| **不做什么** | 不据此重训、不改实验配置、不 remap；不把 raw 数据集或权重树展开进本目录 |
| **Git** | 本文件与 `05_packaging/figures/*` 可随证据提交；勿捎带无关脏文件 |

---

## 2. 顶层目录地图

| 路径 | 用途 | 状态 |
|---|---|---|
| `00_Overview/` | 跨会话交接、当前阶段、七篇路线、文献流程与模板 | ACTIVE |
| `00_Practice_UAV_Aerial_Detection/` | 练手主线：文献主题树、Learning_Notes、Writing、P0_EI 证据 | ACTIVE |
| `01_Paper1_OpenWorld_Risk/` | Paper 1 / B 开放世界风险：Practice 同构预备包 + 既有备忘 | IDLE/PREP（Post-EI；ACTIVE 仍为 P0） |
| `02_Paper2_3D_Disaster/` | 三维灾后场景 | PAUSED |
| `03_Paper3_Comm_Perception/` | 通感协同感知 | PAUSED |
| `04_Paper4_Risk_ISAC/` | 风险感知 ISAC | PAUSED |
| `05_Paper5_Multimodal_Risk/` | 多模态风险感知 | PAUSED |
| `06_Paper6_Active_Inspection/` | 主动式无人机巡检 | PAUSED |
| `07_Paper7_MultiUAV_Decision/` | 多无人机协同决策 | PAUSED |
| `08_RailUAV_SOD/` | 论文 A · RailUAV-SOD 数据/管线/审计预备包 | IDLE/PREP（Post-EI） |
| `11_Datasets/` | 数据根：`raw/` · `processed/` · `external/`（**不展开像素/权重树**） | ACTIVE（数据仓） |
| `90_English_Learning/` | 与当前阶段同步的英语/听力/写作节奏 | SUPPORT |
| `99_Attachments/` | 全项目附件、教程、查阅材料、归档 | REFERENCE |
| `Ultralytics/` | 本地检测框架工作树（训练/推理依赖；勿当证据仓） | TOOLING |
| `.obsidian/` | Obsidian 配置 | 本地工具（不收录细目） |
| `.trash/` | 本地回收 | 不收录 |
| `AGENTS.md` / `PROJECT_CONTEXT.md` / `README.md` | 执行规则 / 跨会话上下文 / 仓库入口 | ACTIVE |

历史练手目录（`00_PrePaper_*` / `00_Startup_*`）已迁入 `99_Attachments/Archive_2026-09-16_PracticePaper/`（见 README 顶注）。

---

## 3. 当前主线快速入口

| 角色 | 路径（均已确认存在） |
|---|---|
| 当前唯一事项 | `00_Overview/Current_Stage.md` |
| 项目指南 / 七篇路线 | `00_Overview/Project_Guide.md` · `00_Overview/Seven_Paper_Roadmap.md` |
| 练手入口 | `00_Practice_UAV_Aerial_Detection/README.md` |
| 练手研究计划 / 阶段 | `00_Practice_UAV_Aerial_Detection/Research_Plan.md` · `Stage_Guide.md` |
| 学习笔记 | `00_Practice_UAV_Aerial_Detection/Learning_Notes/`（含 `11_EI_Packaging_Neighbor_Failure_Repro.md` 等） |
| 文献矩阵 ↔ 主题夹 | `00_Practice_UAV_Aerial_Detection/Literature/Literature_Matrix.md` ↔ `01_Slicing_Inference/` … `04_Aerial_Benchmarks_Eval/` |
| 写作大纲 / 双文计划 | `00_Practice_UAV_Aerial_Detection/Writing/P0_EI_Outline.md` · `P0_Two_Paper_Plan_2026-09-22.md` |
| P0_EI 证据仓 | `00_Practice_UAV_Aerial_Detection/Experiments/papers/P0_EI/` |
| Run 索引 | `00_Practice_UAV_Aerial_Detection/Experiments/papers/P0_EI/Run_Index.md` |
| Packaging 叙事 | `00_Practice_UAV_Aerial_Detection/Experiments/papers/P0_EI/05_packaging/`（含 `Neighbor_Protocol_Table.md`） |
| 对照图 | `00_Practice_UAV_Aerial_Detection/Experiments/papers/P0_EI/05_packaging/figures/` |
| 缩写表（实测路径） | `99_Attachments/查阅/Abbreviation_Glossary.md`（根目录 `Abbreviation_Glossary.md` 链接目前缺失实体） |

---

## 3b. 2026-09-24 全局政策 + A/B 案头指针（讨论产物）

> **不**改变唯一 ACTIVE=**P0_EI**；A/B 仍 **IDLE/PREP**；**不**解锁采集/训练。  
> **总索引（权威入口）：** [`00_Overview/INDEX_Discussion_Products_2026-09-24.md`](00_Overview/INDEX_Discussion_Products_2026-09-24.md)

| 角色 | 权威路径 |
|---|---|
| **policy** | `00_Overview/Venue_and_Claim_Policy_JCR_2026-09-24.md`（JCR-primary + claim ladder）；旧稿镜像 `Venue_Quartile_Policy_2026-09-22.md` |
| **boundary** | `01_Paper1_OpenWorld_Risk/AB_Independent_Publication_Boundary.md` · `AB_Direction_Judgment_With_Literature_2026-09-24.md` · `Paper1_Direction_Worth_Judgment_2026-09-24.md` |
| **A prep** | `08_RailUAV_SOD/Writing/PartFamily_CollectionDifficulty_and_VenueBounds_2026-09-24.md` · `08_RailUAV_SOD/POST_EI_HANDOFF.md` · `Writing/` 案头草案簇；Learning_Notes 课程计划 `_PLAN_Learning_Notes_Curriculum_2026-09-24.md` → **pending**（sibling） |
| **B prep** | `01_Paper1_OpenWorld_Risk/Writing/Claim_Freeze_C1_C2.md` · `Literature/Literature_Matrix_Addendum_2026-09-24.md` · `POST_EI_HANDOFF.md` · `Writing/B_OpenWorld_Risk_Outline.md` |
| **catalog** | 本文件 + `00_Overview/POST_EI_HANDOFF_A_B_Packages.md` + 上列 INDEX |

细目与 `.bak` 列示见 INDEX；下方 §4–§7 **P0_EI 图表/证据骨架保持不变**。文末「Paper1 / Post-EI / 案头 / JCR」各节为同日增量明细，与本表互指。

---
## 4. P0_EI 图表 ↔ 基准数据对照表

相对根前缀：`00_Practice_UAV_Aerial_Detection/Experiments/papers/P0_EI/`

| 图/产物 | 基准数据路径 | 报告/说明 | Run ID |
|---|---|---|---|
| **fig1** VisDrone metrics (`05_packaging/figures/fig1_visdrone_metrics.png`) | `01_visdrone_main/data/D_TESTDEV_summary.json`；逐图 `D_TESTDEV_per_image_metrics.csv` | `01_visdrone_main/StageD_TestDev_Report.md` | `P0-BENCH-D-TESTDEV-20260917-01` |
| **fig2** UAVDT metrics (`05_packaging/figures/fig2_uavdt_metrics.png`) | `03_cross_uavdt/data/E_FULL_summary.json`；逐图 `E_FULL_per_image_metrics.csv` | `03_cross_uavdt/StageE_UAVDT_Report.md` | `P0-BENCH-E-UAVDT-20260918-FULL` |
| **fig3** dual-set small-recall (`05_packaging/figures/fig3_dual_set_small_recall.png`) | **同一** D + E summaries（**禁止 pool D+E**） | Stage D / Stage E 报告 | D + E 上表两个 Run ID |
| **fig4** 1660 timing (`05_packaging/figures/fig4_timing_1660.png`) | `04_timing/data/B_TIMING_summary.json`；`B_TIMING_timings.csv` | `04_timing/StageB_Timing_Report.md` | `P0-BENCH-B-TIMING-20260917-01` |
| **fig5** Stage F deltas (`05_packaging/figures/fig5_stageF_deltas.png`) | `02_paired_stats/data/F_summary.json`；亦有 `F_bootstrap_deltas.csv` | `02_paired_stats/StageF_Paired_Stats_Report.md` | `P0-BENCH-F-TESTDEV-20260917-01` |
| Packaging 叙事表 | （对照文字，非数值源） | `05_packaging/Neighbor_Protocol_Table.md` | — |
| 再生脚本 | 读取上表 JSON | `05_packaging/figures/generate_plots.py` · `FIGURES.md` | — |

---

## 5. P0_EI 证据骨架

```text
Experiments/papers/P0_EI/
  README.md
  Run_Index.md
  00_freeze/          权重 SHA、环境冻结、类别映射、DensK1 定义、config freeze
  01_visdrone_main/   Stage C/D（cal48 + VisDrone test-dev）+ data/
  02_paired_stats/    Stage F 图级配对 + data/
  03_cross_uavdt/     Stage E UAVDT + data/
  04_timing/          Stage B 1660 计时 + data/
  05_packaging/       邻域表 / 失败边界 / 复现附录 / figures/
```

### 关键文件（已扫描）

| 阶段夹 | 关键文件 |
|---|---|
| `00_freeze/` | `Environment_Freeze.md` · `weight_sha_reverify.txt` · `Class_Mapping_Preregister.md` · `class_mapping_preregister.json` · `DensK1_Definition.md` · `stage_d_config_freeze.json` · `stage_e_config_freeze.json` · `script_sha256.txt` · `pip_freeze.txt` · `env_snapshot.txt` · `git_snapshot.txt` · `gpu_snapshot.txt` |
| `01_visdrone_main/` | `StageD_TestDev_Report.md` · `StageC_Cal48_Dev_Report.md` · `StageD_Channel_Decision.md` · `data/D_TESTDEV_summary.json` · `D_TESTDEV_per_image_metrics.csv` · `D_TESTDEV_status.json` · `C_cal48_summary.json` · `C_cal48_metrics.csv` |
| `02_paired_stats/` | `StageF_Paired_Stats_Report.md` · `data/F_summary.json` · `F_bootstrap_deltas.csv` · `F_wilcoxon_recall_small.csv` · `F_status.json` |
| `03_cross_uavdt/` | `StageE_UAVDT_Report.md` · `StageE_Channel_Decision.md` · `data/E_FULL_summary.json` · `E_FULL_per_image_metrics.csv` · `E_FULL_status.json` |
| `04_timing/` | `StageB_Timing_Report.md` · `data/B_TIMING_summary.json` · `B_TIMING_timings.csv` · `B_TIMING_protocol.json` |
| `05_packaging/` | `Neighbor_Protocol_Table.md` · `Failure_Boundary_Cases.md` · `Reproducibility_Appendix.md` · `Next_Authorized_Runs.md` · `README.md` · `figures/` |

### 冻结权重落点（来自 `00_freeze/Environment_Freeze.md`，本目录不存 `.pt`）

| 项 | 值 |
|---|---|
| Primary `last.pt` | `11_Datasets/processed/VisDrone/BT1/BT1-LOCAL-20260913-01/train/weights/last.pt` |
| Archive twin | `11_Datasets/processed/VisDrone/BT1/BTD1-CAL48-20260913-01/baseline_archive/BT1-LOCAL-20260913-01/train/weights/last.pt` |
| SHA256 | `bc42d54e37acaf1f698af487439dc222fa86fb4498623e8cf954df14e0aa5533` |
| 复核记录 | `00_freeze/weight_sha_reverify.txt` |

---

## 6. 其他重要对应

| 对应关系 | 路径 |
|---|---|
| 文献矩阵 ↔ 主题文件夹 | `Literature/Literature_Matrix.md` ↔ `Literature/01_Slicing_Inference/` · `02_HighRes_Efficient_SOD/` · `03_Multiscale_Zoom_Inference/` · `04_Aerial_Benchmarks_Eval/` |
| 写作计划 ↔ 大纲 | `Writing/P0_Two_Paper_Plan_2026-09-22.md` ↔ `Writing/P0_EI_Outline.md` |
| 缩写表 | `99_Attachments/查阅/Abbreviation_Glossary.md` |
| 文献登记 / 周审 | `00_Overview/Literature_Registry.md` · `Literature_Tracking_Workflow.md` · `Weekly_Literature_Audits/` |
| Paper 1 | `01_Paper1_OpenWorld_Risk/README.md` · `Stage_Guide.md` · `Research_Plan.md` |
| 实验入口 README | `00_Practice_UAV_Aerial_Detection/Experiments/README.md` |
| 执行读取序 | 根目录 `AGENTS.md` §1（其中 `Literature/matrices/Literature_Matrix.md` 与 `Experiments/Experiment_Plan.md` 当前**不存在**；实测矩阵在 `Literature/Literature_Matrix.md`） |

---

## 7. 故意不收录

| 类别 | 说明 |
|---|---|
| `.git/` | 版本历史 |
| `.obsidian/` · `.trash/` | 编辑器 / 回收站 |
| `11_Datasets/raw/**` 与 processed 下图像/标签像素树 | 只记文件夹用途；权重仅记 freeze 文档中的路径与 SHA |
| `Ultralytics/` 全量源码与缓存 | 工具依赖，非论文证据 |
| 大权重 `.pt` / `.npy` 预测缓存 / smoke 失败桶 | 证据仓规则见 `P0_EI/README.md`；SHA 以 `00_freeze/` 为准 |
| 无关脏工作区文件 | 例如未跟踪的 `99_Attachments/Pytorch教程/YOLO8.md`——不纳入本目录维护提交 |

---

*本文件为人工维护主目录；图 ↔ 数据表（§4）是权威对照，再生脚本不得发明指标。*

## Paper1 新增文档（2026-09-24）

| 路径 | 说明 |
|---|---|
| `01_Paper1_OpenWorld_Risk/Paper1_Dataset_Feasibility_Memo.md` | 数据集前置可行性备忘（非开工单） |
| `01_Paper1_OpenWorld_Risk/Paper1_Direction_Worth_Judgment_2026-09-24.md` | 未来可 UAV 采线下的方向/难度/发表再评估 |

| `01_Paper1_OpenWorld_Risk/AB_Independent_Publication_Boundary.md` | A/B 独立发表边界：贡献与结果互不绑定（2026-09-24 用户口径） |
| `01_Paper1_OpenWorld_Risk/AB_Direction_Judgment_With_Literature_2026-09-24.md` | A/B 分轨方向判断（文献依据·未来可UAV·独立发表） |

## Post-EI A/B 预备包（2026-09-24）

| 路径 | 说明 |
|---|---|
| `00_Overview/POST_EI_HANDOFF_A_B_Packages.md` | A/B 解锁纪律与登记 |
| `00_Overview/Current_Stage.md` § Post-EI 预备包登记 | IDLE 表；ACTIVE 仍为 P0_EI |
| `08_RailUAV_SOD/` | A 全树：Research_Plan / Stage_Guide / Literature / Writing / Experiments / Learning_Notes |
| `08_RailUAV_SOD/POST_EI_HANDOFF.md` | A 侧交接 |
| `01_Paper1_OpenWorld_Risk/` 扩展 | B 补齐 Mainline_Current、Completion_Metrics、Experiments/papers/B_*、Writing 提纲等 |
| `01_Paper1_OpenWorld_Risk/POST_EI_HANDOFF.md` | B 侧交接 |
| `01_Paper1_OpenWorld_Risk/Stage_Guide.md` | **干净稿**替换原冲突标记版 |
| `01_Paper1_OpenWorld_Risk/Literature/Literature_Matrix_Addendum_2026-09-24.md` | SRLF/Meng/conformal 等划界增补 |
| 既有备忘（保留） | `AB_Independent_Publication_Boundary.md` · `AB_Direction_Judgment_With_Literature_2026-09-24.md` · `Paper1_Dataset_Feasibility_Memo.md` · `Paper1_Direction_Worth_Judgment_2026-09-24.md` |

**命名说明：** A 使用 `08_RailUAV_SOD`（`02`–`07` 已为 Paper2–7）；B 继续使用既有 `01_Paper1_OpenWorld_Risk`。

## A/B 案头预备新增（2026-09-24 晚）

> 状态仍为各包 **PREP/IDLE**；未改 `00_Overview/Current_Stage.md` 唯一 ACTIVE=P0_EI。

### B · `01_Paper1_OpenWorld_Risk/`

| 路径 | 说明 |
|---|---|
| `Writing/Claim_Freeze_C1_C2.md` | **新建** C1/C2 案头冻结卡（精确句/范围/判据/近邻划界） |
| `Literature/Literature_Matrix_Addendum_2026-09-24.md` | **加厚** Practice 列式（已覆盖/缺口/增量） |
| `Learning_Notes/03_Open_World_Perception.md` | **加厚** Stage ① 可核对知识块 |
| `Learning_Notes/04_Railway_Context_and_Risk.md` | **加厚** |
| `Learning_Notes/05_Experiment_Design_and_Uncertainty.md` | **加厚** |
| `Writing/B_OpenWorld_Risk_Outline.md` | **扩展** Intro + Related Work 骨架 |
| `Research_Plan.md` / `Mainline_Current.md` / `Completion_Metrics.md` / `POST_EI_HANDOFF.md` | **更新** 冻结指针与案头清单 |

### A · `08_RailUAV_SOD/`

| 路径 | 说明 |
|---|---|
| `Literature/Literature_Matrix.md` §5 | **加厚** A0 已覆盖/未证实缺口/A增量 |
| `Writing/Taxonomy_Draft.md` | **新建** 部件×缺陷（超越扣件-only） |
| `Writing/Annotation_Timing_Protocol_D4_Draft.md` | **新建** D4 受控人时协议 |
| `Writing/Synthetic_Disclosure_Checklist.md` | **新建** 合成 fidelity–utility 披露 |
| `Writing/Collection_Protocol_Draft.md` | **新建 FUTURE** 采集协议（需 Current_Stage 授权） |
| `Writing/SciData_Disclosure_Template_Stub.md` | **新建** Sci Data 披露模板桩 |
| `Research_Plan.md` / `Mainline_Current.md` / `Completion_Metrics.md` / `POST_EI_HANDOFF.md` | **更新** |

## JCR Venue / Claim 政策更新（2026-09-24）

> **不**改变唯一 ACTIVE=P0_EI；A/B 仍 IDLE/PREP。主尺 = **JCR**；主张强/中/弱；地板 = 相关论文 **JCR Q2/Q3**。

| 路径 | 说明 |
|---|---|
| `00_Overview/Venue_and_Claim_Policy_JCR_2026-09-24.md` | **新建** 全局 JCR-primary + claim ladder 政策 |
| `00_Overview/Venue_Quartile_Policy_2026-09-22.md` | **指针更新** → 以 2026-09-24 文件为准 |
| `00_Overview/POST_EI_HANDOFF_A_B_Packages.md` | **更新** venue 表述 + 政策指针 |
| `01_Paper1_OpenWorld_Risk/Writing/Claim_Freeze_C1_C2.md` | **更新** 弱 fallback W1–W3（不定死） |
| `01_Paper1_OpenWorld_Risk/AB_Direction_Judgment_With_Literature_2026-09-24.md` | **更新** 「三区」→ JCR Qx；主张梯子 |
| `01_Paper1_OpenWorld_Risk/Research_Plan.md` | **更新** venue/claim ladder |
| `01_Paper1_OpenWorld_Risk/Writing/B_OpenWorld_Risk_Outline.md` | **更新** 不定死 + venue 一句 |
| `01_Paper1_OpenWorld_Risk/Mainline_Current.md` | **更新** JCR 表述 |
| `08_RailUAV_SOD/Writing/Taxonomy_Draft.md` | **扩展** §7 部件族采集难度排序 |
| `08_RailUAV_SOD/Writing/PartFamily_CollectionDifficulty_and_VenueBounds_2026-09-24.md` | **新建** 族×难度×工作/发表上下限 |
| `08_RailUAV_SOD/Research_Plan.md` / `Mainline_Current.md` / `Writing/RailUAV_SOD_Outline.md` | **更新** Sci Data 主轨 + JCR Q2/Q3 fallback |
| `PROJECT_CONTEXT.md` | **更新** 分区口径短注 |
