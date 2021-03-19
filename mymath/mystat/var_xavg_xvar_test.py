import unittest
import numpy as np

from mymath.mystat.MyStat import MyStat


class MyTestCase(unittest.TestCase):
    DELTA = pow(10, -3)

    def test_var(self):
        self.assertAlmostEqual(6.333333, np.float(np.var([5, 0, 3], ddof=1)), delta=self.DELTA)
        self.assertAlmostEqual(12.5, np.float(np.var([10, 5], ddof=1)), delta=self.DELTA)

    def test_xavg(self):
        self.assertAlmostEqual(1.5, MyStat.xavg([5, 0, 3], [0, 1, 1]), delta=self.DELTA)
        self.assertAlmostEqual(0, MyStat.xavg([10, 5], [0,0]), delta=self.DELTA)

    def test_xvar(self):
        self.assertAlmostEqual(4.5, MyStat.xvar([5, 0, 3], [0, 1, 1]), delta=self.DELTA)
        self.assertAlmostEqual(0, MyStat.xvar([10, 5], [0, 0]), delta=self.DELTA)



if __name__ == '__main__':
    unittest.main()
