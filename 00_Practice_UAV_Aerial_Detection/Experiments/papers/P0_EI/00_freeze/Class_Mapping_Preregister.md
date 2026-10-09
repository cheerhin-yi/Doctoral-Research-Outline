# Stage E — VisDrone → UAVDT class mapping (pre-registered, pre-results)

**Status:** FROZEN before any Stage E predictions.

## UAVDT DET classes

car, truck, bus (standard UAVDT detection taxonomy).

## Included mapping

| VisDrone (YOLO id) | VisDrone name | UAVDT name | UAVDT id |
|---:|---|---|---:|
| 3 | car | car | 0 |
| 4 | van | car | 0 |
| 5 | truck | truck | 1 |
| 8 | bus | bus | 2 |

van → car is an explicit merge for cross-benchmark vehicle comparability.

## Excluded (not scored)

pedestrian, people, bicycle, tricycle, awning-tricycle, motor.

## Hard rules

- Same frozen last.pt; **no** UAVDT fine-tune.
- Mapping **must not** change after seeing scores.
- Stage E only checks trend under domain shift — not SOTA on UAVDT.

> 2026-09-27：第 7、18 行文本编码修复（去除误入的控制字符 `\t`/`\b`/`\v`，恢复 truck/bus/van 字样，与 `class_mapping_preregister.json` 一致）。**映射本身未改**。

> AI生成
