# 视觉里的矩阵

层：必学为主。当前阶段应读。

## 必学

矩阵乘 \(\mathbf{y}=\mathbf{A}\mathbf{x}\)：\(\mathbf{A}\) 是 \(m\times n\)，\(\mathbf{x}\) 是 \(n\times 1\)，\(\mathbf{y}\) 是 \(m\times 1\)。内维必须相等。全连接层就是这一步，\(\mathbf{A}\) 是权重。

秩 \(\mathrm{rank}(\mathbf{A})\) 是独立的行（或列）数。图像协方差秩低，表示像素方向高度相关。

特征值：\(\mathbf{A}\mathbf{v}=\lambda\mathbf{v}\)。\(\lambda\) 是拉伸倍数，\(\mathbf{v}\) 是方向。PCA 里大的 \(\lambda\) 是主变化方向。

SVD：\(\mathbf{A}=\mathbf{U}\boldsymbol{\Sigma}\mathbf{V}^{\mathsf T}\)。\(\boldsymbol{\Sigma}\) 的对角 \(\sigma_i\ge 0\) 是奇异值。压缩时丢掉小的 \(\sigma_i\)。

卷积写成滑动内积。核 \(\mathbf{K}\) 尺寸 \(k_h\times k_w\)，步长 \(s\)，填充 \(p\)。输出高

\[
H_{\mathrm{out}}=\lfloor (H+2p-k_h)/s\rfloor+1
\]

\(H\) 是输入高，单位是像素。宽同理。YOLO 的 stride 是特征图像素对应原图的步长，不是优化器步长。

框：\((x,y,w,h)\)，\(x,y\) 中心或左上角以该论文为准，\(w,h\) 宽高，单位像素。面积 \(a=wh\)。本项目小目标常用 \(0<wh<1024\)。

IoU：交面积除并面积，取值 \([0,1]\)。阈值 \(0.5\) 表示重叠过半算匹配。它不是概率。

## 查阅

伪逆 \(\mathbf{A}^{+}\)：方程没唯一解时的最小二乘解。张量分解：多通道滤核的低秩近似，读压缩论文再翻。
