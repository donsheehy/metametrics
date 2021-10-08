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
		test_params = [(30000, 500, False),
						(30000, 5000, False), 
						(30000, 50000, False)]
		self.SEED = 123
		self.metricspaces = dict()
		print("\n= = = = = = = = = =")
		for M, N, is_uniform in test_params:
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
			A = X[:N//2]
			B = X[N//2:]
			self.metricspaces[(M, N, is_uniform)] = [A, B]

	def print_cache(self, is_before, A, B):
		if is_before:
			print("Before (Cache Size): ", end='')
		else:
			print("After (Cache Size): ", end='')

		if type(A) == type(B) == type(MetricSpace()):
			print(len(A.cache) + len(B.cache))
	
	def clear_cache(self, A, B):
		A.cache = {}
		B.cache = {}
	
	def print_parameterization_details(self, M, N, is_uniform):
		print("\n=====\n")
		print(f"With M={M} and N={N}")
	
	@skipIf(not TEST_COMPUTATIONS,
			"Skipping computational tests")
	def test_greedy(self):
		for test_param, point_sets in self.metricspaces.items():
			self.print_parameterization_details(*test_param)

			A = point_sets[0]
			B = point_sets[1]

			self.clear_cache(A, B)

			print("Running Greedy Hausdorff Distance")
			self.print_cache(is_before=True, A=A, B=B)
			d_A, d_B = calcGreedy(A, B)
			self.print_cache(is_before=False, A=A, B=B)

			A_g = MetricSpace(points = d_A, dist = A.distfn, cache = {}, turnoffcache = A.turnoffcache)
			B_g = MetricSpace(points = d_B, dist = B.distfn, cache = {}, turnoffcache = B.turnoffcache)
			self.print_cache(is_before=True, A=A_g, B=B_g)
			d = naiveHD(A_g, B_g)
			self.print_cache(is_before=False, A=A_g, B=B_g)

	@skipIf(not TEST_COMPUTATIONS,
			"Skipping computational tests")
	def test_naive(self):
		for test_param, point_sets in self.metricspaces.items():
			self.print_parameterization_details(*test_param)

			A = point_sets[0]
			B = point_sets[1]

			self.clear_cache(A, B)

			print("Running Naive Hausdorff Distance")
			self.print_cache(is_before=True, A=A, B=B)
			d = naiveHD(A, B)
			self.print_cache(is_before=False, A=A, B=B)

if __name__ == '__main__':
	unittest.main()
