# 论文跟踪—审计—归档—索引更新

## 1. 职责与入口

本流程由Codex每周定时主动检索，并在本仓库执行审计、去重、归档和联动更新；也支持用户手动提供ChatGPT检索结果。检索消息是线索，不是可信文献或可引用证据。无需为每批再次确认常规检索、审计和文件更新。

已于2026-09-07创建Codex定时任务“博士论文每周跟踪与审计”（ID：`automation-6`），绑定当前项目任务，每周一09:00（北京时间）执行。这不是ChatGPT消息接收服务，不依赖用户每周粘贴清单。首次检索最近30天，之后从上次成功覆盖日期向前重叠7天检索到当前日期；未完成区间不推进覆盖日期。

每轮覆盖铁路无人机巡检、开放世界风险感知、三维灾情评估、任务导向/语义通信、通信受限协同感知、UAV通信、UAV-ISAC、Risk/Task-Aware ISAC、RGB+RF/CSI多模态感知、不确定性、主动感知、Next-Best-View、多无人机、MARL/GNN和应急决策，记录每组实际覆盖及缺口。

优先来源：IEEE TWC、JSAC、TSP、TMC、T-ITS、TII、TIM、TCCN、RA-L、TRO、Automation in Construction、Advanced Engineering Informatics（AEI）、Measurement、TGRS，以及CVPR/ICCV/ECCV、ICRA/IROS、ICC/GLOBECOM/ICASSP。直接相关的重要近邻与可信预印本亦可纳入，载体优先级不替代实际相关性。

只有值得关注的新论文（Must Read或有明确用途的Recommended）、影响创新/边界/实验判断的重要进展、关键更正撤稿或需要用户处理的执行阻塞才通知。无变化、重复或仅Reference Only的常规归档只写本地周报，保持安静。

这是一条文献维护支持线：允许对Paper 1–7维护候选、风险与索引，不代表开始暂停方向的系统研究、学习或实验，不计为阶段精读完成。当前学习任务及阶段门仍由[Current_Stage.md](Current_Stage.md)决定。真实研究边界仍以[七篇路线](Seven_Paper_Roadmap.md)及各方向研究计划为准；遇到冲突只报告并登记待决事项。

| 文件 | 职责 |
|---|---|
| [Literature_Registry.md](Literature_Registry.md) | 全局工作ID、标识符、版本关系、唯一正文位置与跨方向入口；去重事实源 |
| 各方向 `Literature/Literature_Matrix.md` | 审计摘要、阅读优先级、创新关系；主归属保存完整记录，其他方向只保存交叉链接 |
| [Innovation_Ledger.md](Innovation_Ledger.md) | 候选创新的最近工作、尚存缺口、风险及待验证动作 |
| [Literature_Audit_Template.md](Literature_Audit_Template.md) | 单篇审计证据；区别作者主张、原文结果和Codex推断 |
| [Weekly_Literature_Audit_Template.md](Weekly_Literature_Audit_Template.md) | 每批输入及处置、周结论、联动完成检查 |

旧论文及矩阵不是本流程已审计的记录。首次遇到旧工作时先匹配旧ID和文件，补审计后采用原位置，不批量迁移、不虚构历史Date Added。不修改或删除 `99_Attachments/paper/`。

## 2. 每周执行顺序与通过门

1. **接收**：记录实际日期、时区、检索覆盖区间、来源消息/文件、检索式与全部候选；周报命名为 `00_Overview/Weekly_Literature_Audits/Weekly_Literature_Audit_YYYY-MM-DD.md`（该目录首次有真实批次时创建）。同周补充同一报告并保留批次ID，例如 `2026-09-07-B01`。只新增批次条目，不覆盖旧记录；重复输入标记重放。
2. **先去重**：按第4节搜索注册表、所有旧矩阵/阅读清单和仓库PDF文件名。已有工作沿用Work ID；未解决身份冲突则 `HOLD`，不归档正文。
3. **核验身份**：实际访问出版社/会议官方论文页、DOI落地页、arXiv记录或作者正式存储库；核对Title、Authors、DOI/arXiv、各日期和版本。搜索摘要、ChatGPT总结不能单独证明论文存在。优先交叉核验正式页与全文；失败记录访问日期及原因，不推断论文虚假。
4. **技术审计**：阅读可获得全文，按模板提取问题、数据及划分、方法、创新、关键结果和局限，并记录页码/节/表与来源。文中未报告写 `Not reported`；因未能核实写 `Unknown`；不适用写 `N/A + 理由`，均不可留空冒充完成。综述/理论论文可无数据或实验，但必须记录其论证方式和覆盖边界。
5. **研究映射**：比较Paper 1–7的实际输入、输出、主张和创新台账，选唯一主方向及必要次方向；直接比较问题、方法、数据协议、评价目标和已有证据，给出重合/冲突理由。仅出现UAV、风险或YOLO关键词不算直接相关。练手论文单独映射 `P0`，不强行塞入Paper 1。
6. **决策**：`PASS` = 身份可验证、版本明确、技术证据足以支持相关性与冲突判断且有项目用途；`HOLD` = 身份/版本/关键技术证据不足、仅摘要或来源矛盾；`REJECT` = 已核实无关或有证据证伪。`Irrelevant`必须REJECT。预印本可PASS，必须注明未同行评审；新颖性冲突高不是拒收理由，反而应保留挑战证据。只有PASS允许新的正文归档。HOLD/REJECT在周报保留标识、理由、缺口与再查条件，不能计入新增或精读完成。
7. **归档并联动**：先写审计证据，再保存一个主正文或稳定参考链接；更新注册表、主矩阵、跨方向引用、受影响创新台账和已有主题Reading_List。没有可合法取得的PDF时用已审计的公开全文链接，不绕过访问限制。论文可由浏览器临时查看审计，但审计前不写入项目正文库。
8. **收尾验证**：逐条核对主矩阵必填字段、工作ID与版本唯一性、正文/审计链接、所有受影响创新与周报条目。任一更新失败则该条 `Sync Status=INCOMPLETE`，周报标记未完成；下次按相同Work ID补齐，不重建正文。全部通过才 `COMPLETE`，不得将局部写入报告成整批完成。

无新论文时仍记录零新增、重复/待核验/排除数量；新版本或创新风险变化单列，不能用“零新增”掩盖有变化。

## 3. 核验与阅读标准

发表日期分别保留首次预印本、当前版本上线、early access、正式卷期/会议出版日期；没有来源就Unknown，不能用检索日替代发表日。Year按当前引用版本的出版/上线年份填写，Date Added是首次通过审计进入索引的实际日期，后续修订只改Last Audited。未来日期必须区分已接受/计划出版与实际已上线。

Publication Status使用 `preprint / accepted / early access / published / withdrawn / retracted / unknown`，版本号单列。只有官方证据能升级状态；arXiv v2不等于正式出版。撤稿、撤回或重要勘误触发重新审计，保留历史，不删除已有正文；在矩阵和台账撤销失效证据的支持作用并检查所有次关联。

载体A–D及四级阅读定义统一见[阅读等级](Paper_Reading_Guide.md)。JCR/中科院/CCF/学校等级须记体系、适用年份、官方来源与核验日；拿不到来源写Unknown，不由期刊名、影响因子或录用宣传推断。载体强弱不能替代研究相关性。

`Audit Status`、`Publication Status`、`Reading Status`、`Reading Priority`、`Sync Status`独立记录。PASS不等于DONE；Must Read不解除阶段门。次方向需要阅读时用主记录链接，并注明阶段条件，不建立第二份正文或重复事实摘要。

## 4. 工作级去重与版本维护

- 全局Work ID用 `W-0001` 起的递增编号；它表示一项工作，而非一个下载文件或arXiv版本。分配前检查注册表最大值；保留原T/L编号为Legacy ID。
- DOI：去掉 `doi:` / `https://doi.org/` 前缀、空格并转小写后精确匹配；arXiv：去掉URL及vN后匹配基础ID，vN单独保留。不同DOI不自动视为不同工作。
- 标题：Unicode规范化、大小写/标点/空白归一后比较，再核对作者、摘要、方法和数据。标题相似只触发疑似重复检查，不能自动合并；缺少标识符也不能跳过去重。
- 官方DOI关联、arXiv journal-ref或作者版本声明可证明preprint→early access→published关系；标题变化保留别名。扩展期刊版是否独立贡献需审计；不明确时HOLD。确有独立问题/证据则分新Work ID并记录 `extends W-xxxx` 与增量依据。
- 同工作同版本重复：只在周报记录重复与来源，不新增矩阵行/PDF。新版本：沿用Work ID，核对方法、数据、结果、局限的变化，追加版本历史并刷新同一主矩阵行；Date Added不变，周报统计为版本更新。
- 一个工作只有一个当前Canonical Reference/PDF。历史版本如已用于实验或引用应原地保留并在版本表标为历史证据，不能当作新论文计数；不得自动覆盖/删除旧文件。纯出版元数据更新无需再下载相同正文。
- 跨方向使用同一Work ID与主记录链接；主归属调整时更新注册表及所有交叉入口，保留旧归属记录。移动已有用户文件需要明确必要性，通常只调整索引。

## 5. 自动归属表

按贡献的主要问题归属，按应用场景或关键词辅助判断；先选现有主题子目录，不匹配时把审计文件和正文直接放在该方向 `Literature/`，不预建大量目录。命名使用 `W-xxxx_Audit.md` 和 `W-xxxx_Year_ShortTitle.pdf`。

| Related Paper | 主问题/边界 | 实际目录 |
|---|---|---|
| P0 | 封闭集小目标、共享检测头、真实速度 | `00_PrePaper_Lightweight_Detection/Literature/` |
| P1 | 已知/未知危险候选、轨道上下文、可信告警 | `01_Paper1_OpenWorld_Risk/Literature/` |
| P2 | 多时相三维灾害测量、侵界量与误差 | `02_Paper2_3D_Disaster/Literature/` |
| P3 | 带宽/时延约束下风险语义传输与协同感知 | `03_Paper3_Comm_Perception/Literature/` |
| P4 | 风险驱动通信—感知功率/带宽/波束/时隙分配 | `04_Paper4_Risk_ISAC/Literature/` |
| P5 | 视觉退化下第二模态可靠融合与缺失模态 | `05_Paper5_Multimodal_Risk/Literature/` |
| P6 | 风险/不确定性驱动复检、视点、停止决策 | `06_Paper6_Active_Inspection/Literature/` |
| P7 | 多机联合任务分配及搜索、传输、处置决策 | `07_Paper7_MultiUAV_Decision/Literature/` |

例如：仅三维分割不等于P2定量测量，图像恢复不等于P5多模态，普通路径规划不等于P6风险复检。此类材料只能根据实际用途定为背景，不能写成直接创新近邻。无法判定主归属则HOLD并说明缺少什么证据。

## 6. 创新与实验联动

凡新证据直接支持、削弱、覆盖或否定候选创新，必须在同一批次更新台账的 **Closest Prior Work、Existing Work、Remaining Gap、Novelty Risk**，包括所有被影响的次方向。不能只贴论文标题；要写已覆盖什么、剩余差异是否可检验、风险为何变化，链接审计证据。

每条影响使用 `I-批次ID-序号` 回链：`Work ID → Innovation ID/边界条款 → 风险变化 → 最小验证假设/唯一变量/指标/停止条件 → 目标Experiment_Plan → 后续Run ID`。没有新证据时Remaining Gap继续待核验，Novelty Risk不得写低风险。不得因为换数据集或堆叠模块就判断创新成立。

阶段未许可时仅在台账和周报记录 `PROPOSED/BLOCKED` 及未来目标文件；不创建暂停论文实验目录，不运行实验。允许且有充分依据时再将待决动作写入已有实验计划，给出计划条目链接；实际运行才登记Run ID。研究边界调整记录旧边界、挑战证据和建议，待用户明确决定后修改研究计划；审计不自行改主张或启用Paper 2–7。

## 7. 每周触发提示

> 按 `00_Overview/Literature_Tracking_Workflow.md` 处理以下本周ChatGPT检索结果（或指定文件）。先逐篇核验和去重，再归档PASS论文，联动主/次方向矩阵和创新台账，最后生成或补充本周Weekly_Literature_Audit。保留HOLD/REJECT及重复记录；缺证据不能编造；不改变当前阶段或研究边界。输入：……

本提示用于额外的手动批次；每周自动检索由上述Codex定时任务执行，避免重复创建同类定时任务。
