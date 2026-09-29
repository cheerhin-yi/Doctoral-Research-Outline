# 优化的共用最小集

层：必学。凸优化细节在扩展章。当前阶段不读。

## 必学

问题写成 \(\min_x f(x)\)，\(x\) 是决策变量。训练时 \(x\) 是网络参数，学习率见 [`03_Calculus_for_Training.md`](03_Calculus_for_Training.md)。分配时 \(x\) 可以是功率或带宽，单位是 W 或 Hz，不要和学习率混用。

约束 \(g(x)\le 0\)。拉格朗日

\[
\mathcal{L}(x,\lambda)=f(x)+\lambda g(x)
\]

\(\lambda\ge 0\) 是乘子，惩罚违反约束。功率上限 \(P\le P_{\max}\) 就是这种约束。

## 查阅

怎么判断凸、对偶、KKT：[`14_Ext_Convex_Optimization.md`](14_Ext_Convex_Optimization.md)。
