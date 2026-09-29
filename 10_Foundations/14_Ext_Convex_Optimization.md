# 扩展：凸优化

层：扩展。当前阶段不读。功率或带宽分配论文再打开。共用最小集在 [`08_Optimization.md`](08_Optimization.md)。

参考：Boyd, Vandenberghe. *Convex Optimization*. Cambridge, 2004. https://web.stanford.edu/~boyd/cvxbook/

## 必学

凸集：两点连线仍在集内。凸函数：连线在函数图像上方。标准形式

\[
\min_x f_0(x)\quad\mathrm{s.t.}\quad f_i(x)\le 0,\ i=1,\ldots,m
\]

\(x\) 是决策变量。\(f_0\) 是目标。\(f_i\) 是不等式约束。都凸时，局部最小即全局最小。

拉格朗日乘子 \(\lambda_i\ge 0\) 对应第 \(i\) 条约束。KKT：驻点、原始可行、对偶可行、互补 \(\lambda_i f_i(x)=0\)。互补表示约束没顶满时乘子为 0。功率上限顶满时，乘子可以非 0。

## 查阅

内点法、ADMM、半定规划：知道是求解器或分解方法，不写迭代式。
