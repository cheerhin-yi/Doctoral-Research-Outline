# 09 跨集外推、类别映射冻结与近邻推理技术（P0 EI）

> 关卡：L3 补强／L4 前置｜过关只查**第二部分**｜[`../Learning_Check_Baseline.md`](../Learning_Check_Baseline.md)  
> 对齐：Stage E（UAVDT）PASS、类别映射 FROZEN、EI 稿「双集证据／不可写通论排序」纪律  
> 权威入口：[`../../00_Overview/Current_Stage.md`](../../00_Overview/Current_Stage.md)

---

## 第一部分：必须掌握

### 学习目标

1. 能说明为何 **VisDrone 训好的冻结权重**接到 UAVDT 时，必须先锁 **类别映射**，且 **看分后不得回改映射**。
2. 能区分：域偏移（domain shift）、协议效应（inference protocol effect）、映射伪效应（label-map artifact）。
3. 能把近邻文献技术（多分辨率推理、密度/均匀切片、SAHI 类切片流水线）映射到本篇五方法，并说清 **本篇不声称发明这些算子**。
4. 能写清：双集上允许的主张句 vs 禁止的「通论五方法排序」句。

### 知识链

```text
冻结权重 last.pt（SHA 固定）
→ 预注册 VisDrone→UAVDT 类别映射（FROZEN）
→ 同一五协议在 UAVDT 上推理
→ VisDrone 兼容匹配器评价（非官方 MATLAB AP）
→ 与 Stage D 对照：趋势一致处 / 排序不一致处
→ 主张边界：协议改变权衡；禁止写跨集通论冠军
→ 近邻技术词表（related work）如何诚实引用
```

### 名词与近邻技术（写 EI Related Work / Method 要用）

| 术语 | 含义（本篇口径） | 本篇落点 |
|---|---|---|
| Inference protocol | 不改权重、只改推理时的输入尺度/切片/融合规则 | 五方法全体 |
| Multi-resolution inference | 同一模型多输入分辨率（如 640 vs 1280） | F640 / F1280 |
| Tiling / cropping inference | 大图切块再检、坐标还原后融合 | DensK1 / UnifAll / SAHI640 |
| Density-guided tile | 用密度或 saliency 选「值得加精」的块（非 GT oracle） | DensK1 |
| Uniform tiling | 规则网格全覆盖 | UnifAll |
| SAHI | Slicing Aided Hyper Inference：工程化切片+重叠+合并 | SAHI640 |
| Soft-NMS / merge-NMS | 切片结果在原图空间去重融合 | 切片类方法的后处理 |
| Domain shift | 训练域（VisDrone）与测试域（UAVDT）分布差 | Stage E 必要性 |
| Class mapping freeze | 跨集类别对齐表在看结果前锁定 | Stage E 门禁 |
| Small-object criterion | 原图像素面积阈值（本项目：0 < w×h < 1024） | D/E/F 共性 |
| Rank instability | 方法名次跨集不完全相同 | 禁止通论排序的证据 |

**不是本篇 novelty、但必须会引用的方向（知名词即可，不要求实现）：**

- 面向航拍小目标的专用检测头 / 超分辨率增强 / 拷贝粘贴增广（多为 **训练期** 方法；本篇冻结权重，只作 related work 对照）。
- Query-based / DETR 系航拍检测、多帧时序检测（超出本篇单帧协议对比边界）。
- 官方 UAVDT MATLAB 评测协议（本篇用 VisDrone 兼容匹配器；文中必须披露差异）。

### 链上要点

1. **映射先于分数。** Stage E 纪律：映射表与 ignore 规则写进 Run 配置后才准推理；任何「看完 small_recall 再改映射」都是不可发表的数据窥探。
2. **双集角色。** VisDrone test-dev（D/F）= 主精度与配对推断；UAVDT（E）= 外推与稳健性，不是第二套调参场。
3. **一致 vs 不一致都要写。** 例：F640 两端都最弱、抬分辨率/切片抬召回并付精度或时间代价 = 可写的稳健趋势；五方法名次不完全同序 = 必须写进讨论，用来挡住「通论排序」。
4. **评价器披露。** 「VisDrone 兼容匹配 + 映射后类别」≠「UAVDT 官方 AP」。EI 方法节或附录写清。
5. **Related work 诚实句模板：** 「本工作采用与 SAHI / 多分辨率推理同族的 **推理协议轴**，在 **冻结检测器** 上系统比较；不提出新骨干或新损失。」

### 与五方法的对应（磁盘名以 Tracker / `summary.json` 为准）

| 协议（文稿常用） | 技术族 | 主要换取 | 主要代价 |
|---|---|---|---|
| F640 | 整图低分辨 | 快 | 小目标易丢 |
| F1280 | 整图高分辨 | 有效分辨率↑ | 算力↑ |
| DensK1 | 密度引导单片+底图 | 局部加精 | 选区失误→漏检 |
| UnifAll | 均匀全覆盖 | 覆盖全 | 延迟高 |
| SAHI640 | SAHI 切片协议 | 工程化切片 | 延迟很高 |

### 练习

1. 写出「映射伪效应」一例：某 UAVDT 类被错误并入 VisDrone 类后，某方法 small_recall 虚高。说明为何冻结映射能挡住这类故事。
2. 对照 Stage D 与 Stage E 的 small_recall 排序，列出：跨集一致的一条趋势、不一致的一条名次变化；各写一句可进讨论的表述。
3. 为 Related Work 列 4 个必须出现的关键词（英文可），并各用半句话说明本篇如何 **用而不冒充发明**。

### 必答题

1. 为什么 Stage E 的主贡献不是「在 UAVDT 上刷更高 AP」，而是服务 EI 主张边界？
2. 若审稿人要求改用官方 UAVDT MATLAB API，你最少要改论文的哪三处披露？本篇实验是否必须立刻重跑？（先答原则，不擅自开跑。）
3. 「F1280 在两集都不是最慢却召回很高」能否改写成「F1280 是无人机场景默认最优协议」？为什么？

---

## 第二部分：我的记录

> 先闭卷写，再对第一部分。保留初稿；订正另起一行。助手不代填。

### 元信息

| 字段 | 填写 |
|---|---|
| 开始日期 | |
| 状态 | `TODO` / `LEARNING` / `REVIEWING` / `PASSED` / `REPEAT` |

### 闭卷串讲（按知识链）

```text
冻结权重 → 映射冻结 → 五协议×UAVDT → 兼容评价 → 与 D 对照 → 主张边界 → related work 词表
```

- 我的复述：

### 练习证据

| 练习 | 证据位置 | 摘要 |
|---|---|---|
| 映射伪效应 | | |
| 跨集一致/不一致 | | |
| Related Work 关键词 | | |

### 必答初稿

1.
2.
3.

### 订正（如有）

-

### 仍不确定

-

### 助手检查区

| 判定 | 缺口 | 日期 |
|---|---|---|
| | | |
