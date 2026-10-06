# 01_YOLO_Research_Core 图片资源

`../../01_YOLO_Research_Core.md` 中「助手批注」里嵌入的示意图（助手 2026-09-27 绘制，2026-10-06 改为紧凑 SVG）。内容按通用 Ultralytics YOLOv8／YOLO11，不含 P0 设置。

- 源文件：`<name>.mmd`（Mermaid）；样式配置：`_mermaid_config.json`（base 主题、白底、1px 灰线、一种浅蓝强调色、13px 无衬线字体、`htmlLabels:false`）。
- 渲染：`@mermaid-js/mermaid-cli@10.9.1`（新版在 `htmlLabels:false` 下文字测宽不准），`mmdc -c _mermaid_config.json -i <name>.mmd -o <name>.svg -b white -q`；渲染后把箭头 `markerWidth/Height` 由 12 改为 8，并给 `edgeLabel rect` 加内联 `fill:#ffffff;opacity:1`。
- SVG 里是真文字（无 `foreignObject`），每张 10–17 KB；不再保留 PNG。
- 嵌入方式：每张图放在对应批注里的折叠 callout 中，固定宽度，例如
  `> > [!example]- 图：C2f 结构` / `> > ![[01_yolo_c2f.svg|680]]`。Obsidian 按文件名解析，故文件名保持唯一。

| 图片 | 内容 | 所在批注（笔记章节） | 嵌入宽度 |
|---|---|---|---:|
| `01_yolo_chain_overview.svg` | 输入→Backbone→Neck→Head→训练／推理总览 | 知识链七行摘要之后 | 660 |
| `01_yolo_preprocess.svg` | 训练与推理的预处理／增强差别 | §1 输入与预处理 | 680 |
| `01_yolo_c2f.svg` | C2f 数据流（cv1→拆分→Bottleneck→Concat→cv2） | §2.2 C2f | 680 |
| `01_yolo_backbone.svg` | Backbone 第 0–9 层与三路输出 | §2.3 模块组成 | 680 |
| `01_yolo_sppf.svg` | SPPF 串联池化 | §2.4 SPPF | 680 |
| `01_yolo_neck.svg` | FPN + PAN 连接（P3／P4／P5） | §3.3 总结 | 680 |
| `01_yolo_head.svg` | 单尺度解耦头的定位／分类分支 | §4.1 结构 | 500 |
| `01_yolo_tal.svg` | TAL 正样本分配 | §4.2 工作模块 | 640 |
| `01_yolo_nms.svg` | NMS 流程（IoU 0.7，最多 300 框） | §4.2 工作模块 | 680 |
| `01_yolo_train.svg` | 训练分支 | §5 训练分支 | 680 |
| `01_yolo_infer.svg` | 推理分支 | §6 推理分支 | 680 |
