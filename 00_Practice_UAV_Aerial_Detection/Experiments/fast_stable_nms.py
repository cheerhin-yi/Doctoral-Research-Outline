"""CPU float64 torchvision NMS with reference-compatible deterministic ordering.

No coordinate offsets or score perturbations: original rows are returned unchanged.
Unique rank scores control tie order INSIDE the operator, per class separately.
Invalid/tiny geometry retains the original denominator-floor reference behavior.
"""
import numpy as np
import torch
from torchvision.ops import nms as compiled_nms
from diagnose_bt1 import nms as reference_nms


def nms(pred, cap=500):
    pred=np.asarray(pred,dtype=np.float64).reshape(-1,6)
    if not isinstance(cap,(int,np.integer)):
        return reference_nms(pred,cap)
    if not len(pred) or cap<=0:return pred[:0]
    wh=pred[:,2:4]-pred[:,:2]
    with np.errstate(over='ignore',invalid='ignore'):
        area=wh.prod(1)
    if not np.isfinite(pred).all() or not np.isfinite(area).all() or np.any(wh<=0) or np.any(area<=1e-12):
        return reference_nms(pred,cap)
    order=np.argsort(-pred[:,4],kind='stable')
    # Rank indices preserve original view/index ties across classes on final merge.
    sorted_pred=pred[order];survivors=[]
    for category in np.unique(sorted_pred[:,5]):
        ranks=np.flatnonzero(sorted_pred[:,5]==category)
        boxes=torch.from_numpy(np.ascontiguousarray(sorted_pred[ranks,:4]))
        scores=torch.arange(len(ranks),0,-1,dtype=torch.float64)
        kept=compiled_nms(boxes,scores,.5).numpy()
        survivors.extend(ranks[kept].tolist())
    return pred[order[np.array(sorted(survivors)[:cap],dtype=int)]]
