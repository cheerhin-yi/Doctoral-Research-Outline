# Google Colab教程
1. 选择在Colab网页登陆
2. 可以选择分配的RAM，磁盘以及GPU
3. 需要先做好drive的同步
4. 谷歌云盘默认的加载路径是_"/content/drive/MyDrive"_
5. 还需要一个**wandb**的API Key：
    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
    **wandb**核心功能有4个。
    - 实验跟踪:experiment tracking (wandb.log)
    - 版本管理:version management (wandb.log_artifact, wandb.save)
    - case分析:case visualization (wandb.Table, wandb.Image)
    - 超参调优:model optimization (wandb.sweep)
6. 下面以有调用yolo8代码为例。
    1. 账号与算力准备
        - 注册 Google 账号，打开 [Google Colab](https://link.wtturl.cn/?target=https%3A%2F%2Fcolab.research.google.com%2F&scene=im&aid=497858&lang=zh)，新建空白笔记本
        - 开启 GPU 算力
        - 验证 GPU 是否生效：`!nvidia-smi`
    2. 安装核心依赖 `!pip install ultralytics==8.3.10 -i https://pypi.tuna.tsinghua.edu.cn/simple`
    3. 挂载云盘`drive.mount('/content/drive')`
    4. 开始训练
```
from ultralytics import YOLO

# 加载nano版轻量化基线模型（和你后续论文基线一致）
model = YOLO('yolov8n.pt')  

# 启动训练，仅10轮快速验证环境
results = model.train(
    data='coco128.yaml',  # 官方自带数据集，自动下载
    epochs=10,            # 仅跑10轮验证，不用跑满
    imgsz=640,            # 输入分辨率
    batch=8,              # 批次大小，显存不够就改成4
    device=0,             # 使用0号GPU
    seed=42,              # 固定随机种子，保证可复现
    project='demo_run',   # 项目文件夹名
    name='yolov8n_baseline' # 本次实验名称
)

# 加载训练好的最佳权重
model = YOLO('demo_run/yolov8n_baseline/weights/best.pt')

# 在验证集上测试，输出全量指标
metrics = model.val(data='coco128.yaml', imgsz=640, device=0)

# 打印核心指标（对应你论文里的核心评价指标）
print("mAP@0.5:", metrics.box.map50)
print("mAP@0.5:0.95:", metrics.box.map)
print("精确率Precision:", metrics.box.mp)
print("召回率Recall:", metrics.box.mr)

# 单张图片推理
results = model.predict(
    source='你的测试图片路径.jpg',
    save=True,        # 保存结果图
    conf=0.25,        # 置信度阈值
    device=0
)
```
5. 熟悉输出目录结构。主要下载和执行目录在/content，笔记本存放在/content/drive/MyDrive。
- `weights/`：存放`best.pt`（最佳权重）和`last.pt`（最后一轮权重）
- `results.png`：训练 loss、指标变化曲线图
- `confusion_matrix.png`：混淆矩阵
- `args.yaml`：本次训练的全部参数配置