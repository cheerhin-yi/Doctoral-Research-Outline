# BT1普通YOLO11n：100轮归档核验

2026-09-13。**训练完成，归档PASS；末轮权重准入受限开发诊断。** 没有重新训练或重新选模，不代表正式来源门、创新效果或投稿要求通过。

## 训练身份与连续性

| Run ID | 实际轮次 | 状态 | 本段墙钟秒 |
|---|---|---|---:|
| BT1-LOCAL-20260912-01 | 1–3 | 已完成、按原安排暂停 | 1121.17 |
| BT1-LOCAL-20260912-02 | 4 | 接续核验完成、暂停 | 378.20 |
| BT1-LOCAL-20260913-01 | 5–100 | PASS、进程结束 | 52463.16 |

三份CSV合并后恰好1–100，无缺轮、重复或非有限数值。各段CSV的time重新计时，合并表保留原值，不能当连续时间轴。上述墙钟合计约14.99小时，包含系统等待，不是实测GPU计费小时。第3→4和第4→5轮接续状态已有PASS证据；数据加载器重建，不声称逐位等价于单进程不中断训练。

配置保持普通YOLO11n P3–P5，VisDrone train6471、cal48监控，seed0，640，batch4，FP32，100轮SGD；GTX1660SUPER 6GiB，独立环境`H:/Conda/envs/UAV_BT1`。固定Ultralytics 8.4.90提交`07958a70205d1388612bd00f8a2f32cf769d8fed`，torch2.7.1+cu126。未改网络、损失或候选专用模块。

## 最终权重与证据

- [第100轮last.pt](../../11_Datasets/processed/VisDrone/BT1/BT1-LOCAL-20260913-01/train/weights/last.pt)：SHA256 `bc42d54e37acaf1f698af487439dc222fa86fb4498623e8cf954df14e0aa5533`。
- `last_pre_strip.pt`内部epoch=99（对应第100轮），优化器仍在；逐张量核对其EMA与最终last一致。框架best保留在原运行，但本批未选用。
- 最终恢复ZIP通过CRC；内部checkpoint哈希与manifest一致，completed_epochs=100。
- 训练末尾10张固定cal图输出检查及P3/P4有限值检查PASS。原完整性检查使用框架默认rect，得到48×80、24×40；本次诊断显式rect=false，得到80×80、40×40，不能混淆两种输入形状。
- 数据清单、固定配置、训练日志与执行快照、环境清单、三段运行状态、最后权重、原始末轮与恢复包已复制归档；原产物未覆盖。没有复制全部原始数据，数据原包与转换旁文件仍按既有路径保存。

统一证据目录：[BTD1-CAL48-20260913-01](../../11_Datasets/processed/VisDrone/BT1/BTD1-CAL48-20260913-01)。

## 第100轮原生监控值

| 指标 | 数值 |
|---|---:|
| Precision | 0.46533 |
| Recall | 0.34912 |
| mAP50 | 0.34101 |
| mAP50–95 | 0.18591 |
| train box / cls / DFL loss | 1.40618 / 0.94879 / 0.88699 |

数值来自第100轮CSV，属于cal48原生训练监控。固定源码`trainer.py:887`的final_eval另外验证best，因此stdout结尾约0.344/0.187的AP不能替换第100轮值；这没有改变本批使用last的选模规则。原生AP不是本项目官方兼容指标，也不能与下述固定conf=.25的诊断Recall直接相比。

## 归档位置与限制

实际归档根目录为`11_Datasets/processed/VisDrone/BT1/BTD1-CAL48-20260913-01/`：

- `baseline_archive/epochs_001_100.csv`：连续100轮表。
- `baseline_archive/archive_manifest.json`：各文件来源、长度、SHA、末轮与恢复包检查。
- `BT1_100epochs_evidence.zip`：46,344,126字节；SHA256 `9419bf3cc870b1e7c940a7075d0092acf11d65711b19165f0d2ea6486cad21b0`。
- `archive_check.json`：归档PASS。该包在同一块本机磁盘，不是异地备份，也没有上传云端。

train维护者副本的作者字节身份Unknown、共享场景／来源组Unknown、训练无区域级ignore、单seed、cal48已用于训练监控等局限保留；不得将本结果视为正式独立测试。

下一项研究证据已在同轮取得，见[cal48漏检诊断](BT1_Cal48_Miss_Diagnosis.md)。不重开100轮训练或学习验收。
