# UAVDT package selection guide (Stage E)

Different mirrors report different sizes. Prefer **identity by layout**, not size alone.

## Prefer (for Stage E DET)

1. **UAVDT-Benchmark-M** from author Baidu (`uwn8`) or author Google Drive  
   - Typical compressed size reported by community mirrors: **~5.5–7.5 GB** (often ~6.3 GB).  
   - After unzip, look for something like:
     - `UAV-benchmark-M/` with sequence folders `M0101`, `M0102`, … each with many `.jpg`
     - GT often comes with **DET/MOT toolkit** package (`UAV-benchmark-MOTD_v1.0` / `GT/`), Baidu code **ilxx**
2. Optional: **Attributes** (Baidu **t9d3**)

## Acceptable if layout matches

- HuggingFace `vanthanh/UAVDT-Benchmark-M` style dumps (~7 GB reported) **only if** after extract you still have original sequence folders + usable DET GT (not only YOLO txt with remapped ids).
- Zenodo `UAVDT.zip` (this host backup): **3,746,830,525 bytes**, MD5 `19f318b1d5e97a47e3dd30ec5bff182b` — third-party reupload; usable **only after** layout audit shows full DET frames+labels.

## Reject / do not use for Stage E mainline

- **UAVDT-Benchmark-S** (SOT / single-object) — wrong task
- Tiny Kaggle “UAVDT YOLO” subsets (hundreds of MB, few sequences)
- Packages that only have COCO/YOLO labels with **unknown class remapping**
- Segmentation-only or tracking-only forks
- Anything that requires retraining or changes frozen `last.pt`

## What to send me after you pick one

For each candidate zip/folder:
1. filename
2. size (bytes or MB/GB)
3. source (Baidu uwn8 / Kaggle URL / HF / Zenodo)
4. first-level folder names after unzip (or zip listing top entries)

I will SHA256 + layout-check before any inference. Mapping stays frozen; no fine-tune.
