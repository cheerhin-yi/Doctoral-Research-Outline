# 单篇论文审计：An unmanned aerial vehicle captured dataset for railroad segmentation and obstacle detection

- Work ID / Legacy ID / Batch ID：W-0001 / N/A（旧索引无同工作记录）/ 2026-09-10-Mainline-A
- Audit Date / Auditor：2026-09-10 / Codex
- Audit Status：PASS（论文身份、方法与数据说明可核验；数据可行性另判）
- Reading Status：SCREENED（定向全文审计，用户学习未DONE）
- Sync Status：COMPLETE（注册表、矩阵、台账和本批周报已联动）
- 输入：用户指定UAV-RSOD数据论文。先检索注册表、各矩阵、Markdown和PDF文件名，未发现已归档同题或DOI；研究计划中旧“UAV-RSOD可选”不是既有论文记录。

## 身份与版本

| 字段 | 核实结果 | 来源／定位（访问2026-09-10） |
|---|---|---|
| Title / Authors | An unmanned aerial vehicle captured dataset for railroad segmentation and obstacle detection；Rampriya R. S.、Taher Al-Shehari、Sabari Nathan、Jenefa A.、Suganya R.、Shunmuga Perumal P.、Taha Alfakih、Hussain Alsalman | [正式论文](https://www.nature.com/articles/s41597-024-03952-3)；Europe PMC全文front |
| DOI / arXiv | 10.1038/s41597-024-03952-3；arXiv N/A，未采用预印本 | 全文article-id |
| Year / Venue / Publication | 2024；Scientific Data 11:1315；published | 全文front |
| First Preprint / Version Online | 首次预印本Unknown，未找到；当前正式论文2024-12-02 | 全文epub date；PMC条目更新时间不是论文新版本日期 |
| Accepted / Early Access / Published | 2024-09-26 / N/A（未核实单独Early Access）/ 2024-12-02 | 全文history及epub |
| 内部等级 / 正式分区 | B（正式期刊）；中科院/JCR/学校认可Unknown，未核验 | 不能由Scientific Data名称推定投稿适用性 |
| 更正／撤回 | 本次正文未见提示；未完成独立全量更正排查 | PMC正式全文，不能承诺绝无更正 |
| 数据记录版本 | 10.5281/zenodo.12606374，记录Version 1；其文件名V1/V2分别指分割包／增强检测包 | [Zenodo](https://zenodo.org/records/12606374)、[API](https://zenodo.org/api/records/12606374)；不能把文件名V2当记录第二版 |

## 技术证据

正文通过Nature PDF和[Europe PMC公开XML全文](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11612275/fullTextXML)取得；以下Par/Tab为XML稳定定位，便于复核。

| 字段 | 作者报告／原文定位 | 审计判断 |
|---|---|---|
| Problem | 铁路航拍轨道分割与六类障碍物检测；摘要、Par11–16 | 直接任务数据入口，非区域分配算法 |
| Dataset | 315原图、2002增强检测图；单站停用轨道，2020-09-15采集；Par11–13；Par21列1602训练／400测试 | 同一采集地点、邻帧和增强关系必须另审计；作者没有提供可直接据此确认独立评测的证据 |
| Annotation / Method | 分割为rail/gauge标记与掩膜；检测先增强再标框；Par14–17、图3(d–g)；V1/V2组织Par19–21 | 分割真值不能当测试ROI或原图检测框；两个用途不可合并宣称标签完备 |
| Contribution | 发布铁路无人机图像、标注及常见模型验证 | 作者“首个”不作为本项目已核实的新颖性判断 |
| Metrics | 表3：YOLO列mAP50:95=49.45%、mAP50=81.05%；SSD MobileNet=52.90%、84.40%；五模型small AP/AR均10.00% | 原文没有证明为何小目标列完全相同；须实际统计尺寸和重算协议，不能由这列推定小目标充足 |
| Protocol / Hardware | Par27给batch2、Colab Pro，GPU写“Tesla 4”；Par28又称YOLOv3，Par27为YOLOv5，表3仅YOLO | 硬件、模型版本、部分指标叙述不一致；不猜型号，不以其数字作本项目公平基线；未提供完整整帧测速 |
| Limitations | 作者Par42承认地域与类别泛化受限；审计发现Par12与表1的长度／高度等描述差异，图片长宽比分布不等于框尺寸 | 增强不能替代独立线路／独立采集；并不证明真实铁路安全或外场泛化 |

## 项目判断

- Related Paper：主P0；次P1仅数据／已知检测与轨道参考，未证明未知路径或风险排序。
- Closest Innovation：P0-A-C1/C2；P1-C1/C2只观察数据适用范围，不增加其主张。
- Novelty Conflict：Partial（铁路UAV已知障碍物任务已有数据与基准）；未提出计算分配，不因它没做预算就推断空白。
- Reading Priority：P0 Must Read；P1 Reference Only，其专属研究仍等待原阶段门。
- 边界影响：无扩大；实验前必须审计真实原图框及来源分组。
- 创新影响：I-2026-09-10-Mainline-A-01，见[创新台账](../../00_Overview/Innovation_Ledger.md)。
- 后续最小验证：静态审计原始标注／派生关系，指标为可配对原图数、小目标数、异常标签及来源独立性；若原图框不可得、分组不可信或小目标不足，暂缓实现。目标：[数据审计](../Experiments/Data_Feasibility_Audit.md)，不是模型Run。
- 决策：PASS的是文献审计；数据集适合主线A与否以实际数据审计结论为准。原文与文件若冲突，两者分别记录。
- Local Path/Reference：[唯一主全文参考：正式论文](https://www.nature.com/articles/s41597-024-03952-3)。XML仅为审计读取渠道，不另建第二份正文库。
- Date Added / Last Audited：2026-09-10 / 2026-09-10。

## 文件级审计补充（2026-09-10）

论文所述1602/400与原包实际1611/391不符；2003框原图面积<1024为0，公开split存在10组字节相同跨集合图像，315原图检测框映射尚未核实。详见[数据审计](../Experiments/Data_Feasibility_Audit.md)。这些发现不撤销论文身份PASS，但否定直接把其公开划分和small列当本项目可行性证据。

## 同步检查

2026-09-10 A0-02补证：官方版本API仅1条记录、附属媒体未启用；原包XML缺source/path。论文代码链接为mAP评价程序，未补齐摘要所述增强脚本与逐图映射。详见[A0-02](../Experiments/A0-02_Data_Gap_Followup.md)。沿用W-0001及唯一正文，版本未升级，PASS与SCREENED不变；数据可行性仍HOLD。注册表、主矩阵、P1交叉入口、创新台账与周报已同步此补证链接。

- [x] 旧ID及PDF名称已去重。
- [x] 注册表和版本历史。
- [x] P0主矩阵；P1交叉索引及T1入口。
- [x] 直接受影响创新四字段及影响记录。
- [x] 周报和数据审计链接。

2026-09-10 A0-04适用性更新：用户接受VisDrone优先并弱化铁路场景。P0阅读优先级转为Reference Only（历史数据／场景参考），原文PASS、SCREENED及P1参考关系保留；主矩阵已同步。
