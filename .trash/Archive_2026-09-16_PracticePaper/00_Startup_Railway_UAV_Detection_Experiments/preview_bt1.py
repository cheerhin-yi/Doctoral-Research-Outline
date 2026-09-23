"""Fixed cal48 qualitative preview; no selection by detection quality."""
import argparse
import json
import os
from pathlib import Path


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--run', type=Path, required=True)
    p.add_argument('--data', type=Path, required=True)
    a = p.parse_args()
    output = a.run/'preview_v2'
    output.mkdir(exist_ok=False)
    os.environ['YOLO_CONFIG_DIR'] = str(a.run/'framework_config')
    os.environ['YOLO_AUTOINSTALL'] = 'false'
    from ultralytics import YOLO
    from PIL import Image, ImageDraw
    data = json.loads(a.data.read_text(encoding='utf-8'))
    paths = Path(data['val']).read_text(encoding='utf-8').splitlines()[:6]
    model = YOLO(str(a.run/'train/weights/last.pt'))
    results = model.predict(paths, imgsz=640, rect=False, device=0, batch=1,
                            conf=.25, iou=.5, max_det=500, save=False, verbose=False)
    rows = []
    for i, result in enumerate(results):
        source = Path(paths[i])  # List inputs may be returned as image0.jpg by the loader.
        gt = Image.open(source).convert('RGB')
        draw = ImageDraw.Draw(gt)
        count = 0
        labels = a.data.parent/'labels/cal48'/source.with_suffix('.txt').name
        for line in labels.read_text(encoding='utf-8').splitlines():
            cls, x, y, w, h = map(float, line.split())
            box = [(x-w/2)*gt.width,(y-h/2)*gt.height,(x+w/2)*gt.width,(y+h/2)*gt.height]
            draw.rectangle(box, outline='#ffdd00', width=2)
            count += 1
        pred = Image.fromarray(result.plot()[:,:,::-1])
        panels = []
        for im in (gt,pred):
            im.thumbnail((960,720));panels.append(im)
        canvas=Image.new('RGB',(sum(im.width for im in panels),max(im.height for im in panels)+40),'white')
        canvas.paste(panels[0],(0,40));canvas.paste(panels[1],(panels[0].width,40))
        d=ImageDraw.Draw(canvas)
        d.text((8,8),f'{i+1}. Ground truth ({count} eligible boxes)',fill='black')
        d.text((panels[0].width+8,8),f'Prediction conf>=0.25 ({len(result.boxes)} boxes)',fill='black')
        name=f'cal_{i+1:02d}_comparison.jpg';canvas.save(output/name,quality=92)
        rows.append(dict(image=source.name, ground_truth_count=count,
                         prediction_count=len(result.boxes), preview=name))
    (output/'manifest.json').write_text(json.dumps(dict(scope='First six cal48, fixed order; qualitative only',
        conf=.25,iou=.5,rect=False,rows=rows),indent=2),encoding='utf-8')
    print(json.dumps(rows),flush=True)


if __name__=='__main__':
    main()
