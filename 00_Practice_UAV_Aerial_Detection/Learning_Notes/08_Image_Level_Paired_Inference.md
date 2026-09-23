# 08 图级配对推断（Stage F 配套）

> 关卡：L3 强相关／L4 前置｜过关只查**第二部分**  
> 对齐产物：`Experiments/papers/P0_EI_StageF_Paired_Stats_Report.md`（Run `P0-BENCH-F-TESTDEV-20260917-01`）

---

## 第一部分：必须掌握

### 学习目标

1. 能说明为何主检验用**配对**（同一 image_id 上两方法）。
2. 能解释 Wilcoxon 符号秩用于 `recall_small` 差；`small_gt=0` 的图为何剔除。
3. 能读懂配对 bootstrap 的 Δ 与 95% CI，并写成不夸大的论文句。
4. 知悉 Holm 校正用于**次要成对比较**；主比较可报原始 p，但需在文中声明。

### 知识链

```text
Stage D per_image_metrics
→ 按 image 对齐两方法
→ 过滤 undefined recall_small
→ 配对差分
→ Wilcoxon（位置） + bootstrap CI（效应）
→ Holm（多比较，次要对）
→ 主张句（C1）
```

### 链上要点

1. **单元是图。** N≈1610 图；有小目标 GT 的配对 Wilcoxon N=1499（以报告为准）。
2. **效应量优先于「星号」。** CI 是否跨 0 直接约束 C1 措辞。
3. **主结果摘要（已冻结，只读）：** F1280 vs DensK1，Δrecall_small≈+0.0409，95% CI [0.0355, 0.0462]，不过 0；Wilcoxon p≈3e-28。精度 Δ 同向为正；延迟近似持平（1660SUPER，one-shot）。
4. **不得：** 看见 p 很小就写「证明 DensK1 无价值」——UnifAll 召回仍可更高但更慢；叙事是预算下的权衡。

### 练习

1. 用自己的话解释：bootstrap 重采样的是**图**，还是框？
2. 若 CI 为 [-0.01, 0.02]，对 C1 应如何改口？
3. 列出 Stage F 报告里主比较之外你准备在附录保留的次要对（至少 2 个）。

### 必答题

1. 为什么 median Δ=0 仍可能得到极小的 Wilcoxon p？
2. Holm 校正若不做，读者可能怎样误读次要对？
3. 把 Stage F 的 CI 与 Stage D 排序一起写进「结果」段时，最低限度要披露哪三件硬件/协议事实？

---

## 第二部分：我的记录

### 元信息

| 字段 | 填写 |
|---|---|
| 开始日期 | |
| 状态 | `TODO` / `LEARNING` / `REVIEWING` / `PASSED` / `REPEAT` |

### 闭卷串讲

- 我的复述：

### 练习证据 / 必答初稿 / 订正 / 助手检查区

-
