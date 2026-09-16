# 博士研究项目 Codex 执行与上下文管理规则

本文件适用于整个仓库。它只规定Codex的执行、上下文和交接方式，不改变各论文研究计划、阶段门或主张。

## 1. 事实来源与读取顺序

- 当前仓库文件是唯一事实来源；聊天摘要和检查点只用于导航，不能覆盖仓库事实。
- 每个新任务开始时，先完整读取以下当前有效文件：
  1. `README.md`
  2. `00_Overview/Project_Guide.md`
  3. `00_Overview/Current_Stage.md`
  4. `00_Overview/Seven_Paper_Roadmap.md`
  5. `00_Overview/Paper_Reading_Guide.md`
  6. `00_Overview/Learning_Note_Method.md`
  7. `00_Practice_UAV_Aerial_Detection/README.md`
  8. `00_Practice_UAV_Aerial_Detection/Research_Plan.md`
  9. `00_Practice_UAV_Aerial_Detection/Stage_Guide.md`
  10. `00_Practice_UAV_Aerial_Detection/Literature/Literature_Matrix.md`
  11. `00_Practice_UAV_Aerial_Detection/Experiments/Experiment_Plan.md`
  12. `00_Practice_UAV_Aerial_Detection/Experiments/Experiment_Tracker.md`
- `Paper_Reading_Guide.md`已经承担发表载体筛选和阅读等级职责；练手论文的具体文献状态以`Literature_Matrix.md`为准。
- 同一任务内已经完整读取且未变化的文件不重复全文读取；先用Git状态确认变化，再复核发生变化或当前任务直接相关的文件。
- 英语任务额外读取`90_English_Learning/README.md`及对应课程和进度文件；Paper 1任务额外读取`01_Paper1_OpenWorld_Risk/`中的入口、研究计划和阶段指南。
- 读取完成后检查Git状态和最近提交。用户未提交及未跟踪内容一律保留，不覆盖用户已有代码、数据、笔记或实验结果。

## 2. 一次只推进一个可检查任务

每轮开始先说明：

- 当前阶段；
- 本轮唯一任务；
- 成功标准；
- 本轮明确不做什么。

阶段指南没有允许时，不下载数据、不训练模型、不修改网络。发现练手论文与Paper 1或七篇论文规划冲突时，只报告冲突，不自行扩大研究问题。

每轮完成后报告：

- 修改文件；
- 验证结果；
- 仍存风险；
- 下一项最小任务。

## 3. 检查点规则

检查点是供人阅读的任务摘要，不是系统内部上下文压缩，也不是新的事实来源。

在以下任一时机生成一次检查点：

- 连续完成3个可检查任务后；
- 当前研究阶段即将切换时；
- 准备开启新Codex任务时；
- 用户明确要求“生成检查点”时；
- 系统压缩后发现任务状态、约束或证据可能丢失时。

检查点只保留：

1. 总目标和明确边界；
2. 当前阶段与唯一任务；
3. 已完成事项及证据位置；
4. 修改文件和Git状态；
5. 已验证结果；
6. 关键决定及理由；
7. 未解决问题和风险；
8. 下一项唯一任务及成功标准。

检查点不保留闲聊、重复说明、已被替代的方案、冗长工具输出或未经核验的推测。除非用户明确要求，不为检查点单独创建文件。

## 4. 压缩后的恢复规则

- Codex系统上下文压缩由运行环境管理，不能把“输出一份摘要”声称为已经执行系统压缩。
- 压缩或新任务续接后，先读取`Current_Stage.md`、检查Git状态，再核对检查点中的文件、运行编号和完成结论。
- 已有检查点与仓库冲突时，以仓库和Git证据为准，并报告差异。
- 不因为上下文压缩重复已经验证完成的工作；如果证据不可定位，则把该事项降级为“待核验”，不能猜测为已完成。

## 5. Token与Prompt Cache纪律

- `PROJECT_CONTEXT.md`用于向其他ChatGPT会话同步项目上下文。研究目标、阶段／授权、代码接口、数据／评价协议、实验完成／失败／恢复、关键结果或技术决策发生重要变化时，先更新事实所属文件，再在同一任务收尾同步该文件的日期、摘要、局限和证据链接。保留失败与未核验状态，不复制大量代码或日志；维护上下文不自动授权实验、提交或推送。

- 稳定规则保存在本文件和项目指南中，不在每轮提示中重复粘贴。
- 同一连续研究任务尽量留在同一个Codex任务中，以追加消息的方式推进；主题或阶段明显变化时，先生成检查点再开启新任务。
- 每轮提示只写本轮变化、目标、成功标准和新增证据；大型日志、论文或文件使用路径定位，不重复粘贴全文。
- 不为提高缓存命中率故意填充无用内容。
- 不无故频繁切换模型、推理强度、输出格式或工具集合。
- 压缩会缩短上下文，但可能暂时降低Prompt Cache命中率；只在里程碑、上下文压力或交接需要时使用，不按固定时间频繁总结。

## 6. Git与文件保护

- 主线A启动项目统一保存在`00_Practice_UAV_Aerial_Detection/`。不得向`99_Attachments/Archive_2026-09-16_PracticePaper/00_PrePaper_Lightweight_Detection/`写入主线A交付物；该目录保留原学习笔记和历史方案，其中LSM-Head及旧阶段指令不再作为当前执行要求。新学习记录写入新项目目录，旧笔记只按需引用。用户已接受弱化铁路场景，当前VisDrone优先，目录名沿用历史；具体任务以Current_Stage.md为准。

- 未经明确要求，不提交、不推送、不改写Git历史。
- 不修改或删除`99_Attachments/paper/`。
- 文件编辑保持最小范围，不顺手整理无关内容。
- 实验结果、失败记录和用户学习初稿不得因整理而删除。

- 2026-09-11用户明确纠正：主线A中AI的主任务是核心研究问题的创新点论证；学习记录由用户后续完成，不得把用户作答／学习验收设为AI科研推进门。旧学习状态如实保留，不代填、不虚标完成；此条不自动开放模型运行，技术／数据／授权范围要求仍有效。

## 7. 使用说明

处理新增论文或每周ChatGPT检索结果时，必须先读 `00_Overview/Literature_Tracking_Workflow.md`、`00_Overview/Literature_Registry.md`、`00_Overview/Innovation_Ledger.md` 及受影响方向的矩阵和研究边界；先审计去重，再归档PASS论文，完成主/次矩阵、必要创新台账四字段和周报同步后才能报告完成。暂停方向允许文献维护，不解除学习与实验阶段门。

Codex、检查点、Token、Skills、Plugins和常用提示方式见：

`99_Attachments/Codex_Usage_Guide.md`
