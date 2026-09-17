# 当前阶段（唯一入口）

更新：2026-09-17（Asia/Shanghai）。

本文件是全项目**唯一当前事项入口**。与源文件冲突时，以本页与 [`Research_Question_Decision_2026-09-16.md`](../00_Practice_UAV_Aerial_Detection/Research_Question_Decision_2026-09-16.md) 为准。

| 入口 | 路径 |
|---|---|
| 练手现行目录 | [`00_Practice_UAV_Aerial_Detection/`](../00_Practice_UAV_Aerial_Detection/README.md) |
| P0 Benchmark | [`Experiments/P0_Benchmark/`](../00_Practice_UAV_Aerial_Detection/Experiments/P0_Benchmark/) |
| T4 过程目录（G 盘） | `G:\Schloar Data\P0_T4_Train\` |
| UAVDT（G 盘） | `G:\Schloar Data\UAVDT\`（布局 PASS：50 序列／40735 帧／50×gt_whole） |

---

## 当前唯一事项

**P0 训练轨已授权（用户 2026-09-17 选 B）：在 Kaggle 双 T4 按锁定配方训练／重训，冻结新权重后重跑对比，并继续面向 2027 EI 会期写稿。**

原「只冻结推理、禁止新训」门已打开；**开训前仍须锁定具体配方**。旧 D/F（1660SUPER）结果保留为历史对照，不删除。

主张骨架仍为 **P0-EI-C1／C2**，但表述改为「T4 训练后的协议对比」——正文须重写，不得再写「全程未训练」。Paper 2–7 仍 PAUSED。

---

## 进度

| 项 | 状态 |
|---|---|
| A–D／F（旧冻结 last.pt，1660SUPER） | PASS（历史对照） |
| E 数据 UAVDT | 布局 PASS；训练／推理未跑 |
| T4 训练轨 | 配方待锁；本机 kaggle CLI／kaggle.json 未就绪 |
| 新权重五方法重跑 | 未开始 |
| 4090 正式时序 | 仍缺；与 T4 分列披露 |

旧冻结权重：`BT1-LOCAL-20260913-01/train/weights/last.pt`，SHA256 `bc42d54e37acaf1f698af487439dc222fa86fb4498623e8cf954df14e0aa5533`。

---

## 实验门

- 训练／微调：已授权，仅限本页锁定配方与 Run ID；禁止顺手改 backbone／loss／头。
- 过程文件 → `G:\Schloar Data\P0_T4_Train\`；终表／Run 记录 → 仓库 `Experiments/`。
- 第三方 UAVDT 子集仍禁止作主库。

### 开训前必须锁定

1. 仅 VisDrone 重训／仅 UAVDT 微调／先 VisDrone 再 UAVDT  
2. 初始化：COCO yolo11n.pt 或续训旧 last.pt  
3. 是否复用 baseline_training_spec（含 100 epoch 等）  
4. Kaggle API 凭证与双 T4 notebook 就绪  

---

## 下一步

1. 用户回复配方 **B1／B2／B3**（见对话）。  
2. 配置 `%USERPROFILE%\.kaggle\kaggle.json` 并安装 kaggle CLI。  
3. 上传数据与权重，提交 2×T4 训练 Run 并登记 ID。  
4. 新权重冻结后重跑五方法。  
