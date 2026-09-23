# 第4轮接续核验

日期：2026-09-12。Run ID：BT1-LOCAL-20260912-02。**PASS：从第3轮检查点恢复，真实完成第4轮并停止，没有重跑第1–3轮或进入第5轮。**

## 实测证据

- 训练前9项检查全部通过：起始轮次、实时模型张量、优化器完整状态、调度器、EMA张量、EMA更新次数、scaler、100轮总日程、batch4。张量和优化器比对真实恢复对象，非仅判断字段存在。
- 第4轮首批与轮末三组学习率均为0.009703，与原100轮线性日程一致。首批损失有限；本轮无OOM或非有限损失。
- 新results.csv只有epoch=4一行；EMA更新次数921→1023。总进程墙钟378.20秒，CSV训练/验证阶段338.453秒。已正常PAUSED，baseline_eligible=false。
- 第3轮原恢复包SHA未改变；第4轮新包通过ZIP完整性、检查点SHA、epoch和优化器字段读取核验。
- 新包SHA256：d200dd8f13348ff31a2a43bf2f5f3addabb60587c081f184cb8ef31fee778ac9。
- 新检查点SHA256：6c89ebe627c0980ec63a3b26caa07665710e82161ddef5c84447f54639107fc7。

## 原生监控指标

cal48：Precision=29.102%，Recall=19.320%，mAP50=16.344%，mAP50–95=7.936%。第3轮对应mAP50=16.299%、Recall=21.021%，本轮指标有涨有跌；不据单轮波动判断方法效果或更改训练协议。这些仍不是官方独立测试或创新效果结果。

## 范围与产物

仅验证本机同环境的有状态恢复。数据加载器重建、轮末未保留的部分累积梯度及框架恢复流程意味着不保证与不中断训练逐位相同；也未验证Kaggle/Colab跨平台恢复。

- [训练前状态比对](../../11_Datasets/processed/VisDrone/BT1/BT1-LOCAL-20260912-02/resume_verification.json)
- [首批学习率核验](../../11_Datasets/processed/VisDrone/BT1/BT1-LOCAL-20260912-02/resume_first_batch.json)
- [最终核验](../../11_Datasets/processed/VisDrone/BT1/BT1-LOCAL-20260912-02/resume_final_review.json)
- [第4轮恢复包](../../11_Datasets/processed/VisDrone/BT1/BT1-LOCAL-20260912-02/recovery/latest_recovery.zip)

执行器新增指定轮末停止及真实状态断言，本地Notebook内嵌代码已同步；云端页面未更新或启动。原始数据、原3轮证据、学习记录及保护附件未改动，未提交、未推送。

下一项唯一任务：使用本次第4轮恢复包从第5轮继续普通基线分段训练；保留100轮日程和固定参数，不重做本次核验或准备数据。
