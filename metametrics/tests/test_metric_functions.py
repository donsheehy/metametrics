# metametrics/metric_functions.py

import unittest

from metricspaces import MetricSpace
from greedypermutation.clarksongreedy import greedy
from random import randrange, randint

from metametrics import Point,naiveHD,greedyHD,calcGreedy,l_inf

from scipy.stats import multivariate_normal

class MetricTest(unittest.TestCase):

	def setUp(self):
		spread = 100
		cardinality = 20
		num_of_spaces = 10
		seed = 472
		self.dist = l_inf
		self.spaces = [
			MetricSpace(
				[Point(randrange(5, spread-5), randrange(5,spread-5))
					for i in range(cardinality)]
				, dist=self.dist) for j in range(num_of_spaces)]
		self.null_space = MetricSpace([],dist=self.dist)
		self.origin_space = MetricSpace([Point(0,0)], dist=self.dist)
		self.p11 = MetricSpace([Point(1,1)], dist=self.dist)
		self.p01 = MetricSpace([Point(0,1)], dist=self.dist)
		self.p10 = MetricSpace([Point(1,0)], dist=self.dist)
		print("Space 0: \n",str(self.spaces[0].points))

	def test_naiveHD_sanity(self):
		test_pairs_expected = [
			[self.null_space, self.null_space, 0],
			[self.null_space, self.origin_space, float('inf')],
			[self.origin_space, self.null_space, float('inf')],
			[self.p11, self.p01, 1],
			[self.p11, self.p10, 1]
		]
		for spcA, spcB, expected in test_pairs_expected:
				with self.subTest(spcA = spcA, spcB = spcB, expected = expected):
					self.assertEqual(naiveHD(spcA,spcB), expected)

		



if __name__ == '__main__':
	unittest.main()
