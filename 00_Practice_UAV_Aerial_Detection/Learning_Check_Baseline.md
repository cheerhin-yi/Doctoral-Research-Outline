# 练手文学习检查基准（助手维护）

路径：`00_Practice_UAV_Aerial_Detection/Learning_Check_Baseline.md`  
更新日期：2026-09-23。  
维护者：助手。用户完成某块笔记**第二部分**后提交检查；**未达标不得进入下一块／下一关**。

权威关系：
- 当前科研唯一事项：`00_Overview/Current_Stage.md`（EI 稿；Stage E 已 PASS，下一门为 EI 包装）。
- 学习推进：本文件 + `Completion_Metrics.md`。
- 写法：研究路线笔记分「第一部分知识链教材」与「第二部分个人记录」；过关只查第二部分。
- `01_YOLO_Research_Core.md`：按你的要求**暂保持单部**；过关查篇内「必须掌握」自检区。

判定：`TODO` → `LEARNING` → `REVIEWING` → `PASSED` / `REPEAT`。  
助手**不得代填**用户作答。

---

## 0. 总规则

1. 检查对象：对应笔记**第二部分**（`01` 除外，见上）。
2. 第一部分是教材，抄写第一部分不等于通过。
3. 必须能**沿知识链闭卷串讲**。
4. 练习要有可复查证据。
5. 必答题保留初稿；空白或明显代写 → `REPEAT`。
6. 关卡内顺序如下；关卡之间 L0→L4。

---

## 1. 块顺序（对齐 P0 EI 路线）

| 顺序 | 笔记 | 关卡 | 状态 | P0 相关性 |
|---|---|---|---|---|
| 1 | `01_YOLO_Research_Core.md`（单部） | L0 | TODO | 基础检测链 |
| 2 | `10_ResNet_Core.md`（可选） | L0 可选 | TODO | 骨干直觉 |
| 3 | `02_PyTorch_and_Reproducibility.md` | L1 | TODO | Run 可复现 |
| 4 | `03_Experiment_Design_and_Uncertainty.md` | L1 | TODO | **主张→实验卡** |
| 5 | `04_Small_Object_and_Multiscale.md` | L2 | TODO | **小目标定义／分辨率轴** |
| 6 | `06_Efficiency_and_Deployment.md` | L2 | TODO | **时间预算／计时边界** |
| 7 | `05_Lightweight_Shared_Head.md` | L2 历史 | TODO | 非必须实现 |
| 8 | `07_Mainline_A_Knowledge_Chain.md` | L3 | TODO | **五方法主链（E 已 PASS 口径）** |
| 9 | `08_Image_Level_Paired_Inference.md` | L3 | TODO | **Stage F 读结果** |
| 10 | `09_Cross_Set_UAVDT_Mapping_and_Related_Tech.md` | L3/L4 | TODO | **跨集映射＋近邻技术词表** |
| 11 | `11_EI_Packaging_Neighbor_Failure_Repro.md` | L4 | TODO | **近邻表／失败例／复现附录** |
| — | 文献边界 + 实验卡（Completion_Metrics L4） | L4 | TODO | C1/C2 可证伪 |

`00_Unified_Core_Knowledge_Map.md` 仅导航，不过关。

**建议：** 若正并行写 EI 稿，可在 L0 串讲达标后，优先 `03→04→06→07→08→09→11`；`02` 仍须在引用 Run／复现清单前 `PASSED`。  
**实验门：** 补齐学习笔记 **不**等于完成 EI 包装实验增量；也不解锁训练／改映射／Paper 2–7。

---

## 2. 分块检查清单

### 2.1 `01`（L0，单部）

知识链：输入→Backbone→Neck→Head→训练/推理分支→IoU/P/R/NMS→误差映射。  
通过：闭卷串讲、自绘结构图、一组 IoU+P/R+简化 NMS 手算、误差映射四例、篇内必答初稿。

### 2.2 `02`（L1）

知识链：数据→DataLoader→forward→loss→backward→val→checkpoint／seed。  
通过：串讲、最小循环标注 shape／梯度、复现清单、泄漏例、必答。

### 2.3 `03`（L1）

知识链：主张→可证伪假设→固定因素→唯一变量→图级评价→停止／负结果→CI。  
通过：P0-EI-C1 实验卡字段齐全、伪对照辨析、允许/禁止论文句各一句、必答。

### 2.4 `04`（L2）

知识链：原图面积→小目标阈值→缩放/切片→还原→原图匹配→recall_small。  
通过：面积手算、四手段一句话区分、污染源两条、必答。

### 2.5 `06`（L2）

知识链：协议→计时边界→预热同步→单次 vs median-of-3→mean/p95/超时→论文速度句。  
通过：SAHI 计时边界图、谨慎/禁止速度句、4090 表最少列、必答。

### 2.6 `05`（L2 历史）

须写明「历史候选、非当前必做」。可不阻塞 L3。

### 2.7 `07`（L3）

知识链：冻结权重→五方法→切片映射→融合→原图评价→耗时→Stage F→Stage E 外推→C1/C2→指向 EI 包装。  
通过：五方法流程图、Stage 纪律（含 E 映射预冻结）、主比较 CI 解读、说明下一门是包装而非第三同质集、必答。

### 2.8 `08`（L3）

知识链：per_image→配对对齐→过滤 undefined→Wilcoxon+bootstrap→Holm→主张句。  
通过：解释重采样单元、CI 跨 0 改口、附录次要对、必答。

### 2.9 `09`（L3/L4）

知识链：冻结权重→映射冻结→五协议×UAVDT→兼容评价→与 D 对照→主张边界→related work 词表。  
通过：映射伪效应例、跨集一致/不一致各一句、四枚 related-work 关键词「用而不冒充发明」、必答。

### 2.10 `11`（L4）

知识链：冻结证据→主张句→近邻表→跨集厚写→失败例→复现附录→（可选）4090 表→停笔检查。  
通过：近邻空表（列名齐全）、失败例四要素草稿、附录清单自检（缺/已具备各≥2）、必答。

### 2.11 L4 总门（Completion_Metrics）

实验卡 + 近邻边界；可与 `11` 合并检查，但不跳过 `09`/`11` 第二部分。

---

## 3. 检查记录（追加，勿删旧行）

| 日期 | 笔记 | 判定 | 主要缺口／补学指令 | 检查者 |
|---|---|---|---|---|
| （尚无） |  |  |  |  |

---

## 4. 变更规则

- 改知识链或通过标准：先改本文件，再改对应笔记第一部分，并在第 3 节留行。
- 2026-09-17：按 P0 Benchmark（A–D/F）重写 `03/04/06/07` 为双部，新增 `08`；`01` 仍单部。
- 2026-09-23：对照当前 EI 架构补 `09`（跨集／映射／近邻技术词表）、`11`（EI 包装）；更新 `07` 为 E 已 PASS；学习顺序延伸至 `09→11`。不因本变更将任何块标为 PASSED。
