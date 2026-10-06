# -*- coding: utf-8 -*-
"""Hand-written compact SVGs for P0_EI_Full_Report_20261006.md (same palette as Learning_Notes/assets/01_YOLO_Research_Core).
Run:  python _make_svgs.py   (writes p0fr_timeline.svg, p0fr_protocols.svg next to this file)
All geometry numbers come from the report sources (Run I geometry_by_size; Reproducibility_Appendix §2.1)."""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent
FONT = "'Noto Sans CJK SC','Microsoft YaHei','PingFang SC','Segoe UI',sans-serif"
TXT, GRAY, LINE, BAND, BAND_B = "#1f2937", "#6b7280", "#9ca3af", "#fafafa", "#d1d5db"
ACC_F, ACC_S = "#eef4ff", "#7c9fdc"
WARN_F, WARN_S = "#fff7e6", "#d4a24c"


def svg_open(w, h):
    return [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'style="background-color:white" font-family="{FONT}" font-size="13">',
            f'<rect x="0" y="0" width="{w}" height="{h}" fill="#ffffff"/>']


def text(x, y, s, size=13, fill=TXT, anchor="start", weight="normal"):
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" '
            f'font-weight="{weight}">{escape(s)}</text>')


def rect(x, y, w, h, fill="#ffffff", stroke=LINE, sw=1, rx=3, extra=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" {extra}/>'


# ---------------------------------------------------------------- timeline
def timeline():
    phases = [
        ("准备", [("09-10", "转主线 A；VisDrone 文件审计 A0-05（官方 Drive 配额超限 → Ultralytics 镜像）", 0)]),
        ("基线与诊断", [
            ("09-12", "批准受限普通基线；Kaggle 手机验证未完成、Colab 版本检查失败 → 改本机 1660 SUPER", 0),
            ("09-12~13", "BT1：YOLO11n 训练 100 轮（三段接续，墙钟约 14.99 h）→ 冻结 last.pt", 1),
            ("09-13~14", "BTD1–BTD11 诊断；BTD8 密度单片 DensK1；BTD9 发现 F1280 强简单基线", 0),
            ("09-16", "决定：不做新机制，只写 EI 推理协议对比稿（C1／C2）", 1),
        ]),
        ("冻结对比", [
            ("09-17", "Stage A 冻结 → B 计时 → C cal48 → D test-dev 一次性终评 → F 配对统计（1660）", 1),
            ("09-17", "冻结 UAVDT 类别映射；UAVDT 下载：作者 Drive 限流 → Zenodo 断流 → 百度网盘", 2),
            ("09-17~18", "T4／Kaggle 重训轨：09-17 选定，Kaggle V1 失败，09-18 撤回（无新权重）", 2),
            ("09-18", "Stage E UAVDT 全量 40735 帧 × 5 协议（墙钟约 4.76 h）", 1),
        ]),
        ("整理", [
            ("09-20", "周报：正式时序计划在 4090 上跑（从未运行）", 0),
            ("09-27", "仓库整理；C1 由“更准且更快”改为“时延不可区分下更准”；Overview", 0),
            ("09-28~29", "学位分备忘：CCF-C／普通 EI 学术博士不计分", 0),
        ]),
        ("正式时序与补充", [
            ("10-01", "本机 GPU 换为 RTX 5060 Ti 16GB；Run G 由 4090 改为 5060 Ti", 0),
            ("10-04", "换盘后 H: 分区丢失 → 冻结环境 UAV_BT1 不复存在", 2),
            ("10-06", "采用 UAV_BT2；Run G（5060 Ti）全部 PASS；C1 时延改为分 GPU 表述", 1),
            ("10-06", "CPU-only 补充分析 Run H／I／J／K（无新推理、无训练）", 1),
        ]),
    ]
    rows = sum(len(p[1]) for p in phases)
    rh, top, w = 24, 34, 760
    h = top + rows * rh + len(phases) * 8 + 34
    o = svg_open(w, h)
    o.append(text(12, 20, "P0_EI 时间线（2026，Asia/Shanghai；依据见报告 §4）", 13, TXT, weight="bold"))
    y = top
    xline = 178
    for name, evs in phases:
        ph_h = len(evs) * rh
        o.append(rect(8, y - 2, w - 16, ph_h + 4, BAND, BAND_B, 1, 3))
        o.append(text(18, y + ph_h / 2 + 5, name, 12, GRAY))
        for d, s, kind in evs:
            cy = y + rh / 2
            fill, stroke = {0: ("#ffffff", LINE), 1: (ACC_F, ACC_S), 2: (WARN_F, WARN_S)}[kind]
            o.append(f'<line x1="{xline}" y1="{y}" x2="{xline}" y2="{y + rh}" stroke="{LINE}" stroke-width="1"/>')
            o.append(f'<circle cx="{xline}" cy="{cy}" r="4" fill="{fill}" stroke="{stroke}" stroke-width="1"/>')
            o.append(text(xline - 10, cy + 4.5, d, 12, GRAY, "end"))
            o.append(rect(xline + 12, y + 3, w - xline - 32, rh - 6, fill, stroke, 1, 3))
            o.append(text(xline + 20, cy + 4.5, s, 12))
            y += rh
        y += 8
    ly = y + 14
    for i, (lab, f, s) in enumerate([("关键产出／决定", ACC_F, ACC_S), ("波折／撤回／丢失", WARN_F, WARN_S), ("背景事件", "#ffffff", LINE)]):
        x = 190 + i * 170
        o.append(rect(x, ly - 10, 14, 12, f, s, 1, 2))
        o.append(text(x + 20, ly, lab, 12, GRAY))
    o.append("</svg>")
    (OUT / "p0fr_timeline.svg").write_text("\n".join(o), encoding="utf-8")


# ---------------------------------------------------------------- protocols
def protocols():
    S = 0.13               # 1400x788 image -> 182 x 102.4 px
    IW, IH = 1400, 788
    pw, ph = 236, 214
    w, h = 3 * pw + 16, 2 * ph + 46
    o = svg_open(w, h)
    o.append(text(12, 20, "五种推理协议在一张 1400×788 VisDrone 图上的视图（几何依据：Run I；附录 §2.1）", 13, TXT, weight="bold"))
    W640 = 640 * S
    panels = [
        ("F640", "整图缩到 640²（缩放 0.457）", "1 次前向", [], False),
        ("F1280", "整图缩到 1280²（缩放 0.914）", "1 次前向", [], False),
        ("DensK1", "F640 + 框中心最多的 1 个窗", "2 次前向；窗：原生分辨率", [(760, 0)], True),
        ("UnifAll", "F640 + 网格全部 6 窗（步长 512）", "7 次前向；x∈{0,512,760} y∈{0,148}", [(x, y) for y in (0, 148) for x in (0, 512, 760)], False),
        ("SAHI640", "sahi 6 片（步长 480）+ 整图", "7 次前向；x∈{0,480,760} y∈{0,148}", [(x, y) for y in (0, 148) for x in (0, 480, 760)], False),
    ]
    for i, (name, l1, l2, wins, sel) in enumerate(panels):
        col, row = (i % 3, i // 3)
        px = 8 + col * pw
        py = 32 + row * ph
        o.append(rect(px, py, pw - 8, ph - 8, BAND, BAND_B, 1, 3))
        o.append(text(px + 10, py + 18, name, 13, TXT, weight="bold"))
        ix, iy = px + (pw - 8 - IW * S) / 2, py + 28
        # image
        o.append(rect(ix, iy, IW * S, IH * S, "#ffffff", LINE, 1, 0))
        if name in ("F640", "F1280"):
            o.append(text(ix + IW * S / 2, iy + IH * S / 2 + 4, "整图", 12, GRAY, "middle"))
        for (x, y) in wins:
            f = WARN_F if sel else ACC_F
            s = WARN_S if sel else ACC_S
            o.append(rect(ix + x * S, iy + y * S, W640, W640, f, s, 1, 0, 'fill-opacity="0.45"'))
        if name == "SAHI640":
            o.append(text(ix + IW * S / 2, iy + IH * S + 13, "+ 整图标准预测（切片数>1 时）", 11, GRAY, "middle"))
        if name in ("DensK1", "UnifAll"):
            o.append(text(ix + IW * S / 2, iy + IH * S + 13, "+ F640 整图", 11, GRAY, "middle"))
        o.append(text(px + 10, py + ph - 40, l1, 12))
        o.append(text(px + 10, py + ph - 22, l2, 11, GRAY))
    # legend / notes panel
    px, py = 8 + 2 * pw, 32 + ph
    o.append(rect(px, py, pw - 8, ph - 8, "#ffffff", BAND_B, 1, 3))
    notes = ["共同终处理 finalize：", "conf ≥ 0.25 → 类内 NMS", "IoU > 0.5 → 最多 500 框",
             "", "窗口不足 640 时填灰（114）；", "SAHI 片不填充、越界贴边；", "SAHI 合并 = GREEDYNMM／IOS 0.5", "（元数据写“NMS”为误称）"]
    for k, s in enumerate(notes):
        o.append(text(px + 10, py + 20 + k * 19, s, 12, TXT if k in (0, 6) else GRAY))
    o.append("</svg>")
    (OUT / "p0fr_protocols.svg").write_text("\n".join(o), encoding="utf-8")


if __name__ == "__main__":
    timeline()
    protocols()
    print("ok")
