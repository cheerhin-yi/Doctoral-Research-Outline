# Paper 1文献工作区

## 主题目录

| 主题 | 文件夹 | 主要回答的问题 | 对应论文主张 |
|---|---|---|---|
| T1 铁路UAV与小目标检测 | [01_Railway_UAV_Detection](01_Railway_UAV_Detection/Reading_List.md) | YOLO在铁路UAV中真正的瓶颈是什么？ | C1的已知检测基础 |
| T2 开放环境目标检测 | [02_Open_World_Detection](02_Open_World_Detection/Reading_List.md) | 如何发现训练类别之外的候选并控制误报？ | C1的未知路径 |
| T3 轨道上下文与风险 | [03_Track_Context_and_Risk](03_Track_Context_and_Risk/Reading_List.md) | 如何把候选转成有任务意义的侵界告警？ | C2 |
| T4 不确定性与评价 | [04_Uncertainty_and_Evaluation](04_Uncertainty_and_Evaluation/Reading_List.md) | 如何评价概率可靠性、告警预算和实验可信度？ | C1/C2支撑 |

## 文件作用

- [Literature_Matrix.md](Literature_Matrix.md)：所有核心论文的主题索引、证据摘要和新颖性冲突；
- [Search_Log.md](Search_Log.md)：保存数据库、检索式、日期和筛选结果；
- [Paper_Note_Template.md](Paper_Note_Template.md)：复制到对应主题目录，用于单篇精读；
- 各主题`Reading_List.md`：管理该主题的阅读顺序、优先级和笔记文件。

## 新增一篇论文的流程

1. 在`Search_Log.md`记录本次检索；
2. 判断主主题，分配唯一ID：T1-xx、T2-xx、T3-xx或T4-xx；
3. 在对应`Reading_List.md`登记；
4. 复制模板到主题目录，命名为`ID_第一作者_年份_短标题.md`；
5. 核验标题、作者、年份、出处、DOI/URL；
6. 精读后把关键证据和冲突结论写回主矩阵；
7. 同一论文跨主题时只建立一份主笔记，在其他主题清单中引用该文件，避免重复。

## 阅读状态

- `TODO`：已发现，尚未核验；
- `SCREENED`：标题、摘要和元数据已核验；
- `READING`：正在精读；
- `DONE`：方法、数据、结果、局限和与Paper 1关系均已记录；
- `EXCLUDED`：与研究问题无直接关系，保留排除理由。

正式写入论文参考文献前，优先使用DOI或出版商页面核验元数据；预印本若已有正式发表版本，应更新为正式版本。
