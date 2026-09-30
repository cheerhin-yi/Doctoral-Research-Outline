# 训练里的导数

层：必学为主。当前阶段：读损失时再翻，不是 P0 正文前提。

## 必学

损失 $L(\theta)$，$\theta$ 是参数。梯度 $\nabla_\theta L$ 的第 $i$ 项是 $\partial L/\partial\theta_i$，指向上升最快的方向。更新常用 $\theta\leftarrow\theta-\eta\nabla_\theta L$。$\eta>0$ 是学习率，无量纲步长系数，不是发射功率。

链式法则：$y=f(g(x))$ 时 $dy/dx=(df/dg)(dg/dx)$。反向传播是把这条用在每一层。

Softmax，类别 $k=1,\ldots,K$，得分 $s_k$：

$$
p_k=\frac{e^{s_k}}{\sum_{j=1}^{K} e^{s_j}}
$$

$p_k\in(0,1)$，$\sum_k p_k=1$。交叉熵 $L=-\sum_k y_k\log p_k$。$y_k$ 是真值，一类问题里一个为 1、其余为 0。$\log$ 是自然对数。

## 查阅

海森是二阶导矩阵，看曲率。KKT 见 [`14_Ext_Convex_Optimization.md`](14_Ext_Convex_Optimization.md)。变分是泛函的导数，读水平集或能量模型再翻。
