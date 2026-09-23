# 单篇论文审计：MRU-YOLO

- Work ID / Legacy ID / Batch ID：W-0007 / N/A / 2026-09-10-Mainline-A。
- Audit Date / Auditor：2026-09-10 / Codex独立近邻审查。
- Audit Status：PASS（身份、正式全文与关键技术证据已核验；不代表实验已复现）。
- Reading Status：SCREENED（针对主线A审计，不记为用户精读DONE）。
- Sync Status：COMPLETE（注册表、矩阵、台账和本批周报已联动）
- 输入来源与定位：补充检索发现的直接近邻；出版社全文与作者代码相互核对。

## 身份、出版与来源

所有访问日期为2026-09-10。

| 字段 | 值 | 一手来源URL、页/节 |
|---|---|---|
| Title / Authors | MRU-YOLO: Marginal-Utility-Guided Selective Local Re-Observation for Small-Object Detection in UAV Imagery；Jiajun Chen, Jinxin He, Yongzhi Wang, Peng Lu, Hengshuo Li | [正式PDF](https://mdpi-res.com/d_attachment/remotesensing/remotesensing-18-02680/article_deploy/remotesensing-18-02680.pdf)，p.1 |
| DOI / arXiv base ID / version | 10.3390/rs18162680；arXiv Unknown，未查得可合并预印本；出版社Version of Record | PDF首页；[Crossref](https://api.crossref.org/works/10.3390/rs18162680) |
| Year / Venue / Publication Status | 2026；Remote Sensing 18(16), 2680；Published | PDF页眉；Crossref |
| First Preprint / Version Online Date | First Preprint Unknown；VoR PDF/XML 2026-08-10 | [版本记录](https://www.mdpi.com/2072-4292/18/16/2680/notes) |
| Early Access / Published Date | 单独Early Access N/A；收到2026-06-27，修回07-22，接受07-30，发表08-10 | PDF p.1；Crossref发表日交叉确认 |
| 载体A–D / 正式等级体系与年份 | Unknown：本次未核验项目载体类别、中科院分区或学校国奖资格 | 不以期刊名称、影响因子或JCR替代目标资格 |
| 更正、撤回、撤稿状态 | 已查版本记录未见单列更正/撤回条目；未完成跨库独立撤稿核验，不能写保证无更正 | 版本记录；Crossref |
| 已有工作匹配 / 版本关系 | 写入前对全局与练手目录MD检索MRU、标题、2680与DOI，无既有Work匹配；不是SAHI/ESOD版本 | 本地去重；未新增重复PDF |

正文可访问性：出版社HTML/XML直接访问多次403/429；公开出版社CDN的正式26页PDF以普通请求成功读取，并核验正文§1–5、表1–9。PDF只用于系统临时目录阅读，未加入仓库或触碰受保护附件目录；主正文使用上述稳定公开PDF链接。作者数据可用性声明（p.23）直接指向[代码仓库](https://github.com/JiajunChen223/MRU-YOLO)。辅助代码冻结到commit `94a525c7331c3226402edf6be3faa2848e73165e`；代码可能晚于论文，不能自动等同发表时实现。

## 技术证据

| 字段 | 作者报告的内容与原文定位 | 审计判断及证据局限 |
|---|---|---|
| Problem | 全图缩放损害UAV小目标细节；全局预测后只对有剩余检出价值的区域增加局部观察。§1、§2.1 | 与P0-A-C1的计算分配问题直接重合；没有铁路数据实验 |
| Dataset | SeaDronesSee ODv2 train8930/val1547、5类；VisDrone2019-DET train6471/val548、10类。分别训练检测器和HGB。§2.6、表3 | VisDrone去掉类别0/11，ignored regions未进入评价掩码；作者明确为转换标签下Ultralytics val指标，非官方test-dev/server结果。不能与官方分数混排 |
| 划分、训练与预训练 | §2.7：150epochs、batch16、SGD、3个完整链seed0/1/2；最佳val checkpoint；HGB仅train候选状态/效用训练，val作排序诊断。作者配置使用yolo11n.pt预训练 | 没有单独冻结test的泛化证据；val参与checkpoint选择，不能称未接触测试。代码fit只使用train，不能据val诊断反推GT在线泄漏；来源组隔离及预训练重叠未独立审计 |
| Method | 同一YOLO11n权重用于全图与局部640输入。固定3×3候选、每侧扩0.1，26维几何/图像/预测统计，HGB排序取Top-2。§2.1–2.4、表2 | 在线不用GT、裁片像素特征或额外图像网络作选择；不是轨道先验。离线每训练图需全图与全部9候选推理并用GT构造效用，有额外训练流程成本 |
| 效用与预算 | 效用为加入一个候选后跨IoU0.50–0.95平均匹配GT数的非负增量；各候选独立标签，非AP本身。预算明确为裁片输入个数，必需全图不计K；运行时间另测。§2.3–2.4，公式14–16 | 固定K不等于毫秒约束、p95约束或硬截止时间。Top-K、边际收益和“有限区域预算”已被覆盖；换名称不能形成差异 |
| 融合/保护 | 原图尺度门128px、局部置信度×0.9、稳定全局预测保护、最终按类NMS。§2.5，公式17–27；表6单列融合消融 | 保护大且置信度高的全局预测，并不保证未选区域的小目标召回；没有铁路风险等级或覆盖概率保证。全图保底、简单冲突保护也不是空白 |
| Contribution | 作者主张预测条件下效用学习、预算内局部回看、来源感知融合三部分。§1末 | 已读到作者主张，不将其“创新”措辞当作独立新颖性审定 |
| Metrics / 表4–5 | 3seed平均AP50–95：Sea global39.496、densityTop2 41.784、learned41.819；VisDrone18.446、21.690、21.725。Table5(b)正oracle效用子集分别1141/1547与532/548，学习排序优于密度代理 | 相对global增量2.323/3.279个百分点，学习排序相对同预算密度仅各0.035个百分点；不能把总增益全部归因边际收益学习，也未证明0.035有统计/实用显著性。代理排序分数不等于全样本召回 |
| Metrics / 表6–8 | 融合相对plain的AP增量1.78/0.33pp；条件oracle相对独立Top2仅0.10/0.12pp；K=1–4及全9对照已做。低密度Sea组AP下降0.17pp | 简单“多看区域”未必提高结果；候选的增量应与密度选择和相同融合比较；区域级/类别级负结果必须保留 |
| Metrics / 表9与§2.8 | RTX3090、同步单图FP16、30预热+300计时图；seed0计时重复5次，表为重复间均值±样本SD。Sea global11.57±0.80ms、MRU32.40±1.21、SAHI587.93±21.03；VisDrone10.33±0.33、30.09±2.44、167.06±5.14。对应MRU30.86/33.24FPS | 这些SD不是逐帧p95；MRU比原始global更慢。表9比较一个SAHI配置，不是相同毫秒预算下充分调优的Pareto前沿；不同设备不可搬用FPS |
| 计时范围 | 论文§2.8称包括预处理、状态/切片、检测、融合NMS，排除磁盘I/O及外部部署开销。作者benchmark源代码有CUDA同步，并分别计global、selection、crop、fusion | 源代码在t0前执行cv2.imread和make_grid_windows，因此至少排除读取/图像解码与候选网格生成；应保留这项文字与实现边界差异。代码可输出p95，但论文表9不提供逐帧p95或违反率；未运行核对发布结果 |
| Limitations | 作者§4承认固定Top2未来可改为随场景/计算约束自适应，视频与更低部署开销也属未来工作 | 审计推断：这已是作者提出的直接延伸，不能仅用“动态预算”一句话宣称新颖。未选区域丢失、类混淆、独立铁路泛化、严格时间控制均未被本文证据解决；未解决不等于无人做过 |

代码核验位置（同一冻结commit）：[训练选择器](https://github.com/JiajunChen223/MRU-YOLO/blob/94a525c7331c3226402edf6be3faa2848e73165e/scripts/train_mru_selector.py)、[流程与划分](https://github.com/JiajunChen223/MRU-YOLO/blob/94a525c7331c3226402edf6be3faa2848e73165e/scripts/reproduce.py)、[计时范围](https://github.com/JiajunChen223/MRU-YOLO/blob/94a525c7331c3226402edf6be3faa2848e73165e/scripts/benchmark_mru_routeA.py)、[作者结果JSON](https://github.com/JiajunChen223/MRU-YOLO/blob/94a525c7331c3226402edf6be3faa2848e73165e/results/paper_results.json)。只读核对，无运行、安装或模型下载。

## 项目判断

- Related Paper：唯一主方向P0；Paper1次方向N/A，仅共用已知检测背景，不自动加跨方向任务。
- Closest Innovation：P0-A-C1、P0-A-C2。
- Novelty Conflict：Direct（预测引导局部高分辨率＋固定预算＋效用排序＋全局保护）；对“轨道先验＋经校准的毫秒控制与区域遗漏评价”的完整组合为Partial/Unknown，不是已确认差异。
- Reading Priority：Must Read；属于当前A0直接近邻核验，不解除S0学习完成门或训练门。
- 边界影响：建议调整候选表述、保持High风险；不改变已知类别检测边界，不加入风险排序/未知发现，也不自动复制作者融合或学习器作为第二项改动。
- 创新影响ID与台账链接：I-2026-09-10-Mainline-A-07；[Innovation Ledger](../../00_Overview/Innovation_Ledger.md)已同步。
- 后续最小验证：首先只在A0完成数据是否具备可部署轨道先验、分辨率余量与独立分组依据的核验；若数据条件不成立即停止主线A。未来阶段允许后，在同一检测器/融合/候选预算下只替换区域选择，纳入密度Top-K与MRU式选择，测AP50–95、small recall、未选区域漏检和完整延迟p95/违反率；在校准侧匹配毫秒预算，测试锁定。若几何走廊或密度基线已等效，候选机制主张停止；目标计划条目为A0-01及后续待开放的主线A实验条目。
- 决策及证据缺口：PASS用于归档直接近邻证据；未复现、无独立来源分组审计、无铁路实测、无学校分区资格结论。只有具体新增机制/协议及近邻排除证据出现后，才能重评新颖性。
- Local Path/Reference：主正文为上面的出版社正式PDF；无仓库正文副本。
- Date Added / Last Audited：2026-09-10 / 2026-09-10。

## 同步检查

- [x] 全局注册表和版本历史已更新；旧ID与正文已搜索。
- [x] 主Literature Matrix全部必填字段有值或有理由的Unknown/N/A。
- [x] 次方向仅交叉引用，已有主题Reading_List入口已同步（本篇无次方向需求）。
- [x] 所有直接受影响创新的四字段已更新。
- [x] 周报记录新增/版本变化/风险/待决动作，链接可解析。
- [x] 全部完成后再把Sync Status改为COMPLETE。
