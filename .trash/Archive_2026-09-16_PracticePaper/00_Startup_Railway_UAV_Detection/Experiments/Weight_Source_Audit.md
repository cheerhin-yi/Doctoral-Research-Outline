# 普通YOLO11n权重来源与十类映射核查

日期：2026-09-11。范围：公开元数据、模型卡、发布文件清单和源码静态阅读。**结论：发现一个有实际权重条目的候选，但本批没有权重达到诊断准入；当前权重门仍HOLD。** 未下载、反序列化或执行任何权重，也未访问模型推理服务。

## 1. 检索与处置

本批3条定向检索式：`YOLO11n VisDrone pretrained weights github`、`site:huggingface.co YOLO11n VisDrone`、`site:github.com VisDrone "yolo11n" "best.pt"`。随后只核实两个较直接的YOLO11n项目及官方类别配置；普通YOLOv8、改结构、单类和论文搜索噪声未展开。不是全网穷尽，也不声称公开合格权重不存在。

| 来源 | 已核实内容 | 缺口与处置 |
|---|---|---|
| [dronefreak/visdrone-yolov11n](https://huggingface.co/dronefreak/visdrone-yolov11n/tree/07d71f7c86d999b0b67ba9ab29c97dbffe35b60a) | 有best.pt的LFS元数据，模型卡、args.yaml和作者工具包相互关联 | 有条件候选HOLD：临时dataset.yaml未公开，权重内部names/nc未核实，训练时源码与版本未绑定，选模日志缺失 |
| [bhung-chung/Drone-Object-Detection](https://github.com/bhung-chung/Drone-Object-Detection/tree/8410e07b4f0092c9332a45fdf52f64f640bfdd43) | README与配置说明训练10类、推理只筛人和车；有训练脚本及结果图 | 不能据“人车任务”误判为只训练2类；但已查Git树没有.pt等权重，GitHub Releases为0，README的best.pt仅本地输出路径，当前无法取得可核验发布权重 |
| Ultralytics默认yolo11n.pt | 既有官方文档证据：COCO 80类预训练 | 只能作为后续训练初始化候选，不是VisDrone十类检测基线，不通过改名字解决分类头差异 |

没有按作者报告的AP或排行榜高低选择候选。模型可供下载也不等于本项目可直接使用；本报告HOLD属于权重准入状态，不新增文献Work ID或论文PASS记录。

## 2. 第一候选的证据链

Hugging Face固定revision：`07d71f7c86d999b0b67ba9ab29c97dbffe35b60a`，API记录最后修改2026-07-05。`best.pt`元数据大小5497370字节，LFS声明SHA256：`b1a3a4e85a51eb1e71bcf3a4b8e7f426d8930e1a9df8e7a331492f334e8129b9`。**这是服务端声明值，尚未用下载文件核验。** 不从大小推定内部架构、类别数或安全性。

[固定版本args.yaml](https://huggingface.co/dronefreak/visdrone-yolov11n/raw/07d71f7c86d999b0b67ba9ab29c97dbffe35b60a/args.yaml)列出model=yolo11n.pt、epochs=300、imgsz=640、batch=16、seed=0、pretrained=true、val=true、split=val、patience=100。300是请求训练轮数，不证明实际训练完成300轮；数据路径为未公开的临时`/tmp/visdrone_yolo_swhtb07i/dataset.yaml`。模型卡列出results.csv，但API实际文件清单没有该文件。卡片中的示例repo_id顺序与实际仓库不同，不能直接照抄下载示例。

模型卡声明AGPL-3.0，工具包LICENSE为Apache-2.0，二者适用对象不同；不把工具包许可当权重或数据许可。模型卡的工具包版本引用不等于该checkpoint的完整环境锁定。训练、验证实际文件清单及test接触方式仍Unknown：卡片“test set有GT”说明评价用途，不能据此指控测试训练或证明完全隔离。

### 类别不一致需要怎样理解

模型卡列出10类。关联GitHub工具包在固定提交`bd5972bf9eae853d61f0bab9b09ae84ed2fa0bea`（2026-08-30）的[yolo_trainer.py](https://github.com/dronefreak/VisDrone-dataset-python-toolkit/blob/bd5972bf9eae853d61f0bab9b09ae84ed2fa0bea/visdrone_toolkit/yolo_trainer.py#L33)中，类别列表含第11项others，默认num_classes=11；数据配置按该列表生成。`scripts/train.py`第150–153行亦有11类处理说明。转换器第125–131行过滤score=0和category=0，并保留其他可映射类别；没有证据表明“删除忽略标注”实现了训练时负样本忽略。

这份代码晚于模型卡revision时间，**不能证明已发布best.pt就是11类或使用了这份代码**。它证明当前关联代码不能直接补足该权重的十类身份。即使将来发现是11类，推理时删掉others输出也不等于原生十类训练基线：标签监督与分类头已经不同，需要另行审阅，不能静默替代。

解除该候选HOLD所需的具体证据是：checkpoint的nc/names及架构版本、该次训练dataset.yaml和实际清单、运行版本／选模准则与实际轮数、原始ignore/others处理和val/test接触记录。部分来源信息可由发布者补充；本轮未发送询问信。下载并读取内部元数据也不能补造缺失训练历史。

## 3. 十类目标映射

本项目目标口径与[固定提交的Ultralytics VisDrone配置](https://github.com/ultralytics/ultralytics/blob/07958a70205d1388612bd00f8a2f32cf769d8fed/ultralytics/cfg/datasets/VisDrone.yaml#L18)对齐；原始标注和评价口径沿用A0-05至A0-07证据。

| 原始VisDrone类别ID | YOLO目标索引 | 名称 |
|---:|---:|---|
| 1 | 0 | pedestrian |
| 2 | 1 | people |
| 3 | 2 | bicycle |
| 4 | 3 | car |
| 5 | 4 | van |
| 6 | 5 | truck |
| 7 | 6 | tricycle |
| 8 | 7 | awning-tricycle |
| 9 | 8 | bus |
| 10 | 9 | motor |

仅在names顺序逐项确认后，导出才可用`原始类别ID=YOLO索引+1`；不能对任意权重盲加1。原始category=0为忽略区域，不是pedestrian；原始category=11为others，不增加成当前第11个待检类别。任意类别的score=0须按原始忽略语义保留供评价处理，不能只按类别范围判有效框。原始标注不改写；训练转换如何处理这些区域尚未通过核查。

## 4. 是否需要自己训练基线

现有证据尚不支持“直接采用公开权重并跳过训练”。推荐进入**可追溯普通YOLO11n基线的准备**，以自己登记训练输入、配置、选模和权重校验消除关键身份缺口；这不是新算法或增加第二项研究改动，也不是本轮训练授权。

当前不应仅为缺少results.csv就认定模型无效；实际阻碍是类别／监督口径与该次训练身份无法对应。后续若取得足够发布证据，可以重新审阅这一候选，无须为了自训而自训。现阶段暂停无限扩展权重搜索，不自动切换到其他检测器。

受限训练前仍要解决train副本身份及研究用途、训练用数据和开发／test隔离、标准训练接口对ignore与others的处理、必要本人学习和检测环境。训练配置、轮数、资源上限与checkpoint规则尚未冻结；不能把本轮读到的作者300轮、batch16直接套到本机6GB显卡。

## 5. 下一项唯一任务：标准训练接口与忽略标签处理静态核查

固定一个Ultralytics代码版本，检查原始八字段标注到YOLO标签、训练样本／负样本处理及验证输出之间的关系。尤其回答：score=0、category=0和11分别怎样处理，删除框是否造成负样本监督偏差；是否能在不增加自定义损失或新模块的边界内形成可披露的普通基线。

只读源码与已完成的审计报告，不下载正式数据／权重、不转换全数据、不实例化模型、不安装检测依赖、不训练。交付具体源码定位、可采用的处理规则及明确剩余阻碍；若必须改变研究边界才能处理，则报告冲突并停下。不能再把“权重有无来源”做成下一轮重复审计。

本轮已完成的Octave 24项核验、数据审计与旧笔记均不重启。模型仍BLOCKED，S0-01未通过，A0整体HOLD；学院／国奖年份未提供，投稿认定继续待核验。

## 6. 证据保存

所有只读网页／API／源码快照保存在被忽略的`11_Datasets/processed/VisDrone/Weight_Source_Audit_2026-09-11/`，含固定revision、访问URL及文件SHA。源码只作为文本保存，未执行；未下载模型、图像或视频。GitHub第二候选固定提交`8410e07b4f0092c9332a45fdf52f64f640bfdd43`，已核查README、训练脚本、类别配置、Git树及Releases；不能由当前树无权重推断作者从未发布过任何文件。

未新增论文审计、矩阵PASS或模型Run ID；不提交／推送、不改原学习目录、保护附件、Paper 1主张和七篇路线。

## 7. 交付核对

新增本报告1份，更新当前入口与计划7份；73个本地链接可定位，十类名称／0–9索引与固定官方配置逐项一致。HF文件清单缺results.csv、两个固定revision及第二仓库无Release权重均有只读API证据；未下载权重验证服务端SHA，未断言已发布模型是11类。48份既有审计、代码、文献和跟踪文件保持本轮前校验值。Git差异检查通过，保护范围无新增内容差异，33份跟踪PDF保留，暂存区为空。无评价重跑、训练、推理、提交或推送；核对记录在本轮忽略目录的delivery_verification.json。
