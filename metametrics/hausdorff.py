from ds2.priorityqueue import PriorityQueue

def dist(point, pointset):
    return min(point.dist(x) for x in pointset)

def dh_oneline(A, B):
    return max(min(a.dist(b) for a in A) for b in B)

def dH(A, B, dh = dh_oneline):
    return max(dh_oneline(A,B), dh_oneline(B,A))

def dh_twoloops(A, B):
    cmax = 0
    for a in A:
        cmin = float('inf')
        for b in B:
            cmin = min(a.dist(b), cmin)
        cmax = max(cmax, cmin)
    return cmax

def dh_earlybreak(A, B):
    cmax = 0
    for a in A:
        cmin = float('inf')
        for b in B:
            cmin = min(a.dist(b), cmin)
            if cmin < cmax:
                break
        cmax = max(cmax, cmin)
    return cmax

def dh_withpausing(A, B):
    nndist = {a: float('inf') for a in A}
    search = {a:iter(B) for a in A}
    pq = PriorityQueue(A, key = lambda a: -nndist[a])

    for a in pq:
        try:
            b = next(search[a])
        except StopIteration:
            break
        nndist[a] = min(nndist[a], dist(a,b))
        pq.insert(a)

    return max(nndist.values())
