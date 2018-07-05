import pydlm_lite
import unittest

class testTrend(unittest.TestCase):

    def setUp(self):
        self.DEGREE = 3
        
    def testInitialization(self):
        newTrend = pydlm_lite.modeler.trends.trend(self.DEGREE)
        newTrend.checkDimensions()

if __name__ == '__main__':
    unittest.main()
