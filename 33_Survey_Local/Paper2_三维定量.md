# Paper 2：斑块内变了多少，哪些变化值得看

日期：2026-10-07。案头协议，不是开工单。Paper 2 仍 PAUSED。样例数字是冻结格式，不是测量结果。没有检查点和 Run ID，不能写进论文。

这篇只留两个主张：R1 和 R4。R2 没有对照就不做。R3 只是检查，不进贡献。不另开文件。

## R1：斑块里的高度和体积

主张在说什么。Paper 1 的框只说明“这里可能有危险”，没有说明高出地面多少、堆积了多少。R1 要证明：对同一块区域的两期影像做重建，沿表面法向比较，并且丢掉低于可检测下限的距离之后，可以得到高度和体积；只算这块区域，比整幅场景乱算更少把植被、阴影算成变化。

它不说：无人机摄影测量已经替代限界车；山区侵限已有公认厘米级；已有铁路许可。

具体干什么。

1. 建目录 `P2_proxy_01/`。放入 `epoch1/images/`、`epoch2/images/`、`gcp_check.csv`、`object_truth.csv`、`mask_proxy.geojson`。`gcp_check.csv` 的 `role` 只能是 `control` 或 `check`。检查点不参加平差。`object_truth.csv` 的体积用尺子、量杯或全站仪事先量，不能从点云反量。
2. 写 `freeze.md` 并冻结。至少包括影像张数、COLMAP 与 CloudCompare 版本、法向邻域、投影半径、核心点间距、已知物体体积。CloudCompare 可以先猜参数，猜完写入 freeze，之后不许再猜。插件说明：https://www.cloudcompare.org/doc/wiki/index.php?title=M3C2_(plugin)
3. 每期单独重建。稀疏用 Schönberger, Johannes L.; Frahm, Jan-Michael. Structure-from-Motion Revisited. CVPR 2016. https://doi.org/10.1109/CVPR.2016.445 密集用 Schönberger, Johannes L.; Zheng, Enliang; Frahm, Jan-Michael; Pollefeys, Marc. ECCV 2016. https://doi.org/10.1007/978-3-319-46487-9_31 命令是 `colmap automatic_reconstructor`，分别指向两期影像。
4. 四项停机，写入 `fail_log.md`。注册影像少于冻结张数的 80% 就停。检查点残差报均值和标准差，不能合成一个数；James 等 2019 要求分开报偏差和精度。https://doi.org/10.1002/esp.4637 反光、植被、阴影空洞不插值。没有检查点就不报立方米。
5. 用掩膜裁两期点云，在 CloudCompare 里 Plugins → M3C2 Distance。保留距离、距离不确定度、显著性。不显著的点不积分。方法是 Lague, Dimitri; Brodu, Nicolas; Leroux, Jérôme. *ISPRS Journal of Photogrammetry and Remote Sensing*, 2013, 82: 10–26. https://www.sciencedirect.com/science/article/abs/pii/S0924271613001184 摄影测量点优先用 James, Mike R.; Robson, Stuart; Smith, Mark W. 2017 的精度图。https://doi.org/10.1002/esp.4125
6. 只对显著点按核心点间距积分，正负体积分开。点云体积减去 `object_truth.csv`。再对未裁剪点云用同一 freeze 重跑。
7. 填三张表。`tables/r1_volume.csv` 列：`object_id,volume_pos_m3,volume_neg_m3,volume_net_m3,truth_m3,bias_m3`。`tables/r1_checkpoints.csv` 列：`point_id,dx_m,dy_m,dz_m`。`tables/r1_ablation_mask.csv` 列：`region,significant_points,area_m2`，行只有 `mask_in` 和 `mask_out`。

怎样算成立。`mask_out` 的显著点必须多于 `mask_in`，否则“斑块有用”不成立。已知物体偏差说不清，只留高度，不报立方米。

难度中。卡在检查点和删除实验，不在新网络。可投 *ISPRS Journal of Photogrammetry and Remote Sensing*。同域综述：Stilla, Uwe; Xu, Yusheng. 2023, 197: 228–255. https://doi.org/10.1016/j.isprsjprs.2023.01.010 应用向可看 *Geomatics*。https://doi.org/10.3390/geomatics2040025 JCR 当年核。

## R4：下限是否改变派发

主张在说什么。点云上很多小距离只是噪声。R4 要证明：加上可检测下限之后，需要派人去看的点，和只按一个绝对距离阈值筛出来的点不是同一批。

它不说：新造了一个不确定性公式。下限方法已有 Anders, Katharina 等. M3C2-EP. *ISPRS Journal of Photogrammetry and Remote Sensing*, 2021, 178: 240–258. https://doi.org/10.1016/j.isprsjprs.2021.06.011 合著者未核全。增量只在派发名单变了没有。

具体干什么。

1. 沿用 R1 的 M3C2 输出，不重跑重建。
2. 在 freeze 里写死 `dispatch_abs_threshold_m`。看完结果再改，这组作废。
3. 集合 A：显著点里距离绝对值大于该阈值。集合 B：A 里再去掉不显著点。
4. 人工变化点先标再数，不能看着显著图改标签。
5. 填 `tables/r4_dispatch.csv`，列：`set,n_points,area_m2,missed_manual_changes`，行是 `A` 和 `B`。

怎样算成立。A 和 B 的点数必须不同。相同则 R4 不成立，只留可视化。漏掉的人工变化多，主张改成“下限会漏检”，不能写成提高决策价值。

难度中高。和 R1 写成同一篇的第二项。

## R2：到参照线的距离

主张在说什么。告警没有“离轨道多近”。R2 要证明：钢轨内缘或中心线能稳定提出来时，障碍到这条折线的三维最近距离，比图像平面距离少一层视角偏差，并且带全站仪或激光残差。

它不说：符合 GB 146.2—2020 验收。标准只说明参照系可以是线路中心。https://ndls.org.cn/standard/detail/6cf36758d85a96cf81ba9b1adc43f225

具体干什么。只在钢轨可见段提取折线，提不出的段标缺口。同一批点算三维距离和图像平面距离。真值用全站仪或激光，不从图上量。填 `tables/r2_distance.csv`，列：`segment_id,dist_3d_m,dist_image_m,truth_m,residual_m`。

怎样算成立。没有对照表，R2 不写。有对照才替换 R4，不另开一篇。难度高。Zschiesche, Kira; Reiterer, Alexander. *Applied Sciences*, 2024, 14(19): 8801 把限界主线放在激光扫描。https://doi.org/10.3390/app14198801 De Burggrave 等 2026 开放页写轻量无人机相对地面激光仍有 2.2 mm 轨距差，这不是本文结果。https://isprs-archives.copernicus.org/articles/XLIX-B2-2026/387/2026/isprs-archives-XLIX-B2-2026-387-2026.pdf

## R3：掩膜是否减少假变化

主张在说什么。植被和阴影可能被当成灾害。R3 要检查：同一对点云、同一套冻结参数，加上掩膜后假显著比例下降，人工确认的堆积仍显著。

具体干什么。复制 R1 点云，有掩膜和无掩膜各跑一次。人工点先标再跑，至少记下变化与非变化。假显著不下降，掩膜只当预处理，不进贡献。不成篇。难度中。
