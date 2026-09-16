# 归档清单（ARCHIVE_MANIFEST）

更新日期：2026-09-16（Asia/Shanghai）  
目的：记录合并学习前已做的归档副本，避免与“源已删除”混淆，并标明**未**被本归档复制的内容。

---

## 1. 核心声明

| 声明 | 状态 |
|---|---|
| 源项目目录是否删除 | **否。源未删除。** |
| 归档性质 | 用户本机快照副本，便于合并学习与回溯 |
| 本 `new_framework/` 草案 | 仅学习框架文档；不替代归档包本身 |
| 数据与权重 | 默认**不**因本次归档而复制 `11_Datasets` 下数据/权重（除非另行显式拷贝） |

---

## 2. 归档根路径（用户本机）

```text
D:\Doctoral-Research-Outline\99_Attachments\Archive_2026-09-16_PracticePaper\
```

其下应包含对练习论文相关目录的副本（以用户机实际文件夹名为准）。常见源与预期去向如下。

---

## 3. 源 → 归档去向

| 源路径（仓库内，相对 Doctoral-Research-Outline） | 归档去向（在 Archive_2026-09-16_PracticePaper 下） | 是否删除源 | 备注 |
|---|---|---|---|
| `00_PrePaper_Lightweight_Detection\` | `...\00_PrePaper_Lightweight_Detection\`（或同等命名副本） | **否** | 含历史 LSM-Head 计划、文献、学习笔记 00–06、旧实验预案 |
| `00_Startup_Railway_UAV_Detection\` | `...\00_Startup_Railway_UAV_Detection\`（或同等命名副本） | **否** | **已有 Experiments 文件夹一并复制进归档** |
| `00_Startup_Railway_UAV_Detection\Learning_Notes\07_*.md` | 随 Startup 副本进入归档 | **否** | 学习合并后 Startup 内另有 00–06 副本（见下） |
| `00_Overview\` 中与阶段相关的当时文件（若用户曾纳入） | 若存在于归档包则保留 | **否** | 以归档包实列为准 |
| `90_English_Learning\`（若纳入） | 若存在则保留 | **否** | 新框架另有更新版草案 |

> 精确子文件夹名以资源管理器中 `Archive_2026-09-16_PracticePaper` 实列为准；本表描述意图与边界。

---

## 4. 学习笔记合并（源仍保留）

用户已在本机将 PrePaper 学习笔记 **00–06** 复制到 Startup 的 `Learning_Notes/`，与原有 **07** 并列：

| 动作 | 源 | 目的 | 源删除？ |
|---|---|---|---|
| 复制学习笔记 00–06 | `00_PrePaper_Lightweight_Detection\Learning_Notes\00`–`06_*.md` | `00_Startup_Railway_UAV_Detection\Learning_Notes\` | **否** |
| 保留 07 | `...\Learning_Notes\07_Mainline_A_Knowledge_Chain.md` | 同目录并列 | **否** |

合并学习后：新框架的知识地图与记录模板指导**如何学**；旧笔记正文可继续作教材，不作废。

---

## 5. 明确未纳入 / 未复制项

| 内容 | 说明 |
|---|---|
| `11_Datasets` 下数据集与权重 | 通常被 gitignore；**本次归档默认不复制**。需要时单独、显式拷贝并登记。 |
| 云端未下载产物 | Kaggle/Colab 若未落盘，归档中不存在 |
| 本草案 `new_framework/` | 生成于助手工作区，供写入用户本地仓库；不是 Archive 文件夹的替代品 |
| Paper 1–7 其他目录 | 不在本次练习论文归档范围内，除非用户另行复制 |

---

## 6. 为何归档

1. **合并学习**：把轻量共享头历史材料与 Startup 主线学习收束到同一学习枢纽，同时保留分叉前快照。  
2. **保护实验资产**：Startup 下已有 BT1 / BTD 等实验协议与结果进入归档副本，防止后续整理误改时无可回退。  
3. **边界清晰**：负结果与书面否决留在归档证据中；LEARNING-CORE 不重跑、不删源。  
4. **主张纪律**：LSM-Head 与旧区域机制等退出执行后，仍可从归档与源目录查阅，避免“删掉等于没发生过”。

---

## 7. 使用建议

- 日常学习：以 Startup + 本新框架文档为准。  
- 回溯对比：打开 `Archive_2026-09-16_PracticePaper`。  
- 恢复误改：从归档副本拷回（拷回前先另存当前损坏版）。  
- 大数据：继续使用原 `11_Datasets` 路径策略；不要假设归档里有完整权重。

---

## 8. 检查清单（用户可勾）

- [ ] 本机存在 `D:\Doctoral-Research-Outline\99_Attachments\Archive_2026-09-16_PracticePaper\`
- [ ] 其下可见 PrePaper 与 Startup 相关副本
- [ ] Startup 归档副本中含 `Experiments\`
- [ ] 源目录 `00_PrePaper_Lightweight_Detection` 与 `00_Startup_Railway_UAV_Detection` 仍在
- [ ] Startup `Learning_Notes` 中可见 00–06 与 07
- [ ] 确认 `11_Datasets` 未被本归档重复占用磁盘（除非曾显式复制）
