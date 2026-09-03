# 领域英语课程

本文件由AI根据[当前科研阶段](../00_Overview/Current_Stage.md)逐模块提供课程。当前只开放模块1，不提前生成后续论文或Paper 1专属内容。

## 📖 使用方法

1. 每次学习5项，先朗读英文，再看领域含义和例句。
2. 合上文件，说出每项在YOLO检测链中的位置或作用。
3. 使用当天表达写一个自己的句子。
4. 按第1、3、7、14和30天复习。
5. 完成全部30项后，再做本模块练习；答案必须最后查看。

音标以常见美式读法为主。复合术语的实际重音会随句子变化；学习重点是能够识别、听辨和正确使用，而不是孤立追求音标细节。

## 🎯 模块1：YOLO检测链英语

### 第1组：任务与输入

1. **object detection** /ˈɑːbdʒekt dɪˈtekʃən/
   - 当前领域含义：目标检测；同时判断图像中有什么目标以及目标在哪里。
   - 常用搭配：perform object detection
   - 领域例句：The model performs object detection on aerial images.
   - 容易混淆：`image classification`只判断整张图像的类别，不负责定位每个目标。

2. **input image** /ˈɪnpʊt ˈɪmɪdʒ/
   - 当前领域含义：送入模型处理的输入图像。
   - 常用搭配：take an image as input
   - 领域例句：The detector takes an RGB image as input.
   - 容易混淆：`input`是进入模型的内容，`output`是模型产生的结果。

3. **image preprocessing** /ˈɪmɪdʒ ˌpriːˈprɑːsesɪŋ/
   - 当前领域含义：图像进入模型前进行的尺寸调整、归一化等处理。
   - 常用搭配：preprocess the input image
   - 领域例句：Image preprocessing resizes the input image before inference.
   - 容易混淆：`preprocessing`不等于只在训练时使用的`data augmentation`。

4. **feature extraction** /ˈfiːtʃər ɪkˈstrækʃən/
   - 当前领域含义：把图像逐步转换成可供检测使用的特征表示。
   - 常用搭配：extract features from an image
   - 领域例句：The backbone performs feature extraction at multiple stages.
   - 容易混淆：技术语境中的`feature`通常译为“特征”，不是日常语境中的“特色”。

5. **feature map** /ˈfiːtʃər mæp/
   - 当前领域含义：卷积网络产生的空间特征张量，通常具有高度、宽度和通道维。
   - 常用搭配：generate a feature map
   - 领域例句：Early layers generate high-resolution feature maps.
   - 容易混淆：`feature map`不是原始图像，也不是最终检测框。

### 第2组：Backbone与Neck

6. **backbone** /ˈbækboʊn/
   - 当前领域含义：从输入图像中提取分层特征的主干网络。
   - 常用搭配：extract features with the backbone
   - 领域例句：The backbone extracts hierarchical features from the input image.
   - 容易混淆：`backbone`只是检测器的一部分，不等于完整检测模型。

7. **neck** /nek/
   - 当前领域含义：连接Backbone与检测头、融合不同尺度特征的部分。
   - 常用搭配：fuse features in the neck
   - 领域例句：The neck fuses feature maps from different backbone stages.
   - 容易混淆：`neck`负责特征融合，`detection head`负责产生检测预测。

8. **detection head** /dɪˈtekʃən hed/
   - 当前领域含义：根据融合后的特征输出类别和边界框预测的部分。
   - 常用搭配：feed features into the detection head
   - 领域例句：The detection head predicts bounding boxes and class scores.
   - 容易混淆：论文中的`head`是模型组件，不是“头部目标”。

9. **downsampling** /ˈdaʊnˌsæmplɪŋ/
   - 当前领域含义：降低特征图空间尺寸的操作。
   - 常用搭配：downsample a feature map
   - 领域例句：Repeated downsampling reduces the spatial resolution of feature maps.
   - 容易混淆：`downsampling`描述降低分辨率的过程，`stride`是实现或描述步幅的参数之一。

10. **stride** /straɪd/
    - 当前领域含义：卷积或特征层相对输入移动或缩小的步幅；检测中也常表示特征图相对输入的总下采样倍数。
    - 常用搭配：a feature map with a stride of 8
    - 领域例句：A smaller stride preserves more spatial details for small objects.
    - 容易混淆：`stride`不是`kernel size`，两者控制的内容不同。

### 第3组：多尺度特征

11. **spatial resolution** /ˈspeɪʃəl ˌrezəˈluːʃən/
    - 当前领域含义：特征图在高度和宽度方向上的细致程度。
    - 常用搭配：preserve spatial resolution
    - 领域例句：High spatial resolution helps preserve small-object details.
    - 容易混淆：`resolution`描述空间尺寸或细节，不等于通道数量。

12. **channel** /ˈtʃænəl/
    - 当前领域含义：图像或特征张量中的特征维度。
    - 常用搭配：align feature channels
    - 领域例句：A convolution layer aligns the channels of multi-scale features.
    - 容易混淆：`channel`不是目标`class`；通道数也不一定等于类别数。

13. **multi-scale feature** /ˌmʌlti ˈskeɪl ˈfiːtʃər/
    - 当前领域含义：来自不同空间尺度、包含不同细节和语义层次的特征。
    - 常用搭配：fuse multi-scale features
    - 领域例句：The neck fuses multi-scale features for objects of different sizes.
    - 容易混淆：`multi-scale features`指不同尺度的特征，不只是把输入图像缩放多次。

14. **bounding box** /ˈbaʊndɪŋ bɑːks/
    - 当前领域含义：用于表示目标位置和范围的矩形框。
    - 常用搭配：predict a bounding box
    - 领域例句：Each detection contains a bounding box and a class prediction.
    - 容易混淆：`bounding box`是框的位置表示，`ground-truth box`特指人工标注参考框。

15. **class score** /klæs skɔːr/
    - 当前领域含义：模型对某个类别的预测分数。
    - 常用搭配：predict class scores
    - 领域例句：The head predicts class scores for each candidate location.
    - 容易混淆：`class score`与最终`confidence score`的具体组合方式可能随模型实现变化。

### 第4组：预测与监督

16. **confidence score** /ˈkɑːnfɪdəns skɔːr/
    - 当前领域含义：用于表示并筛选检测预测可信程度的分数；精确定义应以所用实现为准。
    - 常用搭配：filter low-confidence predictions
    - 领域例句：Predictions with low confidence scores are removed.
    - 容易混淆：不要默认所有YOLO版本都用完全相同的置信度计算方式。

17. **classification** /ˌklæsɪfɪˈkeɪʃən/
    - 当前领域含义：预测目标属于哪个已知类别的任务或分支。
    - 常用搭配：perform object classification
    - 领域例句：The classification branch predicts the object category.
    - 容易混淆：检测中的分类分支不负责精确预测边界框坐标。

18. **bounding-box regression** /ˈbaʊndɪŋ bɑːks rɪˈɡreʃən/
    - 当前领域含义：预测或优化目标框位置和尺寸的任务。
    - 常用搭配：perform bounding-box regression
    - 领域例句：The regression branch predicts the location and size of each box.
    - 容易混淆：这里的`regression`是连续数值预测，不是统计课程中特指的某一种回归模型。

19. **ground truth** /ˌɡraʊnd ˈtruːθ/
    - 当前领域含义：训练或评价时使用的人工标注参考答案。
    - 常用搭配：match predictions with ground truth
    - 领域例句：Predicted boxes are compared with ground-truth boxes during evaluation.
    - 容易混淆：`ground truth`是参考标注，`prediction`是模型输出。

20. **label assignment** /ˈleɪbəl əˈsaɪnmənt/
    - 当前领域含义：训练时确定哪些预测位置或候选与哪些真实目标对应。
    - 常用搭配：assign ground-truth labels to predictions
    - 领域例句：Label assignment matches training candidates with ground-truth objects.
    - 容易混淆：`label assignment`是训练匹配过程，`annotation`是数据标注过程。

### 第5组：训练与推理

21. **loss function** /lɔːs ˈfʌŋkʃən/
    - 当前领域含义：训练时衡量预测与监督目标差异并提供优化信号的函数。
    - 常用搭配：calculate the training loss
    - 领域例句：The loss function combines classification and box-regression terms.
    - 容易混淆：`loss`用于训练优化，`evaluation metric`用于评价结果，两者不能直接互换。

22. **forward pass** /ˈfɔːrwərd pæs/
    - 当前领域含义：输入经过模型并产生预测或训练输出的一次前向计算。
    - 常用搭配：run a forward pass
    - 领域例句：A forward pass produces predictions from the input batch.
    - 容易混淆：`forward pass`产生输出，`backward pass`计算梯度。

23. **training** /ˈtreɪnɪŋ/
    - 当前领域含义：使用训练数据、损失和优化过程更新模型参数。
    - 常用搭配：train the model on a dataset
    - 领域例句：During training, the model updates its parameters using the calculated loss.
    - 容易混淆：`training`会更新参数，`validation`和`inference`通常不更新参数。

24. **inference** /ˈɪnfərəns/
    - 当前领域含义：使用训练好的模型对输入产生预测的过程。
    - 常用搭配：perform inference on an image
    - 领域例句：During inference, the detector outputs candidate boxes and scores.
    - 容易混淆：`inference`是产生预测，`evaluation`还包括用标注和指标衡量这些预测。

25. **prediction decoding** /prɪˈdɪkʃən diːˈkoʊdɪŋ/
    - 当前领域含义：把模型原始输出转换为可解释的边界框坐标和分数。
    - 常用搭配：decode model predictions
    - 领域例句：Prediction decoding converts raw outputs into candidate detections.
    - 容易混淆：`decoding`生成候选检测，`non-maximum suppression`处理候选之间的重复。

### 第6组：筛选与评价

26. **confidence threshold** /ˈkɑːnfɪdəns ˈθreʃhoʊld/
    - 当前领域含义：筛除低置信度预测时使用的阈值。
    - 常用搭配：set a confidence threshold
    - 领域例句：A higher confidence threshold removes more low-score predictions.
    - 容易混淆：置信度阈值与NMS使用的IoU阈值作用不同。

27. **non-maximum suppression** /nɑːn ˈmæksɪməm səˈpreʃən/
    - 当前领域含义：根据分数和重叠程度抑制重复候选框，简称NMS。
    - 常用搭配：apply non-maximum suppression
    - 领域例句：Non-maximum suppression removes duplicate detections for the same object.
    - 容易混淆：NMS主要处理重复框，不是用于训练的损失函数。

28. **intersection over union** /ˌɪntərˈsekʃən ˈoʊvər ˈjuːniən/
    - 当前领域含义：两个区域交集面积与并集面积的比值，简称IoU。
    - 常用搭配：calculate the IoU between two boxes
    - 领域例句：IoU measures the overlap between a predicted box and a ground-truth box.
    - 容易混淆：IoU衡量两个框的空间重叠，不等于Precision或Recall。

29. **precision and recall** /prɪˈsɪʒən ænd rɪˈkɔːl/
    - 当前领域含义：Precision关注预测为正的结果中有多少正确；Recall关注真实目标中有多少被找到。
    - 常用搭配：report precision and recall
    - 领域例句：Precision reflects false-positive control, whereas recall reflects missed detections.
    - 容易混淆：`precision`不是定位精度的日常含义；在检测评价中它有明确的统计定义。

30. **average precision and mean average precision** /ˈævərɪdʒ prɪˈsɪʒən ænd miːn ˈævərɪdʒ prɪˈsɪʒən/
    - 当前领域含义：AP概括单个类别在不同置信度下的Precision–Recall表现；mAP对多个类别的AP求平均。
    - 常用搭配：evaluate the model using AP and mAP
    - 领域例句：Mean average precision summarizes detection performance across classes.
    - 容易混淆：`average precision`通常简称AP，不等于分类任务中的`accuracy`；mAP的IoU范围必须同时说明。

## 🔗 必会固定搭配

1. **extract features from an image**：从图像中提取特征。
   - The backbone extracts features from the input image.
2. **fuse multi-scale features**：融合多尺度特征。
   - The neck fuses multi-scale features from different backbone stages.
3. **predict bounding boxes and class scores**：预测边界框和类别分数。
   - The detection head predicts bounding boxes and class scores.
4. **assign ground-truth labels**：分配真实标签。
   - The training procedure assigns ground-truth labels to candidate predictions.
5. **calculate the training loss**：计算训练损失。
   - The model calculates the training loss after label assignment.
6. **decode model predictions**：解码模型预测。
   - The inference pipeline decodes model predictions into candidate boxes.
7. **suppress duplicate detections**：抑制重复检测。
   - NMS suppresses duplicate detections with high overlap.
8. **evaluate detection performance**：评价检测性能。
   - We use precision, recall, AP, and mAP to evaluate detection performance.

## 🧱 本模块语法句型

### 句型1：描述输入和输出

```text
X takes A as input and outputs B.
X接收A作为输入，并输出B。
```

使用规则：主语`X`是第三人称单数时，使用`takes`和`outputs`。

正确例句：

- The backbone takes an image as input and outputs feature maps.
- The detection head takes fused features as input and outputs box predictions.

常见错误：

- 错：The backbone take an image as input.
- 对：The backbone takes an image as input.
- 错：The model outputs to bounding boxes.
- 对：The model outputs bounding boxes.

### 句型2：描述组件作用

```text
X is used to do something.
X is responsible for doing something.
X用于或负责完成某项功能。
```

使用规则：`is used to`后接动词原形；`is responsible for`后接名词或动词的`-ing`形式。

正确例句：

- The neck is used to fuse multi-scale features.
- The detection head is responsible for predicting bounding boxes.

常见错误：

- 错：The neck is used to fusing features.
- 对：The neck is used to fuse features.
- 错：The head is responsible for predict boxes.
- 对：The head is responsible for predicting boxes.

## 📝 闭卷练习

完成后把本人答案写入[学习进度记录](Progress_Log.md)，再查看后面的参考答案。

### 英译中

1. The backbone extracts hierarchical features from the input image.
2. The neck fuses feature maps with different spatial resolutions.
3. The detection head takes fused features as input and outputs bounding boxes and class scores.
4. Non-maximum suppression is used to suppress duplicate detections.
5. Precision and recall evaluate different aspects of detection performance.

### 中译英

1. Backbone从输入图像中提取特征。
2. Neck负责融合多尺度特征。
3. 检测头输出边界框和类别分数。
4. IoU衡量预测框和真实框之间的重叠。
5. NMS用于抑制重复检测框。

### 口述任务

不看课程内容，使用至少6个必会固定搭配，口述下面的检测链：

```text
输入图像
→ Backbone
→ 多尺度特征
→ Neck
→ Detection Head
→ 训练分支或推理分支
→ 解码与NMS
→ Precision、Recall、AP和mAP
```

### 段落任务

用80–150个英文单词说明一个YOLO检测器如何把输入图像转换为最终检测结果。必须包含：

- `takes ... as input`
- `is used to`或`is responsible for`
- Backbone、Neck和Detection Head
- prediction decoding和NMS
- 至少一种评价指标

先独立完成，不逐句翻译中文答案，也不直接复制下面的参考段落。

## 🔒 参考答案：完成后再看

### 英译中参考

1. Backbone从输入图像中提取分层特征。
2. Neck融合具有不同空间分辨率的特征图。
3. 检测头接收融合后的特征作为输入，并输出边界框和类别分数。
4. 非极大值抑制用于抑制重复检测。
5. Precision和Recall评价检测性能的不同方面。

### 中译英参考

1. The backbone extracts features from the input image.
2. The neck is responsible for fusing multi-scale features.
3. The detection head outputs bounding boxes and class scores.
4. IoU measures the overlap between a predicted box and a ground-truth box.
5. NMS is used to suppress duplicate detections.

### 段落参考

A YOLO detector takes an image as input and processes it through several stages. First, the backbone extracts hierarchical features from the image. The neck then fuses multi-scale feature maps with different spatial resolutions. The detection head is responsible for predicting bounding boxes and class scores. During inference, prediction decoding converts the raw outputs into candidate detections. A confidence threshold removes low-score predictions, and non-maximum suppression suppresses duplicate boxes. Finally, precision, recall, AP, and mAP can be used to evaluate detection performance. Each stage has a different role, but the stages form one continuous detection pipeline.

### 常见错误检查

- 把`Backbone`、`Neck`和`Head`写成三个互不连接的句子，却没有说明输入输出关系。
- 在`is used to`后使用`-ing`形式。
- 在`is responsible for`后直接使用动词原形。
- 把`training`和`inference`写成完全相同的过程。
- 把prediction decoding与NMS当成同一个操作。
- 把Precision解释为边界框定位是否精确。
- 写mAP时不说明采用的IoU阈值或范围。

## ⏭️ 下一模块门禁

模块2只在EL-01通过后生成，主题为IoU、Precision、Recall、AP、mAP和错误分析。科研S0-01没有完成时，不生成PyTorch或专项论文英语模块。
