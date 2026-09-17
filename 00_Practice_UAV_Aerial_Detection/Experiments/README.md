# Experiments（练手文）

**默认只读／HOLD：** 不新训、不新建 BTD 编号、不改网络。已有结果与脚本保留作证据。

## 分类索引（文件仍在本目录，避免打断相对链接）

### 计划与跟踪
- `Experiment_Plan.md` · `Experiment_Tracker.md`
- `Restricted_Baseline_Training_Plan.md` · `Diagnostic_Admission_Review.md`

### A0 可行性／数据／评价
- `A0-01` … `A0-08`（书面任务）
- `Data_Feasibility_Audit.md` · `VisDrone_Feasibility_Audit.md`
- `Label_Adapter_Check.md` · `Training_Interface_Audit.md` · `Weight_Source_Audit.md`
- `Official_Runtime_Crosscheck.md`

### BT1 基线训练
- 文档：`BT1_*.md`
- 脚本：`run_bt1.py` · `prepare_bt1_data.py` · `bt1_checkpoint.py` · `diagnose_bt1.py` · `preview_bt1.py` · `summarize_bt1_diagnosis.py` · `test_bt1_*.py` · `BT1_Cloud_Training.ipynb` · `baseline_training_spec.json`

### BTD 诊断（2–9、11）
- 协议／结果：`BTD*_*.md`
- 相关脚本：`analyze_*.py` · `compare_*.py` · `run_diag500_pair.py` · `run_fast_pipeline.py` · `verify_*.py` · `check_*.py` · `fast_stable_nms.py` · `finalize_conditional_recovery.py` 等

### 数据获取
- `acquire_visdrone.py` · `fetch_visdrone_mirror.py` · `convert_visdrone_labels.py` · `analyze_visdrone.py` · `analyze_uav_rsod.py` · `audit_uav_rsod.py` · `check_uav_rsod_sources.py`
- `run_official_octave_check.m`

缩写见 [`../../99_Attachments/Abbreviation_Glossary.md`](../../99_Attachments/Abbreviation_Glossary.md)。