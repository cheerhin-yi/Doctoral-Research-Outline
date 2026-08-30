# Markdown数学公式写法

_适用于本项目的Markdown学习笔记、研究计划、实验记录和论文草稿。_

---

## 基本规则

本项目统一使用GitHub可渲染的LaTeX数学语法：行内公式使用一对美元符号，独立公式使用两对美元符号。GitHub使用MathJax渲染Markdown中的数学表达式，并同时支持`math`代码块。[^1]

### 行内公式

源码：

```markdown
当预测概率为 $p_i$、真实标签为 $y_i$ 时，计算单样本误差。
```

显示：当预测概率为 $p_i$、真实标签为 $y_i$ 时，计算单样本误差。

### 独立公式

源码：

```markdown
$$
\operatorname{Precision}=\frac{TP}{TP+FP}
$$
```

显示：

$$
\operatorname{Precision}=\frac{TP}{TP+FP}
$$

### `math`代码块

GitHub也支持下面的写法，但本项目优先使用`$$...$$`，以便与常用Markdown编辑器保持一致。

````markdown
```math
\operatorname{Recall}=\frac{TP}{TP+FN}
```
````

## 常用语法

| 目的 | Markdown/LaTeX源码 | 显示效果 |
|---|---|---|
| 下标 | `$x_i$` | $x_i$ |
| 多字符下标 | `$AP_{\mathrm{small}}$` | $AP_{\mathrm{small}}$ |
| 上标 | `$x^2$` | $x^2$ |
| 分数 | `$\frac{a}{b}$` | $\frac{a}{b}$ |
| 平方根 | `$\sqrt{x}$` | $\sqrt{x}$ |
| $n$次根 | `$\sqrt[n]{x}$` | $\sqrt[n]{x}$ |
| 绝对值 | `$|x|$` | $|x|$ |
| 范数 | `$\lVert\mathbf{x}\rVert_2$` | $\lVert\mathbf{x}\rVert_2$ |
| 求和 | `$\sum_{i=1}^{n}x_i$` | $\sum_{i=1}^{n}x_i$ |
| 积分 | `$\int_a^b f(x)\,\mathrm{d}x$` | $\int_a^b f(x)\,\mathrm{d}x$ |
| 极限 | `$\lim_{x\to0}f(x)$` | $\lim_{x\to0}f(x)$ |
| 近似 | `$a\approx b$` | $a\approx b$ |
| 不等式 | `$0\le p\le1$` | $0\le p\le1$ |
| 属于 | `$y_i\in\{0,1\}$` | $y_i\in\{0,1\}$ |
| 期望 | `$\mathbb{E}[X]$` | $\mathbb{E}[X]$ |
| 概率 | `$\Pr(Y=1\mid X=x)$` | $\Pr(Y=1\mid X=x)$ |
| 向量 | `$\mathbf{x}$` | $\mathbf{x}$ |
| 矩阵 | `$\mathbf{A}$` | $\mathbf{A}$ |

## 希腊字母与常用符号

| 名称 | 源码 | 显示 | 名称 | 源码 | 显示 |
|---|---|---|---|---|---|
| alpha | `$\alpha$` | $\alpha$ | beta | `$\beta$` | $\beta$ |
| gamma | `$\gamma$` | $\gamma$ | delta | `$\delta$` | $\delta$ |
| lambda | `$\lambda$` | $\lambda$ | mu | `$\mu$` | $\mu$ |
| sigma | `$\sigma$` | $\sigma$ | tau | `$\tau$` | $\tau$ |
| 大写Sigma | `$\Sigma$` | $\Sigma$ | epsilon | `$\varepsilon$` | $\varepsilon$ |
| 无穷 | `$\infty$` | $\infty$ | 正负 | `$\pm$` | $\pm$ |
| 乘号 | `$\times$` | $\times$ | 点乘 | `$\cdot$` | $\cdot$ |
| 交集 | `$A\cap B$` | $A\cap B$ | 并集 | `$A\cup B$` | $A\cup B$ |

## 多行公式

### 对齐等式

源码：

```markdown
$$
\begin{aligned}
P_{\mathrm{conv}} &= K^2C_{\mathrm{in}}C_{\mathrm{out}},\\
P_{\mathrm{dw}} &= K^2C_{\mathrm{in}},\\
P_{\mathrm{pw}} &= C_{\mathrm{in}}C_{\mathrm{out}}.
\end{aligned}
$$
```

显示：

$$
\begin{aligned}
P_{\mathrm{conv}} &= K^2C_{\mathrm{in}}C_{\mathrm{out}},\\
P_{\mathrm{dw}} &= K^2C_{\mathrm{in}},\\
P_{\mathrm{pw}} &= C_{\mathrm{in}}C_{\mathrm{out}}.
\end{aligned}
$$

### 分段函数

```markdown
$$
f(x)=
\begin{cases}
1, & x\ge\tau,\\
0, & x<\tau.
\end{cases}
$$
```

$$
f(x)=
\begin{cases}
1, & x\ge\tau,\\
0, & x<\tau.
\end{cases}
$$

### 矩阵

```markdown
$$
\mathbf{K}=
\begin{bmatrix}
f_x & 0 & c_x\\
0 & f_y & c_y\\
0 & 0 & 1
\end{bmatrix}
$$
```

$$
\mathbf{K}=
\begin{bmatrix}
f_x & 0 & c_x\\
0 & f_y & c_y\\
0 & 0 & 1
\end{bmatrix}
$$

## 本项目常用公式模板

以下公式是写法模板，不代表各论文已经完成或必须使用这些方法。

### 目标检测

$$
\operatorname{IoU}(B_p,B_g)
=
\frac{|B_p\cap B_g|}{|B_p\cup B_g|}
$$

$$
\operatorname{Precision}=\frac{TP}{TP+FP},
\qquad
\operatorname{Recall}=\frac{TP}{TP+FN}
$$

$$
F_1
=
\frac{2\,\operatorname{Precision}\,\operatorname{Recall}}
{\operatorname{Precision}+\operatorname{Recall}}
$$

### 均值与标准差

$$
\bar{x}=\frac{1}{n}\sum_{i=1}^{n}x_i,
\qquad
s=\sqrt{\frac{1}{n-1}\sum_{i=1}^{n}(x_i-\bar{x})^2}
$$

### 模型效率

$$
\operatorname{FPS}=\frac{1000}{t_{\mathrm{ms}}}
$$

$$
R_{\mathrm{reduction}}
=
\frac{Q_{\mathrm{base}}-Q_{\mathrm{new}}}{Q_{\mathrm{base}}}\times100\%
$$

其中，$Q$可以表示参数量、GFLOPs或延迟，但不同量不能混在同一个下降比例中。

### 相机投影

$$
s
\begin{bmatrix}
u\\v\\1
\end{bmatrix}
=
\mathbf{K}
\begin{bmatrix}
\mathbf{R} & \mathbf{t}
\end{bmatrix}
\begin{bmatrix}
X\\Y\\Z\\1
\end{bmatrix}
$$

其中，$(X,Y,Z)$为三维点，$(u,v)$为像素坐标，$\mathbf{K}$为相机内参，$\mathbf{R}$和$\mathbf{t}$为外参。

### 通信

$$
\operatorname{SNR}=\frac{P_s}{P_n}
$$

$$
C=B\log_2\left(1+\operatorname{SNR}\right)
$$

其中，$B$为带宽，$C$为理想信道容量模板。实际论文使用前必须重新核验信道假设。

### 优化与决策

$$
\min_{\mathbf{x}}\; f(\mathbf{x})
\quad
\text{s.t.}\quad
g_j(\mathbf{x})\le0,
\quad j=1,\ldots,m
$$

$$
J(\pi)
=
\mathbb{E}_{\pi}
\left[
\sum_{t=0}^{T}\gamma^t r_t
\right]
$$

## 公式中的文字、单位与变量

- 多字符说明使用正体：`$AP_{\mathrm{small}}$`显示为$AP_{\mathrm{small}}$
- 数学变量使用斜体：`$x_i$`显示为$x_i$
- 向量和矩阵使用粗体：`$\mathbf{x}$`、`$\mathbf{K}$`
- 函数名使用正体：`$\operatorname{IoU}$`、`$\log$`、`$\exp$`
- 微分符号使用正体：`$\mathrm{d}x$`
- 单位放在数学环境外，或使用正体：`$t=25\,\mathrm{ms}$`
- 百分号在公式中需要转义：`$15\%$`
- 中文说明尽量放在公式外，避免不同渲染器字体不一致

## 常见错误

| 错误写法 | 问题 | 推荐写法 |
|---|---|---|
| `\[x+y\]` | 部分Markdown编辑器不渲染 | `$$x+y$$` |
| `$AP_small$` | 只有首个字符成为下标 | `$AP_{\mathrm{small}}$` |
| `$x*100%$` | 星号和百分号可能解释错误 | `$x\times100\%$` |
| `$sin(x)$` | 函数名被当作变量连乘 | `$\sin(x)$` |
| `$||x||$` | 范数括号大小和间距不稳定 | `$\lVert x\rVert$` |
| 公式紧贴中文标点 | 阅读和渲染不稳定 | 行内公式后再写中文标点 |
| 在代码块内期待公式渲染 | 普通代码块只显示源码 | 使用`$...$`、`$$...$$`或`math`代码块 |

## 提交前检查

- [ ] 行内公式使用`$...$`
- [ ] 独立公式使用`$$...$$`
- [ ] 每个左括号、花括号和数学定界符都有对应闭合
- [ ] 多字符下标使用花括号和`\mathrm{}`
- [ ] 百分号写成`\%`
- [ ] 矩阵、多行等式和分段函数在GitHub预览中正常
- [ ] 公式后解释所有首次出现的变量和单位
- [ ] 不把近似公式写成严格定义
- [ ] 不在表格单元格中放大型独立公式

## 参考

[^1]: GitHub. “Writing mathematical expressions.” GitHub Docs. https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions
