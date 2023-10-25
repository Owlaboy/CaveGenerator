import unittest
from triangulator import BowyerWatson
from minimalTreeGenerator import prim

class TestTriangulator(unittest.TestCase):
    def setUp(self):
        self.testingArray = [(812, 422), (686, 311), (782, 512), (288, 67), (793, 234),
                    (756, 354), (65, 406), (853, 493), (395, 442), (630, 478)]
        self.triangulation = BowyerWatson(self.testingArray, 1000, 500)
        self.minimumTree = prim(self.triangulation)

    def test_PrimReturnsCorrectAmountOfLines(self):
        self.assertEqual(len(self.minimumTree), len(self.testingArray)-1)
