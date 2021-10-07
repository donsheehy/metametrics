from metricspaces import MetricSpace
from greedypermutation.clarksongreedy import greedy
from random import randrange, randint

from metametrics import Point

def naiveDirectedHD(A: MetricSpace, B: MetricSpace, cmax: float = 0):
    for a in A:
        cmin = float('inf')
        cont = True
        for b in B:
            d = A.dist(a,b)
            if d < cmax:
                cont = False
                break
            if d < cmin:
                cmin = d
        if cont and cmin > cmax:
            cmax = cmin
    return cmax

def naiveHD(A: MetricSpace, B: MetricSpace, cmax: float = 0):
    return max(naiveDirectedHD(A, B, cmax), naiveDirectedHD(B, A, cmax))

def calcGreedy(A, B):
    return (list(greedy(A)), list(greedy(B)))

def greedyHD(A: MetricSpace, B: MetricSpace):
    # cache of A_g - no of distances A_g had to compute
    d_A, d_B = calcGreedy(A, B)
    A_g = MetricSpace(points = d_A, dist = A.distfn, cache = A.cache, turnoffcache = A.turnoffcache)
    B_g = MetricSpace(points = d_B, dist = B.distfn, cache = B.cache, turnoffcache = B.turnoffcache)
    return naiveHD(A_g, B_g)

def l_inf(p: Point, q: Point):
    return max(abs(p.x - q.x), abs(p.y - q.y))
