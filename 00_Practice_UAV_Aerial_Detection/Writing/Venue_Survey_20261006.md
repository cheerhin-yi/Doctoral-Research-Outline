# P0_EI 投稿 venue 调研（2026-10-06）

> **性质：** 案头调研。**不**改变 [`../../00_Overview/Current_Stage.md`](../../00_Overview/Current_Stage.md) 的唯一 ACTIVE（**P0_EI**），也**不**替用户选定会期或 venue。最终选择由用户（和导师）决定。
> **核查日期：** 2026-10-06（Asia/Shanghai）。每条事实后面的 `[n]` 对应文末 URL；核不到的写 **待补**。录用风险和契合度是本文的**判断**，不是官方数据。
> **依据：** [`Venue_and_Claim_Policy_JCR_2026-09-24.md`](../../00_Overview/Venue_and_Claim_Policy_JCR_2026-09-24.md)（JCR 为主尺；会议看 CCF；EI 只是描述项；地板 = JCR Q2/Q3）；[`SWJTU_Info_College_Degree_Credit_Note_2026-09-28.md`](../../00_Overview/SWJTU_Info_College_Degree_Credit_Note_2026-09-28.md)（下称"学位备忘"）；[`P0_EI_Paper_Overview_and_Experiments.md`](../P0_EI_Paper_Overview_and_Experiments.md) §1.7；[`P0_EI_Outline.md`](P0_EI_Outline.md)。
> **论文画像：** 同一个冻结 YOLO11n，在 VisDrone test-dev 和 UAVDT 上对比五种推理协议（F640／F1280／DensK1／UnifAll／SAHI640）。包括配对统计，GTX 1660 SUPER 与 RTX 5060 Ti 时延分开报告，像素–时延归一化，以及密度切片。**没有新算法**；贡献是基于证据的协议选择建议。

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
