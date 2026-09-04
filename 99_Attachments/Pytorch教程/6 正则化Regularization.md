# 正则化
在机器学习中，误差可以分解为：偏差，方差与噪声之和。即误差=偏差+方差+噪声
Regularization是一种减少方差的策略。
正则化方式有 L1 和 L2 正则项两种。其中 L2 正则项又被称为权值衰减(weight decay)。
**L1 让没用的参数归零，L2 让所有参数变小。**  
在 PyTorch 中，L2 只需设置 `weight_decay` 参数即可，L1 需手动加损失。绝大部份模型（尤其 Transformer）都默认使用 L2 正则化。
## Dropout
在训练时**随机“丢弃”一部分神经元**，用来防止过拟合。
- **训练时**：每个神经元以概率 p（通常 0.2~0.5）被暂时“关闭”，即输出置 0，相当于这个神经元本轮不参与前向和反向传播。
- **效果**：每次训练都是随机抽取一个“子网络”，最终等效于**集成了大量不同网络的预测**，模型被迫学习更鲁棒的特征，不会过度依赖某些特定神经元。
### 使用情况
- **全连接层（尤其密集层）**：这是 Dropout 最初设计的主战场，当全连接层参数量大、容易过拟合时，Dropout 效果显著。
- **训练数据较少的任务**：数据量不足以支撑大模型时，Dropout 能大幅缓解过拟合。
- **传统 CNN 的末尾几层**：早期 CNN（VGG、ResNet）常在最后的全连接分类器前加 Dropout。
- **Transformer / 大模型**：
    - 早期 Transformer（如原始 Attention 论文）在注意力权重、残差分支、前馈网络中都曾广泛使用 Dropout。
    - 如今预训练大模型（GPT、LLaMA）因为使用了海量数据，常将 Dropout 设置得很小（如 0.1）甚至完全不用，转而依赖数据增强、权重衰减等其它正则化。
    - **微调阶段**，如果下游任务数据集很小，经常会重新引入或调大 Dropout，防过拟合效果明显。
###  核心要点
- **位置**：通常放在激活函数之后，或者注意力权重计算后。
- **PyTorch 实现**：`torch.nn.Dropout(p=0.5)`，加在层之间即可。
- **注意**：Dropout 只在训练时生效，评估或推理时需手动调用 `model.eval()` 将其关闭QAA 。
# 标准化Batch Normalization
称为批标准化。批是指一批数据，通常为 mini-batch；标准化是处理后的数据服从$N(0,1)$的正态分布。
**Batch Normalization 是先将数据标准化成“均值为 0、方差为 1”的分布（类似正态分布），再通过网络自学的 γ、β 重新缩放偏移，而不是缩放到 0~1 区间。**
批标准化的优点有如下：
- 可以使用更大的学习率，加速模型收敛
- 可以不用精心设计**权值初始化**[[4 模型训练#权值初始化]]
- 可以不用 dropout 或者较小的 dropout
- 可以不用 L2 或者较小的 weight decay
- 可以不用 LRN (local response normalization)
Batch Normalization 的提出主要是为了解决 Internal Covariate Shift (ICS)。在训练过程中，数据需要经过多层的网络，如果数据在前向传播的过程中，尺度发生了变化，可能会导致梯度爆炸或者梯度消失，从而导致模型难以收敛。
Batch Normalization 层一般在激活函数前一层。
## Batch Normalization in PyTorch
在 PyTorch 中，有 3 个 Batch Normalization 类，以图片为例，$B$是一次性输入多少张图片，$C$是通道数
- nn.BatchNorm1d()，输入数据的形状是 $B \times C \times 1D_feature$
- nn.BatchNorm2d()，输入数据的形状是 $B \times C \times 2D_feature$
- nn.BatchNorm3d()，输入数据的形状是 $B \times C \times 3D_feature$
以`nn.BatchNorm1d()`为例，如下：
```
torch.nn.BatchNorm1d(num_features, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
```
参数：
- num_features：一个样本的特征数量，这个参数最重要。这个在图像里面是通道数。
- eps：在进行标准化操作时的分布修正项
- momentum：指数加权平均估计当前的均值和方差
- affine：是否需要 affine transform，默认为 True
- track_running_stats：True 为训练状态，此时均值和方差会根据每个 mini-batch 改变。False 为测试状态，此时均值和方差会固定
主要属性：
- runninng_mean：均值
- running_var：方差
- weight：affine transform 中的 $\gamma$
- bias：affine transform 中的 $\beta$
在训练时，均值和方差采用指数加权平均计算，也就是不仅考虑当前 mini-batch 的值均值和方差还考虑前面的 mini-batch 的均值和方差。
在训练时，均值方差固定为当前统计值。
所有的 bn 层都是根据**特征维度**（图像里面的通道）计算上面 4 个属性，详情看下面例子。
## 其他 Normalization（用到再说）
### Layer Normalization
提出的原因：Batch Normalization 不适用于变长的网络，如 RNN
思路：每个网络层计算均值和方差
### Instance Normalization
提出的原因：Batch Normalization 不适用于图像生成。因为在一个 mini-batch 中的图像有不同的风格，不能把这个 batch 里的数据都看作是同一类取标准化。
思路：逐个 instance 的 channel 计算均值和方差。也就是每个 feature map 计算一个均值和方差。
包括 InstanceNorm1d、InstanceNorm2d、InstanceNorm3d。
### Group Normalization
提出的原因：在小 batch 的样本中，Batch Normalization 估计的值不准。一般用在很大的模型中，这时 batch size 就很小。
思路：数据不够，通道来凑。 每个样本的特征分为几组，每组特征分别计算均值和方差。可以看作是 Layer Normalization 的基础上添加了特征分组。
