# Literature（论文文献区）

> 规则（强制）：本目录**只**按「论文槽位」组织。每篇待投/在写论文一个子目录：`papers/<PaperID>/`。  
> 禁止把过程性长审计、候选路线评审、搜索流水账堆在根目录。  
> 当前唯一活跃槽位：`papers/P0_EI/`（冻结权重推理协议对比，EI 会议稿）。

## 目录层级

```text
Literature/
  README.md                 ← 本规则
  00_Index.md               ← 全部论文槽位总表
  _templates/               ← 新开论文时复制
  papers/
    P0_EI/
      README.md
      related_work_matrix.md
      notes/                ← 与本篇 related work 直接相关的篇级笔记
```

## 准入 / 不准入

| 准入 | 不准入 |
|---|---|
| 本篇拟引用或对照的文献笔记 | 已否决候选方法的长评审 |
| 一篇一篇的对比矩阵（短） | 与当前主张无关的数据集专项审计流水 |
| 检索结论摘要（可附在 matrix） | 重复的过程日志 |

历史材料已迁至：`_Archive_20260923_PreP0_Cleanup/Literature/`（不参与正文写作）。
