# 原版评价代码的Octave兼容交叉核验

日期：2026-09-11。状态：**有限兼容核验通过，24/24，最大绝对差异0。** 本轮实际执行作者评价函数，补齐A0-07未完成的运行证据；运行时为GNU Octave，不是MATLAB。A0整体及模型准入仍未通过。

## 1. 实际完成

从[Octave官方下载入口](https://octave.org/download)获取11.3.0 Windows 64位压缩包，独立解压到被忽略的`11_Datasets/external/octave-11.3.0/`。实际可执行文件为`octave-11.3.0-w64/mingw64/bin/octave-cli.exe`；未运行系统安装器、未改全局PATH或Codex Python环境。命令使用无GUI、无历史、忽略用户初始化文件的模式。

压缩包481127074字节，SHA256：`fd3cf0e885467a15211b8ceded42800432a5462481324d49a896ef257e05d1a0`。官方下载地址重定向到GNU镜像`mirror.checkdomain.de`；下载记录保留原始和最终URL。本次记录本地完整性校验，未核验GPG签名，不把本地SHA称为独立签名验证。Octave为GPLv3软件，随包image 2.20.0元数据标明GPLv3+。

使用现有A0-05工具包ZIP，固定提交`005445782213e20cb91bc50a597db3dd949e749a`，校验值仍为`30298f4e0b56dcb5a49ab4a0d790b2c3329da5fa4391757920b74294351ff3b6`。解包到本轮新输出目录，运行前后11个原包文件校验一致。

调用A0-07/probe_02现有`run_a007_official.m`，其SHA仍为`c7164829182f23624f71dbe1b6406391fdcc1daee60bb81a00a637d38b9b4170`。新增[运行包装器](run_official_octave_check.m)只负责加载依赖、调用、记录和导出，未修改输入、断言预期或作者函数。`mean2`来自随包image 2.20.0，源码SHA为`a1d766f961fdb245edbf52a7f1a4d20eced94b56fc803a99f7094f0a089f773a`；实现为`mean(I(:))`，没有自写替代函数或安装额外包。

## 2. 结果及证据边界

| 检查 | 实际结果 |
|---|---|
| 运行批次 | attempt_01，一次执行完成，进程退出0 |
| 断言 | 24/24通过；24个结果字段齐全 |
| 对原手算预期 | 最大绝对差异0，阈值1e-8 |
| 对已保存Python结果 | 最大绝对差异0；只是比较旧JSON，没有重跑Python评价器 |
| 作者源码、旧输入与调用入口 | 校验一致，未修改 |
| MATLAB／真实图像／检测模型 | 均未运行 |

逐项输出、预期与差异见本轮`comparison.json`及`comparison.csv`，用例解释沿用[A0-07报告](A0-07_Evaluator_Semantics_Check.md)，不重复抄录24条。结果覆盖全图截断、类别重复汇总、ignore处理、IoU边界和小目标诊断等既有构造条件。C19/20/21/24使用项目小目标统计包装并调用作者匹配函数，不能称为官方自带小目标指标。

结论只支持“指定提交在Octave 11.3.0＋image 2.20.0下，对这24项构造条件符合已有预期”。不证明MATLAB逐位等价、所有同分排序／数值边界、实际模型导出接口、官方服务端或完整真实数据表现。正式诊断仍需核对导出字段、类别、顺序与计时接口；没有新疑点时不再扩展或重跑本批构造核验。

## 3. 产物与复核方式

本轮输出根目录：`11_Datasets/processed/VisDrone/Official_Runtime_Check_2026-09-11/`，被Git忽略。

- `runtime_download.json`：来源、字节数、下载SHA。
- `toolkit_sha256_before.json`、`toolkit/`：运行前校验与未改动作者源码。
- `attempt_01/runtime.json`：Octave／包版本、实际函数解析路径、通过状态。
- `attempt_01/octave.log`、`actual.json`：实际调用日志与24项原始数值。
- `attempt_01/original_save.mat`：旧入口原生保存；`results_matlab_format.mat`为额外MAT格式副本，仅格式转换，不代表已由MATLAB读取。
- `comparison.json`、`comparison.csv`：与预期和旧Python输出逐项比较。

必要复核时使用独立新输出目录，调用`run_official_octave_check(repoDir, outputDir)`；包装器拒绝覆盖既有目录。运行命令参数由实际路径组成，示例：

```text
octave-cli.exe --no-gui --no-history --no-init-file --quiet --eval "addpath('D:/Doctoral-Research-Outline/00_Startup_Railway_UAV_Detection/Experiments'); run_official_octave_check('D:/Doctoral-Research-Outline','D:/Doctoral-Research-Outline/11_Datasets/processed/VisDrone/Official_Runtime_Check_2026-09-11/attempt_02');"
```

示例attempt_02没有运行。运行时在忽略目录，不随Git迁移；在新电脑复核需按本报告版本和校验准备运行时。既有A0-07报告保留当时“未运行”历史状态，当前补证以本报告为准。

## 4. 当前准入与下一项唯一任务

[诊断准入](Diagnostic_Admission_Review.md)中的本批评价兼容条件获得有限PASS；权重、检测环境、本人学习和模型输入输出接口条件仍未齐，全部模型BLOCKED。来源Unknown仍限制正式主张，S0-01未通过，国奖适用性待学院／年份核验。

**下一项：轻量基线权重来源与十类映射核查（只读）。** 优先核实普通YOLO11n的公开VisDrone权重是否有可复核训练数据、checkpoint选择、十类顺序、软件版本和使用条件；默认COCO权重不视为合格十类基线。先限定作者／官方可追溯入口；没有合格权重就给出缺口与是否需要受限训练的决策材料，不自动训练或改网络，不下载来源不明权重。已通过的本批评价核验不再作为下一轮工作。

本轮无论文新增、真实数据下载、检测依赖安装、训练、推理或模型Run ID；不提交、不推送，Paper 1及七篇路线不变。

## 5. 交付检查

新增本报告与运行包装器2份，更新入口／计划7份；75个本地链接检查通过，Git差异检查通过。46份既有文献、A0-05至A0-09审计、构造脚本、台账与实验追踪保持本轮前校验值；保护目录、七篇路线与Paper 1研究计划相对HEAD无内容差异，跟踪PDF仍33份。暂存区为空，未提交／推送。运行时及数值输出均被Git忽略，交付核对与产物校验见本轮`delivery_verification.json`。
