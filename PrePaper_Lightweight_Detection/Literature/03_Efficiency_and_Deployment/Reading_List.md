# L3：效率与部署阅读清单

## 本主题要回答

- 参数量、GFLOPs、延迟和端到端FPS为何不等价？
- PyTorch、ONNX、TensorRT结果如何公平比较？
- 固定硬件和计时范围需要记录什么？

## 阅读清单

| ID | 论文 | 优先级 | 状态 | 重点阅读 | 笔记 |
|---|---|---|---|---|---|
| L3-01 | [TakuNet](TakuNet%20-%20an%20Energy-Efficient%20CNN%20for%20Real-Time%20Inference%20on%20Embedded%20UAV%20Systems%20in%20Emergency%20Response%20Scenarios.pdf) | SHOULD | SCREENED | Jetson/Raspberry Pi、FP16、能耗、分类边界 | 待创建 |
| L3-02 | [EUAVDet](EUAVDet%20-%20An%20Efficient%20and%20Lightweight%20Object%20Detector%20for%20UAV%20Aerial%20Images%20with%20an%20Edge-Based%20Computing%20Platform.pdf) | MUST | SCREENED | Jetson Nano、FPS、计时范围、精度—速度权衡 | 待创建 |
| L3-03 | 真实推理速度与部署评价规范 | MUST | TODO | 预热、同步、batch、计时范围 | 待检索 |

## 本主题完成门

- [ ] 至少3篇直接相关论文完成精读；
- [ ] 固定可复核的速度计时协议；
- [ ] 明确何种证据才能支持C0-2。
