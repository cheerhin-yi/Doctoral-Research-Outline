# 符号

层：必学。当前阶段应读。

## 必学

标量用斜体 $a$ ，向量用粗体 $\mathbf{x}$ ，矩阵用大写 $\mathbf{A}$ 。第 $i$ 个分量是 $x_i$ 。矩阵第 $i$ 行第 $j$ 列是 $A_{ij}$ 。

转置 $\mathbf{A}^{\mathsf T}$ 把行变成列。常见尺寸：图像块 $\mathbf{x}\in\mathbb{R}^{H\times W\times C}$ ， $H$ 高、 $W$ 宽、 $C$ 通道。

范数： $\Vert \mathbf{x}\Vert_2=\sqrt{\sum_i x_i^2}$ ，长度。 $\Vert \mathbf{x}\Vert_1=\sum_i |x_i|$ 。论文里的 $\Vert \cdot\Vert$ 不说明时，默认是 $\Vert \cdot\Vert_2$ 。

 $\arg\max_i s_i$ 是使 $s_i$ 最大的下标，不是最大值本身。最大值是 $\max_i s_i$ 。

期望 $\mathbb{E}[X]$ 是随机变量 $X$ 的平均。方差 $\mathrm{Var}(X)=\mathbb{E}[(X-\mathbb{E}[X])^2]$ 。

线性值与分贝：

$$
G_{\mathrm{dB}} = 10\log_{10} G
$$

 $G$ 是功率比，无量纲。 $G_{\mathrm{dB}}$ 的单位是 dB。幅度比用 $20\log_{10}$ 。信噪比若已是功率比，用 10。

## 查阅

花体 $\mathcal{L}$ 常表示损失或集合，以该公式下文定义为准。 $\mathcal{N}(\mu,\sigma^2)$ 是均值 $\mu$ 、方差 $\sigma^2$ 的正态。
