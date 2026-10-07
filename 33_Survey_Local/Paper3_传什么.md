# Paper 3：比特不够时传整图、裁剪，还是传字段

日期：2026-10-07。案头协议，不授权实验。Paper 3 仍 PAUSED。样例预算是冻结格式，不是实测速率。

这篇只留两个主张：R1 和 R2。R3 只是检查，不进贡献。不训练新的语义网络，不做 Mesh，不做通感分配。不另开文件。

## R1：结构化包是否保住复核

主张在说什么。整幅航拍图经常超过能传的比特。R1 要证明：在同一个比特预算、同一条加性高斯白噪声下，只传类别、框、分数、高度和下限的包，危险召回不低于“只传风险斑块 JPEG”；接收端还能复核高度。整图 JPEG 要么发不完，要么召回更差。

它不说：本文发明了语义通信。文本语义传输已有 Xie, Huiqiang; Qin, Zhijin; Li, Geoffrey Ye; Juang, Biing-Hwang. *IEEE Transactions on Signal Processing*, 2021. https://doi.org/10.1109/TSP.2021.3071210 四类已有路线见 Wheeler, Dylan; Natarajan, Balasubramaniam. *IEEE Access*, 2023. https://doi.org/10.1109/ACCESS.2023.3243065 本文只比三种报文，不训练端到端编解码器。

具体干什么。

1. 建目录 `P3_proxy_01/`。`frames/images/` 放图。`frames/dets.csv` 每行一个框：`frame_id,cls,x,y,w,h,score,height_m,lod_m`。没有 Paper 2 时高度和下限留空，并写 `height_source: missing_proxy`。框来自同一冻结检测器，接收端不重训。
2. 写 `freeze.md` 并冻结。至少包括每帧比特预算、JPEG 质量、信噪比列表、包字段顺序、裁剪外扩像素。例子可以写 `bit_budget: 8000`、`jpeg_quality: 40`、`snr_db: 0,5,10,15`。看完召回再改质量，这组作废。
3. 造三种报文。整图按冻结质量做 JPEG，超过预算就降质量；降到仍超过就记 `dropped`，不换图。斑块用框加外扩像素裁剪后再编码。包按字段顺序写成定长记录，超预算就按分数从低到高丢框。丢弃顺序写进 freeze。
4. 三种报文加同一噪声。接收符号 \( y = x + n \)，\( n \) 为高斯噪声，信噪比只用冻结列表。不写山区路径损耗。
5. 填 `tables/r1_task_bits.csv`，列：`mode,snr_db,n_frames,n_dropped,recall,false_per_frame,height_mae_m,bits_mean`。行是 `jpeg_full`、`jpeg_crop`、`packet`。召回只在发送端有危险框的帧上算，接收框与发送框 IoU 大于 0.5 算命中。0.5 是本协议匹配线，不是 VisDrone 官方 AP。高度全空就写 `NA`，不能写成误差为零。

怎样算成立。`packet` 的召回低于 `jpeg_crop`，R1 不成立，退成“裁剪是否优于整图”，不称语义通信。整图没有丢帧且召回更高，说明预算太松，冻结作废，不能把质量调到包赢为止。

难度中。公开图加仿真就能做。可投方向是任务通信。专刊页：Gündüz, Deniz; Qin, Zhijin 等. *IEEE Journal on Selected Areas in Communications*, 2023, 41(1). https://ieeexplore.ieee.org/ielx7/49/9991040/09991044.pdf 应用向可看 *Ad Hoc Networks*。López-Villegas, Isaac; Martínez-Rios, Erick Axel; Izquierdo-Reyes, Javier; Bustamante-Bello, Rogelio; Falcone, Francisco. 2026, 182: 104063. https://www.sciencedirect.com/science/article/pii/S1570870525003117 会议看 IEEE ICC 或 GLOBECOM，不计入七篇。JCR 当年核。

## R2：删掉哪个字段会伤任务

主张在说什么。包里的字段不是都值得占比特。R2 要证明：在 R1 同一信道下，删掉类别后召回下降；删掉高度后测量误差无法算；删掉下限后接收端不能做派发过滤。

它不说：每个字段都同等重要。要的是删除之后任务变差，不变就不是贡献。

具体干什么。

1. 复制 R1 的 `packet`，不改预算和噪声。
2. 分别把 `cls`、`height_m`、`lod_m` 置空，各跑一遍。
3. 填 `tables/r2_field_ablation.csv`，列：`dropped_field,recall,false_per_frame,height_mae_m,dispatch_possible`。`dispatch_possible` 只有下限还在时为 yes。

怎样算成立。三行都和完整包一样，R2 不成立，这篇只剩 R1 或弱退路。难度中。和 R1 写成同一篇的第二项。

## R3：中继少转发是否保住高风险

主张在说什么。第二架机是中继，不是第二套检测器。R3 只检查：按分数排序后，转发预算减半，高风险召回是否还在。

具体干什么。把 R1 的包按 `score` 排序。中继预算写成侦察预算的一半。高风险定义写死，例如 `score>=0.5`，看完再改则作废。比较全转发和优先转发的高风险召回。没有增益，不进贡献。

它不说：多机 Mesh 或通感分配已经做成。无人机网络的续航和监管限制见 Wan, Fayu; Yaseen, Muhammad Bilal; Riaz, Muhammad Bilal; Shafiq, Anum; Thakur, Atul; Rahman, Md Owahedur. *Results in Engineering*, 2024, 24: 103271. https://www.sciencedirect.com/science/article/pii/S2590123024015251 难度中高。不成篇。
