---
AIGC:
  ContentProducer: '001191110102MAD55U9H0F10002'
  ContentPropagator: '001191110102MAD55U9H0F10002'
  Label: '1'
  ProduceID: '6a7e4462-43c4-4ec6-99ed-a845c8c02314'
  PropagateID: '6a7e4462-43c4-4ec6-99ed-a845c8c02314'
  ReservedCode1: '4e58b4ef-3c48-4876-bbe4-40f1b7f9e5e0'
  ReservedCode2: '4e58b4ef-3c48-4876-bbe4-40f1b7f9e5e0'
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

### §2 术语详解

- **YOLO 家族演进**：YOLOv1（2016，单阶段端到端）→ v2/v3（多尺度、anchor、FPN）→ v5（工程化、易用）→ v8（anchor-free、C2f 模块）→ YOLO11（2024 最新）。
- **YOLO 后缀 n/s/m/l/x**：模型规模从 nano 到 extra-large。n 最轻最快（适合低显存/边缘），x 最重最准。YOLO11n 即 nano 版（约 2.6M 参数量级），是 [项目] BT1 固定检测器，因为 GTX 1660 6GiB 显存只能跑小模型。
- **Faster R-CNN**：两阶段经典。流程=主干特征 → RPN 出候选 → RoIAlign 裁剪 → 分类+回归。精度高、速度慢（非实时）。
- **FCOS**：全卷积单阶段 anchor-free，在特征图每个位置直接预测“到四边的距离 + center-ness（中心度）”。center-ness 用于压低远离目标中心位置的误检。
- **DETR**：把检测当成“集合预测”问题，用固定数量的可学习 query 直接出框，天然去掉 NMS。缺点：小目标性能弱、收敛慢、需要长训练。
- **RT-DETR**：DETR 的实时改进版，用混合编码器在计算开销可控前提下改善多尺度（含小目标）特征，速度可对标 YOLO 系。
- **SSD**：多尺度默认框（在不同层设不同尺度的锚）单阶段检测器，历史基线代表。
- **GFLV2**：在 GFL（Generalized Focal Loss）上增加“定位质量估计”分支——用 DFL 回归分布的高峰/方差统计量来调制分类分数，使分数与框质量对齐。它是 [项目] BTD12 被 DISMISSED 候选（尺度条件 DFL 重评分）的近邻依据。
- **Grounding DINO**：开放词汇检测器。把文本 prompt 编码后与图像特征做交叉注意力对齐，可检测任意文本指定的类别。是 [扩展] RailUAV-SOD 标注管线的主引擎（M1 本地主力）。
- **DINO-X**：更强的开放词汇基础模型，通常以 API/云端方式调用，[扩展] 预实验中作“上限参照 M2”。
- **T-Rex2**：无需文本的开放集检测器——用“视觉提示”（点击目标、画框）即可检测同类目标，[扩展] M3 视觉提示兜底。
- **SAM / SAM2**：Segment Anything（分割一切）模型，输入点/框/掩码提示即可输出高质量分割掩码；SAM2 支持视频。
- **Grounded SAM**：Grounding DINO 检框 + SAM 分割的组合管线，[扩展] 用于开放词汇标注管线生成实例掩码。

---

## 3. 训练与优化

| 缩写／词 | 英文全称 | 中文含义 | 项目内用法与说明 |
|---|---|---|---|
| Epoch | Epoch | 一轮全量训练 | 全部训练样本过一次前向+反向=1 epoch。100 轮=每个样本被学习 100 次。[项目] BT1 跑满 100 轮 |
| Batch / batch size | Batch size | 批大小 | 一次前向/反向处理的样本数；越大梯度越稳但显存占用越高。batch=4 表示每次处理 4 张图 |
| lr / LR | Learning rate | 学习率 | 梯度下降步长，控制权重更新幅度：过大发散、过小收敛慢 |
| Warmup | Learning rate warmup | 学习率预热 | 前 T 轮用很小 lr 逐步升到目标 lr，避免初期大学习率破坏预训练权重 |
| Scheduler | LR scheduler | 学习率调度 | 训练中按轮/按步降低 lr（如余弦退火、余弦退火衰减），后期用更小步长精细收敛 |
| SGD | Stochastic Gradient Descent | 随机梯度下降 | 更新：θ ← θ − lr·∇L(θ)。经典优化器，[项目] BT1 使用 |
| Adam / AdamW | Adaptive Moment Estimation (+ Weight Decay) | 自适应优化器 | 用一阶/二阶矩自适应调节每参数步长，收敛快；AdamW 把权重衰减与梯度解耦，微调/大模型常用 |
| EMA | Exponential Moving Average | 指数滑动平均 | 对训练中权重做滑动平均，见 §3.1 公式 |
| last.pt / best.pt | Ultralytics 权重文件 | 末轮/最优轮权重 | last.pt=训练结束时的权重；best.pt=按验证集指标最优的权重。[项目] 固定取末轮 EMA last.pt，不按 cal48 选模 |
| Checkpoint | Checkpoint | 训练断点包 | 保存 优化器状态+学习率+轮次+权重的包，可从中断处恢复 |
| Resume | Resume training | 续训 | 从 checkpoint 继续训练。[项目] BT1 三段接续 1–3／4／5–100 |
| Seed | Random seed | 随机种子 | 固定随机初始化/增强/打乱顺序以可复现；seed0 固定 |
| Freeze | Freeze weights | 冻结权重 | 冻结=不更新该层梯度。项目冻结 last.pt 只做推理对比，不训练 |
| Fine-tune | Fine-tuning | 微调 | 在预训练权重上用新数据继续小步长训练。项目门禁：禁止（除非书面授权） |
| Pretrain | Pre-trained weights | 预训练初始化 | 用大规模数据预训练权重作为初始值（如 COCO 预训练 → VisDrone 适配），收敛更快、效果更好 |
| FP32 / FP16 / BF16 | Floating Point 32/16 / Brain FP16 | 浮点精度 | 权重/激活的数值精度；FP16 减显存但需混合精度保稳定性；BF16 与 FP32 动态范围相近 |
| AMP | Automatic Mixed Precision | 混合精度 | 前向用 FP16 加速省显存，主权重仍 FP32，梯度缩放防溢出。[项目] BT1 amp=false（纯 FP32） |
| BN | Batch Normalization | 批归一化 | 对一批特征做标准化（减均值除方差）再缩放平移，稳定训练、允许更大 lr |
| Aug | Data Augmentation | 数据增强 | 训练时对图像随机变换（缩放/翻转/加噪声等）增加多样性、防过拟合 |
| Mosaic | Mosaic augmentation | 拼图增强 | 把 4 张图拼成 1 张训练，增加小目标样本与场景多样性，YOLO 系标配 |
| Normalization | Input normalization | 输入归一化 | 推理/训练前把像素缩放到固定范围（如 [0,1] 或均值方差标准化），保证与训练分布一致 |
| 类别映射 | Class mapping | 类别对应 | 数据集类别 ID 与模型类别索引的映射表。项目 VisDrone 十类→YOLO 索引，FROZEN_PRE_RESULTS 冻结 |

### §3.1 训练关键公式

**EMA 权重更新**（[项目] 正式检测器 last.pt 即末轮 EMA）：

```
θ_EMA ← α·θ_EMA + (1−α)·θ_current
```

| 参数 | 含义 |
|---|---|
| θ_current | 当前训练轮的模型权重 |
| θ_EMA | 历史滑动平均权重（更稳定） |
| α | 衰减系数（decay），通常 0.99~0.9999；α 越大历史占比越高、跟随越慢 |

作用：对训练噪声做低通滤波，通常比单独一次末轮权重泛化更稳。**注意：** 取 EMA 不等于测速时用了“平均多个模型”，它仍是单检测器。

**Warmup（线性预热）**：

```
lr(t) = lr_base × (t / T_warmup)    （t ≤ T_warmup 时线性增长）
```

| 参数 | 含义 |
|---|---|
| t | 当前迭代/轮次 |
| T_warmup | 预热期长度 |
| lr_base | 目标学习率 |

作用：跳过初始不稳定的高 lr 阶段。

---

## 4. 损失函数

| 缩写／词 | 英文全称 | 中文含义 | 说明 |
|---|---|---|---|
| Loss | Loss function | 损失函数 | 训练要最小化的标量目标，度量预测与真值的差距 |
| Cls loss | Classification loss | 分类损失 | 预测类别与真实类别的差距，常用 BCE（多标签）或 CE（多分类） |
| Reg loss | Regression loss | 回归损失 | 框坐标与真值坐标的差距，常用 IoU 系损失或 L1 |
| Objectness | Objectness loss | 目标性损失 | “该位置是否有目标”的二分类损失，无目标位置提供负样本 |
| BCE | Binary Cross Entropy | 二元交叉熵 | 二分类损失，见 §4.1 公式 |
| CE | Cross Entropy | 交叉熵 | 多分类交叉熵，见 §4.1 公式 |
| Focal Loss | Focal Loss | 焦点损失 | 对难分样本加重权、对易分样本降权，缓解前景/背景极度不平衡，见 §4.1 公式 |
| DFL | Distribution Focal Loss | 分布焦点损失 | 把框回归变成连续分布预测，见 §4.1 公式 |
| QFL | Quality Focal Loss | 质量焦点损失 | 把分类分数对齐到定位质量（IoU），见 §4.1 公式 |
| GFL | Generalized Focal Loss | 广义焦点损失 | = QFL + DFL，分类与回归统一用分布形式，GFLV2 在其上加定位质量估计 |
| GIoU / DIoU / CIoU / SIoU | Generalized / Distance / Complete / Scylla-IoU | IoU 损失变体 | 缓解 IoU=0 无梯度及中心点/宽高比不对齐，见 §4.1 公式 |
| NWD | Normalized Wasserstein Distance | 归一化沃瑟斯坦距离 | 把框建模为高斯分布再求距离，微小目标匹配比 IoU 更稳定，见 §4.1 公式 |

### §4.1 损失公式详解

**IoU（交并比）——所有匹配与 IoU 损失的基础：**

```
IoU(A,B) = |A∩B| / |A∪B|      ∈ [0,1]
```

| 参数 | 含义 |
|---|---|
| A, B | 预测框与真值框的矩形区域 |
| A∩B | 两框交叠面积 |
| A∪B | 两框并集面积 |

问题：两框不相交时 IoU=0，无梯度；且无法反映“离得近还是远”。因此有了下面几个变体：

**GIoU**：

```
GIoU = IoU − (|C \ (A∪B)|) / |C|     ∈ [−1, 1]
```

| 参数 | 含义 |
|---|---|
| C | A、B 的最小外接矩形 |
| C \ (A∪B) | C 中不属于两框的面积（空白区） |

作用：两框不相交时也给出可学习梯度（把外接框往里推）。

**DIoU**：

```
DIoU = IoU − ρ²(b, b_gt) / c²
```

| 参数 | 含义 |
|---|---|
| b, b_gt | 预测框与真值框的中心点 |
| ρ²(·) | 两中心点欧氏距离的平方 |
| c | 最小外接矩形的对角线长度 |

作用：直接惩罚中心点偏移，收敛更快。

**CIoU**（YOLOv5/v8/v11 回归默认）：

```
CIoU = DIoU − α·v
      v = (4/π²) · (arctan(w_gt/h_gt) − arctan(w/h))²
      α = v / ((1 − IoU) + v)
```

| 参数 | 含义 |
|---|---|
| w, h / w_gt, h_gt | 预测框与真值框的宽高 |
| v | 宽高比一致性惩罚项 |
| α | 动态权衡系数：IoU 越低时对 v 惩罚越小 |

作用：在 DIoU 基础上再对齐宽高比。SIoU 另加角度对齐项。

**BCE（二元交叉熵）**：

```
L_BCE = −[ y·log(p) + (1−y)·log(1−p) ]
```

| 参数 | 含义 |
|---|---|
| y ∈ {0,1} | 真实标签（是否为目标/该类别） |
| p ∈ [0,1] | 模型预测该类的概率 |

**CE（多分类交叉熵）**：

```
L_CE = −Σ_c y_c·log(p_c)      （c 遍历所有类别）
```

**Focal Loss**（处理难/易样本不平衡）：

```
L = −α_t · (1 − p_t)^γ · log(p_t)
```

| 参数 | 含义 |
|---|---|
| p_t | 正例取 p、负例取 1−p（该样本的置信度） |
| α_t | 类别平衡权重（控制正负样本比例） |
| γ | 聚焦指数：γ 越大，对易分样本降权越多、难分样本占比越大（常用 2） |

**DFL（分布 Focal Loss，回归分支）**：把框回归从单点改为离散分布，对两个相邻分箱做交叉熵：

```
DFL(S_i, S_{i+1}) = −[ (y_{i+1} − y)·log(S_i) + (y − y_i)·log(S_{i+1}) ]
```

| 参数 | 含义 |
|---|---|
| y | 目标回归位置（连续值） |
| y_i, y_{i+1} | 左右两个分箱的边界位置 |
| S_i, S_{i+1} | 网络预测这两个分箱的概率 |

[项目] BTD12 曾审查“用 DFL 分布统计量做尺度条件重评分”，因近邻 GFLV2 已覆盖 → DISMISSED。

**QFL（质量 Focal Loss，分类分支）**：分类目标从 0/1 变成“IoU 质量”连续标签：

```
L_QFL = −|y − σ|^β · [ y·log(σ) + (1−y)·log(1−σ) ]
```

| 参数 | 含义 |
|---|---|
| y | 连续质量标签（IoU 或 0/1 硬标签） |
| σ | 预测分数 |
| β | 调制指数（默认 2），对与标签接近的样本降权 |

**GFL 总损失 = QFL（分类） + DFL（回归）**。

**NWD（归一化沃瑟斯坦距离）**：把框看作二维高斯分布：

```
NWD(N_a, N_b) = exp( −√(W₂²(N_a, N_b)) / C )
W₂²(N_a, N_b) = ‖μ_a − μ_b‖₂² + ‖Σ_a^{1/2} − Σ_b^{1/2}‖_F²
```

| 参数 | 含义 |
|---|---|
| N_a, N_b | 两个框对应的高斯分布（μ=中心，Σ 由 w,h 构造） |
| W₂² | 二阶沃瑟斯坦距离平方 |
| ‖·‖₂ | 向量欧氏范数 |
| ‖·‖_F | 矩阵 Frobenius 范数 |
| C | 与数据小目标尺寸有关的常数（用于归一化到 [0,1]） |

作用：微小目标 IoU 匹配非常不稳定，W₂ 距离对“两个小框错位几个像素”更宽容，[项目] W-0011。

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

### §5.1 指标公式详解（重点）

**1) 框匹配规则（决定 TP/FP/FN）**

```
对每个 GT 框：与所有同类别预测框计算 IoU，取 IoU ≥ 匹配阈值且得分最高的框 → 该预测=TP；
未匹配到任何 GT 的预测框 → FP；没有被任何预测框匹配的 GT → FN。
每图输出先按置信度降序截断到 maxDets（本项目 500）个，再参与匹配。
```

| 符号 | 含义 |
|---|---|
| IoU | 见 §4.1，匹配用阈值通常 IoU=0.5 |
| maxDets | 每图最多保留的检测框数（本项目 500） |
| TP/FP/FN | 真阳/假阳/假阴（见上表） |

**2) Precision / Recall / F1**

```
Precision = TP / (TP + FP)          （检测出的框里有多少是对的）
Recall    = TP / (TP + FN)          （真目标里有多少被检出）
F1        = 2·Precision·Recall / (Precision + Recall)
```

**3) AP（单类平均精度）——最核心的指标**

把该类所有预测框按置信度**降序**排列，逐框累积 TP/FP，得到一条 (Precision, Recall) 曲线（PR 曲线），AP 即曲线下面积：

```
AP = Σ_{n} (R_{n+1} − R_n) · P_interp(R_{n+1})
P_interp(r) = max_{r′ ≥ r} P(r′)     （插值：取右端最大精度，保证曲线单调）
```

| 符号 | 含义 |
|---|---|
| n | 按置信度排序后的框序号 |
| R_n, P_n | 到第 n 个框为止的累积召回/精度 |
| P_interp(r) | 召回率为 r 处的插值精度 |

**参数解读**：AP 同时惩罚“漏检”（降召回）和“误检”（降精度），是检测器质量的单值综合度量。

**4) mAP（各类平均）**

```
mAP = (1/C) · Σ_{c=1..C} AP_c
```

| 符号 | 含义 |
|---|---|
| C | 类别数（本项目 VisDrone 十类） |
| AP_c | 第 c 类的 AP |

- **mAP50**：用 IoU=0.5 做匹配阈值时算出的 mAP（对框位置不敏感，较宽松）。
- **mAP75**：IoU=0.75 时的 mAP（对框位置更苛刻）。
- **mAP50-95**：对 IoU ∈ {0.5, 0.55, …, 0.95} 共 **10 个阈值**分别算 mAP，再取平均。**是 COCO 及本项目的总排名指标**；对框质量、尺度都非常敏感。

**5) 分尺度指标（COCO 口径）**

| 记号 | 定义 | 本项目等价物 |
|---|---|---|
| AP_s | GT 面积 < 1024px²（即 <32×32）的 AP | 本项目小目标口径一致 |
| AP_m | GT 面积 1024 ~ 9216px²（32×32~96×96） | — |
| AP_l | GT 面积 ≥ 9216px²（≥96×96） | — |

注意：本项目评测的“小目标”用 `0 < w×h < 1024` 直接判定，与 COCO small 面积界一致，但未用 COCO 的完整评分器；两者直接比较需说明口径。

**6) AR（平均召回）**：在每图最多保留 maxDets 个检测的条件下，对 IoU ∈ {0.5,…,0.95} 平均的召回，常记 AR@100/300/1000。

**7) 项目相关公式**

```
small_recall = TP_small / GT_small          // 只统计面积<1024 的小目标
超时率       = #{t_i > T_budget} / N_frame  // 超过声明预算的帧占比
mean_ms      = (1/N) Σ t_i                   // 平均整帧耗时
p95          = 排序后第 ⌈0.95·N⌉ 个耗时值       // 95 分位耗时
```

| 符号 | 含义 |
|---|---|
| T_budget | 声明的整帧时间预算（本项目 40ms 是相对参考，非硬期限） |
| t_i | 第 i 帧的端到端推理耗时（含协议规定的整条链路） |
| N / N_frame | 图像总数 |
| small_recall | 本项目 P0 主指标（Stage D/E 报告中的核心数字） |

**8) GT oracle（真值上界）**：用 GT 事后选窗/修复得到的“理论最优”，只用于界定空间，**严禁**写成可部署方法精度。[项目] GT 逐图选择 F1280 与最佳单片仅净增 33 就是 oracle 分析。

**9) TIDE（错误分析）**：TIDE 把检测错误按“分类错/定位差/重复/漏检/误检/背景”分解，量化每种错误对 AP 的影响占比。[项目] W-0010 审计；BTD11 借鉴其思路做 FN/FP 分解。

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

### §6 术语详解

- **NMS（非极大值抑制）**：同一目标的多个重叠框只保留得分最高的一个。步骤：①按置信度降序排列；②取最高分框，删除与其 IoU 超过阈值（本项目 0.5）的同类别框；③重复直到处理完。作用：抑制重复检测。[项目] BTD5/6 用公共 NMS 等价加速（约 27ms→6-7ms），这是工程加速、不算创新。
- **Soft-NMS**：不直接删除重叠框，而是按重叠度降低其分数，缓解密集场景下相邻目标被误删的问题。[扩展]
- **Adaptive NMS**：根据目标密度自适应调整 NMS 保留阈值，专门针对拥挤场景（人群/密集小目标）。[项目] W-0012 审计。
- **conf threshold（置信阈值）**：低于该分数的框被丢弃。[项目] 正式协议 conf=.25；低分归因实验用 .10（会带来 FP 激增，只作分析不作方法）。
- **max500**：每图按置信度降序最多保留 500 个框，与官方 maxDets 语义一致；超出部分不参与匹配。
- **Slicing / Tiling（切片推理）**：把高分辨率大图切成一格一格的小块（带重叠）分别推理，再把结果坐标还原到原图、合并去重。解决“小目标在原图占比小、直接缩放会丢失”的问题。
- **Tile size / Overlap**：切片尺寸（如 640×640）与相邻切片重叠比例（如 25%）。重叠保证切片边缘目标不被切断。
- **SAHI**：Slicing Aided Hyper Inference，通用切片推理框架（含切片-推理-坐标还原-合并 NMS 的完整链路），[项目] 五协议之一 `SAHI640`（640 切片/重叠 0.25）。
- **DensK1（密度单片）**：用粗略预测（或密度图）选出得分最高的 1 个局部窗口，再对该窗口做高分辨率推理，即“先粗后精”的典型区域策略；[项目] 是 F640 与 F1280 之间的对照方法。
- **UnifAll（均匀切片）**：不做选择，把整图均匀切块全部推理再合并；召回高但耗时线性增长，[项目] 五协议之一。
- **F640 / F1280**：整图直接缩放到边长 640/1280 输入。F1280 因输入分辨率高、对小目标更友好，且省去切片合并开销，[项目] 成为“强简单基线”（常优于密度单片）。
- **预算（time budget）**：声明“整帧从图像输入到最终输出的耗时上限”。本项目 40ms 只是相对参考、非业务硬期限；报告必须同时给 mean/p95/超时率。
- **pipeline（推理管线）**：本项目链=原图 → 固定 YOLO11n → 全图/局部窗推理 → 坐标还原 → 公共 NMS 去重 → 忽略区/匹配评估。不同协议只改“输入与选区策略”，其余冻结。
- **FPS**：每秒处理帧数 = 1000/mean_ms，时延的倒数，机载部署常用。
- **Cache（缓存）**：把一次推理的预测结果存盘，后续分析只读缓存、不重复推理。**缓存分析的耗时不算检测速度**（[项目] 纪律）。

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

### §7 术语详解

- **OVD（开放词汇检测）**：检测目标不限于训练时见过的类别，而是由**文本提示词**临时指定类别（如“绝缘子”“螺栓”），模型靠文本-视觉对齐完成检测。是 RailUAV-SOD 标注管线的技术底座。
- **OSR（开放集识别）**：只学过已知类别，但推理时能输出“未知”标志，与 OVD 的差异：OSR 不要求定位未知类别，只要求能拒识/报未知。[扩展] Paper 1 风险感知相关。
- **Zero-shot / Few-shot（零样本/少样本）**：零样本=推理时直接用（无目标域训练）；少样本=给极少量样例（如 1-10 张）即可适应。开放词汇检测器天然具备 zero-shot 检测能力。
- **Prompt（提示词）**：输入模型的文本描述，可简单（类别名）也可详细（描述性句子）。[项目] 提示三条件 C1（裸术语）/C2/C3（描述性）用于衡量“提示工程对召回的影响”。
- **Visual prompt（视觉提示）**：不用文字，用“点击/画框/画线”指示模型要检测的目标（T-Rex2 的核心交互方式），适合难以用文本描述的类别。
- **Grounding（对齐）**：把文本与图像中具体区域建立对应关系，输出“该文本对应图像中的哪个框”。
- **CLIP**：对比学习让图像编码器与文本编码器嵌入空间对齐，是 Grounding DINO 等开放词汇模型的基础组件之一。
- **VLM / LMM / LLM**：视觉语言模型（图+文理解）、多模态大模型、大语言模型；可承担术语生成、标注结果解析、规则抽取等作用。[扩展] 术语表五元组共享资产的工程部分。
- **Known / Unknown（已知/未知类别）**：开放世界风险感知把目标分成训练见过的（Known）与没见过的（Unknown），分别评测；Paper 1 的协议数据就按这个划分。[扩展]
- **M1 / M2 / M3（模型分层）**：[项目] 预实验的模型分层策略：M1=本地小模型（Grounding DINO Swin-T，1660 可跑）；M2=DINO-X Pro API（上限参照）；M3=T-Rex2 视觉提示救援（前两者失效时用）。

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

### §8 术语详解

- **VisDrone2019-DET**：无人机视角目标检测基准，含 10 类（pedestrian、people、bicycle、car、van、truck、tricycle、awning-tricycle、bus、motor），图像来自中国多城市航拍。官方划分 train/val/test-dev/test-challenge。[项目] 用 Ultralytics 维护者副本：train 6471 / val 548 / test-dev 1610（文件级审计完成）。
- **UAVDT**：无人机检测跟踪数据集，城市道路/车辆场景，50 序列 40735 帧（本项目用 DET 真值）。[项目] Stage E 用它做**跨数据集迁移检验**（冻结 VisDrone 权重直接推理）。
- **UAV-RSOD**：无人机铁路小目标数据集候选，因分片重复等问题历史审计 HOLD，不在当前关键路径。
- **COCO**：80 类通用检测基准，提供预训练权重与标准评测口径（AP 系列指标即 COCO 定义）。注意：本项目评测器是“VisDrone 兼容”而非 COCO 官方评分器。
- **YOLO txt 标注**：每行一个目标 `class cx cy w h`，坐标归一化到 [0,1]（除以图像宽高）；[项目] convert_visdrone_labels.py 完成 8 字段→YOLO 转换。
- **COCO JSON**：COCO 的标注格式（images/annotations/categories 三段结构），是许多评测工具的标准输入。
- **8 字段标注**：VisDrone 原始标注每行 8 个数：`bbox_left bbox_top bbox_w bbox_h score class truncation occlusion`；`score` 为标注置信（非推理分数），`truncation/occlusion` 为截断/遮挡标记。
- **cal48**：从 val 按固定规则（SHA256 排序取前 48）挑出的**开发集**，用于训练监控与反复诊断；不是独立测试集，写论文必须披露。
- **diag500**：val 中其余约 500 张，也属**开发证据**，不再冒充未接触测试集。
- **test-dev**：官方测试集（无公开标注的正式排行集）；本项目用维护者镜像 GT 做了一次性评估（Stage D），不等于官方 leaderboard 分数。
- **去重（Deduplication）**：第二片候选窗按“未被第一片覆盖的粗框数量”重排序，减少重复检出（[项目] BTD3 去重密度对照）。

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

### §9 术语详解

- **GPU / VRAM**：训练推理算力与显存（视频内存）。本项目本机 GTX 1660 SUPER **6 GiB**，只能跑小模型（YOLO11n 级别）；大模型/开放词汇基础模型受限，需 API 或 4090。
- **CUDA / cuDNN**：NVIDIA 的并行计算驱动/深度网络加速库，是 PyTorch GPU 版依赖；`torch2.7.1+cu126` 表示对应 CUDA 12.6 的构建。**注意**：本项目曾发现 CPU 版 torch（+cpu）导致 CUDA 不可用，须安装匹配 CUDA 版本。
- **torch / torchvision / ultralytics**：PyTorch 深度学习框架 / 视觉工具箱 / YOLO 官方工具链；环境冻结报告锁定版本（Ultralytics 8.4.90 等）以保可复现。
- **ONNX / TensorRT**：模型部署格式与加速引擎；本项目当前无部署验证，不得宣称机载可用。
- **Conda**：Python 虚拟环境管理；本项目独立环境 `H:/Conda/envs/UAV_BT1`，脚本迁移需重建环境而不是只复制代码。
- **RSS / GiB**：进程常驻内存 / 二进制容量单位（1 GiB=2³⁰ 字节）；资源守卫（如 RSS<3GiB）保证实验不把机器跑死。
- **NumPy**：数值计算库，缓存分析脚本依赖；曾因 NumPy int64 JSON 序列化问题导致 BTD7-01 归档失败（典型工程坑）。
- **SHA256**：密码学哈希（64 位十六进制），用于校验权重/数据文件完整性；[项目] 冻结权重指纹 `bc42d54e37acaf...`。
- **JSON / CSV / CRC**：配置文件/结果摘要格式；逐图像指标表格式；数据完整性校验（ZIP 内文件 CRC 核对）。
- **Run ID**：一次实验的唯一编号（如 `P0-BENCH-E-UAVDT-20260918-FULL`），先登记后运行；是证据可追溯的最小单元。

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

### §10 术语详解

- **EI（Engineering Index / Compendex）**：工程领域最常用的会议论文检索库。会议论文被 EI 检索是毕业/评奖常见硬指标；**CCF 会议（如 ICIP/PRCV）本身也常被 EI 检索**，所以投 CCF-C 不损失 EI。
- **Scopus / ISTP**：另一种引文数据库 / 科技会议录索引；PRCV 论文集由 Springer 出版，同时被 EI+ISTP 检索。
- **SCI / JCR / 中科院分区**：期刊体系：SCI 是期刊引文索引；JCR 把期刊按影响因子分 Q1–Q4；国内常用中科院分区（1–4 区，小类/大类）。**注意**：用户当前接受“中科院小类三区或 JCR 三区”，但具体学院/参评年度认可仍待核验。
- **CCF（中国计算机学会）推荐目录**：把会议/期刊分 A/B/C 三级，是国内计算机学科毕业/评奖的“硬通货”；只有 Full/Regular paper 计入，Workshop/短文不算。
- **会议代号**：CVPR/ICCV/ECCV（视觉 A 类顶会）、NeurIPS/ICLR/AAAI（AI 顶会，A 类）、ICIP（CCF-C，图像处理，IEEE 出版，录用率约 45%）、PRCV（CCF-C，国内模式识别大会，LNCS 出版）、WACV/BMVC/ACCV（CCF-C，应用/英国/亚洲视觉会议）、ICASSP（CCF-B 信号处理旗舰）、ICME（CCF-B 多媒体）。[项目] EI 稿目标 2027 会期：ICIP 2027（约 2027 年 1–2 月截稿）、PRCV 2027（约 2027 年 4 月底）、BMVC 2027 等；WACV 2027 已截稿。
- **LNCS**：Springer 的 Lecture Notes in Computer Science 丛书，PRCV 论文集所在，EI 检索。
- **IEEE Xplore**：IEEE 论文数字图书馆，ICIP 等 IEEE 会议论文集上线处。
- **CFP（Call for Papers）**：征稿启事，含截稿/录用/终稿日期与格式要求，投稿前必读。
- **Camera-ready**：录用后的最终版提交（含作者信息、终稿格式、版权）。
- **Double-blind（双盲评审）**：审稿人不知道作者、作者不知道审稿人；投稿文件须匿名（无作者名、致谢、可反查的仓库链接）。
- **Workshop**：主会旁边的专题研讨会，一般不计入 CCF 认定（但录用容易、可作练手/补充成果）。
- **录用率**：录用数/投稿数；CVPR 2026 约 25.4%，ICIP 2022 约 44%——同是 C 类难度差别很大，投稿定位要匹配。
- **水会（predatory conference）**：无实质审稿、为收注册费而办的会议；选择 EI 会议需查往届是否稳定被 EI 检索、主办方是否正规。

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

### §11 术语详解

- **Wilcoxon 符号秩检验**：非参数配对检验，用于“同一批图像上两方法差异是否显著”（不要求正态分布）。输出 p 值：p<0.05 视为显著差异。[项目] Stage F 对 1499 图（含小目标的图）做 F1280 vs DensK1 等配对检验。
- **Bootstrap（自助法）**：从原样本有放回地重采样多次（如 B=10000 次），每次计算统计量，得到其抽样分布，从而给出置信区间；比单点估计更稳健。[项目] Δ small recall 的 95% CI 由 bootstrap 给出。
- **Holm 校正**：多重比较（多对方法同时检验）时控制整体误报率的方法：把 p 值从小到大排序，逐级乘以校正系数；比 Bonferroni 更宽松。[项目] 次级对比用 Holm 校正 p。
- **95% CI（置信区间）**：区间估计；若 Δ 的 95% CI 不跨 0，则两个方法差异“统计上显著”（结合检验 p）。[项目] F1280 vs DensK1 的 Δ small recall CI=[0.0355, 0.0462] 不跨 0。
- **median / mean**：中位数（抗离群）/ 均值；报告耗时两者都给出，因为均值受长尾帧影响大。
- **p 值**：原假设成立下看到当前结果的概率；p<0.05 通常视为显著。
- **N（样本量）**：参与统计的图像数（图级单元），如 N=1610（test-dev）/ N=40735（UAVDT）。
- **配对（paired）**：同一批图像上比较两种方法（逐图成对），消除图像间差异，统计功效更高。

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