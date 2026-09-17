# 单篇论文审计：Integrated Visual Sensing and Efficient Deep Learning for UAV-Based Track Foreign Object Detection

- Work ID / Legacy ID / Batch ID：W-0006 / N/A（既有索引无匹配）/ 2026-09-10-Mainline-A
- Audit Date / Auditor：2026-09-10 / Codex独立证据审查
- Audit Status：PASS
- Reading Status：SCREENED（定向证据核验，未登记精读DONE）
- Sync Status：COMPLETE（注册表、矩阵、台账和本批周报已联动）
- 输入来源与定位：指定DOI 10.1109/JSEN.2026.3667586；别名RVGC-YOLO、RVGC-YOLO-Tiny（同一工作）。

## 身份、出版与来源

本页全部URL访问日期为2026-09-10。

| 字段 | 值 | 一手来源URL、访问日期、页/节 |
|---|---|---|
| Title / Authors | Integrated Visual Sensing and Efficient Deep Learning for UAV-Based Track Foreign Object Detection；Haifeng Song、Yu Mei、Shaoqing Liu、Zixuan Zhang、Hairong Dong | [作者上传全文](https://www.researchgate.net/publication/401474971_Integrated_Visual_Sensing_and_Efficient_Deep_Learning_for_UAV-Based_Track_Foreign_Object_Detection)，第1页；[出版社提交的Crossref记录](https://api.crossref.org/works/10.1109/JSEN.2026.3667586) |
| DOI / arXiv base ID / version | 10.1109/jsen.2026.3667586；未找到arXiv版本；当前技术副本为作者接受稿，2026-03-08上传 | 作者内容上传说明；正文IEEE接受稿水印给出同一DOI |
| Year / Venue / Publication Status | 2026；IEEE Sensors Journal 26(7):10316–10326；published | Crossref核实正式出版，不仅依据ResearchGate自动元数据；当前全文不是经逐字比对的最终版 |
| First Preprint / Version Online Date | 首次预印本日期Unknown / 当前作者公开副本上传2026-03-08 | 作者上传说明不等于首次公开或接受日期 |
| Early Access / Published Date | Early Access精确日期Unknown / 正式出版2026-04-01 | Crossref published-print；created=2026-03-02仅为注册记录日期，不当作Early Access |
| 载体A–D / 正式等级体系与年份 | B（内部正式期刊级）；中科院/JCR/学校等级Unknown，本页不作分区判断 | [项目规则](../../00_Overview/Paper_Reading_Guide.md) |
| 更正、撤回、撤稿状态 | 所访问记录未见撤回提示；未完成独立全量更正检索 | 作者页及Crossref记录 |
| 已有工作匹配 / 版本关系 | 全仓库Markdown、注册表、PDF文件名无题名/RVGC/DOI匹配；接受稿DOI与Crossref正式版一致，归同Work ID | 2026-09-10去重；正文页眉“2024”模板占位不用于判定出版年 |

## 技术证据

| 字段 | 作者报告的内容与原文定位 | 审计判断及证据局限 |
|---|---|---|
| Problem | UAV铁路轨道已知异物的检测精度和机载计算限制；§I | 与P0新应用任务直接相邻 |
| Dataset（版本、规模、划分、预训练/泄漏） | UAV-RSOD 2002图、6类；分层采样8:1:1；§IV-A、表I。训练100 epochs、batch32；§IV-B、表II | 未说明如何将315原图及增强派生图按来源隔离，不能认定无泄漏，也不能仅凭此断言已泄漏；实际原图/增强组审计由W-0001及数据审计处理。预训练权重版本未核实 |
| Method（核心机制、区域来源、额外计算） | YOLOv8n中C2f-RVG、GSConv、CA；Tiny版本再迭代剪枝及MGD蒸馏；§II–III、图2 | 全图网络优化，没有主线A式轨道ROI裁剪；CA关注区域不是显式走廊提取。多个改动不能作为主线A单变量消融证据 |
| Contribution（作者主张） | 轻量铁路异物检测及剪枝蒸馏部署；§III/§V | 已覆盖“UAV-RSOD＋轻量YOLO＋边缘测速”；不能把该组合本身当新贡献 |
| Metrics（数值、基线、表号） | 表III：YOLOv8n为88.38 mAP50、60.70 mAP50–95、194.22 FPS(tr)。表VI：RVGC为89.60/63.72/194.81；Tiny为87.95/61.78/226.08；YOLO11n为90.43/63.48/208.78 | 对比时保留精度—速度交换：Tiny并非全面胜出。表III/VI的RVGC原生PyTorch FPS分别40.90/40.94，不能隐藏差异；正文GSConv“FPS(pt)+18.24”实际对应表III TensorRT列变化，并非PyTorch列 |
| 计时与预算 | §IV-B/§V-A：Jetson Orin NX 8GB；TensorRT8.6.1 FP16；batch1、预热10次、测400图。起点为预处理后数据就绪，终点为原始输出张量；含前向及必要H2D/D2H同步，排除CPU后处理/NMS | 因此226.08 FPS不是完整检测流程FPS。输入尺寸在本次网页文本中乱码，记录Unknown，待视觉核对原PDF后再填；不猜为640×640 |
| Limitations（作者与审计分开） | 作者结尾提出未来极端天气多模态及开放集研究；§V-D天气测试为模拟；审计：缺来源分组隔离证据和全流程延迟 | 不把模拟天气结果解释为真实铁路外场安全保障；本工作不是未知类别识别证据 |

以上技术证据均来自[作者上传接受稿全文](https://www.researchgate.net/publication/401474971_Integrated_Visual_Sensing_and_Efficient_Deep_Learning_for_UAV-Based_Track_Foreign_Object_Detection)，主要为§IV–V、表I–III/VI–VII。正式DOI页本次未正常取回，出版身份由Crossref复核；未绕过登录或付费限制，未在项目新增正文PDF。

## 项目判断

- Related Paper：主P0；次P1（只作已知异物检测基线及范围边界参考，不提供P1未知检测或风险排序主张证据）。
- Closest Innovation：主P0-A-C1、P0-A-C2；次方向P1-C1仅关联已知路径基线，P1-C2无直接证据。
- Novelty Conflict：Partial；应用、轻量目标及部署评价重合，主线A的区域选择机制并未在本工作中被覆盖；由此不能推断主线A创新已成立。
- Reading Priority：P0为Must Read；P1为Reference Only，仍等待其原阶段启动。
- 边界影响：不复用其蒸馏/剪枝作为主线A第二项改动；不把“实时铁路安全”措辞扩展到本项目风险决策。
- 创新影响ID：I-2026-09-10-Mainline-A-06，已在[创新台账](../../00_Overview/Innovation_Ledger.md)联动；P1保持原两项主张。
- 后续最小验证：先核实UAV-RSOD原始组及增强组，再确定可比较的无泄漏划分；同划分、同精度模式、同全流程计时下比较原始YOLO11n与主线A。若增益依赖随机增强划分或排除裁剪/融合时间，停止相关主张。运行仍由[实验计划](../Experiments/Experiment_Plan.md)管理。
- 决策及证据缺口：PASS，作者全文和出版社注册记录足以支持身份、相关性、范围及速度口径判断；输入尺寸乱码、代码权重、数据分组及最终版变更仍未核验。它是有局限的先例，不是可直接搬用的公平数值基准。
- Local Path/Reference：[唯一当前全文参考：作者接受稿](https://www.researchgate.net/publication/401474971_Integrated_Visual_Sensing_and_Efficient_Deep_Learning_for_UAV-Based_Track_Foreign_Object_Detection)。
- Date Added / Last Audited：2026-09-10 / 2026-09-10。

## 同步检查

- [x] 全仓库旧ID、注册表和PDF文件名已搜索。
- [x] 注册表与正式版/作者稿关系已更新。
- [x] P0主矩阵已更新。
- [x] P1仅交叉引用已同步，未复制正文/事实行。
- [x] P0-A-C1/C2四字段、P1已知路径参考及影响记录已核对。
- [x] 周报已同步；全部完成后再改Sync Status为COMPLETE。

2026-09-10 A0-04适用性更新：用户接受VisDrone优先并弱化铁路场景。P0阅读优先级转为Reference Only（历史数据／场景参考），原文PASS、SCREENED及P1参考关系保留；主矩阵已同步。
