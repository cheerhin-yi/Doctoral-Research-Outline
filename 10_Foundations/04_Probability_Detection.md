# 检测评价里的概率

层：必学为主。当前阶段应读。

## 必学

$P(A)$ 是事件 $A$ 的概率，$[0,1]$。条件概率 $P(A\mid B)=P(A,B)/P(B)$，$P(B)>0$。贝叶斯：

$$
P(y\mid x)=\frac{P(x\mid y)P(y)}{P(x)}
$$

$y$ 是类别，$x$ 是观测。$P(y)$ 先验，$P(x\mid y)$ 似然，$P(y\mid x)$ 后验。检测置信度是模型打分，不要直接当成已校准的后验。

期望 $\mathbb{E}[X]$，方差见 [`01_Notation.md`](01_Notation.md)。

一张图上：真阳 TP、假阳 FP、假阴 FN。精度 $P=\mathrm{TP}/(\mathrm{TP}+\mathrm{FP})$，召回 $R=\mathrm{TP}/(\mathrm{TP}+\mathrm{FN})$。分母是预测框数或真值框数，不是图像数。

匹配：预测框与真值框 IoU 不低于阈值才算 TP。本项目协议对比常用 IoU $=0.5$。小目标召回的分母是小真值框数。

置信区间：点估计 $\hat\theta$，区间 $[\hat\theta-c,\hat\theta+c]$。$c$ 由样本量和方差来。区间不含 0，才说两方法差异在该水平上可分辨。它不是业务期限。

## 查阅

假设检验全表、Bootstrap：知道「用重采样估计区间」即可。p 值小只表示在该假设下数据少见，不是效应大。
