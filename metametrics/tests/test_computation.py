# metametrics/tests/test_computation.py

import unittest
from unittest import skipIf
from metametrics.tests.test_config.test_config import TEST_COMPUTATIONS

from metricspaces import MetricSpace
from greedypermutation.clarksongreedy import greedy
from random import randrange, randint, seed

from scipy.stats import multivariate_normal

from metametrics import Point,naiveHD,greedyHD,calcGreedy,l_inf

class ComputationTest(unittest.TestCase):
	
	def setUp(self):
		M = 30000
		N = 5000
		is_uniform = False
		self.SEED = 123
		#np.random.seed(123)
		print("\n=====\n")
		print(f"With M={M} and N={N}")
		if is_uniform:
			seed(self.SEED)
			points = [Point(randrange(5, M-5), randrange(5,M-5)) for i in range(N)]
		else:
			mean = [M, M]
			cov = [[M/2, 0.5*(M/2)], [0.5*(M/2), M/2]]
			mn = multivariate_normal(mean, cov)
			points = [Point(point[0], point[1]) for point in mn.rvs(size=N, random_state=self.SEED).round().astype(int)]
		points = list(dict.fromkeys(points))
		N = len(points)
		print(f"After removing duplicate elements: {N}")
		X = MetricSpace(points = points, dist=l_inf)
		self.A = X[:N//2]
		self.B = X[N//2:]

	def print_cache(self, is_before, A=None, B=None):
		if is_before:
			print("Before (Cache Size): ", end='')
		else:
			print("After (Cache Size): ", end='')

		if A == B == None:
			print(len(self.A.cache) + len(self.B.cache))
		elif type(A) == type(B) == type(MetricSpace()):
			print(len(A.cache) + len(B.cache))
	
	def clear_cache(self):
		self.A.cache = {}
		self.B.cache = {}
	
	@skipIf(not TEST_COMPUTATIONS,
			"Skipping computational tests")
	def test_greedy(self):
		self.clear_cache()

		print("Running Greedy Hausdorff Distance")
		self.print_cache(is_before=True)
		d_A, d_B = calcGreedy(self.A,self.B)
		self.print_cache(is_before=False)

		A_g = MetricSpace(points = d_A, dist = self.A.distfn, cache = {}, turnoffcache = self.A.turnoffcache)
		B_g = MetricSpace(points = d_B, dist = self.B.distfn, cache = {}, turnoffcache = self.B.turnoffcache)
		self.print_cache(is_before=True, A=A_g, B=B_g)
		d = naiveHD(A_g, B_g)
		self.print_cache(is_before=False, A=A_g, B=B_g)

	@skipIf(not TEST_COMPUTATIONS,
			"Skipping computational tests")
	def test_naive(self):
		self.clear_cache()

		print("Running Naive Hausdorff Distance")
		self.print_cache(is_before=True)
		d = naiveHD(self.A,self.B)
		self.print_cache(is_before=False)

if __name__ == '__main__':
	unittest.main()
