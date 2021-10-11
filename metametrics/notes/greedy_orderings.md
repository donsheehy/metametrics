# Greedy orderings

```python3 {cmd output="svg" hide}

from random import randint
from greedypermutation import Point
from greedypermutation.clarksongreedy import greedy
from greedypermutation.greedytree import GreedyTree
from metricspaces import MetricSpace
from greedypermutation.greedytree import Node,Bunch
import svgwrite

N = 10
lowBound, upBound = 300, 700



P = list(set([Point([randint(lowBound,upBound), randint(lowBound,upBound)]) for i in range(N)]))

M = MetricSpace(P)

gt = list(GreedyTree(M))

dwg = svgwrite.Drawing('greedy_tree_gallery/greedy_tree_test51.svg', size=(1000,1000))

def connect(parentPt, childPt):
  dwg.add(dwg.line(parentPt, childPt, stroke="black", stroke_width="4"))

def point(parentPt, num):
  x,y = parentPt
  dwg.add(dwg.text(str(num), x=[x+10],y=[y+10], color="black"))
  try:
    dwg.add(dwg.circle(parentPt, r=5, fill="red", stroke="black", stroke_width="3"))
  except:
    print("Problem point: ",parentPt)

def bunch(center, radius):
  dwg.add(dwg.circle(center,r=radius,fill="green", opacity="0.15"))

root, _ = gt[0]

for c,p in gt[1:N]:
  px,py = p
  rad = c.dist(p)
  bunch((px,py), rad)
  prev = c

for c,p in gt[1:N]:
  cx,cy = c
  px,py = p
  connect((cx,cy),(px,py))

idx = 0
for p, _ in gt:
  px,py = p
  point((px,py), idx)
  idx +=1

print(dwg.tostring())
dwg.save()
```
