# BT-1本机预检与云端交接

日期：2026-09-12。用户已批准独立Conda、本机小参数跑通后转云端。**本机预检PASS；云端Notebook已准备，两个平台已连接；Kaggle手机验证BLOCKED，尚无云端模型训练。** 不重启已通过的本机步骤，不再次请求相同执行范围的批准。

## 已实际完成

| 项目 | 可复核结果 |
|---|---|
| 独立环境 | `H:/Conda/envs/UAV_BT1`；由`E:/miniconda3`创建；Python3.12.14、torch2.7.1+cu126、torchvision0.22.1+cu126、固定Ultralytics8.4.90；pip check通过。原`PrePaper_Lightweight_Detection`环境未用于本轮 |
| 初始化 | 官方assets/v8.3.0/yolo11n.pt；5,613,764字节；SHA256 `0ebbc80d4a7680d14987a577cd21342b65ecfd94632bd9a8da63ae6417644ee1`；仅COCO初始化，非VisDrone成品权重 |
| 派生输入 | train字典序前4图：299行→263行正标签＋36排除；按既定哈希排序的cal48：3794行→3652＋142。逐行审计保留，无训练区域ignore；未转换全量6471图，也未解码diag500／test-dev |
| 实际运行 | `BT1-SMOKE-20260912-01`，GTX1660SUPER6GiB，640、batch1、FP32、seed0、1轮4batch；验证只用cal48前4图；从COCO权重加载448/499项，十类输出训练完成 |
| 保存与重载 | 保存last、best及末轮清理前原件；明确重新加载last检查，未用best选择候选。末轮SHA256 `27d55ce4d5faf5db112258364e8054101490b0bf484e82172fdc48174549d263` |
| 输出通路 | 重载后1张cal图预测及P3/P4分类分支读取通过；形状分别`[1,10,48,80]`、`[1,10,24,40]`，数值有限；未计算候选区域排序 |
| 资源 | 整个预检记录148.75秒，最大CUDA已分配内存383,404,544字节；是这4张图和此次实现的观测，不是全量batch1显存上界或端到端FPS |

训练1轮后的原生AP和框架速度保留在日志，仅说明监控输出存在，**不能作论文检测结果或创新效果**。`baseline_eligible=false`，没有100轮普通基线，也没有候选有效性证据。

后处理预测沿用了框架默认矩形padding，此次对应384×640输入，而不是固定640×640；故读取到48×80与24×40。这里只验证张量接口，后续候选诊断必须显式固定padding／尺寸映射，不能将本次输出当作其已冻结协议。训练本身为640配置。

## 路径与版本证据

- 原始数据保持在`11_Datasets/raw/VisDrone/`，未移动或改写；初始化在`11_Datasets/raw/Models/Ultralytics/v8.3.0/yolo11n.pt`。
- 本机小样本派生目录：`11_Datasets/processed/VisDrone/BT1/smoke_data_v1/`，含原始旁文件、五列标签、清单、conversion.jsonl及preparation.json。
- 运行目录：`11_Datasets/processed/VisDrone/BT1/BT1-SMOKE-20260912-01/`，含run_status.json、environment.json、resolved_args.json、last_pre_strip.pt及train/weights/last.pt。
- 安装与来源证据：`11_Datasets/processed/VisDrone/BT1/execution_2026-09-12/`中的smoke_01.log、downloads.json、两个pip安装报告、pip_freeze.txt、conda_explicit.txt及executed_source_hashes.json。
- 代码：[批量包装](prepare_bt1_data.py)调用未改动的[原适配器](convert_visdrone_labels.py)；[执行器](run_bt1.py)负责标准训练、失败停止、保存与重载。

框架首次把设置与Arial.ttf字体写到了仓库根目录Ultralytics/，另做了版本更新查询，但没有升级包。已将本轮创建的缓存完整移动到`execution_2026-09-12/incidental_framework_cache/`，保留证据；执行器现先创建专用配置目录，避免回退根目录。只重验配置路径，未重跑模型。实跑源码原件为`run_bt1_executed_smoke.py`，其哈希与实跑记录对应；当前云端版本仅增加目录创建，不能把事后修正冒充原预检使用的字节。

## 云端可直接接续的入口

[BT1_Cloud_Training.ipynb](BT1_Cloud_Training.ipynb)内嵌三份脚本和参数文件及各自SHA，无需上传整个私有仓库。支持Colab／Kaggle的Python3.11–3.12 Linux GPU运行时：创建独立venv，固定torch组合和源码提交，下载并严格校验同一train／val／COCO初始化，派生6471张train和cal48，随后从COCO重新开始普通基线。不会接续本机预检权重，不下载test-dev。

云端默认batch4，可按用户授权在启动前改为1并记录；100轮、seed0、FP32及末轮EMA规则不变。Notebook对安装、资源下载、准备和训练设置超时；运行失败不自动重试、换数据或改参数。源码正常训练路径在Windows本机通过，云端依赖、GPU、完整标签转换和整组训练尚未实测，不能写成云端READY或复现成功。

先登录选定平台，上传此Notebook并选择GPU；Kaggle还需开启Internet。建议保持Notebook私有。先检查结果目录及会话限制，再运行训练格；训练结束后保存生成的证据ZIP。可使用已有持久目录，但Notebook不自动挂载Drive或授予权限，也不购买服务。免费资源／会话时长不保证，参见[Colab官方限制](https://research.google.com/colaboratory/faq.html)；平台中断须保留可取得的产物，未完成100轮不可准入。

## 2026-09-12单平台与断点续训更新

- 当前平台： [Kaggle BT1](https://www.kaggle.com/code/cheerhinyi/bt1-visdrone-yolo11n-baseline/edit)。手机验证未完成，Internet禁用，未执行训练格；不能称为GPU额度耗尽。
- Colab已导入[历史备用Notebook](https://colab.research.google.com/drive/1HxyPC00WgRzixmr_a2GhacGoYoxc1Bac)，首格因Python兼容检查停止，未安装依赖、下载数据或训练；随后切换2026.07时遇会话数量限制。该备份仍为旧版本，切换时须更新，当前不使用Colab。
- 用户决定：只先用Kaggle；额度耗尽后，核验前一训练会话已停止并取回恢复包，再在Colab接续同一100轮进度。训练失败不自动改变batch／数据／模型，也不从头重跑。
- [恢复模块](bt1_checkpoint.py)每轮原子替换latest_recovery.zip，第1轮、每5轮及末轮保留编号副本；包含FP32实时模型、EMA、优化器、调度器、scaler、随机状态、轮次、数据转换哈希及配置。默认60分钟后于完整轮次边界暂停，总目标100轮不变，累计训练墙钟仍限24小时。
- 运行产物在/kaggle/working/bt1_runs；环境和原始下载移至/kaggle/temp，避免把环境及数据包塞进约20GiB的平台输出。首次安装前仍核验50GiB空闲；不满足就停止。
- 每段暂停后先保存Kaggle私有输出版本，并下载及核验恢复ZIP，再启动下一段；仅写工作盘不能保证平台销毁后的保存。当前尚未生成或下载真实云端恢复包。
- 新增[构造测试](test_bt1_checkpoint.py)通过：实时模型与EMA、优化器动量及学习率回读，配置不符、损坏、越界ZIP、已完成100轮输入拒绝。没有YOLO训练，没有重跑本机预检。真实训练恢复仍待首段检查。
- 跨GPU、数据加载器重建和轮内中断可能改变随机次序，不能宣称与不中断训练逐位相同；轮内中断回到上个完整轮次，不虚报未完成进度。只加载本项目可信来源的恢复包。
- 旧执行器和Notebook原件保留于execution_2026-09-12/的before_resume文件，原本机运行证据不变。

**下一项唯一任务：完成Kaggle手机验证后，选择免费GPU和Internet，运行首个基线训练段并封存可恢复产物。** 不重新安装本机环境，不运行学习考核；手机验证须由用户在平台完成。


正式来源独立性仍Unknown，训练ignore偏差仍存在，弱响应候选仍PROPOSED／High风险，国奖适用性待学院与年度；没有解除test-dev、正式方法实验或网络修改的边界。未提交、未推送，旧笔记及保护附件保留。

## 本地初步效果检查（用户最新授权）

2026-09-12用户因暂无合适手机号明确改为本机执行，取代当前Kaggle优先等待。BT1-LOCAL-20260912-01已启动，batch4、640、FP32、seed0；首段约15分钟后轮末暂停，总目标仍100轮。full_data_v2已完成6471张train与cal48转换；full_data_v1在4504图后因尾逗号格式停止并完整保留，转换器v0.2按既有审计规则兼容尾逗号。实际训练源码与参数见BT1-LOCAL-20260912-01-launch；暂未生成完整基线或创新结果。Kaggle远程草稿仍为上一版本，恢复云端时需重新同步本地Notebook。

2026-09-12续训更新：本机第3→4轮核验PASS，02号已暂停在第4轮；下一项使用02号恢复包从第5轮继续，详见[核验报告](BT1_Epoch4_Resume_Verification.md)。前述真实续训待验证状态仅为历史记录；跨平台仍未验证。
