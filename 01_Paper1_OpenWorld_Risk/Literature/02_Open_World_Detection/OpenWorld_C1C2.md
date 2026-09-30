# 开放世界检测：和 C1/C2 有关的结论

主张见 `../../Writing/Claim_Freeze_C1_C2.md`。实验未授权。数字只来自已下全文。

C1 要闭集 YOLO 加一条未知候选，在固定告警预算下提高危险召回。只涨 unknown AP 不算成功。C2 要同一批候选上的轨道上下文排序。这批全文没有 C2。

## 未知基线，不是贡献

| 论文 | 能用的原文 | 入口 |
|---|---|---|
| YOLO-World，CVPR 2024 | 实时开放词汇。主表数字本次未定位，不写。 | https://openaccess.thecvf.com/content/CVPR2024/html/Cheng_YOLO-World_Real-Time_Open-Vocabulary_Object_Detection_CVPR_2024_paper.html |
| YOLOE，ICCV 2025 | LVIS 上比 YOLO-Worldv2-S 高 3.5 AP，训练成本少 3 倍，推理快 1.4 倍。 | https://openaccess.thecvf.com/content/ICCV2025/html/Wang_YOLOE_Real-Time_Seeing_Anything_ICCV_2025_paper.html |
| CastDet，ECCV 2024 | VisDroneZSD novel 类 46.5% mAP。航拍开放词汇，不是危险告警。 | https://arxiv.org/abs/2311.11646 |

投稿前在 YOLO-World 和 YOLOE 里冻结一个。不要两个同时当贡献。

## 只证明未知召回，没有预算

| 论文 | 原文 | 入口 |
|---|---|---|
| OWOD，CVPR 2021，Table 2 Task 1 | ORE：WI 0.02193，A-OSE 8234，known mAP 56.34 | https://openaccess.thecvf.com/content/CVPR2021/html/Joseph_Towards_Open_World_Object_Detection_CVPR_2021_paper.html |
| OrthogonalDet，CVPR 2024，Table 2 | U-Recall 24.6，WI 0.0299，A-OSE 4148 | https://openaccess.thecvf.com/content/CVPR2024/html/Sun_Exploring_Orthogonality_in_Open_World_Object_Detection_CVPR_2024_paper.html |
| OW-OVD，CVPR 2025 摘要 | U-Recall +15.3，U-mAP +15.5 | https://openaccess.thecvf.com/content/CVPR2025/html/Xi_OW-OVD_Unified_Open_World_and_Open_Vocabulary_Object_Detection_CVPR_2025_paper.html |
| DEUS，CVPR 2026 | M-OWODB Task 1–3 U-Recall 65.1、66.2、69.0 | https://openaccess.thecvf.com/content/CVPR2026/html/Heo_Detecting_Unknown_Objects_via_Energy-based_Separation_for_Open_World_Object_CVPR_2026_paper.html |
| EW-DETR，CVPR 2026 摘要 | 无回放下 FOGS +57.24%。不是危险召回曲线。 | https://openaccess.thecvf.com/content/CVPR2026/html/Monga_EW-DETR_Evolving_World_Object_Detection_via_Incremental_Low-Rank_DEtection_TRansformer_CVPR_2026_paper.html |

OW-DETR、CAT、RandBox、OWOBJ、OW-Rep、NoOVD 已下全文，但主结果单元格没定位，不写数字。

## 顶刊

TCSVT 综述（DOI [10.1109/TCSVT.2024.3480691](https://doi.org/10.1109/TCSVT.2024.3480691)，全文 https://arxiv.org/abs/2410.11301 ）仍用 mAP、WI、A-OSE、UR。未知提案被列为第一个挑战。没有预算轴。Open-CRB（TPAMI 2025）没下到 PDF，不用。

## 缺口

没有危险召回–告警预算曲线。没有删除未知支路的实验。没有轨道区域或相对距离排序。VisDroneZSD 的 46.5% 不能当铁路危险召回。
