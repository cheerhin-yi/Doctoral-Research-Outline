# 08 航拍 SOD 封闭集基线与指标

> 关卡：**L3**。过关只查**第二部分**。  
> 纪律：YOLO / RT-DETR = **基线工具，非本篇贡献**；主贡献仍是数据+双审计。  
> 先修：`03` 忽略区/D5、`04` 原图尺度、`05` Technical Validation 角色。  
> **禁止：** 把 B 的告警预算/危险召回写进本篇主表。

---

## 第一部分：应知

### 学习目标

1. 能说明数据文 Technical Validation 里「同协议基线表」最少应固定哪些轴。  
2. 能把小目标/稀缺缺陷指标与 D0–D5、忽略区规则对齐。  
3. 能区分「基线证明数据可用」与「方法文刷 SOTA」。  
4. 能草拟空基线表表头，并写出合规 Validation 句。

### 知识链

```text
冻结 taxonomy 与 split
  → 选择封闭集检测器族（YOLO / RT-DETR…）
  → 同协议训练/评价设定
  → 主指标：mAP 等 + 稀缺缺陷 Recall 等（待冻结）
  → 小目标/原图像素协议（与视角笔记衔接）
  → 失败边界例（漏检模式）
  → 回链 Run ID（授权后）
  → 写入 Technical Validation（非 Related Work 吹牛）
```

---

### 术语表（CN / EN）

| 中文 | English | 一句话 |
|---|---|---|
| 封闭集检测 | closed-set detection | 类目冻结后的标准检测 |
| 同协议 | same protocol | 划分/忽略区/输入/NMS 等轴固定 |
| mAP | mean Average Precision | 常用检测综合指标 |
| 稀缺类召回 | rare-class recall | 真实稀缺缺陷上的召回 |
| NMS | non-maximum suppression | 抑制重叠框 |
| 输入尺度 | input size / imgsz | 网络喂入分辨率 |
| 原图尺度协议 | native-resolution protocol | 小目标定义回到原图像素 |

---

### 通俗讲解：基线是「压力测试数据」，不是「你的新发明」

#### 1. 为什么数据文也要跑 YOLO / RT-DETR

审稿人要看到：别人下载你的数据后，用常见检测器按你的协议能得到合理分数；失败模式可解释。  
你换成更新的检测器可以，但**换协议却不说明**会使表不可比。

#### 2. 同协议表轴（清单意识）

最少固定并披露：

1. 模型名与权重来源  
2. 输入尺寸与是否 letterbox  
3. 增强是否用于 val/test（通常否）  
4. 置信度阈值与 NMS  
5. 类别映射（part×defect → 训练类）  
6. split 哈希 / 场景隔离说明  
7. 硬件与随机种子  
8. 忽略区与 D5 是否计入  

未授权前：只学「表轴」，**不跑主 Run**。

#### 3. 小目标指标：不要照抄 VisDrone 当铁路标准

Practice 小目标笔记的思想可借鉴（原图尺度、召回口径），但铁路部件的「small」阈值要按本项目 GSD/像素协议冻结。  
**禁止：** 直接宣称「我们遵循 VisDrone small 定义故铁路科学」而不说明域差异。

#### 4. 与 D0–D5 的对齐

| 内容 | 建议 |
|---|---|
| D0 | 对照；是否单独训练负例按协议 |
| D1–D4 | 主表候选 |
| D5 | 不进主 mAP 或单独质量列 |
| 忽略区 | 不计入该区 TP/FP |

#### 5. 失败边界例（数据文需要）

强阴影弹条、砟掩埋、远端尺度断崖、板缝假裂纹：各给图例，证明你理解域，而不是只报总分。

#### 6. 合规 vs 违规 Validation 句

- 合规：「Under a fixed split and ignore-region protocol, YOLO11 and RT-DETR provide closed-set baselines confirming the benchmark is trainable.」  
- 违规：「We propose a novel detector that significantly outperforms SOTA and improves alarm recall under budget.」——前半抢方法贡献，后半属 B。

---

### 常见错误 / 禁止说法

| 禁止 | 改法 |
|---|---|
| 基线模型当 novelty | 写明工具角色 |
| 改忽略区抬 mAP 不披露 | 冻结并哈希协议 |
| 只报总体 mAP 藏稀缺类崩盘 | 并列稀缺 Recall |
| 告警 AUPRC 进 A 主表 | 删；留给 B |

---

### 练习

1. 草拟空基线表表头（列名即可）。  
2. 写一句合规 Validation 句、一句违规「更强检测器」句。  
3. 若仅真实稀缺类 Recall 很低、合成曲线却很高——主张如何并列披露。

### 必答题

1. 为什么基线模型本身通常不算 A 的 novelty？  
2. 忽略区定义改变却不披露时，mAP 比较会发生什么？  
3. Technical Validation 里最少要让读者复现哪三件事？

---

### 参考答案

#### 练习 1 参考

`model | weights | imgsz | conf | NMS | class map | split hash | ignore rule | mAP | rare recall | hardware | seed`

#### 练习 2 参考

- 合规：见上文英文句。  
- 违规：「我们提出更强检测器并刷新 SOTA」——数据文主贡献应是基准与审计，不是新头。

#### 练习 3 参考

并列报告：总体指标（含合成训练）与「仅真实稀缺类」指标；讨论合成效用不能替代真实稀缺覆盖；收缩「真实缺陷基准已充足」的措辞。

#### 必答 1 参考

A 主张是可复用基准+审计；检测器可替换。把基线当 novelty 会把自己写成方法文，并与近邻方法文错位。

#### 必答 2 参考

不可比：一方把难区忽略抬分，另一方计入，mAP 差异可能来自协议作弊而非数据/方法。

#### 必答 3 参考

（1）数据划分与忽略规则；（2）训练/推理超参与后处理；（3）主指标计算脚本或足够细节以复现表中数字。

---

### 补充：授权后的 Run 纪律（只读，不执行）

- 每个正式表行回链 Run ID；  
- 学习 PASSED ≠ 授权训练；  
- ACTIVE 仍以 `Current_Stage` 为准。

### 补充：无 B 告警指标的自检

删掉文中所有「budget / alarm recall / dispatch / risk AUPRC」后，基线表是否仍完整？应完整。若不完整，说明你把 B 指标误植进了 A。

---

### 当前边界

- 不训练、不开正式 Run ID。  
- 指标集未最终冻结。

---


### 补充课：基线表「可换模型、不可静默改规则」

- 换 YOLO ↔ RT-DETR：允许，表中新开行。  
- 静默改忽略区、混入合成 test、改类映射：不允许；若改，必须新协议版本号。  
- 基线模型不是 novelty；Technical Validation 证明数据可用。

### 补充课：小目标报表建议列（阈值未冻结前只记列名）

| 列 | 含义 |
|---|---|
| AP_small (native) | 原图像素/面积协议下的 AP |
| Recall@D1 | 缺失类召回 |
| Recall@rare | 真实稀缺桶 |
| D5 rate | 质量压力 |

### 补充课：无 B 指标自检

删光文中 budget / alarm recall / dispatch / risk AUPRC 后，基线表是否仍完整？应完整。


### 补充课：失败边界例要进 Validation 意识

强阴影弹条、道砟半掩埋、远端尺度断崖、板缝假裂纹——各准备图例位置（授权后），证明你理解域，而不是只报总分。忽略区与 D5 是一等公民列，不是脚注。


### 补充课：Technical Validation 最少让读者复现的三件事

1. 数据划分与忽略规则（含 split 哈希意识）  
2. 训练/推理超参与后处理（conf、NMS、imgsz）  
3. 主指标计算口径（类映射、D5/忽略是否计入）

### 补充课：合规 vs 违规句（再练一次）

- 合规：固定划分与忽略协议下，YOLO 与 RT-DETR 提供封闭集基线，证明基准可训练。  
- 违规：我们提出更强检测器并提升告警召回——抢方法贡献且泄漏 B。


### 边界重申

不训练、不开正式 Run ID。指标集未最终冻结。Learning PASSED ≠ 授权训练。基线工具 ≠ A 的 novelty。

### 与 `04`/`03` 接口

小目标阈值回指原图 GSD/像素协议；D5 与忽略区是基线表一等公民列；Validation 证明数据可用，告警预算留给 B。


学习口诀：同协议可换模型；静默改规则等于表作废；基线证明数据可用，不证明你发明了新检测器。


### 再练：表头最小集（默写）

`model | weights | imgsz | conf | NMS | class_map | split_hash | ignore_rule | mAP | rare_recall | hardware | seed`

## 第二部分：我的记录

### 元信息

| 字段 | 填写 |
|---|---|
| 日期 | |
| 目标（1–3 句） | |
| 状态 | `TODO` / `LEARNING` / `REVIEWING` / `PASSED` / `REPEAT` |

### 闭卷复述

```text
冻结协议 → 同协议基线 → 指标与忽略区 → 失败例 → Validation 写法
```

- 我的复述：

### 练习证据

| 练习 | 证据 | 摘要 |
|---|---|---|
| 空表表头 | | |
| 合规/违规句 | | |
| 稀缺 vs 合成并列 | | |

### 必答作答

1.  
2.  
3.  

### 自评

| 维度 | 1–5 | 备注 |
|---|---:|---|
| 同协议轴能列全 | | |
| 基线≠贡献 | | |
| 无 B 告警指标 | | |

### 错误 / 不确定 / 助手检查

-


### 补充：同协议「可换模型、不可换静默规则」

换 YOLO↔RT-DETR：允许，表中新开行。  
静默改动忽略区、把合成混进 test、改类映射：不允许。若改，必须新协议版本号 + 旧表作废说明。

### 补充：小目标报表建议列

| 列 | 含义 |
|---|---|
| AP_small (native) | 原图面积/像素阈值下的 AP |
| Recall@D1 | 缺失类召回 |
| Recall@rare | 真实稀缺桶 |
| D5 rate | 质量压力 |

阈值数字未冻结前，学习阶段只记列名。

### 练习补充题（含参考）

4. 有人只用合成 test 报 mAP 并宣称基线很强——错在哪？  
   **参考：** 违反默认不混测；测的是生成器可分性，不能证明真实走廊可用性。


### 与 `04`/`03` 的接口三句

1. 小目标阈值必须回指原图 GSD/像素协议（`04`），不能只写网络 imgsz。
2. D5 与忽略区规则（`03`）是基线表的一等公民列，不是脚注。
3. Technical Validation 证明「数据可用」；告警预算证明留给 B。

### 当前边界（重申）

- 不训练、不开正式 Run ID。
- 指标集未最终冻结。
- Learning PASSED ≠ 授权训练。


### 补充：基线表最小可读示例（数字均为占位 Unknown）

| model | imgsz | split | ignore | mAP50:95 | rare_recall | note |
|---|---:|---|---|---:|---:|---|
| YOLO11-s | 1280 | hashTBD | protocol-vDRAFT | — | — | tool baseline |
| RT-DETR-l | 1280 | hashTBD | protocol-vDRAFT | — | — | tool baseline |

授权前勿填写真实分数冒充已跑。
