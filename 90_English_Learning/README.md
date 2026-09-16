# 项目英语学习支持线（更新版）

更新日期：2026-09-16  
本目录草案对齐：**每天约 1 小时**，目标 **2026 年 12 月 CET-4**（**请确认官方考试日期与报名**），并与科研 LEARNING-CORE 同步。

详细日程见上级 [Completion_Metrics.md](../Completion_Metrics.md)。  
个人作答与测试只写入 [Progress_Log.md](Progress_Log.md)。状态默认 `TODO`；**不编造基线测验成绩或已通过结果**。

本线**不改变**科研唯一阶段门，也不等于论文研究方向。

---

## 当前基础与目标

- 基础：工作后重新系统学习；历史四级约 350–400（在 Progress_Log 由本人确认/更新）。  
- 近端：读懂目标检测摘要与当前学习章节相关句。  
- 12 月：CET-4 应试能力（听/读/写/译）。  
- 科研英语：跟随每日科研主题；**不**提前用英语学习启动训练或 Paper 1–7。

---

## 每天 60 分钟

| 块 | 时长 | 内容 |
|---|---:|---|
| CET-4 | 30m | 听力 / 阅读 / 写作 / 翻译轮转 |
| 科研英语 | 30m | 术语 + 句型 + 短译，绑定当日 Dxx |
| 收尾 | 含在内 | 闭卷 1 句或 1 个错点 → Progress_Log |

每周安排一次检查点/分项模拟；**考前最后 4 周**改为考试向（见并行计划）。完整限时模考可作为冲刺期唯一时长例外。

---

## 与科研阶段耦合

| 科研周 | 科研英语重点 | 特别注意 |
|---|---|---|
| Week1 基础 | YOLO 链、指标、train/eval、reproducibility | 对应 E-R01–07 |
| Week2 | 小目标、多尺度、**共享头作历史/候选话题**、效率与延迟 | **不再**把 lightweight shared head 写成固定未来方向；英语中使用 candidate/historical |
| Week3 | 切片/坐标、oracle、time budget、baseline/ignore、文献与实验设计 | 对应 E-R15–21；禁 overclaim |

三周后：科研英语跟随当时科研阶段；CET 比重在考前 4 周上升。

---

## 文件职责

| 文件 | 职责 |
|---|---|
| 本 README | 入口、规则、模块顺序 |
| [Progress_Log.md](Progress_Log.md) | 本人作答、测试、CET 分项、状态 |
| [../Completion_Metrics.md](../Completion_Metrics.md) | 至 12 月完整日程与模块必答题 |
| 原仓库 `Domain_English_Lessons.md`（若仍保留） | 可继续作题库；新日程以并行计划为准 |

同一事实只留一处：课程/题干在课程或并行计划；作答只在 Progress_Log。

---

## 领域模块顺序（更新）

1. YOLO 检测链、训练与推理 — 与 Week1 同步开放  
2. IoU / P / R / AP / mAP 与错误分析 — Week1  
3. PyTorch 训练、验证与可复现 — Week1  
4. 公平对照、数据泄漏与不确定性 — Week1 末 / Week3  
5. 小目标、多尺度、P2–P5 — Week2  
6. **轻量共享检测头（历史 / 候选话题）** — Week2；**非固定研究方向**  
7. 参数量、GFLOPs、显存、延迟、FPS、p95 — Week2–3  
8. 切片、坐标、oracle vs deployable、time budget — Week3  
9. 文献摘要、Method / Experiments 阅读 — Week3 起  
10. 写作句型（Intro/Related/Method 等）— 有材料后再开；无结果不编数字  

---

## 分工

**AI**：筛选术语、给音标/搭配/例句、批改、区分 must-use / recognize / ignore、按周测调整。  
**用户**：闭卷先答、保留初稿、按反馈自写订正、记录生词交筛、不另堆无边界大词表。

---

## 当前英语任务状态

- 总状态：`TODO`  
- 第一优先：按并行计划 D01/E-R01 开始（检测链英语）  
- 通过条件见并行计划与 Progress_Log 模板；**当前未宣称 PASSED**

英语证据不替代科研 S0/LEARNING-CORE 的手算与闭卷复述。
