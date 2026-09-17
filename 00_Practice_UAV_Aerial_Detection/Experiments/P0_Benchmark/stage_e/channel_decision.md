# Stage E — External validation channel decision

- **Date:** 2026-09-17 Asia/Shanghai
- **E_STATUS: BLOCKED**
- **Reason:** Target external set **UAVDT** is **not present** on this machine under 11_Datasets/ (raw/processed/external scanned; no UAVDT tree/ZIP).
- **Not used as substitute:** UAV-RSOD remains **A0-02 HOLD** (augmented package only; original 315-image GT/mapping Unknown). Using it would violate Stage E discipline and prior HOLD.
- **No scatter-search** of new datasets in this step (protocol + memory).
- **No download** executed (needs explicit path or download authorization).
- **No inference / no metrics** until channel READY.

## What READY requires

1. Legal local UAVDT DET images + GT (or user-authorized download + SHA freeze), and
2. Frozen VisDrone→UAVDT class mapping **before** any predictions (see class_mapping_preregister.json), and
3. Same frozen last.pt (no fine-tune), five methods one-shot, VisDrone-compatible matcher on mapped subset only.

## Intention of Stage E (when unblocked)

Trend check under domain shift for frozen strategies — **not** UAVDT SOTA claim.
