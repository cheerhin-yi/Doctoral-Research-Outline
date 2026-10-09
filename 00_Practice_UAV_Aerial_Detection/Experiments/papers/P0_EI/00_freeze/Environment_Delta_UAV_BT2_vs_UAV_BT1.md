# 环境差异：UAV_BT2（现用）vs UAV_BT1（冻结）

> 记录日期：2026-10-06（Asia/Shanghai）。本文件只补记，不改动 `Environment_Freeze.md`、`env_snapshot.txt`、`pip_freeze.txt` 及 Stage D/E 冻结 JSON 中的原始记录。

## 1. 状态

| 项 | 内容 |
|---|---|
| UAV_BT1（冻结） | `H:\Conda\envs\UAV_BT1`，Stage A–F 全部结果所用环境（`Environment_Freeze.md`、`env_snapshot.txt`、`pip_freeze.txt`、`stage_d/e_config_freeze.json`）。2026-10-04 换盘后 H: 分区不再挂载，该环境已不存在。可按 `.temp/conda-backup/UAV_BT1_conda-export.yml` 与 `UAV_BT1_pipfreeze.txt`（2026-09-29 15:57 导出，未入库）重建 |
| UAV_BT2（现用） | `F:\Conda\envs\UAV_BT2`，2026-10-04 新建；**2026-10-06 用户决定正式采用**，用于 Run G（RTX 5060 Ti 正式时序）及以后的任何重跑 |
| 不变 | 冻结权重 `last.pt`（SHA256 `bc42d54e37acaf1f698af487439dc222fa86fb4498623e8cf954df14e0aa5533`）、五协议定义与参数、评价器（`diagnose_bt1.prepare_gt + match_gt`）、类映射、运行脚本 |
| 快照（2026-10-06 16:12） | `env_snapshot_UAV_BT2_20261006.txt`、`pip_freeze_UAV_BT2_20261006.txt`、`conda_explicit_UAV_BT2_20261006.txt`（同目录） |

## 2. 版本差异

UAV_BT1 列取自 Stage A 冻结快照（2026-09-17）；Stage A 之后才装的包（sahi、scipy）取自 2026-09-29 的 UAV_BT1 备份。

| 项 | UAV_BT1（冻结） | UAV_BT2（现用） | 判断 |
|---|---|---|---|
| GPU | GTX 1660 SUPER 6 GiB，`GPU-43b14c17-b685-e8ad-ab90-abc0d70fca06`，sm_75 | RTX 5060 Ti 16 GiB（16311 MiB），`GPU-1d6d4cde-f073-217b-3867-015abdbd5478`，sm_120 | 不同硬件，计时只能各自成表 |
| 驱动 | 591.86 | 591.86（nvidia-smi 显示 CUDA 13.1） | 相同 |
| Python | 3.12.14（conda-forge） | 3.10.22（Anaconda） | **不同** |
| torch / torchvision | 2.7.1+cu126 / 0.22.1+cu126 | 2.7.1+cu128 / 0.22.1+cu128 | 版本相同，CUDA 构建不同（cu126 不支持 sm_120） |
| CUDA runtime / cuDNN | 12.6 / 90701 | 12.8 / 90701 | runtime 不同，cuDNN 相同 |
| ultralytics | 8.4.90，pinned `11_Datasets/processed/VisDrone/BT1/execution_2026-09-12/ultralytics-07958a7.zip`，sha256 `c415c540760c1e282fb3caa212ae963fe4c0667633fb9aed113a8ceb261bfa80` | 8.4.90，`direct_url.json` 指向同一 zip、同一 sha256 | **一致** |
| ultralytics-thop | 2.1.6 | 2.1.6 | 相同 |
| opencv-python | 5.0.0.93 | 5.0.0.93 | 相同 |
| pillow | 12.3.0 | 12.3.0 | 相同 |
| numpy | 2.5.2 | 2.2.6 | **不同** |
| sahi | Stage A 未装；运行时版本未冻结（`Reproducibility_Appendix.md` §10 开放项）；09-29 备份为 0.11.32 | 0.11.32 | 与 BT1 最后状态一致；Stage B–E 运行时的版本仍无法证明 |
| scipy（Stage F Wilcoxon） | Stage A 未装；09-29 备份为 1.18.1 | 1.15.3 | **不同** |
| matplotlib（`generate_plots.py`） | 3.11.2 | 3.10.9 | 不同；重生成的图样式可能有细微差异 |
| contourpy / networkx | 1.4.0 / 3.6.1 | 1.3.2 / 3.4.2 | 间接依赖 |
| sahi 依赖（pybboxes、shapely、fire、terminaltables、termcolor、tqdm 等） | 09-29 备份中已有 | 已有 | 与备份一致 |
| platform 字符串 | Windows-11-10.0.26200 | Windows-10-10.0.26200 | 同一系统版本号；Python 3.10 的 `platform` 把 Windows 11 报成 Windows-10 |

## 3. 使用规则

1. **Run G 计时：** RTX 5060 Ti + UAV_BT2，按 `P0-BENCH-G-5060TI-{SMOKE,CAL48,TESTDEV}-20261001-01` 运行；结果只写 `04_timing/Timing_5060Ti_Table.md`，**永不**与 1660／UAV_BT1 的时延放进同一表或同一列。
2. **精度重跑：** 在 UAV_BT2 下的任何精度重跑（子集或全量）须登记新 Run ID，并与冻结数字逐项核对（同图同协议的 tp、fp、small_tp）；差异如实记录。冻结的 Stage D／E／F 数字不被替换。
3. **统计重算：** 即使只在 CPU 上重算 Stage F 类统计，scipy 版本已变，也须登记新 Run ID。
4. Run G 开始当天若环境有任何变动，须再抓一次快照，存为新的带日期文件。

> AI生成
