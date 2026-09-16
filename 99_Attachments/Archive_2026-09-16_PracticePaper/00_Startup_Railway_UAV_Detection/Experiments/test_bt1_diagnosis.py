"""Boundary tests for NEW real-image diagnostic adapters, not training tests."""
import unittest
import numpy as np
from diagnose_bt1 import prepare_gt, match_gt, nms, axis_windows, response_scores
from check_visdrone_semantics import drop_ignored, row, match


class DiagnosisBoundaries(unittest.TestCase):
    def test_integral_adapter(self):
        for width in [4,5,6]:
            raw=np.array([row(category=0,score=0,w=width),row(),row(x=128,y=128,w=1,h=1)],float)
            g,ids,_=prepare_gt(raw,128,128)
            expected,_=drop_ignored(raw.tolist(),[],128,128)
            self.assertEqual(g.tolist(),expected)

    def test_match_normal_ignore_duplicate_and_all_sizes(self):
        for raw,ds in [([row(score=0),row()], [row(score=.9),row(score=.8),row(score=.7)]),
                       ([row(w=31,h=33),row(w=32,h=32)], [row(w=32,h=32,score=.9)]),
                       ([row()], [row(score=.9),row(score=.8)]),
                       ([row()], [row(w=5,score=.9)])]:
            g,ids,integral=prepare_gt(np.array(raw,float),128,128)
            pred=np.array([d[:4]+[d[4],d[5]-1] for d in ds],float); pred[:,2:4]+=pred[:,:2]
            matched,fp,ign=match_gt(g,ids,pred,integral,128,128)
            expected,det=match([r[:4]+[1-r[4]] for r in raw],[r[:5] for r in ds])
            self.assertEqual(len(matched),sum(r[4]==1 for r in expected))
            self.assertEqual(fp,sum(r[5]==0 for r in det)); self.assertEqual(ign,sum(r[5]==-1 for r in det))
            if len(raw)==2 and raw[0][2]==31: self.assertEqual(matched,{1})

    def test_window_edges_and_nms(self):
        self.assertEqual(axis_windows(1000),[0,360])
        self.assertEqual(axis_windows(300),[0])
        p=np.array([[0,0,10,10,.8,0],[0,0,10,10,.8,0],[0,0,10,10,.8,1]],float)
        self.assertEqual(nms(p).tolist(),p[[0,2]].tolist())

    def test_response_padding_mapping_and_class_gate(self):
        p3=np.full((10,80,80),-10.); p4=np.full((10,40,40),-10.)
        p3[2,20,20]=0.;p4[2,10,10]=0.
        peaks,scores,chosen=response_scores([p3,p4],640,640,np.empty((0,6)),[(0,0,640,640)])
        k=np.flatnonzero((peaks[:,0]==164)&(peaks[:,1]==164))[0]
        self.assertGreater(peaks[k,5],0)
        p4[3,10,10]=1.
        peaks,_,_=response_scores([p3,p4],640,640,np.empty((0,6)),[(0,0,640,640)])
        self.assertEqual(peaks[k,5],0)
        peaks,_,_=response_scores([p3,p4],320,640,np.empty((0,6)),[(0,0,640,320)])
        self.assertTrue(np.all((peaks[:,1]>=0)&(peaks[:,1]<320)))


if __name__=='__main__': unittest.main()
