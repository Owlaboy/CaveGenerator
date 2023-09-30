import unittest
import shapely
import pygameTestRenderer
from triangulator import BowyerWatson
from display import RoomRectGenerator, RoomPoints


class TestTriangulator(unittest.TestCase):
    def setUp(self):
        self.roomList = RoomRectGenerator(1000, 500, 10)
        self.roomPoints = RoomPoints(self.roomList)
        self.triangulation = BowyerWatson(self.roomPoints, 1000, 500)


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

    def test_polygonDoesntHaveAnIntersectingLine(self):
        pass

    def test_test(self):
        self.assertEqual(1,1)