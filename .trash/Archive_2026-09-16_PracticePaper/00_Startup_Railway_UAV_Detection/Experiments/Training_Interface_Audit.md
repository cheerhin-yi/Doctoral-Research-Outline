# 标准YOLO11n训练接口与忽略标签处理静态核查

日期：2026-09-11。**静态核查已完成；可继续无模型的标签接口准备，训练协议未冻结，模型仍BLOCKED、A0整体HOLD。** 本轮只下载并阅读官方源码文本，未导入检测包、实例化模型、转换真实数据或运行评价器。既有数据审计及Octave 24项结果均未重跑。

## 1. 结论与适用范围

普通YOLO11n可以承载VisDrone十类检测，但其标准五列标签与分类损失不传递VisDrone的区域级忽略信息。删除score=0、category=0或11的标签行，只是删除正监督；没有匹配到保留目标的位置仍参与负分类监督。不能把它称为训练时保留了忽略语义，也不能推断忽略区内每一个位置必然是负样本——与有效目标的正匹配仍可能发生。

建议为受限探索准备“标准十类监督、原始标注评价”的普通基线，公开上述偏差，并让同一检测器的全部计算分配对照共享同一权重和训练口径。这是基线限制，不是论文创新，也不能证明偏差对不同选区策略影响相等。真正使忽略区域不参与训练损失，需要另行核验／改变训练数据链和损失掩码；本轮不实施，不增加新损失、遮黑图像、删除整图或补标。

[A0-06第4节](A0-06_Evaluation_Protocol_Draft.md)已规定：“若现有接口做不到，应明确训练协议偏差并统一全部基线，不在本阶段增加新损失解决它。”本报告落实该条，提出可核验的准备口径；没有授权训练或宣布正式来源门通过。若后续坚持训练时严格中性忽略，则该普通接口不满足要求，须返回边界决策，不能悄悄改损失。

## 2. 固定源码与可复核位置

固定官方仓库提交`07958a70205d1388612bd00f8a2f32cf769d8fed`，源码版本字段为`8.4.90`。沿用上轮VisDrone配置的同一提交以避免混读版本；不声称这是最新版本，也未验证其在本机的可安装性／CUDA兼容性。以下结论限定于该提交的普通detect路径。

| 环节 | 原文定位 | 核查结果 |
|---|---|---|
| 版本 | [__init__.py 第3行](https://github.com/ultralytics/ultralytics/blob/07958a70205d1388612bd00f8a2f32cf769d8fed/ultralytics/__init__.py#L3) | 静态版本8.4.90，未安装 |
| 模型 | [yolo11.yaml](https://github.com/ultralytics/ultralytics/blob/07958a70205d1388612bd00f8a2f32cf769d8fed/ultralytics/cfg/models/11/yolo11.yaml)、[Detect 第89–142行](https://github.com/ultralytics/ultralytics/blob/07958a70205d1388612bd00f8a2f32cf769d8fed/ultralytics/nn/modules/head.py#L89-L142) | n尺度、P3–P5普通Detect，无end2end配置；不是LSM-Head |
| 十类实例化 | [train.py 第139–202行](https://github.com/ultralytics/ultralytics/blob/07958a70205d1388612bd00f8a2f32cf769d8fed/ultralytics/models/yolo/detect/train.py#L139-L202) | 从数据配置传nc并附names；只改名字不能得到已训练十类权重 |
| 损失选择 | [tasks.py 第594–596行](https://github.com/ultralytics/ultralytics/blob/07958a70205d1388612bd00f8a2f32cf769d8fed/ultralytics/nn/tasks.py#L594-L596) | 普通DetectionModel进入v8DetectionLoss，类名含v8不代表只适用YOLOv8 |
| 官方转换 | [VisDrone.yaml 第18–87行](https://github.com/ultralytics/ultralytics/blob/07958a70205d1388612bd00f8a2f32cf769d8fed/ultralytics/cfg/datasets/VisDrone.yaml#L18-L87) | 仅以文本score不等于0保留行；category减1；输出五列，未传ignore |
| 标签读取 | [utils.py 第244–309行](https://github.com/ultralytics/ultralytics/blob/07958a70205d1388612bd00f8a2f32cf769d8fed/ultralytics/data/utils.py#L244-L309)、[dataset.py 第93–200行](https://github.com/ultralytics/ultralytics/blob/07958a70205d1388612bd00f8a2f32cf769d8fed/ultralytics/data/dataset.py#L93-L200) | 检查五列、坐标范围及类别；异常可排除整张image/label；缺失与空标签都可表示无正目标 |
| 批次格式 | [augment.py 第2260–2359行](https://github.com/ultralytics/ultralytics/blob/07958a70205d1388612bd00f8a2f32cf769d8fed/ultralytics/data/augment.py#L2260-L2359) | 普通框路径生成cls、bboxes和batch_idx；分割mask不是VisDrone忽略区接口 |
| 目标分配与损失 | [tal.py 第248–288行](https://github.com/ultralytics/ultralytics/blob/07958a70205d1388612bd00f8a2f32cf769d8fed/ultralytics/utils/tal.py#L248-L288)、[loss.py 第336–455行](https://github.com/ultralytics/ultralytics/blob/07958a70205d1388612bd00f8a2f32cf769d8fed/ultralytics/utils/loss.py#L336-L455) | 非前景target_scores置0；分类BCE对位置及类别求和，未乘区域忽略掩码；可选类别权重也不是区域掩码 |
| 原生验证与导出 | [val.py 第129–219行](https://github.com/ultralytics/ultralytics/blob/07958a70205d1388612bd00f8a2f32cf769d8fed/ultralytics/models/yolo/detect/val.py#L129-L219)、[第395–459行](https://github.com/ultralytics/ultralytics/blob/07958a70205d1388612bd00f8a2f32cf769d8fed/ultralytics/models/yolo/detect/val.py#L395-L459) | 原生指标来自转换后cls/bboxes；TXT委托Results、JSON按COCO形式导出，不能直接冒充作者八字段结果 |

`mask_gt`是填充后的有效GT掩码，`fg_mask`是正匹配掩码；两者均未接收原始忽略区域。框回归只作用于正匹配，不会抵消未匹配位置的分类负监督。以上为沿数据流的静态推导，未通过张量／梯度运行测试，不推断偏差大小或实际精度。

官方转换还存在两个具体注意点：

- 第53行移动原图，第87行清理源目录，因此不直接执行其download块；后续适配器必须另存派生标签并保护原始图像／标签。
- 对score非0的category=11，减1会得到超出十类范围的10；category=0则得到-1。这是条件性代码后果，不是声称本地数据存在这些组合。转换代码也没有正宽高检查；读取器的范围断言不能替代几何有效性检查。不能依赖其自动排除整图来处理A0-05已发现的三条零高标注。

## 3. 下一步适配器采用的明确规则

本表用于下一项构造样例核验；不是已经生成的全量训练标签或已冻结的训练协议。原始八字段与图像保持原样，转换逐行保留来源、原行号和排除原因。

| 原始记录 | 派生训练标签规则 | 必须保留的信息／解释 |
|---|---|---|
| 有效类别1–10，GT score=1，几何有效 | 输出类别减1及归一化中心xywh五列 | 十类顺序沿用[权重审查](Weight_Source_Audit.md)；不按遮挡／截断删目标 |
| 任意类别score=0 | 不输出正标签 | 原值及位置保留在审计旁文件；**没有训练区域中性屏蔽** |
| category=0，含非零score的条件情形 | 不输出任务类，记录类别和score组合 | 不映射成pedestrian；评价继续读取原始忽略区域 |
| category=11，含非零score的条件情形 | 不输出第11类，记录others | 非任务类；评价时也不能自动把其周围全部预测忽略 |
| 宽或高≤0 | 排除该行并记录原因，不删除整图、不补高 | 适用于A0-05已定位三行；类别／score原因同时记录，避免丢失异常 |
| 字段数错、非有限值、非整数类别／标志、score非0/1、类别超出0–11、越界几何 | 报明确错误并停止该次生成，不静默修复 | 不是已发现新异常；为构造样例定义防误处理规则 |
| 原始标签文件存在但为空，或所有行被有记录地排除 | 可输出明确的空标签文件，并记录两种不同来源 | 标准训练仍有负分类监督；不把“无有效正标签”证明为无人／无目标场景 |
| 标签文件缺失 | 阻止生成，不能伪装为空图 | 比框架默认缺失即空更严格，防止漏文件悄悄改变监督 |

归一化规则：`xc=(x+w/2)/W`、`yc=(y+h/2)/H`、`wn=w/W`、`hn=h/H`；保持已有坐标基准，不额外加减1。下一任务用人工框验证非方图、边界与往返换算容差；不套用评价器内部的`max(1,...)`去修复训练原标注。完整有效范围与输出小数精度在适配器中显式检查，避免极小框被舍入成零宽高。

不把类别0区域覆盖的其他有效正框自动删去；作者评价的区域并集过滤属于评价口径，不能未经说明变成新的训练清洗策略。不增加类别权重、增强或新损失作为解决方案；标准实现已有模块保持原样，训练初始化、默认增强和checkpoint选择需在实际训练准入前另行固定。

## 4. 训练与评价两条数据链

训练准备：原始训练标注 → 有审计记录的十类派生标签 → 标准YOLO监督。派生旁文件保存忽略信息用于追溯，**普通损失不会因此自动读取它**。本轮未读取真实标签作新增统计，不知道各类排除数量及其对训练的影响。

评价准备：预测回到原图坐标 → 统一合并和排序 → 导出类别1–10及原图左上角xywh、预测置信度等作者所需字段 → 保留原始GT，由[已核验的作者代码兼容运行时](Official_Runtime_Crosscheck.md)处理。原生YOLO验证只可明确标为内部监控，不能替代论文协议指标；未来用其选择checkpoint也必须披露。真实预测导出、排序、截断及数值容差尚未实测，不将本次静态审查称为接口运行PASS。

模型推理与区域选择不读取GT。测试GT只进入离线评价，不把忽略区当作可部署区域输入。train/val共享来源、train/test-dev副本身份与独立来源组Unknown继续保留；一致监督只控制对照中的一个变量，不能消除来源泄漏或保证方法新颖性。

## 5. 证据存放与下一项唯一任务

本轮11份源码快照、访问URL、字节数和SHA256位于被Git忽略的`11_Datasets/processed/VisDrone/Training_Interface_Audit_2026-09-11/`，清单为`source_access.json`及`additional_source_access.json`。另复用上轮同提交的`Weight_Source_Audit_2026-09-11/official_visdrone_pinned.yaml`，SHA256为`627f60f7602db38b6a462301ced87ad24bcdee2a692eaa9d4e02448492bb29fe`。源码仅作本地静态审计快照，不是安装环境；稳定正文链接见第2节。

下一项唯一任务：**最小标签转换器与构造样例核验**。只在新项目Experiments内实现不依赖检测框架的适配器，使用人工八字段标签和人工图像尺寸，检查十类映射、score／category组合、空与缺失、无效几何、往返坐标、逐行追溯、原件不变和重复执行保护；明确异常是否导致停止。输出必须限于独立派生目录且不覆盖既有结果。

成功标准：适配器、构造样例与实际通过／失败记录可复核，明确它只删除正标签、不实现训练ignore。**不转换全量VisDrone、不安装检测依赖、不下载权重、不创建模型Run ID、不运行模型或重跑旧24项评价样例。** 通过后再落实必要学习、训练范围与独立环境等剩余准入，不能从转换器通过直接跳到训练。

## 6. 本轮交付核对

新增本报告，更新7份当前入口／计划；80个本地链接可定位，12份固定源码／配置校验值一致，Git差异检查通过。对照本轮开始校验值，141份既有文档／脚本未变，未缺失文件；33份Git跟踪PDF保留，保护目录及七篇路线／Paper 1研究计划相对HEAD无内容差异，暂存区为空。具体变更、链接与保护核验记录保存在同目录`delivery_verification.json`。

原学习初稿、数据／文献历史报告、已有评价脚本与输出、实验跟踪表均保留；无新增论文、模型训练或推理记录，不提交、不推送。12份源码校验通过仅证明保存的文本与下载清单一致，不代表运行兼容性通过。
