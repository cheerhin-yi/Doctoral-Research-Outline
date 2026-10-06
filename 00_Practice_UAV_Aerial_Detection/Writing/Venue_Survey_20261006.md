# P0_EI 投稿 venue 调研（2026-10-06）

> **性质：** 案头调研。**不**改变 [`../../00_Overview/Current_Stage.md`](../../00_Overview/Current_Stage.md) 的唯一 ACTIVE（**P0_EI**），也**不**替用户选定会期或 venue。最终选择由用户（和导师）决定。
> **核查日期：** 2026-10-06（Asia/Shanghai）。每条事实后面的 `[n]` 对应文末 URL；核不到的写 **待补**。录用风险和契合度是本文的**判断**，不是官方数据。
> **依据：** [`Venue_and_Claim_Policy_JCR_2026-09-24.md`](../../00_Overview/Venue_and_Claim_Policy_JCR_2026-09-24.md)（JCR 为主尺；会议看 CCF；EI 只是描述项；地板 = JCR Q2/Q3）；[`SWJTU_Info_College_Degree_Credit_Note_2026-09-28.md`](../../00_Overview/SWJTU_Info_College_Degree_Credit_Note_2026-09-28.md)（下称"学位备忘"）；[`P0_EI_Paper_Overview_and_Experiments.md`](../P0_EI_Paper_Overview_and_Experiments.md) §1.7；[`P0_EI_Outline.md`](P0_EI_Outline.md)。
> **论文画像：** 同一个冻结 YOLO11n，在 VisDrone test-dev 和 UAVDT 上对比五种推理协议（F640／F1280／DensK1／UnifAll／SAHI640）。包括配对统计，GTX 1660 SUPER 与 RTX 5060 Ti 时延分开报告，像素–时延归一化，以及密度切片。**没有新算法**；贡献是基于证据的协议选择建议。

> **2026-10-06 18:40 更新：**用户决定 P0 只是练手，**不计学位分**；会议 **CCF-C 优先，CCF-C 难中则改投普通 EI**，期刊范围放宽。§0–§4 里按学位分做的取舍因此失效，现行结论以文末 **§7** 为准（§1–§6 保留作记录）。

---

## 0. 结论先行

1. **2026 年 11 月到 2027 年 4 月之间能投、核实过截稿日的会议，按学位备忘全部 0 分。**能计分的 CCF-B 会议里，ICASSP 2027 和 ICRA 2027 已经截稿；ICME 2027（CCF-B，计 8 分）截稿日**待补**。
2. **能计分的出口在期刊。** SCI 期刊 JCR Q1/Q2 计 15 分，Q3/Q4 计 8 分；EI 中文刊计 8 分。一篇一作 SCI 期刊还能满足"至少一篇第一作者 SCI 期刊"这条硬要求，这是会议做不到的。
3. **推荐（详见 §4）：** ① *Drones*（MDPI，JCR Q2，滚动投稿）；② *Journal of Real-Time Image Processing*（SCI+EI，非 CCF，不开 OA 可免 APC；JCR 分区待补）；③ **ICIP 2027**（2027-03-31 截稿）**只作为"练手会议"备选**，学位 0 分。

---

## 1. 口径冲突：政策"EI 会议优先"与学位备忘"普通 EI 0 分"

| 来源 | 说法 |
|---|---|
| 政策 §8 + `Research_Plan.md` §1 + `P0_Two_Paper_Plan_2026-09-22.md` | P0 走 **EI 会议优先**，主跟踪 ICIP 2027 全文；不承诺录用 |
| 政策 §1.5 | 会议按 CCF 目录定档；**EI 只是描述项**，不能替代 CCF／JCR |
| 政策 §5 | 弱 fallback 的地板 = 相关论文发 **JCR Q2 或 Q3** |
| 学位备忘 §1–§2 | 学术博士：**CCF-C 会议和期刊不计分**（明确点名 ICIP、ACCV、ICPR、BMVC）；**普通 EI 会议 0 分**，也不能顶"一篇 SCI 期刊"；CCF-B 计 8；SCI 一／二区计 15，三／四区计 8；EI 中文刊计 8 |

**判断：**

- 两份文件**没有逻辑矛盾，但优化目标不同。**"EI 会议优先"是按练手和速度设计的（政策本身就写了 P0 不是 Trans、不承诺录用）。学位备忘算的是学位分。ICIP 2027 是 **CCF-C**（第七版 2026 目录仍为 C 类 [K1][K2]），所以"主跟踪 ICIP"就等于"主跟踪一个 0 分出口"。
- **机会成本：**P0 是目前唯一证据完整的稿子（Stage A–G PASS，Run H–K 已入库）。如果它去了 0 分出口，学位要求的两篇可计分 SCI 期刊就都得等后面的论文。
- **建议的调和办法（需用户决定，本文不落实）：**把 P0 的主出口从"EI 会议"改成"**可计分的 SCI 期刊，JCR Q2 为目标、Q3 为地板**"，这正好落在政策 §5 的地板上，也符合 §1.5"EI 不替代 JCR"。ICIP 2027 降为可选的练手路线。注意第二篇的安排（"必须引用会议版为初步实证"）要跟着改：P0 如果发期刊，第二篇就引用期刊版，两篇的主张边界仍然要分开。
- **另一个灰区，需要分委员会书面确认：**有些期刊同时是 SCI 和 **CCF-C**，例如 *IEEE GRSL*、*IET Image Processing*、*IVC*、*PRL*（第七版均为 C 类 [K1]）。学位备忘第 4 条说"CCF-C 期刊不计分"，第 2 节又说校级期刊目录与 JCR"就高不就低"，而且备忘自己把 *IVC*、*PRL* 列为校目录 B 档的候选。所以这类期刊算 8／15 还是 0，**目前无法从文件判定**，在此之前不作首选。

---

## 2. 对比总表

图例：**计分** = 按学位备忘给学术博士的分值（期刊按发表当年 JCR；本文只能按现在的分区估）。"—" = 不适用。

### 2.1 会议

| Venue | 截稿（来源） | 索引 | CCF（第七版 2026） | 学位计分 | 篇幅／模板 | 审稿／通知 | 费用 | 与"无新方法基准文"契合（判断） | 录用风险（判断） |
|---|---|---|---|---|---|---|---|---|---|
| **ICIP 2027**（新加坡，2027-11-29～12-03 [C1]） | **2027-03-31** [C1]；官网 CFP 页还是占位内容，没有日期 [C2] | Proceedings - ICIP 在 Compendex [E1] | **C** [K1][K2] | **0** | 2027 待补；2026 版为 5 页正文 + 第 6 页只放参考文献，双盲，spconf 模板，自引 ≤2 篇 [C3] | 通知日待补 | 注册费待补 | 中高：EDICS 有 "Image and video content analysis" 和 "Remote sensing images" [C3]；但 5 页装不下五协议 × 两数据集 × 两 GPU | 中 |
| ICASSP 2027（多伦多） | 2026-09-23，**已截止** [C4] | Compendex [E1] | B [K1] | 8 | — | — | — | — | 不可投 |
| **IGARSS 2027**（雷克雅未克，2027-07-11～16） | **2027-01-11** [C5]；CFP 正文另有一句写 01-10 [C6]，**按 01-10 准备** | IGARSS 系列在 Compendex [E1] | 未列入 [K1] | **0**（普通 EI） | 全文 4 页（进 Xplore）或 400–600 词摘要 [C6] | 2027-03-12 通知 [C5] | 待补 | 中：GRSS 范围是对地遥感及其数据处理 [C6]，UAV 图像可以算进去，但 4 页很紧 | 低–中 |
| **ICME 2027**（厦门，2027-07-13～17 [C7]） | **待补**（官网暂无 CFP [C7]；2026 届为 2025-12-12，AOE 延到 12-31 [C8]，只能参考，不能当 2027 日期） | Proceedings - ICME 在 Compendex [E1] | **B** [K1][K2] | **8** | 2026 届：≤6 页（含参考文献），双盲 [C8] | 2026 届录用率约 15% 口头 + 15% 海报 [C8] | 待补 | 低–中：多媒体顶会看重新意 | **高** |
| ICRA 2027 | 2026-09-16，**已截止** [C9] | Compendex [E1] | B [K1] | 8 | — | — | — | — | 不可投 |
| IROS 2027（佛罗伦萨，2027-09-26～10-01 [C11]） | **2027-03-01** [C10] | IROS 系列在 Compendex [E1] | C [K1] | **0** | 待补 | 待补 | 待补 | 低：机器人会，本文没有闭环系统 | 高 |
| ACCV | 2026 届已于 2026-07-05 截止 [C12]；下一届待补 | LNCS 在 Compendex [E1] | C [K1] | 0 | — | — | — | — | 窗口内无届次 |
| ICPR／ICPRv | ICPR 2028（悉尼，2028-08）不在窗口内 [C13]；ICPRv 2027（纯线上，Springer LNCS，8 或 15 页，双盲）截稿**待补** [C14] | LNCS 在 Compendex [E1] | ICPR = C [K1]；ICPRv 是否等同 ICPR **待补** | 0（最好情况） | 见左 | 待补 | 待补 | 中 | 中 |
| CCDC 2027（中国控制与决策会议） | 2026-10-31（早于窗口）[C15] | CCDC 在 Compendex [E1] | 未列入 | 0 | 待补 | 2027-02-10 通知 [C15] | 待补 | 低：控制方向 | 低 |
| ICUS 2027（IEEE 无人系统会议） | 2027 届未公布；2026 届延期到 2026-07-10 [C16] | ICUS 在 Compendex [E1] | 未列入 | 0 | 待补 | 待补 | 待补 | 中：无人系统 | 低 |
| PRCV 2027 | 2027 届未公布 [C17]；2026 届延期到 2026-05-30 [C18] | LNCS 在 Compendex [E1] | C [K1] | 0 | 待补 | 待补 | 待补 | 中 | 中 |

### 2.2 期刊（均为滚动投稿）

| 期刊 | 索引 | JCR | CCF（第七版） | 学位计分 | 篇幅／模板 | 审稿周期 | APC／费用 | 与"无新方法基准文"契合（判断） | 录用风险（判断） |
|---|---|---|---|---|---|---|---|---|---|
| ***Drones*（MDPI）** | SCIE、Ei Compendex [J1][E1] | **Q2（Remote Sensing）** [J1][J2]；IF 5.2 [J2] | 未列入 [K1] | **15**（前提是发表当年仍为 Q1／Q2） | 首投可用自由格式，修回时套 MDPI 模板 [J4]；页数上限待补 | 首次决定中位约 21.1 天（2026 上半年）[J1] | CHF 2600 [J3] | **高**：范围就是 UAV 设计与应用 [J1]；要求完整实验细节、可复现 [J4]；接受扩展后的会议论文 [J4] | 中 |
| *Remote Sensing*（MDPI） | SCIE、Ei Compendex [J5][E1] | **Q1（Geosciences, Multidisciplinary）** [J5] | 未列入 | 15（同上前提） | MDPI 模板；页数上限待补 | 首次决定中位约 22 天 [J5] | CHF 2700 [J6] | 中高：UAV 遥感在范围内 | 中 |
| *Sensors*（MDPI） | Compendex [E1]；SCIE 待补 | **Q2**（Instruments & Instrumentation、Chemistry Analytical、EE）[J7]；IF 4.0 [J7] | 未列入 | 15（同上前提） | MDPI 模板 | 待补 | CHF 2600 [J8] | 中：范围包含 "Vision/camera-based sensors" [J9] | 低–中 |
| *Journal of Real-Time Image Processing*（Springer） | Compendex [E1]；SCIE 待补 | **待补**（需 JCR 登录） | 未列入 [K1] | 8 或 15（看 JCR） | 待补 | 首次决定中位 2 天（含直接拒稿）；进入外审的稿件一般约 100 天 [J10] | 混合刊：走订阅路线无 APC；OA 价格待补 [J10] | **高**：稿件**必须讨论实时性** [J10]，正好对上 P0 的双 GPU 时延和像素–时延归一化 | 中 |
| *IEEE JSTARS* | Compendex [E1] | 待补 | 未列入 | 8 或 15 | IEEE 期刊双栏；摘要 150–250 词 [J11]；页数上限待补 | 单盲，至少 2 位审稿人 [J11]；周期待补 | 全 OA，APC **US$1800** [J11] | 中：偏对地观测应用；VisDrone 是低空街景视角 | 中高 |
| *IEEE GRSL* | Compendex [E1] | 待补；IF 4.4 [J12] | **C**（第七版）[K1] | **待确认**（SCI 但又是 CCF-C，见 §1） | **最多 5 页**；第 4–5 页非会员每页 $230（通讯作者是 GRSS 会员则免）[J12] | 平均周转约 30 天 [J12] | 传统出版无 APC；OA 选项 US$2645 [J12] | 中：要求 "new and significant" [J12]，纯基准写成 letter 有难度 | 中高 |
| *IET Image Processing* | Compendex [E1] | 待补 | **C** [K1] | **待确认**（同上） | 待补 | DOAJ 记录从投稿到发表平均 36 周 [J13] | 全 OA，最高 US$2800／£2190／€2550 [J13] | 中 | 中 |
| *Measurement*（Elsevier） | Compendex [E1] | 待补 | 未列入 | 8 或 15 | 双盲 [J14] | 首次决定 7 天，外审后决定 57 天，到录用 126 天 [J14]（⚠ 官方页拦截了本次抓取，数值来自搜索引擎对官方页的摘录，投稿前要复核） | 混合刊；OA 为 US$3800 [J14]（同上，需复核） | 低–中：属于测量科学，要包装成"时延／精度测量" | 中高 |
| **EI 中文刊**：西南交通大学学报、测绘学报、遥感学报、光学精密工程、电子与信息学报、计算机辅助设计与图形学学报、航空学报 | 2026 年 Compendex 状态均为"Renewed（保持收录）" [E1] | — | CCF 国际目录不涉及；CCF 中文目录档次待补 | **8**（学位备忘"EI 中文刊"档） | 各刊模板，待补 | 待补 | 待补 | 中：中文刊对"协议对比＋工程建议"相对友好；按刊再核范围 | 中 |
| （对照）中国图象图形学报 | **不在** Compendex 中文刊名单 [E1] | — | — | 不能按"EI 中文刊"计 | — | — | — | — | — |

**预警／剔除：**上表所有候选刊都不在中科院 2025 年《国际期刊预警名单》（共 5 种）里 [W1][W2]。学位备忘举的剔除例子（*Neurocomputing*、*MTA*）不在这份名单上，说明学院**另有剔除名单**；学院现行剔除名单**待补**，投稿前要核。

---

## 3. 时间窗（2026-11 至 2027-04，已核实部分）

| 日期 | 事件 | 学位计分 |
|---|---|---|
| 2026-10-31 | CCDC 2027 截稿 [C15]（窗口前） | 0 |
| 2026-11-10 | IGARSS 2027 投稿系统开放 [C5] | — |
| 2027-01-10／11 | IGARSS 2027 截稿 [C5][C6] | 0 |
| 待补（2026 届为 12 月） | ICME 2027 截稿 [C8] | 8 |
| 2027-03-01 | IROS 2027 截稿 [C10] | 0 |
| **2027-03-31** | **ICIP 2027 截稿** [C1] | 0 |
| 随时 | 上表期刊 | 8／15 |

---

## 4. 推荐 Top 3

### ① *Drones*（MDPI）：首选

- **能计分：**SCIE + Ei，JCR **Q2**（Remote Sensing）[J1][J2]，不在 CCF 目录 → 按学位备忘计 **15 分**，前提是发表当年 JCR 仍为 Q1／Q2；同时满足"一作 SCI 期刊"硬条件。
- **契合：**期刊专做 UAV [J1]，要求完整实验细节和可复现 [J4]；P0 的冻结 SHA、Run ID、配对统计和失败例都是加分项。
- **节奏：**首次决定中位约 21 天 [J1]，滚动投稿，不受会期限制。
- **风险和代价：**APC CHF 2600 [J3]；"没有新方法"会被问贡献，引言要像 Outline 那样写成 "experimental evaluation + protocol-selection guidance"，把负结果写进贡献边界；MDPI 在导师或学院眼里的口碑**先当面确认**。
- **替补：***Remote Sensing*（JCR Q1 Geosciences Multidisciplinary [J5]，CHF 2700 [J6]），可以用 MDPI 的转投机制 [J4]。

### ② *Journal of Real-Time Image Processing*：不开 OA、不走 MDPI 时的首选

- **能计分：**在 Compendex [E1]，不在 CCF 目录 [K1] → 至少 8 分；JCR 若为 Q1／Q2 则 15 分。**JCR 分区待补**（需要用学校 JCR 账号查）。
- **契合：**期刊要求稿件**必须讨论实时性** [J10]；P0 的 1660／5060 Ti 分表、像素–时延归一化、"时延排序取决于 CPU／流水线"这些边界正好是它的主题。
- **代价：**混合刊，走订阅路线**不付 APC** [J10]；外审一般约 100 天 [J10]，比 MDPI 慢。
- **风险：**中。期刊偏实现和工程；要补一段"什么情况下能达到实时预算"的讨论。

### ③ ICIP 2027：只作为"练手会议"路线（学位 0 分）

- **好处：**它是 P0 现有计划主跟踪的会议，而且窗口内唯一核实过截稿日（**2027-03-31** [C1]）、方向对口、档次也说得过去的图像会议；在 Compendex [E1]。
- **代价：**CCF-C [K1] → **学位 0 分**，也不能顶 SCI 期刊；按 2026 版规则要压到 5+1 页、双盲、自引 ≤2 篇 [C3]，大部分证据（UAVDT 聚类 bootstrap、密度切片、复现附录）只能放补充材料。
- **用法：**只有用户明确要会议练手或曝光时才选。录用后再投期刊扩展版要有实质扩展，并在首页和 cover letter 里声明（*Drones* 明确接受这种稿件 [J4]）。**会议和期刊不能同时投同一份稿。**

**没进 Top 3 的原因：**ICME 2027 是唯一能计分（CCF-B，8 分）的会议，但截稿日待补，2026 届录用率大约只有 30% [C8]，没有新方法的稿子风险高；截稿日公布后可以再评估。IGARSS 2027 最快（1 月截稿），但 0 分、只有 4 页。GRSL 和 IET-IPR 要等分委员会确认 CCF-C 期刊算不算分。

---

## 5. 待补清单（投稿前必须查）

1. JCR 2025 版分区：JRTIP、JSTARS、GRSL、IET-IPR、Measurement、Sensors（SCIE 状态）（Clarivate 需登录）。
2. 学院现行剔除名单；SCI 且 CCF-C 的期刊是否计分（问学位分委员会，要书面答复）。
3. ICIP 2027 正式 CFP（篇幅、双盲、通知日、注册费）；ICME 2027 截稿日；IROS 2027 篇幅。
4. Drones／Remote Sensing 是否有页数上限；JRTIP 的 OA 价格和篇幅；JSTARS 的页数和超页费。
5. *Measurement* 数据需要从官方页复核（这次被拦截）。

---

## 6. URL

**CCF／EI／预警**
- [K1] CCF 第七版目录（2026-03-31 发布；正式版 PDF 下载链接在页内）：https://www.ccf.org.cn/Academic_Evaluation/By_category/2026-03-31/870181.shtml ；PDF：https://www.ccf.org.cn/ccf/contentcore/resource/download?ID=112CF3BF7E1140ACEB271ADAED12A67ADFABB8FF099E40C2759502A85C8A281F
- [K2] CCF 计算机图形学与多媒体分类页（ICIP = C；ICME／ICASSP = B；IET-IPR = C）：https://www.ccf.org.cn/Academic_Evaluation/CGAndMT/
- [E1] Elsevier Compendex Source List（SERIALS 更新于 2026-08-07；中文刊表更新于 2026-07-10）：https://www.elsevier.com/products/engineering-village/databases/compendex ；xlsx：https://assets.ctfassets.net/o78em1y1w4i4/1vOKA5ELqWIoXeukEI0KPk/25a74b602fc5149a096bd87bf7d9c5e1/COMPENDEX_Source-list-082026.xlsx
- [W1] 中科院期刊分区表团队 2025 年《国际期刊预警名单》发布说明：http://iae.cas.cn/jw/kycx/202504/t20250401_7585150.html
- [W2] 2025 名单全文（5 种）：https://cs.zjut.edu.cn/ueditor/jsp/upload/file/20250327/1743049103176038839.pdf

**会议**
- [C1] IEEE SPS：ICIP 2027（日期、地点、截稿 2027-03-31）：https://signalprocessingsociety.org/events/2027-ieee-international-conference-image-processing-icip
- [C2] ICIP 2027 官网（CFP 尚未更新）：https://2027.ieeeicip.org/ ；https://2027.ieeeicip.org/call-for-papers/
- [C3] ICIP 2026 Author Kit（5+1 页、双盲、自引 ≤2、EDICS）：https://2026.ieeeicip.org/author-kit/
- [C4] ICASSP 2027 CFP：https://2027.ieeeicassp.org/call-for-papers/
- [C5] IGARSS 2027 Important Dates：https://2027.ieeeigarss.org/important_dates.php
- [C6] IGARSS 2027 CFP：https://2027.ieeeigarss.org/call_for_papers.php
- [C7] IEEE CASS：ICME 2027（厦门，2027-07-13～17）：https://ieee-cas.org/event/conference/2027-ieee-international-conference-multimedia-expo-icme
- [C8] ICME 2026 作者须知（截稿、6 页、录用率）：https://2026.ieeeicme.org/author-information-and-submission-instructions/
- [C9] ICRA 2027 截稿延期公告：https://2027.ieee-icra.org/announcements/call-for-papers-submission-deadline-extended/
- [C10] IEEE RAS：IROS 2027 截稿：https://www.ieee-ras.org/event/call-for-papers-paper-submission-deadline-iros-2027-ieee-rsj-international-conference-on-intelligent-robots-and-systems-iros-27403-0/
- [C11] IROS 2027 官网：https://2027.ieee-iros.org/
- [C12] ACCV 2026 Submissions：https://accv2026.org/submissions/
- [C13] ICPR 2028：https://icpr2028.org/
- [C14] ICPRv 2027 CFP：https://www.icpr2027.com/web/cfp
- [C15] CCDC 2027：http://www.ccdc.neu.edu.cn/main.htm
- [C16] ICUS 2026 CFP：https://icus.c2.org.cn/Call-for-Papers/
- [C17] PRCV CFP 页：https://www.prcv.cn/CallforPapers/index.asp
- [C18] PRCV 2026 延期公告：https://en.caai.cn/site/content/8018.html

**期刊**
- [J1] Drones 主页（索引、JCR Q2、首次决定天数、范围）：https://www.mdpi.com/journal/drones
- [J2] Drones Statistics（IF 5.2、JCR Q2）：https://www.mdpi.com/journal/drones/stats
- [J3] Drones APC：https://www.mdpi.com/journal/drones/apc
- [J4] Drones Instructions for Authors（自由格式、可复现、会议扩展稿、转投）：https://www.mdpi.com/journal/drones/instructions
- [J5] Remote Sensing 主页（索引、JCR Q1、首次决定天数）：https://www.mdpi.com/journal/remotesensing
- [J6] Remote Sensing APC：https://www.mdpi.com/journal/remotesensing/apc
- [J7] Sensors Statistics（IF 4.0、JCR 分区）：https://www.mdpi.com/journal/sensors/stats
- [J8] Sensors APC：https://www.mdpi.com/journal/sensors/apc
- [J9] Sensors Aims & Scope：https://www.mdpi.com/journal/sensors/about
- [J10] JRTIP 主页（混合刊、实时性范围、审稿时长）：https://link.springer.com/journal/11554
- [J11] JSTARS Information for Authors（APC US$1800、单盲、摘要字数）：https://www.grss-ieee.org/publications/jstars-information-for-authors/
- [J12] GRSL（5 页、页费、OA US$2645、IF 4.4、周转约 30 天）：https://www.grss-ieee.org/publications/geoscience-and-remote-sensing-letters/
- [J13] IET Image Processing（DOAJ：APC 上限、单盲、平均 36 周）：https://doaj.org/toc/1751-9667 ；API：https://doaj.org/api/search/journals/issn:1751-9667
- [J14] Measurement（Elsevier；insights 页本次被拦截，数值待复核）：https://www.sciencedirect.com/journal/measurement ；https://www.sciencedirect.com/journal/measurement/about/insights

**2026-10-06 补充（§7 用）**
- [C19] IJCNN 2027 主页（开普敦，2027-06-14～18；CFP 下载）：https://ijcnn.org/2027
- [C20] IJCNN 2027 Important Dates（常规论文 2027-01-31；通知 03-15；终稿 04-12；≤6 页 IEEE 双栏）：https://ijcnn.org/2027/event-type/important-date
- [C21] M. Scarpiniti, D. Comminiello, "The IJCNN 2025 Review Process"（arXiv 2603.19244；5,526 投 / 2,152 录，38.94%；常规论文 1,533/4,225）：https://arxiv.org/abs/2603.19244
- [C22] IROS 2025 Digest（1,991/4,306 = 46%；本次未能下载原 PDF，数值取自搜索引擎摘录，**待复核**）：https://www.iros25.org/templates/iros2025/doc/IROS2025-Digest.pdf
- [C23] CGI-AI 2027 CFP（凯恩斯，2027-07-05～09；TVC 轨 2027-02-28；LNCS 轨 2027-04-20，通知 05-31，终稿 06-20；主题含 detection、photogrammetry and remote sensing）：https://easychair.org/cfp/cgi-ai27 ；官网：https://www.cgs-network.org/cgi27/
- [C24] CGI 2025 论文集（Springer LNCS；402 投 / 124 篇全文，30.8%；2026-07 出版）：https://link.springer.com/book/9783032222633
- [C25] IEEE SMC 2025 Handbook（"over 2,100 submissions … approximately 1,200 accepted papers"）：https://www.ieeesmc2025.org/files/content/SMC25-Handbook.pdf
- [C26] ICIC 官网（2026 届截稿 2026-03-20）：http://ic-icc.cn/ ；收录说明（口头论文进 Springer LNCS/LNAI/LNBI 并 EI；海报论文只进 OA 网站）：http://www.ic-icc.cn/2026/Indexing.php
- [C27] ICIC 2025 论文集（4,032 投 / 1,206 录，29.9%）：https://link.springer.com/book/10.1007/978-981-95-0036-9
- [C28] PRCV 2025 论文集（2,370 投 / 692 录，29.2%）：https://link.springer.com/book/10.1007/978-981-95-5693-9
- [C29] ICANN 2026 Submission（2026 届截稿 2026-03-30）：https://e-nns.org/icann2026/submission/
- [C30] ICANN 2025 论文集（375 投 / 170 全文 + 8 摘要，约 45%）：https://link.springer.com/book/10.1007/978-3-032-04546-1
- [C31] ICIG 2025（420 投 / 137 录，32.6%，双盲，LNCS）：https://icig.csig.org.cn/2025/9045/list.html
- [C32] CSIG：ICIG 2027 承办征集（2027 届未定）：https://en.csig.org.cn/199/202607/53641.html
- [C33] CVM 2027 Submission（摘要 2026-10-23，全文 2026-10-26）：https://iccvm.org/2027/submission.htm
- [C34] PRICAI 官网（2027 届仅有承办征集）：https://www.pricai.org/
- [C35] ICSIP 2027 主页（南通，2027-07-16～18；2016–2026 历届进 IEEE Xplore／Ei／Scopus）：https://www.icsip.org/ ；投稿须知（2027-02-05 截稿，03-05 通知，≤5 页，双盲，Word/LaTeX，EasyChair）：https://www.icsip.org/submission.html
- [C36] ICSIP 2027 注册费（03-20 前：学生作者 US$480／¥3400，普通作者 US$550／¥3900，IEEE 学生会员 US$450／¥3150；超页 ¥500／页）：https://www.icsip.org/reg.html ；联系页（秘书 "Ms. Veronica Reed"，icsip2016@vip.163.com）：https://www.icsip.org/contact.html
- [C37] ICIVC 2026 主页（昆明理工大学与 IEEE 合办；2026-06-05 终截；进 IEEE Xplore，EI／Scopus）：https://www.icivc.org/
- [C38] CVIDL 2026 主页（全文 2026-03-07；长沙 05-22～24）：https://www.cvidl.org/ ；出版页（2020–2025 届 Ei Compendex／Scopus 封面）：http://www.cvidl.org/publication.html
- [C39] ICGIP 2026（SPIE；2026-09-25 截稿）：https://www.icgip.org/
- [C40] YAC 2027 会议概况（北京，2027-05-07～09；中国自动化学会主办，北京信息科技大学承办；往届英文稿进 IEEE Xplore 并 EI）：https://www.caayac.org.cn/yac2027/ ；投稿要求（2027-01-31 截稿，03-20 通知，03-31 终稿；4–8 页，>6 页每页 ¥400；IEEE 双栏，LaTeX/Word 模板）：https://www.caayac.org.cn/submission/
- [C41] CCC 2026（初稿 2026-03-10，通知 04-10，终稿 05-10）：http://www.ccc2026.cn/
- [C42] CAC 2026 论文投稿页：http://cac.org.cn/article/type/4-1.html ；征文公告（截稿 2026-06-01；本次未能直接打开，日期来自搜索摘录，需复核）：https://www.caa.org.cn/article/192/5959.html
- [C43] ICCRD 2027（新加坡，2027-01-15～17；2026-10-30 截稿）：https://www.iccrd.org/index.html ；https://www.iccrd.org/sub.html
- [C44] ICICR 2027 CFP（武汉，2027-06-11～13；2027-02-28 截稿）：http://www.icrconf.com/Instructions_for_Authors/CFP/
- [C45] WASET（掠夺性会议）条目：https://en.wikipedia.org/wiki/World_Academy_of_Science,_Engineering_and_Technology
- [J15] IEEE Access Stages of Peer Review（"typical acceptance rate of about 20%"；二元决定）：https://ieeeaccess.ieee.org/authors/stages-of-peer-review/
- [J16] IEEE Access APC（US$2,160，无页数上限）：https://ieeeaccess.ieee.org/about/article-processing-charges/
- [J17] Signal, Image and Video Processing（混合刊；IF 2.7 (2025)；首次决定中位 4 天）：https://link.springer.com/journal/11760
- [J18] Machine Vision and Applications（IAPR 主办；混合刊；IF 2.0 (2025)；首次决定中位 30 天）：https://link.springer.com/journal/138
- [J19] Journal of Electronic Imaging CFP（目标六周内首次决定；页面拦截 curl，来自搜索摘录，需复核）：https://www.spiedigitallibrary.org/journals/journal-of-electronic-imaging/call-for-papers

---

## 7. 2026-10-06 用户决定：练手不计分；CCF-C 优先，难中则普通 EI

> **决定（2026-10-06 18:40）：**P0 只是练手，学位分不再考虑。会议**CCF-C 优先**；如果 CCF-C 难中，就改投**普通 EI**；期刊范围放宽，按难度和录用率排序。
> **口径：**录用率只用官方或主办方公开的数字（论文集前言、大会手册、程序委员会报告），并注明届次和出处；没有就写**待补**，不用 openresearch、LetPub 一类第三方数字。"难度"和"契合度"是本文的**判断**。CCF 档次按第七版目录 [K1]；EI 收录按 Compendex 2026-08 源列表 [E1]。
> **时间窗：**2026-11 到 2027-06。今天 2026-10-06，P0 证据已齐（Stage A–G PASS），但稿子还没写。

### 7.1 CCF-C 会议（按录用率由低到高，录用率低 = 难；录用率待补的放最后）

| # | 会议 | 2027 截稿（来源） | 最近录用率（届次，来源） | 篇幅／模板 | EI 收录 | 与"无新方法基准文"契合（判断） | 难度（判断） |
|---|---|---|---|---|---|---|---|
| 1 | PRCV 2027 | **待补**（2026 届延到 2026-05-30 [C18]） | **29.2%**（2025：692/2,370）[C28] | LNCS；页数待补 | LNCS 在 Compendex [E1] | 中：国内 CV 主会，偏方法 | 高 |
| 2 | ICIC 2027 | **待补**（2026 届 2026-03-20 [C26]） | **29.9%**（2025：1,206/4,032）[C27] | LNCS；页数待补 | **只有口头论文**进 LNCS 并 EI，海报论文只进 OA 网站 [C26] | 中 | 高（还要被分到口头） |
| 3 | CGI-AI 2027（原 CGI，CCF 列为 "CGI"） | TVC 期刊轨 **2027-02-28**；**LNCS 轨 2027-04-20**，通知 05-31 [C23] | **30.8%**（CGI 2025：124/402）[C24] | LNCS；页数待补 | LNCS 在 Compendex [E1] | 中高：主题含 detection、photogrammetry and remote sensing [C23]；CGI 2025 论文集里已有 UAV 小目标 YOLO 论文 [C24] | 中高；论文集出版慢（CGI 2025 的 2026-07 才出 [C24]） |
| 4 | ICIG 2027 | **待补**（2027 届承办方还在征集 [C32]） | **32.6%**（2025：137/420，双盲）[C31] | LNCS | LNCS 在 Compendex [E1] | 中高：图象图形学会主会 | 中高 |
| 5 | **IJCNN 2027**（开普敦，06-14～18） | **2027-01-31**；通知 03-15；终稿 04-12 [C20] | **38.9%**（2025：2,152/5,526；常规论文 36.3%）[C21] | **≤6 页，IEEE 双栏**（LaTeX/Word）[C20]；是否双盲待补 | "Proceedings of the IJCNN" 在 Compendex [E1]；IEEE Xplore | 中：神经网络综合大会，应用和实证论文的空间比视觉会大 | **中** |
| 6 | ICANN 2027 | **待补**（2026 届 2026-03-30 [C29]） | **约 45%**（2025：170 全文 + 8 摘要 / 375）[C30] | LNCS | LNCS 在 Compendex [E1] | 中 | 中 |
| 7 | IROS 2027（佛罗伦萨） | **2027-03-01** [C10] | **46%**（2025：1,991/4,306）[C22]，**待复核** | 待补 | IROS 系列在 Compendex [E1] | **低**：机器人会，P0 没有闭环系统 | 中，但会被问"机器人贡献在哪" |
| 8 | IEEE SMC 2027（胡志明市，2027-10-07～10） | **待补**（只有 wikicfp 写 2027-04-15，官网未核到） | **约 57%**（2025：约 1,200/2,100+）[C25] | 待补 | SMC 系列在 Compendex [E1] | 中：大综合会 | 低–中 |
| 9 | **ICIP 2027**（新加坡） | **2027-03-31** [C1] | **待补**（没有官方数字） | 2026 版：**5 页 + 1 页参考文献**，双盲，spconf（LaTeX/Word），自引 ≤2 篇 [C3] | Compendex [E1] | **高**：EDICS 有 image/video content analysis 和 remote sensing images [C3] | 中（判断）；篇幅最紧 |

**窗口内没有可投届次或不相关：**ICONIP 2027、PRICAI 2027 [C34]、KSEM 2027、ICTAI 2027、BMVC 2027 都**待补**（未公布）；MMM 2027 已截稿，MMM 2028 不在窗口内；CVM 2027 全文 2026-10-26 截稿 [C33]，太早，稿子来不及；ACCV 2026 已过 [C12]；ICPR 2028 不在窗口内 [C13]；ICPADS、ISBI 方向不符。（参照：ICME 2027 是 CCF-B，截稿待补，2026 届录用约 30% [C8]，只作对照。）

### 7.2 普通 EI 会议（非 CCF）

| 会议 | 截稿（来源） | 录用率 | EI 记录（Compendex 源列表 [E1] + 官网） | 篇幅 | 费用 | 主办方声誉（判断） |
|---|---|---|---|---|---|---|
| **ICSIP 2027**（第 12 届，南通，07-16～18） | **2027-02-05**；通知 03-05；注册 03-20 [C35] | 待补 | ICSIP 2016–2025 每届都在 Compendex 非连续出版物表 [E1]；官网列出 2016–2026 的 Xplore 链接 [C35] | **≤5 页**，双盲，Word/LaTeX，EasyChair [C35] | 学生作者 **¥3400**（US$480），普通作者 ¥3900，超页 ¥500／页（03-20 前）[C36] | ⚠ **会务秘书处运作**：秘书用英文化名 "Ms. Veronica Reed"，联系邮箱是 163 个人邮箱 [C36]；有大学合办，十年 EI 记录真实，**不是掠夺性会议**，但学术声誉一般 |
| **YAC 2027**（第 42 届中国自动化学会青年学术年会，北京，05-07～09） | **2027-01-31**；通知 03-20；终稿 03-31 [C40] | 待补 | YAC 系列在 Compendex 连续出版物表，2021–2024 届在非连续表 [E1]；官网写"往届英文稿件均已被 IEEE Xplore 收录，并被 EI 检索" [C40] | **4–8 页**，>6 页每页 ¥400；IEEE 双栏；LaTeX/Word 模板；中英文都收（只有英文全文进 Xplore/EI，长摘要不进）[C40] | 注册费待补（页面写"即将发布"） | ✅ **学会主办**（中国自动化学会，北京信息科技大学承办）[C40]；方向偏自动化，视觉稿要写成"无人机感知" |
| **IGARSS 2027**（雷克雅未克） | **2027-01-10／11** [C5][C6] | 待补 | IGARSS 在 Compendex [E1] | 4 页 [C6] | 待补 | ✅ GRSS 旗舰会；出国开会成本高 |
| ICIVC 2027 | **待补**（2026 届 2026-06-05 终截，07-17～19 昆明 [C37]） | 待补 | ICIVC 2020–2025 在 Compendex [E1] | 2026 届 4–12 页，每个注册含 6 页 | 待补 | ⚠ 2026 届由昆明理工大学与 IEEE 合办 [C37]，但"秘书"联络是会务公司常见的形式；中等 |
| CVIDL 2027 | **待补**（2026 届 2026-03-07 [C38]） | 待补 | CVIDL 2020、2022–2025 在 Compendex [E1]；官网列 2020–2025 [C38] | 待补 | 待补 | ⚠ 由商业会议代理（艾思科蓝 ais.cn）推广；中等偏低 |
| CCC 2027（中国控制会议） | **待补**（2026 届初稿 2026-03-10 [C41]） | 待补 | CCC 系列在 Compendex [E1] | 待补 | 待补 | ✅ 学会主办；方向是控制，契合低 |
| CAC 2027（中国自动化大会） | **待补**（2026 届 2026-06-01，需复核 [C42]） | 待补 | CAC 多届（含 2018、2022–2025）在 Compendex [E1] | 待补 | 待补 | ✅ 中国自动化学会；契合低–中 |
| CCDC 2027 | 2026-10-31 [C15]（只剩 3 周，不现实） | 待补 | Compendex [E1] | 待补 | 待补 | ✅ 学会；控制方向 |
| ICCRD 2027（新加坡） | 2026-10-30 [C43]（太近） | 待补 | ICCRD 2025、2026 在 Compendex [E1] | 待补 | 待补 | ⚠ 商业会务平台（iConf）运作 |
| ICICR 2027（武汉） | 2027-02-28 [C44] | 待补 | 待补（源列表未核到） | 待补 | 待补 | ⚠ 商业会务风格网站，EI 记录未核实，不建议 |
| ICGIP（SPIE） | 2026 届 2026-09-25 已过 [C39]；2027 届大概率不在窗口内 | 待补 | SPIE Proceedings 在 Compendex [E1] | — | — | 中等；SPIE 论文集路线 |
| ❌ **WASET**（waset.org 上的 "ICANN/ICIIC…" 等同名会议） | — | — | — | — | — | **掠夺性**，会名故意和 ICANN 等正规会议撞名 [C45]；一律不投 |

**识别要点（判断）：**会名和正规会撞名；"秘书"用英文化名、163／QQ 个人邮箱；同一网站一年开很多场；"保证 EI"；用邮件投稿。以上命中越多越要谨慎。投之前要在 [E1] 源列表里查**往届**论文集是否真被收录。

### 7.3 期刊（放宽后，按难度由高到低）

官方公开录用率的只有 *IEEE Access*（约 20% [J15]）；MDPI、Springer、Elsevier、IET 都没有在官方页面给出期刊级录用率 → **待补**。所以排序依据是**判断**：分区／影响因子、范围有多窄、是否硬性要求新方法、审稿速度。

| 难度档 | 期刊 | 索引／CCF | 官方录用率 | 速度／费用 | 备注（判断） |
|---|---|---|---|---|---|
| 高 | *Remote Sensing* | SCIE、EI；JCR Q1 [J5] | 待补 | 约 22 天首次决定；CHF 2700 [J5][J6] | 要求遥感贡献 |
| 高 | *IEEE JSTARS* | EI [E1] | 待补 | APC US$1800 [J11] | 偏对地观测 |
| 高 | *IEEE GRSL* | EI；CCF-C [K1] | 待补 | ≤5 页，约 30 天 [J12] | letter 要求 "new and significant" |
| 中高 | *Drones* | SCIE、EI；JCR Q2 [J1][J2] | 待补 | 约 21 天；CHF 2600 [J1][J3] | 契合最高 |
| 中高 | *IEEE Access* | EI [E1] | **约 20%** [J15] | 二元决定（接收／拒稿），无页数上限，APC US$2,160 [J15][J16] | 录用率低，但不要求"顶尖新意"，实证论文常见 |
| 中 | *J. Real-Time Image Processing* | EI [E1] | 待补 | 外审约 100 天；订阅路线免 APC [J10] | 必须讨论实时性 |
| 中 | *Machine Vision and Applications* | EI [E1]；CCF-C [K1] | 待补 | 首次决定中位 30 天；IF 2.0 (2025) [J18] | IAPR 主办，偏工程 |
| 中 | *IET Image Processing* ／ *IET Computer Vision* | 都在 EI [E1]；都是 CCF-C [K1] | 待补 | IET-IPR：OA 最高 US$2800，平均 36 周 [J13]；IET-CV 本次被 Cloudflare 拦截，待补 | |
| 中 | *Measurement* | EI [E1] | 待补 | 需复核 [J14] | 要包装成测量问题 |
| 中低 | *Sensors* | EI；JCR Q2 [J7] | 待补 | CHF 2600 [J8] | |
| 中低 | *Signal, Image and Video Processing* | EI [E1] | 待补 | 首次决定中位 4 天（含直接拒稿）；IF 2.7 (2025)；混合刊 [J17] | |
| 中低 | *J. Electronic Imaging*（SPIE）／*J. Applied Remote Sensing*（SPIE） | 都在 EI [E1] | 待补 | JEI 目标六周内首次决定 [J19]（需复核） | |
| 中低 | *Applied Sciences*、*Electronics*（MDPI）、*Remote Sensing Letters*（T&F） | 都在 EI [E1] | 待补 | MDPI 有 APC，金额待补 | 宽范围 |
| 中低（中文） | 计算机工程与应用、激光与光电子学进展（都在 Compendex 中文刊表 [E1]）；另见 §2.2 的西南交通大学学报等 | EI 中文刊 | 待补 | 待补 | 中文刊对"协议对比 + 工程建议"相对友好 |

### 7.4 排序后的最终短名单与推荐

**判断 CCF-C 难不难中：**窗口内能核实截稿日的 CCF-C 会议（IJCNN 约 39%、IROS 约 46%、ICIP 待补）录用率在三到五成之间。对一篇证据扎实、但没有新方法的一作首投稿来说，"难但能中"。所以按用户的规则**先走 CCF-C**，并把普通 EI 作为**并行可选或落选后的去处**。

| 排名 | 选择 | 截稿 | 录用率 | 模板／篇幅 | 为什么 |
|---|---|---|---|---|---|
| **CCF-C 首选** | **IJCNN 2027** | 2027-01-31 [C20] | 38.9%（2025）[C21] | IEEE 会议双栏（LaTeX `IEEEtran` conference／Word，以 2027 作者须知为准），**≤6 页** [C20] | 截稿日已核实；6 页是 CCF-C 候选里最宽的；有官方录用率；**03-15 出结果，来得及转投 ICIP** |
| **CCF-C 备选** | **ICIP 2027** | 2027-03-31 [C1] | 待补 | spconf（LaTeX/Word），**5 + 1 页**，双盲，自引 ≤2（按 2026 版 [C3]，2027 版待补） | 契合度最高；正好接在 IJCNN 通知之后 |
| （CCF-C 第三道） | CGI-AI 2027 LNCS 轨 | 2027-04-20 [C23] | 30.8%（2025）[C24] | Springer LNCS 单栏（LaTeX/Word）；页数待补 | ICIP 之后还能接；录用率低，出版慢 |
| **普通 EI 首选** | **ICSIP 2027** | 2027-02-05 [C35] | 待补 | IEEE 会议模板（Word/LaTeX），**≤5 页**，双盲 [C35] | 图像处理范围对口；十年 Xplore／EI 记录 [E1]；截稿日和费用都已核实（学生 ¥3400）[C36]；⚠ 会务秘书处运作 |
| **普通 EI 备选** | **YAC 2027** | 2027-01-31 [C40] | 待补 | YAC LaTeX/Word 模板（IEEE 双栏），**4–8 页**（>6 页每页 ¥400）[C40] | 学会主办，声誉最稳；篇幅宽；注册费待补；方向偏自动化 |

**一稿不能两投。**IJCNN（01-31 截稿，03-15 通知）和 ICSIP／YAC（01-31／02-05 截稿）**时间重叠**，同一份稿只能选一边：

- **路线 A（推荐，符合"CCF-C 优先"）：**IJCNN 2027 → 03-15 若被拒 → 两周改成 5+1 页投 ICIP 2027（03-31）→ 若还被拒，再投 CGI-AI LNCS（04-20），或者等 2027 年中普通 EI（ICIVC／CAC 2027，截稿待补）。
- **路线 B（用户或导师判断 CCF-C 太难时）：**ICSIP 2027（02-05）→ 03-05 若被拒 → 仍可投 ICIP 2027（03-31）。也就是说，先投普通 EI 也不会错过 ICIP。

**倒排时间表（以 2026-10-06 为起点）**

*IJCNN 2027（首选，01-31 截稿）*
- 10-06～10-31：定 6 页的论文主线（只保留主表 + 2～3 张图：协议×数据集 AP/时延、像素–时延归一化、密度切片）；下载 IJCNN／IEEE 会议模板；确认是否双盲（待补）。
- 11-01～11-30：写完初稿全文（引言把贡献写成 "empirical evaluation + protocol-selection guidance"，负结果写进贡献边界）。
- 12-01～12-31：导师第一轮修改；压缩到 6 页；参考文献核对。
- 2027-01-01～01-20：第二轮修改、英文润色、图表终版；检查 PDF 是否符合 IEEE 要求。
- 01-24：内部定稿；**01-31 提交**（截止时区待补，按提前一天提交）。
- 03-15 通知 → 04-12 终稿 [C20] → 06-14～18 开普敦参会（注册费、签证待补；IEEE 会议一般要求至少一位作者注册并到场，以 2027 正式规则为准）。

*ICIP 2027（备选，03-31 截稿）*
- 02-01～03-14（等 IJCNN 结果期间）：**先准备**一份 5+1 页 spconf 双盲版本，但不提交。
- 03-15 若被 IJCNN 拒：结合评审意见修改，03-28 定稿，**03-31 提交**。若 IJCNN 录用，就撤掉 ICIP 计划。

*ICSIP 2027（普通 EI 首选，02-05 截稿）*
- 10-06～11-30：同上，写成 5 页双盲初稿。
- 12 月：导师修改；1 月：润色；01-29 定稿；**02-05 提交**（EasyChair）。
- 03-05 通知 → **03-20 前注册**（学生 ¥3400）[C36] → 07-16～18 南通。

*YAC 2027（普通 EI 备选，01-31 截稿）*
- 节奏同 IJCNN，篇幅控制在 6 页以内，避免超页费；**01-31 提交** → 03-20 通知 → 03-31 终稿 → 05-07～09 北京 [C40]。

**一句话推荐：**主投 **IJCNN 2027**（2027-01-31，CCF-C，2025 年录用率约 39%，6 页）；被拒就在 03-31 前转投 **ICIP 2027**。如果用户或导师认为 CCF-C 太难，就改投 **ICSIP 2027**（2027-02-05，十年 IEEE Xplore/EI 记录，学生注册 ¥3400），备选 **YAC 2027**（2027-01-31，中国自动化学会主办）。普通 EI 被拒后仍然赶得上 ICIP 2027。

### 7.5 本节待补
1. ICIP、PRCV、ICIG、ICIC、ICANN、SMC 2027 的正式 CFP（截稿日、篇幅）；ICIP 的官方录用率；IROS 2025 的 46% 要从原 PDF 复核 [C22]。
2. IJCNN 2027 是否双盲、截止时区、注册费；YAC 2027 注册费；ICSIP、YAC 历届录用率。
3. 各期刊官方录用率（除 IEEE Access 外均没查到）；IET-CV、JEI、JARS 的速度和 APC。
4. MDPI／商业会务类会议在导师和学院眼里的口碑，**先当面确认**。
