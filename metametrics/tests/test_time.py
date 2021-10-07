# metametrics/tests/test_time.py

import unittest
from metametrics.tests.test_config.timer import timer

from metricspaces import MetricSpace
from greedypermutation.clarksongreedy import greedy
from random import randrange, randint

from scipy.stats import multivariate_normal

from metametrics import Point,naiveHD,l_inf

class TimeTest(unittest.TestCase):

    def setUp(self):
        M = 300
        N = 5000
        is_uniform = True
        #np.random.seed(123)
        if is_uniform:
            points = [Point(randrange(5, M-5), randrange(5,M-5)) for i in range(N)]
        else:
            mean = [M, M]
            cov = [[M/2, 0.5*(M/2)], [0.5*(M/2), M/2]]
            mn = multivariate_normal(mean, cov)
            SEED = 123
            points = [Point(point[0], point[1]) for point in mn.rvs(size=N, random_state=SEED).round().astype(int)]
            points = list(dict.fromkeys(points))
        N = len(points)
        X = MetricSpace(points = points, dist=l_inf)
        self.A = X[:N//2]
        self.B = X[N//2:]

    @timer
    def test_naive(self):
        d = naiveHD(self.A,self.B)

if __name__ == '__main__':
    unittest.main()
