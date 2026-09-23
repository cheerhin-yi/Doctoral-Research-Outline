# Mermaid画图语法指南

_这里只保留完成本项目知识链、结构、流程和分支图最常用的少量语法；需要什么就查什么，不按比例学习。_

---

## 🎯 最小使用方法

Mermaid代码放在Markdown代码块中：


```mermaid
flowchart LR
    start[开始] --> finish[完成]
```


- `flowchart LR`：从左到右
- `flowchart TB`：从上到下
- 节点ID使用英文或拼音，如`input_image`
- 方括号中的文字是图上显示的内容
- 每行写一条连接，先画主链，再补分支

## 📚 常用节点与连线

```mermaid
flowchart LR
    accTitle: Mermaid常用节点
    accDescr: 展示开始、处理、判断、数据和结束节点，以及实线、带文字连线和虚线连接。

    start_node([开始]) --> process_node[处理步骤]
    process_node --> decision_node{是否满足条件}
    decision_node -->|是| data_node[(数据或记录)]
    decision_node -.->|否| revise_node[返回修正]
    revise_node --> process_node
    data_node --> finish_node([完成])
```

| 用途 | 写法 |
|---|---|
| 普通步骤 | `step[处理步骤]` |
| 开始或结束 | `start_node([开始])` |
| 判断 | `decision{是否满足}` |
| 数据或记录 | `data[(实验记录)]` |
| 实线箭头 | `a --> b` |
| 带文字箭头 | `a -->|输出| b` |
| 虚线关系 | `a -.-> b` |
| 无箭头连接 | `a --- b` |

## 🔗 知识链模板

```mermaid
flowchart LR
    accTitle: 主题知识链
    accDescr: 从学习前提经过核心机制、输出和评价，最终连接到失败分析与项目决策。

    input[输入或前提] --> mechanism[核心机制]
    mechanism --> output[产生的输出]
    output --> evaluation[怎样评价]
    evaluation --> failure[可能失败]
    failure --> decision[项目中的决策]

    classDef core fill:#dbeafe,stroke:#2563eb,stroke-width:2px,color:#1e3a5f
    classDef evidence fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#14532d
    classDef risk fill:#fef9c3,stroke:#ca8a04,stroke-width:2px,color:#713f12

    class input,mechanism,output core
    class evaluation,decision evidence
    class failure risk
```

## 🗂️ 分组与分支模板

```mermaid
flowchart TB
    accTitle: 训练与推理分支
    accDescr: 共同前向过程在模型输出后分别进入训练和推理两条处理分支。

    input[输入] --> forward[模型前向]

    subgraph training_branch ["训练分支"]
        target[(真值)] --> loss[计算损失]
        forward --> loss
        loss --> update[更新参数]
    end

    subgraph inference_branch ["推理分支"]
        forward --> postprocess[后处理]
        postprocess --> prediction[最终预测]
    end
```

## ⚙️ 让图更清楚

- 换行：`node[第一行<br/>第二行]`
- 连线命名：`a -->|特征| b`
- 节点分类：先写`classDef`，再写`class node_id class_name`
- 注释：`%% 这一行不会显示`
- 复杂图拆成“总览图＋局部图”

每张支持可访问性字段的图建议加入：

```text
accTitle: 3到8个词的图名
accDescr: 一句话说明这张图展示什么关系
```

不要使用`%%{init}`主题指令或`style node ...`内联样式；需要颜色时使用`classDef`。

## ✍️ 其他常用图类型

### 时序交互

```mermaid
sequenceDiagram
    accTitle: 简单交互顺序
    accDescr: 学习者依次检查代码输出并把证据保存到实验记录。

    participant learner as 学习者
    participant code as 代码
    participant record as 实验记录
    learner->>code: 检查实现
    code-->>learner: 返回输出
    learner->>record: 保存证据
```

### 状态变化

```mermaid
stateDiagram-v2
    accTitle: 笔记状态变化
    accDescr: 笔记从待学习经过记录和验证后进入完成状态，验证失败时返回补充。

    [*] --> 待学习
    待学习 --> 记录中
    记录中 --> 待验证
    待验证 --> 已完成
    待验证 --> 记录中
```

## 🚫 常见错误

- 节点ID含空格：错误`input image`，正确`input_image`
- 把保留字`end`直接作为节点ID
- 一张图节点过多仍不分组
- 用很长的句子作为节点文字
- 只靠颜色表达含义
- 代码块没有写语言标识`mermaid`

## 🔍 怎么检查

1. 先只画3—6个节点的主链
2. 确认能渲染后再增加分支
3. 检查箭头是否表达因果或数据流
4. 检查每个节点是否能在正文找到解释
5. 可粘贴到[Mermaid Live Editor][mermaid-live]预览

[mermaid-live]: https://mermaid.live/ "Mermaid Live Editor"
