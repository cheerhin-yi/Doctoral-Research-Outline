---
AIGC:
  ContentProducer: '001191110102MAD55U9H0F10002'
  ContentPropagator: '001191110102MAD55U9H0F10002'
  Label: '1'
  ProduceID: '72a9728a-f567-496d-96f8-32a6a73db005'
  PropagateID: '72a9728a-f567-496d-96f8-32a6a73db005'
  ReservedCode1: '9e1ced78-ef5f-4676-a17a-43896ba4279d'
  ReservedCode2: '9e1ced78-ef5f-4676-a17a-43896ba4279d'
---

# 目标检测名词与缩写字典（OD Glossary）

更新日期：2026-09-23（初版，覆盖已读仓库文档中出现的术语，并扩充后续论文会用到的词汇）。

**分工说明**：本文件聚焦**目标检测领域**的名词与缩写（含英文全称、中文含义、在本仓库中的用法），与 [`Abbreviation_Glossary.md`](Abbreviation_Glossary.md)（项目内部代号：BT／BTD／A0／W-xxxx／P0-EI 等）互补。项目内部代号速查见本文件 **§12**；实验运行细节以 [`Experiment_Tracker.md`](../00_Practice_UAV_Aerial_Detection/Experiments/Experiment_Tracker.md) 为准。

**阅读约定**：`[项目内]` 标记表示该词已在仓库文件（PROJECT_CONTEXT／Current_Stage／实验报告等）中出现并对应具体用法；`[扩展]` 表示尚未出现、为后续论文（RailUAV-SOD 基准、开放词汇标注管线、Paper 1 开放世界风险感知）预留的词汇。

---

## 1. 检测任务与范式

| 缩写／词 | 英文全称 | 中文含义 | 说明／项目内对应 |
|---|---|---|---|
| OD | Object Detection | 目标检测 | 本项目核心任务（航拍小目标检测） |
| SOTA | State-of-the-Art | 当前最优水平 | 对比基线用语，[项目内] 明确禁止把 P0 说成 SOTA |
| One-stage | One-stage detector | 单阶段检测器 | 直接回归类别+框，如 YOLO、FCOS |
| Two-stage | Two-stage detector | 两阶段检测器 | 先提候选再分类回归，如 Faster R-CNN |
| Anchor | Anchor box | 锚框（先验框） | 早期 YOLO 使用；YOLO11 已 anchor-free |
| Anchor-free | Anchor-free detector | 无锚框检测器 | 基于中心点/角点直接预测 |
| Small object | Small object detection | 小目标检测 | [项目] 本项目定义：原图面积 `0 < w×h < 1024`（即边长 < 32px 量级），见 §5 |
| Tiny object | Tiny object detection | 微小目标检测 | [扩展] 常指 <16px 或面积 <256px 的目标；NWD 等指标关注 |
| Dense / Crowded | Dense object detection | 密集/拥挤目标检测 | [扩展] 对应 Adaptive NMS（W-0012）场景 |
| One-stage / two-stage | — | 单/两阶段 | 同上 |
| RPN | Region Proposal Network | 区域提议网络 | Faster R-CNN 的候选框生成器 |
| RoI / RoIAlign | Region of Interest / Region of Interest Align | 兴趣区域 / 兴趣区域对齐 | 两阶段器的池化操作 |
| Backbone | Backbone network | 主干网络 | 提取特征，如 YOLO11 的 CSP 系 |
| Neck | Neck network | 颈部网络（特征融合） | 如 FPN、PANet |
| Head | Detection head | 检测头（输出层） | 分类头+回归头 |
| FPN | Feature Pyramid Network | 特征金字塔网络 | 多尺度特征融合 |
| PANet | Path Aggregation Network | 路径聚合网络 | 自底向上增强位置信息 |
| BiFPN | Bidirectional FPN | 双向加权特征金字塔 | EfficientDet 提出 |
| SPP / SPPF | Spatial Pyramid Pooling (Fast) | 空间金字塔池化 | YOLO 系 Neck 常用 |
| C2f / CSP | Cross Stage Partial / C2f module | 跨阶段局部连接模块 | YOLOv8+ 的 Basic Block |
| P3 / P4 / P5 | Pyramid feature levels | 金字塔特征层级 | [项目] 小目标主要在 P3 高分辨率层；见 BTD1 "P3-only" |
| Stride | Downsampling stride | 下采样步长 | 特征图相对原图的缩小倍数 |
| Receptive field | Receptive field | 感受野 | 特征点对应原图范围，小目标依赖浅层 |
| Feature map | Feature map | 特征图 | 卷积输出 |
| Heatmap | Heatmap | 热力图 | 中心点/密度表示 |
| Embedding | Feature embedding | 特征嵌入向量 | [扩展] 开放词汇比对基础 |

### §1 术语详解

- **OD（目标检测）**：同时完成“在哪（定位，输出矩形框坐标）”与“是什么（分类）”的图像任务。输出一般为一个框列表：`(类别, 置信度, x, y, w, h)`。小目标检测是其难点子任务。
- **One-stage / Two-stage（单阶段/两阶段）**：两阶段先由 RPN 生成候选框，再对候选框细分类+回归（精度高、速度慢，如 Faster R-CNN）；单阶段直接在整图上密集预测（速度快，如 YOLO/FCOS）。本项目固定 YOLO11n（单阶段）。
- **Anchor（锚框）**：预置的一组先验框（多种尺度×多种长宽比），模型学习“相对锚框的偏移”。YOLOv5 及更早版本依赖它；YOLOv8/11 已改为 anchor-free。
- **Anchor-free（无锚框）**：不预设框，直接在特征图每个位置预测中心点/角点及到边框的距离。设计更简单、边界样本更均衡。
- **RPN**：Faster R-CNN 里的一个小网络，负责输出“可能含目标”的候选框（含是否含目标的分数与粗框）。
- **RoI / RoIAlign**：从特征图上截取候选框对应的特征区域再送入分类头。RoIAlign 用双线性插值消除量化误差（替代旧 RoIPooling 取整）。
- **Backbone / Neck / Head**：主干网负责提取特征；Neck 负责多尺度特征融合（如 FPN）；Head 输出最终类别与坐标。
- **FPN**：自顶向下把高层语义特征逐层与浅层特征拼接，使低分辨率层也能利用高分辨率层的细节，同时改善小目标与多尺度问题。
- **PANet**：在 FPN“自顶向下”基础上加“自底向上”路径，让小目标（浅层）拿到更深层的语义信息，位置信息更强。
- **BiFPN**：对 FPN 各层特征做“可学习权重加权融合”，EfficientDet 使用。
- **SPP / SPPF**：用多个不同大小的池化核并行池化再拼接，扩大感受野并聚合多尺度；SPPF 是 SPP 的快速近似（串行 3 个 5×5 等价于单次 13×13）。
- **C2f / CSP**：CSP 思想是把通道分成主路与旁路，分支梯度交叉再融合，减少冗余计算并保持梯度丰富。C2f 是 YOLOv8/11 的具体实现模块（含残差分支）。
- **P3 / P4 / P5**：FPN 输出的三个特征层，对应 stride 8/16/32（特征图 1px ≈ 原图 8/16/32px）。P3 分辨率最高、最适合小目标。[项目] BTD1“P3-only”即只用 P3 层做弱响应恢复。
- **Stride（步长）**：特征图相对原图的缩小倍数；也指卷积滑动步长。
- **感受野**：单个特征点能“看到”的原图区域大小。浅层感受野小，小目标细节在浅层更清晰，所以小目标检测常用高分辨率输入 + 浅层特征。
- **Feature map**：卷积网络中间层输出的三维张量（通道×高×宽），承载视觉特征。
- **Heatmap**：二维得分图，每个位置一个值（如中心点得分、密度计数），常用于 anchor-free 和密度分析。[项目] 密度单片 DensK1 即基于粗略预测的密度热图选窗。
- **Embedding**：把语义信息编码成固定维向量（如 512/1024 维），文本与图像嵌入可通过相似度对齐——开放词汇检测的核心机制。
- **Small / Tiny object**：小目标在 COCO 定义为面积 <32×32=1024px²；Tiny（微小）常指 <16×16=256px²。本项目小目标定义与 COCO small 同口径（`0<w×h<1024`），但未按 COCO 的绝对像素解释。[扩展]

---

## 2. 模型家族与版本

| 缩写／词 | 英文全称 | 中文含义 | 项目内对应 |
|---|---|---|---|
| YOLO | You Only Look Once | 只看一次（端到端检测系列） | [项目] 家族基准 |
| YOLO11n | Ultralytics YOLO11 nano | YOLO11 nano 版本 | [项目] BT1 固定检测器（P3–P5） |
| YOLOv5/8 | Ultralytics YOLO 系列 | 常用工程版本 | [扩展] 近邻对照常用 |
| Faster R-CNN | Faster R-CNN | 两阶段代表 | [扩展] 对照/学术引用 |
| FCOS | Fully Convolutional One-Stage Object Detection | 全卷积单阶段 | [扩展] anchor-free 代表 |
| DETR | Detection Transformer | Transformer 检测 | [扩展] 端到端，去 NMS |
| RT-DETR | Real-Time DETR | 实时 DETR 变体 | [扩展] 实时场景对照 |
| SSD | Single Shot MultiBox Detector | 多框单阶段 | [扩展] 历史基线 |
| GFLV2 | Generalized Focal Loss V2 | 广义焦点损失 V2 | [项目] W-0013 近邻审计 |
| Grounding DINO | Grounding DINO | 开放词汇检测器 | [扩展] 开放词汇标注管线主引擎（RailUAV-SOD） |
| DINO-X | DINO-X | 开放词汇基础模型 | [扩展] 预实验 M2 上限参照 |
| T-Rex2 | T-Rex2 | 视觉提示开放集检测器 | [扩展] 预实验 M3 视觉提示兜底 |
| SAM / SAM2 | Segment Anything Model (v2) | 分割一切模型 | [扩展] Grounded-SAM 2 标注管线 |
| Grounded SAM | Grounded SAM | 定位+分割组合 | [扩展] 开放词汇标注管线 |

---

## 3. 训练与优化

| 缩写／词 | 英文全称 | 中文含义 | 项目内用法 |
|---|---|---|---|
| Epoch | Epoch | 一轮全量训练 | [项目] BT1 跑满 100 轮 |
| Batch / batch size | Batch size | 批大小 | [项目] BT1 训练 batch=4；诊断 batch=1 |
| lr / LR | Learning rate | 学习率 | [项目] 训练超参，日志可见 |
| Warmup | Learning rate warmup | 学习率预热 | 训练前段小步长 |
| Scheduler | LR scheduler | 学习率调度 | 按轮下降 |
| SGD | Stochastic Gradient Descent | 随机梯度下降 | [项目] BT1 优化器 |
| Adam / AdamW | Adaptive Moment Estimation (+ Weight Decay) | 自适应优化器 | [扩展] |
| EMA | Exponential Moving Average | 指数滑动平均 | [项目] 固定取末轮 EMA `last.pt` 为正式权重 |
| last.pt / best.pt | Ultralytics 权重文件 | 末轮/最优轮权重 | [项目] 用 last.pt，不按 cal48 最佳选模 |
| Checkpoint | Checkpoint | 训练断点包 | [项目] 分段训练恢复用 |
| Resume | Resume training | 续训 | [项目] BT1 三段接续 1–3／4／5–100 |
| Seed | Random seed | 随机种子 | [项目] seed0 固定 |
| Freeze | Freeze weights | 冻结权重 | [项目] 五方法对比用冻结 `last.pt`，不训练 |
| Fine-tune | Fine-tuning | 微调 | [项目] 门禁：禁止（除非书面授权） |
| Pretrain | Pre-trained weights | 预训练初始化 | [项目] COCO 预训练 → VisDrone 适配 |
| FP32 / FP16 / BF16 | Floating Point 32/16 / Brain FP16 | 浮点精度 | [项目] BT1 FP32、amp=false |
| AMP | Automatic Mixed Precision | 混合精度 | [扩展] |
| BN | Batch Normalization | 批归一化 | 训练技巧 |
| Aug | Data Augmentation | 数据增强 | [扩展] Mosaic、Mixup 等 |
| Mosaic | Mosaic augmentation | 拼图增强 | YOLO 系训练增强 |
| Normalization | Input normalization | 输入归一化 | 推理前预处理 |
| 类别映射 | Class mapping | 类别对应 | [项目] VisDrone 十类映射，FROZEN_PRE_RESULTS |

---

## 4. 损失函数

| 缩写／词 | 英文全称 | 中文含义 | 说明 |
|---|---|---|---|
| Loss | Loss function | 损失函数 | 训练优化目标 |
| Cls loss | Classification loss | 分类损失 | BCE 或 CE |
| Reg loss | Regression loss | 回归损失 | 框坐标 |
| Objectness | Objectness loss | 目标性损失 | 是否有目标 |
| BCE | Binary Cross Entropy | 二元交叉熵 | 分类损失基础 |
| CE | Cross Entropy | 交叉熵 | 多分类 |
| Focal Loss | Focal Loss | 焦点损失 | 缓解难易样本不平衡 |
| DFL | Distribution Focal Loss | 分布焦点损失 | [项目] BTD12 审查对象 |
| QFL | Quality Focal Loss | 质量焦点损失 | GFL 系列 |
| GFL | Generalized Focal Loss | 广义焦点损失 | GFLV2 基础 |
| GIoU / DIoU / CIoU / SIoU | 广义/距离/完全/旋转 IoU 损失 | IoU 损失变体 | 回归质量 |
| NWD | Normalized Wasserstein Distance | 归一化沃瑟斯坦距离 | [项目] W-0011：小目标匹配/回归度量 |

---

## 5. 评估与指标

| 缩写／词               | 英文全称                                       | 中文含义          | 项目内用法                              |
| ------------------ | ------------------------------------------ | ------------- | ---------------------------------- |
| GT                 | Ground Truth                               | 真值标注          | 评估参照                               |
| TP                 | True Positive                              | 真阳性           | 正确检出的框                             |
| FP                 | False Positive                             | 假阳性           | 误检                                 |
| FN                 | False Negative                             | 假阴性           | 漏检                                 |
| TN                 | True Negative                              | 真阴性           | 背景判断正确                             |
| Precision          | Precision                                  | 精确率           | TP/(TP+FP)                         |
| Recall             | Recall                                     | 召回率           | TP/(TP+FN)                         |
| F1                 | F1 score                                   | 调和平均          | 2PR/(P+R)                          |
| AP                 | Average Precision                          | 平均精度          | 单类 PR 曲线下面积                        |
| mAP                | mean AP                                    | 各类 AP 平均      | [项目] 原生 Ultralytics mAP ≠ 官方兼容 AP  |
| mAP50              | mAP @ IoU=0.5                              | 匹配阈 0.5 的 mAP | [项目] BT1 cal48 mAP50=.34101        |
| mAP50-95           | mAP IoU 0.5:0.95                           | 多阈值平均         | [项目] 0.18591（cal48）                |
| AP_s / AP_m / AP_l | AP by size                                 | 分尺度 AP        | COCO 指标族                           |
| AR                 | Average Recall                             | 平均召回          | 最大检测数下召回                           |
| IoU                | Intersection over Union                    | 交并比           | 匹配/后处理阈值                           |
| conf / score       | Confidence / score                         | 置信度/分数        | [项目] conf=.25 固定                   |
| maxDets            | Maximum detections                         | 每图最大输出框       | [项目] 500 框截断                       |
| 匹配                 | Matching / assignment                      | 框匹配           | [项目] IoU=.5 贪心匹配                   |
| Ignore             | Ignore region                              | 忽略区           | [项目] 官方 ignore；训练删除正标签 ≠ 正确 ignore |
| small_recall       | Small-target recall                        | 小目标召回         | [项目] P0 主指标，见 Stage D/E            |
| 超时率                | Budget exceed rate                         | 超时率           | [项目] 超过参考时限的帧比例                    |
| p95                | 95th percentile                            | 95 分位耗时       | [项目] 报告时序分布                        |
| mean_ms            | Mean milliseconds                          | 平均耗时(毫秒/帧)    | [项目] 1660/4090 分列                  |
| GT oracle          | Oracle                                     | 真值上界          | [项目] 仅离线界定空间，不算可部署                 |
| TIDE               | TIDE: A General Toolbox for Error Analysis | 错误分析工具箱       | [项目] W-0010 审计                     |
| 错误分解               | Error structure / decomposition            | 错误结构分解        | [项目] BTD11：Cls/Loc/Both、分数/定位/类别   |

---

## 6. 推理、切片与后处理

| 缩写／词 | 英文全称 | 中文含义 | 项目内用法 |
|---|---|---|---|
| NMS | Non-Maximum Suppression | 非极大值抑制 | [项目] 公共 NMS IoU=.5（BTD5/6） |
| Soft-NMS | Soft-NMS | 软化 NMS | [扩展] |
| Adaptive NMS | Adaptive NMS | 自适应 NMS | [项目] W-0012 审计（行人密集） |
| conf threshold | Confidence threshold | 置信阈值 | [项目] .25 / .10 低分对照 |
| max500 | Max detections per image | 500 框上限 | [项目] 与官方 maxDets 一致 |
| Slicing / Tiling | Slicing / tiling inference | 切片推理 | 整图切小块分别推理 |
| Tile size / Overlap | Tile size / overlap | 切片尺寸/重叠率 | SAHI 参数（640/0.25 等） |
| SAHI | Slicing Aided Hyper Inference | 切片增强超推理 | [项目] 五协议之一 `SAHI640` |
| DensK1 | Density-based top-1 crop | 密度单片 | [项目] 密度启发式选 1 个局部窗 |
| UnifAll | Uniform slicing all tiles | 均匀切片 | [项目] 五协议之一 |
| F640 / F1280 | Full image 640 / 1280 | 整图输入 | [项目] F1280 是强简单基线 |
| 预算 | Time budget | 整帧时间预算 | [项目] 40ms 为相对参考，非硬期限 |
| pipeline | Inference pipeline | 推理管线 | 图像→预测→坐标还原→NMS→匹配 |
| FPS | Frames per second | 每秒帧数 | 时延反指标 |
| Cache | Cached prediction | 缓存预测 | 缓存分析 ≠ 推理测速 |

---

## 7. 开放词汇 / 大模型（[扩展]，面向 RailUAV-SOD 与 Paper 1）

| 缩写／词 | 英文全称 | 中文含义 | 说明 |
|---|---|---|---|
| OVD | Open-Vocabulary Detection | 开放词汇检测 | 任意文本可检 |
| OSR | Open-Set Recognition | 开放集识别 | 拒绝未知类 |
| Zero-shot | Zero-shot | 零样本 | 无训练直接用 |
| Few-shot | Few-shot | 少样本 | 少量样例 |
| Prompt | Prompt / text prompt | 提示词 | 术语工程（C1 裸术语/C3 描述性提示） |
| Visual prompt | Visual prompt | 视觉提示 | 点击/框提示（T-Rex2） |
| Grounding | Grounding | 文本-视觉对齐 | 定位到框 |
| CLIP | Contrastive Language-Image Pretraining | 图文对比预训练 | 对齐基础模型 |
| VLM | Vision-Language Model | 视觉语言模型 | 多模态 |
| LMM | Large Multimodal Model | 多模态大模型 | 组合感知 |
| LLM | Large Language Model | 大语言模型 | 术语工程/解析 |
| 术语表 | Prompt/term engineering | 术语工程 | [项目] 五元组共享资产 |
| Known / Unknown | Known / unknown classes | 已知/未知类别 | Paper 1 协议 |
| M1 / M2 / M3 | 分层模型 | 本地小模型 / API 上限 / 视觉提示救援 | 预实验模型分层 |

---

## 8. 数据集与数据

| 缩写／词 | 英文全称 | 中文含义 | 项目内用法 |
|---|---|---|---|
| VisDrone | VisDrone2019-DET | 无人机视角检测基准 | [项目] 主数据集（6471/548/1610+） |
| UAVDT | UAV Detection and Tracking | 无人机检测跟踪基准 | [项目] Stage E 外部迁移（40735 帧） |
| UAV-RSOD | UAV Railway-small dataset | 无人机铁路小目标 | [项目] 历史候选（HOLD） |
| COCO | Common Objects in Context | 通用检测基准 | [项目] 预训练来源；AP 定义 |
| 小目标定义 | 0 < w×h < 1024 | 面积定义 | 与 COCO small 定义不同 |
| YOLO 标注 | YOLO txt 标注 | cx cy w h 归一化 | 标注格式 |
| COCO JSON | COCO annotation JSON | COCO 标注格式 | 转换目标 |
| 8字段标注 | VisDrone 8 字段 | VisDrone 标签 | 原八字段 |
| 类别映射 | Class mapping | 类别 | [项目] 冻结映射 |
| Split | Train/val/test split | 划分 | train/val/test-dev |
| cal48 | Calibration 48 | 校准集 48 张 | 开发集（反复用于开发诊断） |
| diag500 | Diagnosis 500 | 诊断集 500 | 开发证据 |
| test-dev | Test-dev set | 官方测试集 | 一次性评估（Stage D） |
| Test-challenge | 挑战赛测试 | 无本公开标注 | 不评估 |
| 去重 | Deduplication | 重复剔除 | BTD 对照 |

---

## 9. 硬件与工程环境

| 缩写／词 | 英文全称 | 中文含义 | 项目内用法 |
|---|---|---|---|
| GPU | Graphics Processing Unit | 图形处理器 | 训练/推理 |
| GTX 1660 SUPER | NVIDIA 显卡 | 本机 GPU | [项目] 6GiB，多数 BTD 测速环境 |
| RTX 4090 | NVIDIA 显卡 | 服务器 GPU | [项目] 双 4090 可用；正式时序表必须与 1660 分列 |
| VRAM | Video RAM | 显存 | [项目] 6GiB 限制：只能跑小模型 |
| CUDA | Compute Unified Device Architecture | NVIDIA 并行计算平台 | [项目] torch2.7.1+cu126 |
| cuDNN | CUDA Deep NN Library | 深度网络加速库 | 依赖项 |
| torch | PyTorch | 深度学习框架 | [项目] 版本见环境冻结报告 |
| torchvision | torchvision | 视觉工具箱 | [项目] 0.22.1 |
| ultralytics | Ultralytics YOLO 库 | YOLO 工具链 | [项目] 8.4.90 |
| ONNX | Open Neural Network Exchange | 模型交换格式 | 部署转换 |
| TensorRT | TensorRT | 推理加速 | 部署优化 |
| Conda | Conda 环境 | 虚拟环境 | [项目] `H:/Conda/envs/UAV_BT1` |
| RSS / GiB | Resident Set Size / Gibibyte | 常驻内存/二进制吉字节 | 资源守卫口径 |
| NumPy | NumPy | 数值计算库 | 缓存分析 |
| SHA256 | Secure Hash Algorithm 256 | 哈希校验 | 权重/数据指纹（bc42d54e...） |
| JSON | JavaScript Object Notation | 数据格式 | 配置/摘要 |
| CSV | Comma-Separated Values | 逗号分隔值 | 逐图指标表 |
| CRC | Cyclic Redundancy Check | 循环冗余校验 | 数据完整性 |
| Run ID | Run Identifier | 运行编号 | 先登记再跑 |

---

## 10. 论文发表与学术会议

| 缩写／词 | 英文全称 | 中文含义 | 说明 |
|---|---|---|---|
| EI | Engineering Index（Compendex） | 工程索引 | 会议检索标志（IEEE/Springer 出版常见） |
| Scopus | Scopus | 摘要引文库 | 会议检索之一 |
| ISTP | Index to Scientific & Technical Proceedings | 科技会议录索引 | PRCV 等 LNCS 会议收录 |
| SCI | Science Citation Index | 科学引文索引 | 期刊 |
| JCR | Journal Citation Reports | 期刊引证报告 | Q1–Q4 分区 |
| 中科院分区 | CAS 分区 | 国内常用分区 | 1–4 区 |
| CCF | China Computer Federation | 中国计算机学会 | 推荐目录 A/B/C |
| CCF-A/B/C | CCF 推荐会议等级 | 会议分级 | 毕业/评奖参考 |
| CVPR | IEEE/CVF Conf. on CVPR | 计算机视觉顶会 | A 类，25% 录用率 |
| ICCV | International Conference on Computer Vision | 视觉顶会 | A 类 |
| ECCV | European Conference on Computer Vision | 欧洲视觉顶会 | A 类 |
| NeurIPS / ICLR / AAAI | 机器学习顶会 | AI 顶会 | A 类（备选去向） |
| ICIP | IEEE Int. Conf. on Image Processing | 图像处理会议 | **CCF-C**，约 45% 录用率，IEEE 出版（EI 检索） |
| ICPR | Int. Conf. on Pattern Recognition | 模式识别会议 | CCF-C，两年一届 |
| PRCV | 中国模式识别与计算机视觉大会 | 国内视觉会议 | **CCF-C**，Springer LNCS（EI+ISTP 检索） |
| WACV | IEEE/CVF Winter Conf. on Applications of CV | 应用视觉会议 | CCF-C（2027 届已截稿） |
| BMVC | British Machine Vision Conference | 英国机器视觉会议 | CCF-C，方法导向 |
| ACCV | Asian Conf. on Computer Vision | 亚洲视觉会议 | CCF-C，两年一届 |
| ICASSP | IEEE Int. Conf. on Acoustics, Speech and SP | 信号处理旗舰会议 | CCF-B |
| ICME | IEEE Int. Conf. on Multimedia and Expo | 多媒体会议 | CCF-B |
| LNCS | Lecture Notes in Computer Science | Springer 丛书 | PRCV 论文集 |
| IEEE Xplore | IEEE 数字图书馆 | 出版平台 | ICIP 等收录 |
| Springer | Springer 出版社 | 出版社 | PRCV 等 |
| CFP | Call for Papers | 征稿通知 | 会议信息源 |
| Camera-ready | 终稿 | 终稿提交 | 录用后 |
| Double-blind | 双盲评审 | 审稿制度 | 投稿时匿名 |
| Workshop | 卫星研讨会 | 会议附件 | 一般不计入 CCF 认定 |
| 录用率 | Acceptance rate | 录用率 | 评估会议难度 |
| 水会 | 低质量会议 | 提示警惕 | EI 会议选择需核实往届检索记录 |

---

## 11. 统计与实验方法

| 缩写／词 | 英文全称 | 中文含义 | 项目内用法 |
|---|---|---|---|
| Wilcoxon | Wilcoxon signed-rank test | 配对符号秩检验 | Stage F 图像级配对检验 |
| Bootstrap | Bootstrap | 自助重采样 | B=10000，配重采样 |
| Holm | Holm 校正 | 多重比较校正 | 次级对比 p 校正 |
| 95% CI | Confidence Interval | 置信区间 | Δ small recall 的 CI 不跨 0 |
| Median / mean | 中位数/均值 | 中心趋势 | 报告口径区分 |
| p 值 | p-value | 显著性 | 双尾 |
| N | 样本量 | 数量 | 图级 N=1610 |
| 配对 | Paired | 配对样本 | 同图对比 |

---

## 12. 项目内部代号速查（详见 Abbreviation_Glossary.md）

| 代号 | 含义 | 备注 |
|---|---|---|
| P0 | 练手论文（Practice 0） | 不计入七篇主论文 |
| Paper 1–7 | 七篇主论文路线 | 2–7 PAUSED |
| BT | Baseline Training | 基线训练（BT1 = YOLO11n 普通基线） |
| BTD | Baseline/机制 Diagnosis | 诊断任务（1–12，无 BTD13） |
| P0-EI-C1/C2 | EI 稿两项主张 | PROPOSED |
| P0-A-C1/C2 | 历史机制主张 | HOLD |
| A0–A5 | 主线 A 阶段门 | 当前 A0 探索、A5 有限开放 |
| W-0001–W-0014 | 文献工作审计号 | 见 Literature 目录 |
| Stage A/B/C/D/E/F | P0 Benchmark 阶段 | 全部 PASS（2026-09-20） |
| 冻结权重 | 冻结 `last.pt` | SHA bc42d54e... |
| 状态词 | PASS/DONE/HOLD/DISMISSED/PAUSED/BLOCKED/PROPOSED | 各含义见 Abbreviation_Glossary §6 |

---

## 13. 更新规则

1. 新术语入库后再用于写作/实验命名；本项目按“先入表、后使用”纪律。
2. 每个词条尽量保留：英文全称、中文含义、项目内用法（或扩展标记）。
3. 与 Abbreviation_Glossary.md 冲突时：项目代号以 Abbreviation_Glossary.md 为准，目标检测领域名词以本文件为准。
4. 新增 Run ID／BTD 号时同步更新 Abbreviation_Glossary.md，本文件只收录其中的检测术语。
5. 本文件不替代实验报告与协议；数字一律以对应 `*_Result.md` 为准。

> AI生成