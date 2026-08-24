# Known / Unknown Protocol

## 目标

验证模型在训练阶段未见类别上的对象发现、未知判断和风险推理。随机train/test不能支持Open-World主张。

## Split设计

| Split | Known类别 | Unknown类别 | 训练实例检查 | 验证用途 | 测试用途 | 状态 |
|---|---|---|---|---|---|---|
| A | 待冻结 | 待冻结 | 0个Unknown实例 | 阈值/校准 | 最终评价 | 待设计 |
| B | 待冻结 | 待冻结 | 0个Unknown实例 | 阈值/校准 | 轮换评价 | 待设计 |
| C | 待冻结 | 待冻结 | 0个Unknown实例 | 阈值/校准 | 轮换评价 | 待设计 |

## 冻结规则

1. 先生成原图组ID，再划分train/val/test，最后执行类别轮换。
2. Unknown类别及其增强/裁剪衍生样本不得进入对应训练。
3. 提示词、阈值和校准参数只根据训练/验证信息确定。
4. 分别记录：Unknown未被发现、被发现但判Known、Known误判Unknown。
5. 指标实现先通过手算样例和极端单元测试。

## 指标候选

Unknown Recall、AUROC、FPR95、A-OSE、Wilderness Impact。最终采用哪些指标取决于预测定义与可复现基线，不机械堆叠。
