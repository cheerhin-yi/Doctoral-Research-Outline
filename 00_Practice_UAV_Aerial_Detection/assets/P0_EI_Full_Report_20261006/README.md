# P0_EI_Full_Report_20261006 图片资源

`../../P0_EI_Full_Report_20261006.md` 中嵌入的示意图（助手 2026-10-06 绘制）。配色与 `Learning_Notes/assets/01_YOLO_Research_Core/` 一致：白底、1px 灰线 `#9ca3af`、浅蓝强调 `#eef4ff`／`#7c9fdc`、13px 无衬线中文字体；另加一种浅橙 `#fff7e6`／`#d4a24c` 标“波折／撤回”。

- 源：`_make_svgs.py`（手写 SVG，无 mermaid）。在本目录执行 `python _make_svgs.py` 重新生成。
- SVG 里是真文字（无 `foreignObject`、无位图）。
- 嵌入方式：折叠 callout + 固定宽度，例如 `> [!example]- 图：…` / `> ![[p0fr_protocols.svg|700]]`。Obsidian 按文件名解析，文件名保持唯一（前缀 `p0fr_`）。

| 图片 | 内容 | 所在章节 | 嵌入宽度 | 数字来源 |
|---|---|---|---:|---|
| `p0fr_protocols.svg` | 五种推理协议在 1400×788 图上的视图（窗口起点、前向次数、finalize） | §3.3 | 700 | `P0_EI/04_timing/data/I_PIXLAT_summary.json`（Run I）；`P0_EI/05_packaging/Reproducibility_Appendix.md` §2.1（Run J） |
| `p0fr_timeline.svg` | 2026-09-10 至 10-06 时间线 | §4 | 720 | 报告 §4 各节所列来源 |
