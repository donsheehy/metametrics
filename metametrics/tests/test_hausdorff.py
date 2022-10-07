import unittest
from metametrics.hausdorff import *

class TestDirectedHausdorff(unittest.TestCase):
    def testonepointsets(self):
        """
        Given sets with only one point each, the Hausdorff distance should
        equal the distance in the original metric.
        """
        pass

    def testtwopointsets_matching(self):
        """
        In this case, the nearest neighbor graph is a matching.
        """
        pass

    def testtwopointsets_nonmatching(self):
        """
        In this case, the nearest neighbor graph is not a matching, i.e.,
        both points have the same nearest neighbor.
        """
        pass

    def testAisbigger(self):
        """
        It should return the correct value when `A` is bigger.
        """
        pass

    def testAissmaller(self):
        """
        It should return the correct value when `A` is smaller.
        """
        pass

    def testAequalsB(self):
        """
        If `A` and `B` are the same set (up to permutation), then the result
        should be zero.
        """
        pass

if __name__ == '__main__':
    unittest.main()
