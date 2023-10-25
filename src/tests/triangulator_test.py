import unittest
import shapely
import random
from triangulator import BowyerWatson

class TestTriangulator(unittest.TestCase):
    def setUp(self):
        self.testingArray = [(812, 422), (686, 311), (782, 512), (288, 67), (793, 234),
                    (756, 354), (65, 406), (853, 493), (395, 442), (630, 478)]
        self.triangulation = BowyerWatson(self.testingArray, 1000, 500)

    def test_trianglesDoNotIntersect(self):
        for triangle in self.triangulation:
            for otherTriangle in self.triangulation:
                if triangle == otherTriangle:
                    continue
                else:
                    for side in triangle.sides:
                        for otherSide in otherTriangle.sides:
                            if side.point1 == otherSide.point1 or side.point1 == otherSide.point2:
                                continue
                            elif side.point2 == otherSide.point1 or side.point2 == otherSide.point2:
                                continue

                            line1 = shapely.LineString([side.point1, side.point2])
                            line2 = shapely.LineString([otherSide.point1, otherSide.point2])
                            intersects = shapely.intersects(line1, line2)                            
                            
                            self.assertEqual(intersects, False)

    def test_allRoomPointsAreInTriangulation(self):
        points = self.testingArray.copy()

        for triangle in self.triangulation:
            if triangle.pointA in points:
                points.remove(triangle.pointA)
            if triangle.pointB in points:
                points.remove(triangle.pointB)
            if triangle.pointC in points:
                points.remove(triangle.pointC)
                    
        self.assertEqual(len(points),0)

    def test_theTriangulationIsUnique(self):
        mixedTestintArray = self.testingArray.copy()
        random.shuffle(mixedTestintArray)

        a = BowyerWatson(self.testingArray, 1000, 500)
        b = BowyerWatson(mixedTestintArray, 1000, 500)

        aSet = set()
        for aTriangle in a:
            aSet.add(aTriangle.pointSet)
        
        bSet = set()
        for bTriangle in b:
            bSet.add(bTriangle.pointSet)


        self.assertEqual(aSet, bSet)
            