# P0_EI 实验槽（论文证据唯一入口）

## 主张

冻结 VisDrone 训练权重，比较五推理协议（F640 / F1280 / DensK1 / UnifAll / SAHI640）在航拍小目标上的召回–精度–代价；VisDrone 主评 + UAVDT 外推；图级配对统计。

## 层级

```text
papers/P0_EI/
  00_freeze/          权重 SHA、环境、映射、协议定义
  01_visdrone_main/   Stage C/D 主精度（含 data/）
  02_paired_stats/    Stage F
  03_cross_uavdt/     Stage E
  04_timing/          Stage B（1660）；4090 另表
  05_packaging/       近邻表 / 失败例 / 复现附录
```

## 纪律

1. **只留论文要用的报告 + 汇总表/CSV/JSON。** 不收 raw `.npy` 预测、smoke 跑、过程诊断长文。  
2. 新跑必须带 Run ID，终态只把 `summary` / 主 CSV 拷入对应 `data/`。  
3. 禁止在本槽恢复 BT/BTD 训练诊断叙事。  
4. 原始大文件若需备份，放仓库外或 `_Archive_*`，不要进 `papers/`。
