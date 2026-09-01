# 练手论文文献工作区

当前已将用户提供的9篇候选原文按主题归档，并完成题名、摘要、方法概述和结论层面的初筛。`SCREENED`不等于精读或可直接引用；阶段2仍需补做系统检索、元数据核验和单篇证据笔记。

全项目阅读顺序与跨论文边界见[已归档论文阅读指南](../../00_Overview/Paper_Reading_Guide.md)。

## 主题目录

| 主题 | 文件夹 | 主要回答的问题 | 对应论文主张 |
|---|---|---|---|
| L1 小目标与多尺度 | [01_Small_Object_and_Multiscale](01_Small_Object_and_Multiscale/Reading_List.md) | P2和尺度重配置何时真正改善小目标检测？ | C0-1 |
| L2 轻量共享检测头 | [02_Lightweight_Shared_Head](02_Lightweight_Shared_Head/Reading_List.md) | 参数共享与轻量卷积是否已有同构方法？ | C0-1 |
| L3 效率与部署 | [03_Efficiency_and_Deployment](03_Efficiency_and_Deployment/Reading_List.md) | 理论复杂度能否转化为真实延迟收益？ | C0-2 |
| L4 评价与可复现性 | [04_Evaluation_and_Reproducibility](04_Evaluation_and_Reproducibility/Reading_List.md) | 小目标、遮挡和速度如何公平评价？ | C0-1/C0-2支撑 |

## 文件作用

- [Literature_Matrix.md](Literature_Matrix.md)：所有核心论文的主题索引、证据摘要和新颖性冲突；
- [Search_Log.md](Search_Log.md)：保存数据库、检索式、日期和筛选结果；
- [Paper_Note_Template.md](Paper_Note_Template.md)：复制到对应主题目录，用于单篇精读；
- 各主题`Reading_List.md`：管理该主题的阅读顺序、优先级和笔记文件。

## 新增一篇论文的流程

1. 在`Search_Log.md`记录本次检索；
2. 判断主主题，分配唯一ID：L1-xx、L2-xx、L3-xx或L4-xx；
3. 在对应`Reading_List.md`登记；
4. 复制模板到主题目录，命名为`ID_第一作者_年份_短标题.md`；
5. 通过出版方或论文原文核验作者、年份、方法、数据和结果；
6. 精读后把关键证据和冲突结论写回主矩阵；
7. 同一论文跨主题时只建立一份主笔记，在其他主题清单中引用，避免重复。

每篇重点记录“新增了什么、是否与LSM-Head同构、用了什么公平基线、是否测真实延迟”。查新完成前，不冻结“新颖”或“首次”表述。本目录不收开放世界、铁路风险、通信、三维、多模态、强化学习或多无人机文献。
