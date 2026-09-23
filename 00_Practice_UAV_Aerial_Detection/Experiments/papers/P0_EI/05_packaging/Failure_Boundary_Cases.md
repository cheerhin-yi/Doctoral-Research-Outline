# Failure_Boundary_Cases — 失败 / 边界例（定性，服务 Discussion）

> 四要素：**协议 | Image ID 或检索规则 | 现象 | 不推广的边界句**。  
> 不宣称任一方法「无价值」。ID 来自 Stage D/E 冻结 CSV 检索；非人工编造。

## (a) 小目标漏检：F640 vs F1280（分辨率轴）

| 字段 | 内容 |
|---|---|
| Protocol | F640 ↔ F1280；Stage D VisDrone test-dev；conf=0.25 IoU=0.5；small=0<area<1024 |
| Image ID | `9999996_00000_d_0000028.jpg`；次选 `9999938_00000_d_0000059.jpg` |
| 检索规则 | 在 `../01_visdrone_main/data/D_TESTDEV_per_image_metrics.csv` 中，要求 `small_gt≥10`，取 **F1280.recall_small − F640.recall_small** 最大者 |
| 现象 | `9999996_…028`：small_gt=14；F640 small_tp=3（sr≈0.21）→ F1280 small_tp=12（sr≈0.86），Δsr≈**+0.64**。次选图 F640 小目标全漏（sr=0）而 F1280 收回约半 |
| 边界句 | 说明低有效分辨率整图易丢小目标；**不**推出「F640 无部署价值」——它仍是最快协议，适合预算极紧且可接受低小召回的场景 |

## (b) 误检抬升：UnifAll / SAHI640（覆盖与切片轴）

| 字段 | 内容 |
|---|---|
| Protocol | UnifAll、SAHI640 vs 同图 F1280；Stage D |
| Image ID | `9999938_00000_d_0000207.jpg`（UnifAll FP=209、SAHI FP=203；F1280 FP=121）；次选 `9999979_00000_d_0000009.jpg`（UnifAll FP=197、prec≈0.12） |
| 检索规则 | 同 CSV 按 `method∈{UnifAll,SAHI640}` 的 **fp** 降序取 Top |
| 现象 | 全覆盖/工程切片在密集或纹理复杂图上显著抬高 FP 与 `n_dets`，精度低于同图 F1280；与聚合表 UnifAll/SAHI 精度低于 F1280 一致 |
| 边界句 | 切片抬召回常付精度；**不**推出「切片一定更差」——在预算允许且优先召回时 UnifAll 仍可作覆盖上界参照 |

## (c) 接缝 / 重复框风险：SAHI640

| 字段 | 内容 |
|---|---|
| Protocol | SAHI640（imgsz=640，overlap=0.25，冻结设置）vs F1280；Stage D |
| Image ID | `0000310_03500_d_0000125.jpg`（SAHI n_dets=104 vs F1280=17，ratio≈6.1，prec≈0.08）；次选 `0000265_03000_d_0000007.jpg`（Δfp SAHI−F1280=+84） |
| 检索规则 | 同 CSV：`F1280.n_dets≥5`，按 **SAHI.fp − F1280.fp** 与 `n_dets` 比放大排序（代理「重复框/过检」风险；非逐框接缝标注） |
| 现象 | 相对同图整图高分辨，SAHI640 检测数与 FP 膨胀，精度很低；符合块重叠 + 融合/NMS 对超参敏感的已知风险 |
| 边界句 | 讨论接缝/重复框需披露 overlap/NMS；**不**在未固定超参时把个例写成「SAHI 族通论失败」 |

## (d) 映射空洞：VisDrone → UAVDT（跨集评价上界）

| 字段 | 内容 |
|---|---|
| Protocol | Stage E；冻结 `../00_freeze/Class_Mapping_Preregister.md` / `class_mapping_preregister.json`（**见分前锁定**） |
| Image ID / 检索规则 | **无单图 ID 必需**：映射规则本身即边界。纳入：car/van→car，truck→truck，bus→bus。排除：pedestrian、people、bicycle、tricycle、awning-tricycle、motor。可在任意含行人/非机动车密集的 UAVDT 序列上目视确认「未映射类不参与计分」 |
| 现象 | E 只评车辆可比子集；行人/自行车等 VisDrone 类在 UAVDT DET 词表中无对应 → 评价**上界受映射约束**，不是检测器「看不见」的独立失败 |
| 边界句 | 跨集趋势检验的合法边界；**禁止**看 E 分后回改映射或把映射外类漏检写成协议失败 |

## 数据与纪律

- D CSV：`../01_visdrone_main/data/D_TESTDEV_per_image_metrics.csv`（已抽样 ID）  
- E CSV：`../03_cross_uavdt/data/E_FULL_per_image_metrics.csv`（(d) 以映射文档为准，可不绑单图）  
- 抽样脚本仅作一次性检索；成稿以本表 ID + 冻结 Run 为准。
