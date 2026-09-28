
# 精读笔记：{{citekey}}

## 题目

{{title}}

## 作者 / 年 / Venue

{% for c in creators %}{{c.lastName}}{% if not loop.last %}, {% endif %}{% endfor %} / {{date | format("YYYY")}} / {{publicationTitle or proceedingsTitle or university}}

## DOI 或 arXiv

{% if DOI %}https://doi.org/{{DOI}}{% endif %}{% if extra %} {{extra}}{% endif %}

## Zotero

[打开条目]({{desktopURI}}) {% if pdfZoteroLink %}[打开 PDF]({{pdfZoteroLink}}){% endif %}

## 为什么读

## 问题

## 机制

输入 → 做什么 → 输出：

相对最笨做法多了哪一步：

## 数据

集合与划分：

标注 / 忽略规则：

预训练与泄漏：

## 实验

主表在比什么：

关键数字（方法，集合，指标，数值，表号）：

-

强简单基线：

消融或失败：

计时 / 硬件口径：

## 主张

1.
2.

作者承认的局限：

稿子暗示但没做的：

证据撑不撑主张：

## 可抄结构

章节顺序：

主表列名：

方法图块名：

## 对应关系

### 问题类型

### 主挂靠

### 次挂靠

### 关系

直接近邻 / 强基线 / 评价口径 / 反例 / 仅术语

### 新颖性冲突

None / Partial / Direct / Unknown

### 冲突理由

比问题、机制、协议、证据：

### 对已冻结主张的影响

无冻结则写无。

### 是否改边界

否 / 待核验 / 建议改哪一句

### 下一步

写回矩阵 / 可引用 / 要复现 / 暂缓 / skip

## 一句结论

## 未解决


{% persist "annotations" %} 
## 划线与批注

{% for a in annotations %}
- p.{{a.pageLabel}} {% if a.color %}({{a.color}}) {% endif %}{{a.annotatedText}} {% if a.comment %} 注：{{a.comment}} {% endif %}{% endfor %} {% endpersist %}