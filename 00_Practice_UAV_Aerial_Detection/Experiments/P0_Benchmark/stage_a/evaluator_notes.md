# Evaluator notes (Stage A pointer)

- 00_Practice_UAV_Aerial_Detection/Experiments/A0-07_Evaluator_Semantics_Check.md
- 00_Practice_UAV_Aerial_Detection/Experiments/check_label_adapter.py
- 00_Practice_UAV_Aerial_Detection/Experiments/convert_visdrone_labels.py
- 00_Practice_UAV_Aerial_Detection/Experiments/Label_Adapter_Check.md
- 00_Practice_UAV_Aerial_Detection/Experiments/A0-06_Evaluation_Protocol_Draft.md
- 00_Practice_UAV_Aerial_Detection/Experiments/A0-07_Evaluator_Semantics_Check.md

Frozen eval gates for P0 benchmark (from instruction + BTD8):
- conf_thres = 0.25
- IoU_thres = 0.50
- small object = 0 < w*h < 1024 in original pixel space
- VisDrone class mapping / ignore / matching: follow A0-07 and existing Label Adapter docs; do not mix native Ultralytics AP with VisDrone-compatible evaluator without naming.
