# papers/<PaperID>/ 实验槽模板

```text
00_freeze/
01_<main_dataset>/
  data/          # summary.json, 主 CSV 仅终跑
02_stats/        # 可选
03_cross_*/      # 可选
04_timing/       # 可选；不同 GPU 分表
05_packaging/    # 投稿表、失败例、复现附录
README.md        # 主张 + 目录说明
```

禁止：过程诊断 MD 堆根目录；禁止提交 raw 预测张量除非审稿硬性要求（默认不提交）。
