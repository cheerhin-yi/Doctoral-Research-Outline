# 英语并行计划：至 2026 年 12 月 CET-4

更新日期：2026-09-16（Asia/Shanghai）  
起点：2026-09-16  
目标考试：**2026 年 12 月大学英语四级（CET-4）**  
**请自行确认当次官方考试日期与报名截止日期**；本文不臆造具体考日。

每日英语：**约 1 小时** = **30 分钟 CET-4** + **30 分钟科研英语**（绑定当日科研主题）。  
科研主线约 4h，合计约 5h/日。进度状态默认 `TODO`，不编造基线分或已通过记录。

配套入口：[90_English_Learning/README.md](90_English_Learning/README.md) · [90_English_Learning/Progress_Log.md](90_English_Learning/Progress_Log.md)

---

## 1. 目标与原则

| 项 | 内容 |
|---|---|
| 基础（用户自述参考） | 工作后重学；历史四级约 350–400（待本人在 Progress_Log 填写，不伪造新测） |
| 近端 | 读懂检测相关摘要与当前章节关键句 |
| 12 月 CET-4 | 听力/阅读/写作/翻译分项可考；冲刺期加长时模拟 |
| 科研同步 | 科研英语主题跟随 LEARNING-CORE 三日主题，不借英语提前开训或宣称新 novelty |
| 线索 A | Week2 作为**历史/候选话题**进入科研英语，不写成固定未来方向 |

原则：先闭卷再对答案；保留初稿；AI 可讲解批改，**不代写**正式作答。

---

## 2. 每日 60 分钟结构

```text
00–05  复习昨日错词/错句（间隔：1/3/7 日优先）
05–30  CET-4 分项（当日轮转）
30–55  科研英语（绑定 Dxx 主题：术语 + 2–4 句 + 短译）
55–60  闭卷写 1 句或记录 1 个反复错误 → Progress_Log
```

CET-4 轮转（四周一循环，可微调）：

| 星期模式 | 30m CET 焦点 |
|---|---|
| 模式 L | 听力（短对话/长对话/短文，择一精听） |
| 模式 R | 阅读（仔细阅读或段落匹配） |
| 模式 W | 写作（提纲 + 120–180 词初稿） |
| 模式 T | 翻译（段落汉译英） |
| 复习日 | 错题回炉，不硬开新大题 |

---

## 3. 与三周 LEARNING-CORE 的耦合（2026-09-16 起约 21 日）

| 科研日 | 科研英语模块（30m） | 目标 | 练习 | 必答题 | 评估要点 |
|---|---|---|---|---|---|
| D01 | E-R01 检测链术语 | 10 词组就位 | 英→中 5；中→英 3 | Backbone/Neck/Head 各一句 | 闭卷说链 |
| D02 | E-R02 多尺度/stride | 描述尺寸变化 | 2 句特征图尺寸 | P3 vs P5 一句对比 | 术语位置对 |
| D03 | E-R03 NMS/解码 | IoU、threshold、suppress | 翻译 3 句 | NMS 作用一句 | 无中式逐字硬译 |
| D04 | E-R04 指标 | P/R/AP/mAP | 指标定义英述 | AP vs mAP | 定义不混 |
| D05 | E-R05 train/eval | train()、loss、backward | 口头解释循环 | 为何 eval 无 backward | 动词时态正确 |
| D06 | E-R06 reproducibility | seed、split、leakage | 写 4 句清单 | 何为 data leakage | 清单可执行 |
| D07 | E-R07 Week1 复习 | 压缩复述 | 80–120 词段落初稿 | 自选 3 术语造句 | 初稿保留 |
| D08 | E-R08 small object | small object、resolution | 2 句失效模式 | 为何小目标丢失 | 因果连接词 |
| D09 | E-R09 multiscale trade-off | trade-off、computational cost | 对比句 3 | P2 利弊 | 让步句 |
| D10 | E-R10 shared head（历史候选） | shared vs independent head | 结构描述 4 句 | 共享边界 | **措辞：candidate/historical** |
| D11 | E-R11 depthwise/FLOPs | depthwise、parameters | 参数对比句 | params ≠ latency | 主张谨慎 |
| D12 | E-R12 latency protocol | latency、FPS、p95 | 测速字段英述 | end-to-end vs pure inference | 字段齐全 |
| D13 | E-R13 error analysis | false negative/positive | 案例 2 句 | 现象→原因 | 逻辑词 |
| D14 | E-R14 Week2 复习 | 线索 A 英语边界 | 短段落：学了什么/不主张什么 | 禁止 overclaim | 边界句正确 |
| D15 | E-R15 slicing/coords | crop、remap、overlap | 坐标步骤英述 | 缩放顺序 | 步骤清晰 |
| D16 | E-R16 oracle vs deployable | oracle、upper bound | 禁句/可写句各 2 | 为何 GT crop 不能证部署 | 伦理式精确 |
| D17 | E-R17 time budget | time budget、overrun | 流水线英述 | mean vs p95 | 统计词正确 |
| D18 | E-R18 baseline/ignore/leak | strong baseline、ignore region | 协议句 4 | ignore 语义 | 无夸大旧结果 |
| D19 | E-R19 literature audit | prior work、gap、claim | 迷你摘要英写 | novelty 如何说 | 证据词 |
| D20 | E-R20 experiment design | hypothesis、ablation、control | 实验卡英文字段 | independent variable | 可证伪措辞 |
| D21 | E-R21 三周回顾 | 综合短文 100–150 词 | 初稿+订正 | 两线索边界 | 初稿保留 |

每周日（或 D07/D14/D21）：**周模拟/检查点** — CET 选 1 个分项限时 + 科研英语段落；结果写入 Progress_Log。

---

## 4. 三周之后 → 12 月考前（阶段划分）

> 日期按周粗分；**官方考日确认后**把最后 4 周钉死为冲刺。

| 阶段 | 大致时间 | CET-4（30m/日） | 科研英语（30m/日） |
|---|---|---|---|
| P0 LEARNING-CORE | 约 2026-09-16 起 3 周 | 分项轮转 + 每周检查点 | 上表 E-R01–21，跟随科研 |
| P1 巩固 | 三周后至考前第 5 周前 | 弱项加倍（总时长仍 30m） | 文献摘要、Method 句型；主题随当时科研阶段 |
| P2 考前 4 周 | 确认官方考日后倒数 28 天 | **考试向**：听力/阅读为主，写作翻译隔日；每周 1 次更长模拟可作唯一时长例外 | 维持：每周 ≥3 次科研句/短译，防生疏 |
| 考后 | CET 后 | 视分数决定是否续 CET 或转六级/论文英语 | 回到纯科研英语 |

内部参考（非承诺）：冲刺期末连续两次完整模拟估分接近通线再谈“就绪”；**未考前不宣称已过级**。

---

## 5. 科研英语模块通用验收（每个 E-Rxx）

每个模块须同时满足：

1. **目标**：能闭卷说出当日术语在检测链/实验链中的位置。  
2. **练习**：完成翻译或造句，证据在 Progress_Log。  
3. **必答题**：至少 1 道概念题用英文短答（可夹中文注释）。  
4. **评估**：术语理解 ≥80% 当日清单；造句无关键术语错用；线索 A 相关日无“已证明创新”式英语 overclaim。

未达标 → 模块标 `REPEAT`，翌日 CET 时间可挤 5–10 分钟只复习错项（总 60m 不变）。

---

## 6. 每周检查点清单

- [ ] CET 分项：日期、材料、正确率/估分、最弱项  
- [ ] 科研英语：本周段落初稿位置、三大错误、下周围绕科研日主题  
- [ ] 状态：`TODO` / `LEARNING` / `REVIEWING` / `PASSED` / `REPEAT`（模块级）  
- [ ] 与科研周门对齐：英语不替代科研手算与闭卷复述  

---

## 7. 报名与日期（待填）

| 项 | 状态 |
|---|---|
| 官方考试日期 | **待确认** |
| 报名截止日期 | **待确认** |
| 准考证/考点 | 待填 |
| 学校是否限制报考资格 | 待核验 |

确认后把日期补进 Progress_Log 首页，并反推 P2 冲刺起算日。
