from pathlib import Path
import inspect, sys
sys.path.insert(0, r'D:\Doctoral-Research-Outline\00_Practice_UAV_Aerial_Detection\Experiments')
import diagnose_bt1 as d
for name in ['prepare_gt','match_gt','sha','WEIGHT_SHA','BASE','RUNS']:
    obj=getattr(d,name)
    if callable(obj):
        print('====', name, '====')
        print(inspect.getsource(obj))
    else:
        print('====', name, '=', obj)
w=d.BASE/d.RUNS[-1]/'train/weights/last.pt'
print('WEIGHT', w)
print('exists', w.exists())
print('sha_ok', d.sha(w)==d.WEIGHT_SHA)
print('sha', d.sha(w))
