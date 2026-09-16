# A0-02：原始数据缺口补证

核验日期：2026-09-10。**本轮公开补证已完成，研究可行性仍为HOLD。** 未取得新增原图检测框、派生映射或来源分组。结论仅覆盖下列已检查公开入口，不等于证明作者没有这些资料。

## 1. 本次新增证据

| 核验入口与定位 | 实际结果 | 对缺口的影响 |
|---|---|---|
| [Zenodo记录API](https://zenodo.org/api/records/12606374)，`files`、`updated`、`metadata.related_identifiers` | HTTP 200；仍只有V1分割、V2检测两个ZIP；MD5与A0-01一致；updated为2024-07-04；未列关联资源 | 未发现新增原图框或映射附件；本轮未重新下载原包 |
| [全部版本API](https://zenodo.org/api/records/12606374/versions)，`hits.total`、`links` | HTTP 200；total=1，唯一记录12606374，无下一页 | 此记录版本链没有可供补证的新版本；不证明所有平台均无其他版本 |
| [附属媒体API](https://zenodo.org/api/records/12606374/media-files) | HTTP 200；enabled=false | 此入口未提供附加视频或侧文件 |
| 两个本地原包只读检查，V2全部2002个XML的`source`和`path`字段 | 两字段均缺失；V1无检测XML；除图片、XML、CSV之外，V2只有类别表、labelmap和模型配置 | 无法从XML来源字段恢复视频、帧号或原图ID。不能把顺序文件名解释为来源组 |
| [正式论文](https://www.nature.com/articles/s41597-024-03952-3)，Abstract、Data augmentation、Code availability；[公开XML](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11612275/fullTextXML) | 摘要称提供增强脚本；正文描述先增强后标框；代码可用性指向评价程序。XML中未列supplementary-material元素 | 增强参数范围不等于每张图的实际变换、随机状态或原图映射；“有原图”不等于“有原图检测框” |
| 论文链接的作者[Gist](https://gist.github.com/dsabarinathan/782fdb7b10bc4ac1424845662892120e)，`mAP.py`中`GT_PATH`、`DR_PATH`、`voc_ap`、`MINOVERLAP` | 网页显示一个mAP.py、一次revision；程序读取既有真值和预测结果，计算VOC式AP；未找到ImageDataGenerator或增强映射内容 | 该链接不能补齐增强脚本或原图标签，也不能单独复现论文COCO式small指标。未执行该程序 |

访问限制：Nature直接访问发生身份跳转，PMC直接页面出现验证页；本次以已有完整XML、搜索可访问正文及官方数据API交叉核对。Gist网页可读，但GitHub API首次TLS失败、一次重试返回403限流；没有取得本地代码快照或API提交哈希，不能声称完成作者所有仓库历史审查。没有绕过限制。

## 2. 缺口判定

| 必要条件 | 已确认 | 仍待取得 | 当前判定 |
|---|---|---|---|
| 315张未增强原图的检测框 | V1提供原图与分割资料；V2提供增强图检测框 | 原图对应VOC/COCO/YOLO标签或作者确认的可复核对应表 | Unknown，未取得；禁止自行造框或逆映射 |
| 原图—增强图关系 | 论文说明315→2002；A0-01哈希已有候选 | 每张派生图的原图ID、几何变换及坐标约定，或可重建的脚本和随机状态 | Unknown；近似图候选不升级为确定映射 |
| 独立评测分组 | 原文单站停用轨道采集；公开split有10组精确跨集合重复 | 视频/航次/连续片段ID、帧号或时间戳；同一布置目标的关联信息 | 目前不能建立可信来源隔离；去掉重复不等于已消除邻帧相关性 |
| 独立小目标样本 | 沿用A0-01：V2原分辨率2003框中面积<1024为0；长边缩至640后为22 | 去除增强相关性后的原始目标尺寸和来源组数量 | Unknown；22不是独立实例数。尺寸结论依赖明确坐标尺度，不能据此断言所有输入设置下都没有小目标 |
| 走廊覆盖验证 | 有分割真值，不能作实际测试输入 | 同帧原图框与掩膜对应、推理可得区域方案 | 未通过；本轮未运行走廊提取或检测 |

数据门仍未通过；即使作者补齐标签，仍需重新判断独立性、小目标数量和走廊条件，不能自动进入训练。方法新颖性High风险也没有因本次补证而降低。

## 3. 检索边界与去重

本批ID：`2026-09-10-A0-02`。沿用数据论文`W-0001`，新增论文0、论文版本更新0、既有工作补证1；不分配新Work ID，不复制正文。检索式：

- `"UAV-RSOD" original annotations github`
- `"UAV Railroad Images" dataset annotations version`
- `"s41597-024-03952-3" supplementary code availability`
- `"UAV-RSOD" "augmentation" "github"`
- `"UAV-RSOD" "original" "annotations" "315"`

结果主要回到正式论文、Zenodo和二手索引，未核实另一个作者发布的补充标注入口。普通RSOD、其他铁路数据及不相干论文不纳入本轮补证；未逐篇审计搜索中的旁支论文，不将其计为新增PASS/HOLD。未穷尽所有平台、私有资料和引用网络，不以搜索未命中证明资料不存在。

## 4. 可复核记录

只读核验脚本：[check_uav_rsod_sources.py](check_uav_rsod_sources.py)。本轮已实际执行，读取原包XML，保存小型官方响应；不调用训练框架。复核可在仓库根目录运行：

```text
python 00_Startup_Railway_UAV_Detection/Experiments/check_uav_rsod_sources.py
```

每次生成新的时间戳目录，不覆盖既有审计。此次快照：`11_Datasets/processed/UAV-RSOD/A0-02/20260910T143434854283Z/`（Git忽略，需另行迁移）。

| 文件 | SHA256 |
|---|---|
| record.json | 7e56ba8d6d2825961d3ef931888185b5e1d385a3dee4438ec0fcf887911c62e8 |
| versions.json | 2676c7d0ab5463beabdb38d51a28ab57901c69642db506e9ed415e38e31da889 |
| media.json | 08bb8ad432c10bdec10914fa777b2eee5ed965662ec8bdd8bb1b090880c2bbb7 |
| results.json | 562f1a887d2c0f492bd5fe5915e19d7bf38bccb606accdbfd60383263d7f8974 |

原包校验和、尺寸及重复清单沿用[A0-01](Data_Feasibility_Audit.md)，不伪称本轮重跑全部图像统计。两个原包未修改，未生成模型训练或推理记录。

## 5. 下一项唯一任务

交付验证：本地Markdown链接检查通过；4份快照SHA256与本报告一致；静态脚本实际运行并通过语法检查；7条主矩阵仍为19字段，W-0001补证未增加工作ID；文献联动完成。原练手目录与HEAD内容无差异，保护附件未改，Git跟踪PDF仍33份。未暂存、提交或推送；没有模型训练或检测推理记录。

**A0-03：审阅作者数据询问信并确认外部求证方式。** [英文草稿](A0-03_Author_Data_Request_Draft.md)已准备，尚未发送。成功标准：用户确认实际发信身份与发送决定；若发送并取得回复，再将可核验资料回写本报告。未获明确授权不发送；作者回复不能预设。等待期间保持HOLD，不自动转向B/C、补标或增加模块。
