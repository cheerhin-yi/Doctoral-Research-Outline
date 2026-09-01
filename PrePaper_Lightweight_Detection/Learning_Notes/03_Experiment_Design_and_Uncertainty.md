# 学习笔记3：实验设计、统计与不确定性

## 为什么服务本练手论文

实验设计是本论文判断检测头改动是否有效的底层能力。这里用它排除数据泄漏、更多参数、不同训练设置和计时条件造成的假收益；Paper 1另有自己的独立笔记和案例。

## 一条实验必须包含什么

每个实验先填写：

| 字段 | 要回答的问题 |
|---|---|
| Claim | 这个实验要改变审稿人对哪个主张的判断？ |
| Hypothesis | 预期发生什么？ |
| Independent Variable | 唯一主动改变什么？ |
| Control | 哪些条件必须相同？ |
| Baseline | 最强且公平的比较对象是什么？ |
| Split | 用什么数据划分，如何防止泄漏？ |
| Metrics | 哪个指标直接决定主张？ |
| Success Criterion | 什么结果才值得保留方法？ |
| Failure Interpretation | 负结果意味着删除、缩小还是换问题？ |
| Output | 最终进入哪张表或图？ |

## 练手论文示例

问题：加入P2检测尺度是否改善公开航拍图像的小目标检测？

- Hypothesis：更高输入分辨率提高小目标Recall；
- Independent Variable：是否加入P2检测尺度；
- Control：同一输入尺寸、YOLO规模、数据split、epoch、增强、预训练、seed和评价代码；
- Baseline：原始P3–P5检测头；
- Metrics：small-object Recall、mAP50–95、FPS和显存；
- Success Criterion：Recall增益在关键场景方向一致，且计算代价可接受；
- Failure Interpretation：若仅增加计算而无稳定Recall收益，不再把普通P2作为有效改进；
- Anti-claim：收益不能归因于更多epoch或不同增强。

## 数据划分与泄漏

本论文优先使用官方划分，并审计连续序列、同源图像和派生样本。以下情况属于泄漏：

- 相邻视频帧跨训练和测试；
- 原图在训练、裁剪图在测试；
- 同一布置重复拍摄跨集合；
- 同一原图的裁剪、增强或重编码版本跨集合；
- 使用测试集选择阈值或校准参数。

## 重复性与统计

- 排错实验可用1个seed；
- 决定是否保留方法的核心结果尽量用3个seed；
- 报告均值、标准差或场景聚类置信区间；
- 统计显著不等于实际有用，还要报告Recall提升、告警减少和计算代价；
- 同一场景中的大量相邻帧不能被当作完全独立样本。

对 $n$ 个独立实验单位的结果 $x_1,\ldots,x_n$，样本均值和样本标准差为：

$$
\bar{x}=\frac{1}{n}\sum_{i=1}^{n}x_i,
\qquad
s=\sqrt{\frac{1}{n-1}\sum_{i=1}^{n}(x_i-\bar{x})^2}
$$

当独立性和分布假设合理时，均值的双侧置信区间可写为：

$$
\bar{x}\pm t_{1-\alpha/2,\,n-1}\frac{s}{\sqrt{n}}
$$

这里的 $n$ 必须对应独立场景、航次或独立训练运行，不能把相邻视频帧数直接代入。

## 不确定性与校准的最低知识

### 区分

- Aleatoric：观测噪声、模糊、遮挡等数据不确定性；
- Epistemic：模型没见过或知识不足；
- Confidence：模型输出分数，不自动等于真实概率；
- Calibration：预测为0.8的事件在长期统计中应约80%正确。

### 指标

- Reliability Diagram；
- Expected Calibration Error；
- Brier Score；
- NLL；
- top-k人工复核命中率。

将置信度划分为 $M$ 个区间 $B_1,\ldots,B_M$ 时，Expected Calibration Error可写为：

$$
\operatorname{ECE}
=
\sum_{m=1}^{M}\frac{|B_m|}{N}
\left|
\operatorname{acc}(B_m)-\operatorname{conf}(B_m)
\right|
$$

二分类情况下，Brier Score和Negative Log-Likelihood可写为：

$$
\operatorname{Brier}
=
\frac{1}{N}\sum_{i=1}^{N}(p_i-y_i)^2
$$

$$
\operatorname{NLL}
=
-\frac{1}{N}\sum_{i=1}^{N}
\left[y_i\log p_i+(1-y_i)\log(1-p_i)\right]
$$

其中，$p_i$是预测概率，$y_i\in\{0,1\}$是真实标签。多分类版本需对类别维度求和。

校准在本论文中默认只用于理解置信度可靠性，不作为核心方法或独立创新。

## 学习任务

- [ ] 为“加入P2检测尺度”写完整实验条目；
- [ ] 为“跨尺度参数共享”写一个删除实验；
- [ ] 写五种数据泄漏及检查方法；
- [ ] 解释为什么相邻帧不能直接计算普通置信区间；
- [ ] 画一张可靠性图并解释理想曲线；
- [ ] 写出一个结果显著但没有工程价值的例子。

## 暂时不学

- 高级贝叶斯深度学习；
- 大规模超参数优化；
- 多种校准算法竞赛；
- 复杂因果推断；
- 复杂因果模型或与本论文无关的评价环境。

## 学习记录区

### 1. 学习会话记录

| 日期 | 本次范围 | 使用资料 | 用时 | 完成证据 |
|---|---|---|---:|---|
|  |  |  |  |  |

### 2. 核心概念与实验预注册练习

| 字段 | 我的填写 |
|---|---|
| Claim |  |
| Hypothesis |  |
| Independent Variable |  |
| Control |  |
| Baseline |  |
| Split |  |
| Primary Metric |  |
| Success Criterion |  |
| Failure Interpretation |  |

### 3. 泄漏、统计与公平性记录

| 风险/反解释 | 检查方法 | 当前例子 | 是否已理解 |
|---|---|---|---|
| 数据泄漏 |  |  | 否 |
| 更多参数/计算 |  |  | 否 |
| 单一seed偶然性 |  |  | 否 |
| 相邻帧伪独立 |  |  | 否 |
| 测试集调参 |  |  | 否 |

### 4. 不确定性与校准笔记

| 概念/指标 | 我的解释 | 能支持的结论 | 不能支持的结论 |
|---|---|---|---|
| Aleatoric/Epistemic |  |  |  |
| Reliability Diagram |  |  |  |
| ECE |  |  |  |
| Brier/NLL |  |  |  |
| top-k复核命中率 |  |  |  |

### 5. 疑问与理解修正

| 原来的理解或疑问 | 实验/资料依据 | 修正后的理解 | 是否解决 |
|---|---|---|---|
|  |  |  |  | 否 |

### 6. 闭卷自测与总结

1. 怎样证明YOLO改动收益不是来自更多参数？
   我的回答：
2. 验证集和测试集在阈值选择中分别扮演什么角色？
   我的回答：
3. 为什么3个seed仍不能替代场景独立测试？
   我的回答：
4. ECE下降但AP_small和Recall_small不变，能支持什么主张？
   我的回答：
5. 一个负结果应如何改变论文计划？
   我的回答：

- 不看资料写出的三句话总结：
- 我识别出的最大实验风险：
- 本轮是否通过：否
- 下一次只做什么：
