> **路径更新 2026-09-16：** 活跃练手目录改为 `00_Practice_UAV_Aerial_Detection/`；旧 `00_PrePaper_*`／`00_Startup_*` 在 `99_Attachments/Archive_2026-09-16_PracticePaper/`。当前事项以 `00_Overview/Current_Stage.md` 为准。

# 项目上下文：博士研究与主线A启动论文

最后核验：2026-09-16。用途：将本文件提供给另一个ChatGPT会话，使其理解目标、现有实现、证据和下一步边界。本文是仓库事实的摘要与导航，不替代研究计划、运行记录或原始产物；与源文件不一致时重新核验，不按旧摘要执行。路径均相对仓库根目录；没有仓库访问权限的会话只能基于本摘要讨论，不能声称已经检查原始文件。

## 1. 当前结论与唯一待办

**2026-09-16 已采用决定：P0 不再追求独立新机制；近程只写 EI 对比／协议稿。** A0 对独立新机制仍 HOLD；A2／A3／A4 未开放；A5 仅对本 EI 稿有限开放。100 轮普通 YOLO11n 及 BTD1–BTD12 已完成；不创建 BTD13，不默认重跑。

**当前唯一待办：撰写 P0 EI 会议稿，并选定 2027 年会期。** 主张仅 P0-EI-C1／P0-EI-C2（PROPOSED）。旧 P0-A-C1／C2 保持 HOLD（历史追踪）。Paper 1 两项主张与 Paper 2–7 保持 PAUSED。

权威入口：[当前阶段](00_Overview/Current_Stage.md)、[主线A当前](00_Practice_UAV_Aerial_Detection/Mainline_A_Current.md)、[2026-09-16决定](00_Practice_UAV_Aerial_Detection/Research_Question_Decision_2026-09-16.md)、[研究计划](00_Practice_UAV_Aerial_Detection/Research_Plan.md)、[阶段指南](00_Practice_UAV_Aerial_Detection/Stage_Guide.md)。

允许整理已有表成稿；若缺同口径 4090 时间表或一次 test-dev 终评，须先登记 Run ID。禁止新训练、改网络、用未采集高原数据占位写结果。不把 VisDrone 写成铁路安全或高原泛化；不承诺期刊录用。

## 2. 研究目标与历史转向

博士项目以铁路无人机巡检为总体应用场景，七篇论文依次研究：危险感知→三维灾害量化→通信受限风险共享→通感资源分配→多模态风险理解→主动复检→多无人机联合决策。当前只推进Paper 1研究链，Paper 2–7保持PAUSED。

Paper 1前先做一篇独立启动／练手论文，不计入七篇主论文。当前题目为“面向无人机航拍的时间预算约束小目标检测”。研究边界：单目RGB、无人机视角、已知类别二维小目标检测；关注固定整帧时间预算下的局部高分辨率计算分配。铁路走廊已退出方法前提，目录名称沿用历史；不能用VisDrone结果推断铁路安全效果。

原区域机制的两项候选问题P0-A-C1/C2是：同预算能否优于整图／增大输入／均匀切片／简单选择，以及能否控制选区漏检与超时。二者均HOLD、未成立。每篇最多两项主要主张，不以增加注意力、损失、增强、蒸馏、剪枝等模块弥补证据不足。

重要历史变化：

- 早期LSM-Head共享轻量P2–P4头及B0/B1/B2/M对照已退出执行；没有这些模型的实验结果。旧P000/P001/P010/P011/P020/P021均未运行、BLOCKED，不复用编号。
- 2026-09-10转主线A可行性审查，后接受VisDrone优先及弱化铁路前提。UAV-RSOD退出当前关键路径。
- 2026-09-11明确AI主任务为核心问题的创新论证；用户学习由本人后续完成。S0-01仍未通过，不代填、不虚标完成。
- 2026-09-12批准受限普通基线；云端受阻后改本机。2026-09-13批准连续接续至100轮，已实际完成。
- 2026-09-16采用决定：近程 EI 会议稿（P0-EI-C1／C2）；中期高原数据后三选一另开；远期再谈 P1；P2／真 ISAC 不启动。P0-A-C1／C2 保持 HOLD。
- 2026-09-14强简单基线与近邻审查促使当前机制暂缓，回到贡献定位决策。

Paper 1保留已知／未知危险候选、轨道上下文排序、固定告警预算危险召回和可信复核方向；候选主张仍待审计与验证，本轮没有启动其开放世界实验。稳定路线见[七篇论文路线](00_Overview/Seven_Paper_Roadmap.md)。

## 3. 仓库与代码结构

本仓库是研究文档加独立实验脚本，不是已封装的训练平台。当前主线A交付统一进入`00_Startup_Railway_UAV_Detection/`；旧目录`00_PrePaper_Lightweight_Detection/`仅保留学习初稿、文献和历史方案。

| 位置 | 职责 |
|---|---|
| `00_Overview/` | 当前阶段、路线、文献注册表、创新台账、周审计与工作规范 |
| `00_Startup_Railway_UAV_Detection/Literature/` | 直接近邻审计、候选及否决报告；主矩阵管理阅读和审计状态 |
| `00_Startup_Railway_UAV_Detection/Experiments/` | 数据审计、标签转换、训练／恢复、诊断／测速／独立校核脚本、协议及结果报告 |
| `00_Startup_Railway_UAV_Detection/Learning_Notes/` | 新学习记录；不以研究审计替代本人掌握证据 |
| `00_Startup_Railway_UAV_Detection/Writing/` | 写作提纲和投稿适用性待核验项，尚无获验证的新方法稿件 |
| `11_Datasets/raw/VisDrone/` | 原始ZIP和评价工具等，Git忽略 |
| `11_Datasets/processed/VisDrone/` | 数据转换、审计、预测、权重、日志、运行证据，Git忽略 |
| `01_Paper1_OpenWorld_Risk/`、`02_...`至`07_...` | 主论文计划与材料；不从当前诊断自动启动后续研究 |

主要代码均在主线A的`Experiments/`：

| 文件 | 实际作用 |
|---|---|
| `acquire_visdrone.py`、`fetch_visdrone_mirror.py`、`analyze_visdrone.py` | 原包获取和文件／标注／重复审计；历史UAV-RSOD另有审计脚本 |
| `convert_visdrone_labels.py`、`check_label_adapter.py` | 原八字段标注到YOLO标签的转换及构造校核，保留排除原因 |
| `prepare_bt1_data.py` | 核验固定train/val ZIP SHA，生成训练和cal48清单、原标注副本及转换日志；拒绝覆盖已有输出 |
| `baseline_training_spec.json` | BT-1固定配置；不是启动文件，内部平台／进度字段部分过时，实际以运行resolved_args和状态为准 |
| `run_bt1.py`、`bt1_checkpoint.py` | 普通YOLO11n训练包装、环境／资源检查、轮末恢复包及接续；支持continuous；不是新网络 |
| `BT1_Cloud_Training.ipynb` | 历史云端交接入口；不代表云端训练已发生 |
| `check_visdrone_semantics.py`、`run_official_octave_check.m` | 评价语义构造检查和原版代码有限兼容交叉核验 |
| `diagnose_bt1.py`、`summarize_bt1_diagnosis.py` | BTD1归档、全图／切片预测、弱响应候选与简单对照、小目标匹配 |
| `analyze_density_residuals.py`、`compare_dedup_density.py` | BTD2/3缓存残差与去重密度对照 |
| `run_diag500_pair.py`、`fast_stable_nms.py`、`check_fast_nms.py`、`run_fast_pipeline.py` | BTD4–6两规则实测、公共NMS等价加速和整帧复测 |
| `analyze_conditional_recovery.py`、`finalize_conditional_recovery.py` | BTD7残差、条件收益及失败后的接续归档 |
| `check_single_crop.py`、`compare_f1280_cache.py` | BTD8/9单片上界、时间测量及F1280缓存强基线比较 |
| `analyze_f1280_errors.py`、`verify_f1280_errors.py` | BTD11缓存错误分解、独立最大匹配证书和GT修复重评 |
| `verify_*.py`、`test_bt1_*.py` | 对应运行的输出、集合守恒、等价性、恢复与语义校核；不能等同创新通过 |

普通推理链：图像→固定YOLO11n→全图预测／可选局部窗口→坐标还原→公共去重→忽略区和匹配评价。原局部池使用原图640窗口、步长512；选择策略和片数按各协议固定。缓存分析脚本与真正加载模型的运行分开登记，缓存分析耗时不能称检测速度。

## 4. 数据集、划分与评价口径

VisDrone2019-DET已完成8,629图文件级审计：train 6,471、val 548、test-dev 1,610。三组均可解码，图像标注对应且CRC通过。原包来自Ultralytics公开维护者副本；val与发布方ZIP字节一致，train/test-dev与作者原包逐字身份仍Unknown。学术用途已有审计依据，完整许可／商业使用范围未独立确认。

十类顺序：pedestrian、people、bicycle、car、van、truck、tricycle、awning-tricycle、bus、motor；原类别1–10映射YOLO索引0–9。原八字段标签保留。3条train零高度异常已定位，原文件未改；普通训练转换不具备区域级ignore，删除正标签并不等于屏蔽该区域的负监督。

| 集合 | 已有用途 | 不能怎样解释 |
|---|---|---|
| train6471 | BT-1单seed普通训练 | 不能声称来源严格独立、训练ignore已解决 |
| cal48 | val按SHA256(`diag-v1:`＋图像文件名)排序取前48；训练监控与反复开发 | 不是独立测试或新评分器拟合后的独立评估集 |
| diag500 | val其余500图；BTD4/6已用于规则验证／测速 | 已属开发证据，不再冒称未接触测试集 |
| test-dev1610 | 已做静态数据审计，拟保留最终模型评价 | 未开展模型评价；静态审计不等于完全未看过数据 |
| test-challenge | 无本项目可用公开真值记录 | 不假设可本地评价 |

未发现跨split字节或RGB精确重复，但有34对跨split近重复候选和人工确认的共享场景线索。文件名前缀不是已确认的航次／城市ID；来源组Unknown，不能宣称跨场景独立泛化。

UAV-RSOD历史审计HOLD：原图检测框与增强来源映射仍不足，有split重复问题；作者询问信只是未发送草稿，当前不阻塞VisDrone。见[VisDrone审计](00_Startup_Railway_UAV_Detection/Experiments/A0-05_VisDrone_File_Audit.md)、[UAV-RSOD审计](00_Startup_Railway_UAV_Detection/Experiments/Data_Feasibility_Audit.md)。

评价必须区分：

- 原生训练监控AP：Ultralytics验证器在cal48得到，不冒充VisDrone官方兼容AP。
- 官方评价语义：工具包提交`005445782213e20cb91bc50a597db3dd949e749a`，忽略区域、排序、类别汇总和maxDets均有特定行为。Python构造24/24与Octave原版有限兼容交叉24/24、差异0；不是MATLAB全域验证或真实模型官方AP结果。
- BTD小目标诊断：有效GT按既定ignore处理，原图面积0<w×h<1024；固定conf=.25、匹配IoU=.5、公共NMS IoU=.5及每图最多500框。cal48有2720小GT、3619全尺寸有效GT；表内FP如无另注均为全尺寸FP，不能与小TP组成Precision。
- 时间包含各协议规定的处理链，必须回链具体运行边界。40ms为F1280测得的相对参考，不是业务硬期限；均值、p95、超限率不得混用，也不宣称真实机载部署。

## 5. 模型与训练身份

普通YOLO11n P3–P5，COCO预训练初始化后适配VisDrone十类；未实施LSM-Head，未改Backbone、Loss或候选专用模块。

- 环境：Windows，独立Conda `H:/Conda/envs/UAV_BT1`；Python3.12、Ultralytics8.4.90（提交`07958a70205d1388612bd00f8a2f32cf769d8fed`）、torch2.7.1+cu126、torchvision0.22.1。
- 训练：GTX1660SUPER 6GiB，imgsz640、batch4、FP32／amp=false、seed0、SGD、100轮。详细超参数看固定JSON及运行快照；诊断通常batch1、FP32。
- 三段连续覆盖1–3、4、5–100，无缺轮／重复；合计约14.99小时墙钟。断点恢复已核验，不声称与单进程不中断训练逐位等价。
- 固定取第100轮末轮EMA `last.pt`，不按cal48最佳值选模；框架best及末尾对best的验证输出不替代末轮指标。
- 权重：`11_Datasets/processed/VisDrone/BT1/BT1-LOCAL-20260913-01/train/weights/last.pt`。
- SHA256：`bc42d54e37acaf1f698af487439dc222fa86fb4498623e8cf954df14e0aa5533`（本次实际复核一致）。

训练和推理框架在外部Conda环境，不是仓库自带；迁移不能只复制脚本后假定环境相同。

## 6. 已完成运行与主要结果

完整编号、协议和状态见[实验跟踪表](00_Startup_Railway_UAV_Detection/Experiments/Experiment_Tracker.md)。以下均为受限开发证据；执行PASS不代表正式门通过。

| 任务／运行 | 实际完成与结论 |
|---|---|
| BT1-SMOKE-20260912-01 | 4图1轮、batch1，148.75秒，训练／保存／重载／P3/P4读取PASS；权重不可用作基线 |
| BT1-LOCAL-20260912-01、02及20260913-01 | 连续完成100轮。末轮cal48原生Precision=.46533、Recall=.34912、mAP50=.34101、mAP50–95=.18591；无正式独立测试 |
| BTD1-CAL48-20260913-01 | 2720小GT中558个全图漏检可被局部恢复；弱响应候选恢复336，P3-only338，密度429；v0.1转HOLD |
| BTD2-DENSITY-20260913-01 | 密度遗漏129个可恢复GT：77未覆盖中心、42覆盖但局部未检出、10合并／匹配变化 |
| BTD3-DEDUP-20260913-01 | cal48去重密度相对原密度小TP1259→1282（补54／丢31），Recall46.29%→47.13%；FP1233→1249；图像配对区间跨0，不能称稳定增益 |
| BTD4-DIAG500-20260913-01 | 23708小GT；密度／去重小TP11129／11402，净+273、Recall+1.15个百分点。均值90.89／90.21ms；相对61ms参考超限89.80%／89.00%，预算失败 |
| BTD5-NMS-20260913-01 | 115构造＋432缓存组逐行等价，9504次计时无差异；公共合并约27ms降至约6–7ms。工程加速非创新；资源偏差见下一节 |
| BTD6-PIPELINE-20260913-01 | 新NMS完整流程3000次输出与BTD4逐值相同；均值51.23／51.25ms，p95 82.63／82.90ms；重校40ms参考超限98.80%／99.07%，预算仍失败 |
| BTD7-RESIDUAL-20260914-01／02 | 01归档失败，02接续完成。105残差为26未覆盖、67覆盖未检出、12合并／匹配；GT最佳第二片1308对去重1282仅净+26，不支持继续第二片重排为唯一创新 |
| BTD8-SINGLE-20260914-01 | cal48密度单片1172，GT最佳单片1223；密度K1均值37.36ms、p95 64.51ms，40ms超限20.83%；尾部预算未通过 |
| BTD9-F1280-20260914-01 | 复用BTD8预测比较，F1280比实际单片更准且更快；当前区域机制HOLD，详见下表 |
| BTD10 | 书面研究重审，无实验Run ID；定位／分数失配和密集后处理只是观察问题，未形成新创新 |
| BTD11-ERROR-20260914-01 | 仅缓存分析，1408小FN和839FP完成分解；5.23秒，144最大匹配证书及修复重评通过，无模型调用 |
| BTD12 | 书面单机制审查，无实验Run ID；尺度条件DFL分布重评分因缺独立创新依据DISMISSED，非实测失败 |

cal48同口径关键比较（conf=.25、IoU=.5）：

| 配置 | 小TP／2720 | 小Recall | 全尺寸FP | 平均整帧／p95 ms |
|---|---:|---:|---:|---|
| F640全图 | 840 | 30.88% | 576 | 本批无可直接比较时间 |
| F640＋密度单片K1 | 1172 | 43.09% | 1051 | 37.36／64.51 |
| F640＋GT最佳单片 | 1223 | 44.96% | 1038 | 无可部署选择器时间 |
| F1280全图 | 1312 | 48.24% | 839 | 27.33／41.44 |

F1280仍有6.94%帧次超过40ms参考，不能称硬实时通过。GT逐图选择F1280或最佳单片最多1345小TP，仅比始终F1280净增33；GT最佳单片独有169个目标不等于能净增169。以上不否定所有切片方法，仅限制当前模型、窗口和开发样本上的机制主张。

BTD11低分空间：阈值.25→.10小TP1312→1624，但FP839→2170（+1331）。独立GT修复分数／定位／类别分别补559／142／198，均不丢原小TP；不能相加，也不是可部署方法收益。低分同类IoU符合证据涉及564个漏检；分数修复最大一对一容量560、实际重评559，不混用这些数量。35/48图已截断到500框，缺NMS前轨迹和原始分布，不能推断完全无响应或NMS误删因果。

核心证据：[100轮归档](00_Startup_Railway_UAV_Detection/Experiments/BT1_100_Epoch_Archive.md)、[BTD6](00_Startup_Railway_UAV_Detection/Experiments/BTD6_Pipeline_Result.md)、[BTD9](00_Startup_Railway_UAV_Detection/Experiments/BTD9_F1280_Result.md)、[BTD11](00_Startup_Railway_UAV_Detection/Experiments/BTD11_Error_Structure_Result.md)。

## 7. 失败、否决与恢复记录

- **实际工程失败**：BTD7-01因NumPy int64的JSON序列化失败而归档中断，计算中间集合已保存。BTD7-02只接续归档及缺失统计并通过校核，01保留FAILED和failure.txt，不改写成从未失败。
- **资源协议偏差**：BTD5未强制实施1GiB内存守卫，单次私有内存1.089GiB、峰值未知；不能称全协议合规。BTD7-01资源样本未落盘、峰值未知；02补有离散采样，不能追补01峰值。
- **效果／预算负结果**：弱响应v0.1不优于简单密度或P3-only；去重两片虽提高召回，BTD4/6整帧预算未通过；BTD8单片尾部预算未通过；BTD9简单F1280超过当前GT单片上界。
- **书面否决**：A0-09熵反馈／成本归一化候选DISMISSED；BTD12尺度条件DFL分布评分DISMISSED。前者受顺序收益／成本近邻覆盖，后者受GFLV2分布质量估计和多变量尺寸条件校准覆盖；不是对应新模型训练失败，也不是穷尽全领域。
- **平台／数据准备阻塞**：Kaggle手机验证未完成，Colab在安装前Python版本检查失败；无云端模型训练。官方train/test-dev下载配额受限后使用维护者副本。A0-05曾因输入尚未组装而静态审计失败，失败目录保留；不算模型失败。
- **暂停不等于失败**：BT1前两段按安排暂停，之后已正确接续到100轮。旧LSM-Head实验未运行，不写成失败实验。

## 8. 重要技术决定与未解决问题

1. 固定末轮EMA、单检测器和统一后处理隔离变量；F1280必须作为后续机制面对的强简单基线，不把分辨率增加或公共NMS加速包装为创新。
2. 区域选择不能用GT；oracle仅离线界定空间。GT修复、缓存分析、实际推理和正式测试分开陈述。
3. 数据来源组Unknown、训练区域ignore偏差、单seed及cal48反复开发限制仍在；diag500也是开发证据。尚无多种子、独立场景或最终test-dev结果。
4. 当前未找到推理可得、能有效区分低分真小目标和假框且超出直接近邻的新信息机制；“存在GT恢复空间”不能替代这一缺口。
5. W-0001–W-0014为主矩阵已有审计记录；PASS表示审计通过，用户阅读仍SCREENED而非DONE。SAHI、QueryDet、ESOD、ROI-Gated SAHI、MRU-YOLO、Dynamic Zoom-in、AutoFocus及GFLV2等已有覆盖不能忽略。本文只汇总仓库审计，不重新核验外部文献。
6. 用户接受中科院小类三区或JCR三区；二者不等价，具体期刊、学院／参评年度和国奖认可仍待核验。没有已确认投稿载体或录用保证。
7. 无Jetson、TensorRT、真实无人机或机载功耗验证成果。不得从桌面GPU结果推断真实机载可用。

## 9. 迁移、Git与证据可用性

2026-09-15本轮开始时：分支main，HEAD为`fb2d58d8829985a329b0dcb6284bcb8696616e84`；本地origin/main引用相同，本轮未联网刷新远端。**工作区不干净**：README、AGENTS、多个Overview文件及其他已有文件有修改；整个主线A目录和周审计目录尚未跟踪。这些是此前工作，不归因于本次文档任务；不能用旧提交号代表当前实验代码版本，应查运行内脚本快照与SHA。

数据、权重、ZIP和大部分JSON默认被忽略；`baseline_training_spec.json`有显式例外。`.obsidian` JSON已取消跟踪并保留本地。仅克隆GitHub不会取得当前未提交的主线A，更不会取得被忽略的训练数据和实验产物；迁移需要另行保存相应目录、固定环境及哈希清单。本文不代替备份，本次未提交或上传。

原始运行根：`11_Datasets/processed/VisDrone/BT1/<Run ID>/`。关键资产：

- `BT1-LOCAL-20260913-01/train/weights/last.pt`：固定末轮权重。
- `BTD1-CAL48-20260913-01/baseline_archive/epochs_001_100.csv`：100轮合并记录。
- `BTD1-CAL48-20260913-01/BT1_100epochs_evidence.zip`：归档包，SHA256 `9419bf3cc870b1e7c940a7075d0092acf11d65711b19165f0d2ea6486cad21b0`，已有报告核验；本次未重新计算此包哈希。它位于同一磁盘，不是异地备份。
- BTD1–BTD9及BTD11运行目录：预测、逐图集合、统计、协议／代码快照、输入输出SHA和校核；BTD7两次运行均保留。

本次核验范围：完整读取当前入口和实验跟踪，检查关键脚本与报告，定位已有运行目录；实算末轮权重SHA、读取100轮CSV末行、BTD11 status与verification文件，与摘要一致。没有重新运行模型、实验或全量校核，也没有重新逐个计算全部产物哈希。其他历史PASS按对应已保存报告陈述。

部分README、Stage_Guide、Experiment_Plan和配置内保留“未运行100轮”“下一项云端训练”“diag500未访问”等历史文字；最新页首和实际结果已明确替代。不要据此重跑。Seven_Paper_Roadmap的前置论文链接仍指旧目录；当前主线A位置以AGENTS及Current_Stage为准。本轮不顺手重写这些历史材料。

## 10. 后续维护规则

每次目标／边界／阶段或授权变化，数据／划分／指标／模型／代码接口变化，运行完成／失败／恢复，关键负结果或技术决定出现时，在同一次任务收尾更新本文件；无需等待用户重复要求。先更新事实所属的计划、跟踪表或结果报告，再修改这里的对应摘要、日期和证据链接。

保持简明：只保留理解与接续必要的身份、结论、局限及路径，不复制大量代码、日志或文献正文。过时计划明确标为历史；失败保留；未验证写Unknown／待核验；不把PASS、HOLD、DISMISSED混为同一含义。每次更新复核本地链接、数字的集合／单位和Git状态；不因维护本文自动提交、推送、开启实验或安排后台任务。

接手会话先读本文，再读Current_Stage和AGENTS并检查Git；按需要打开实际证据。没有用户／导师新的方向决定前，只支持当前决定所需的材料整理与讨论，不自动创建新候选或运行任务。
