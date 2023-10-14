import unittest
import shapely
from triangulator import BowyerWatson
from functions.roomGenerator import roomRectGenerator, roomPoints

class TestTriangulator(unittest.TestCase):
    def setUp(self):
        self.room_list = roomRectGenerator(1000, 500, 10)
        self.roomPoints = roomPoints(self.room_list)
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

    def test_allRoomPointsAreInTriangulation(self):
        points = self.roomPoints.copy()

        for triangle in self.triangulation:
            if triangle.pointA in points:
                points.remove(triangle.pointA)
            if triangle.pointB in points:
                points.remove(triangle.pointB)
            if triangle.pointC in points:
                points.remove(triangle.pointC)
                    
        self.assertEqual(len(points),0)
            