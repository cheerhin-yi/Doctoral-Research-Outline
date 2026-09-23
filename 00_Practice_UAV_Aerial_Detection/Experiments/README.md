# Experiments（论文实验区）

> 规则（强制）：按 **论文槽位** 组织：`papers/<PaperID>/`。  
> 根目录禁止堆积脚本、诊断 MD、notebook、预测缓存。  
> 当前活跃：`papers/P0_EI/`。

## 目录层级

```text
Experiments/
  README.md
  00_Index.md
  _templates/
  papers/
    P0_EI/
      00_freeze/
      01_visdrone_main/
      02_paired_stats/
      03_cross_uavdt/
      04_timing/
      05_packaging/
```

## 每篇论文实验槽最低要求

| 子目录 | 放什么 |
|---|---|
| `00_freeze/` | 权重哈希、环境、类别映射、方法定义 |
| `01_*_main/` | 主数据集终评报告 + `data/summary.json` 等 |
| `02_stats/` | 统计检验（若有） |
| `03_cross_*` / `04_timing/` / `05_packaging/` | 按主张增减；命名保持语义清晰 |

## 明确删除/迁出的类型（本清理已执行）

- BT1 / BTD* 训练与诊断过程文、A0 可行性长文、根目录分析脚本与 notebook  
- `P0_Benchmark/**/preds/*.npy`、smoke 跑、Ultralytics cache、`__pycache__`  
- 解释性选包指南、已撤销训练轨长文  

上述内容在：`_Archive_20260923_PreP0_Cleanup/Experiments/`。
