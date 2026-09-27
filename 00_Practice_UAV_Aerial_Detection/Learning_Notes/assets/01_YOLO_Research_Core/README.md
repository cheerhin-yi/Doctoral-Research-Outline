# 01_YOLO_Research_Core 图片资源

这些是 `../../01_YOLO_Research_Core.md` 中嵌入的示意图（助手 2026-09-27 绘制，内容按通用 Ultralytics YOLOv8／YOLO11）。

- 源文件：`.mmd`（Mermaid）。
- 渲染：mermaid-cli（`mmdc -b white`），生成 `.svg` 和 2 倍分辨率的 `.png`。
- 嵌入方式：笔记用 `![[assets/01_YOLO_Research_Core/<name>.png]]` 嵌入 PNG，因为 SVG 里的文字放在 foreignObject 中，在部分查看器中可能无法显示。
- 修改方法：改 `.mmd` 后重新渲染，例如 `npx -y @mermaid-js/mermaid-cli -i 01_yolo_c2f.mmd -o 01_yolo_c2f.png -b white -s 2`。

| 图片 | 源文件 | 内容 | 嵌入位置（笔记章节） |
|---|---|---|---|
| `01_yolo_chain_overview.png` | `01_yolo_chain_overview.mmd` | Backbone→Neck→Head→训练／推理总览 | 知识链七行摘要之后 |
| `01_yolo_preprocess.png` | `01_yolo_preprocess.mmd` | 训练与推理的预处理／增强差别 | §1 输入与预处理 |
| `01_yolo_c2f.png` | `01_yolo_c2f.mmd` | C2f 数据流（cv1→拆分→Bottleneck→Concat→cv2） | §2.2 C2f |
| `01_yolo_backbone.png` | `01_yolo_backbone.mmd` | Backbone 第 0–9 层与三路输出 | §2.3 模块组成 |
| `01_yolo_sppf.png` | `01_yolo_sppf.mmd` | SPPF 串联池化 | §2.4 SPPF |
| `01_yolo_neck.png` | `01_yolo_neck.mmd` | FPN + PAN 逐层连接（第 10–22 层） | §3 Neck |
| `01_yolo_head.png` | `01_yolo_head.mmd` | 单尺度解耦头的定位／分类分支 | §4.1 Head 结构 |
| `01_yolo_tal.png` | `01_yolo_tal.mmd` | TAL 正样本分配流程 | §4.2 第 8 条 |
| `01_yolo_nms.png` | `01_yolo_nms.mmd` | NMS 流程 | §4.2 第 9 条 |
| `01_yolo_train.png` | `01_yolo_train.mmd` | 训练分支 | §5 训练分支 |
| `01_yolo_infer.png` | `01_yolo_infer.mmd` | 推理分支 | §6 推理分支 |
