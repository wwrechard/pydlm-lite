import pydlm_lite
import unittest

class testSeasonality(unittest.TestCase):

    def setUp(self):
        self.DEGREE = 7
        
    def testInitialization(self):
        newSeasonality = pydlm_lite.modeler.seasonality.seasonality(self.DEGREE)
        newSeasonality.checkDimensions()

if __name__ == '__main__':
    unittest.main()
        
