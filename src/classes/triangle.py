from classes.edge import Edge
from functions.distanceBetweenPoints import distanceBetweenPoints
from math import acos, sin
import sys

sys.path.append('../src')


class Triangle:
    def __init__(self, point1, point2, point3):
        """initializator of the object. This method also calculates the circumcenter/circle of the triangle.

        Args:
            point1 (tuple): first point
            point2 (tuple): second point
            point3 (tuple): third point
        """
        self.pointList = [point1, point2, point3]
        self.pointA = point1
        self.pointB = point2
        self.pointC = point3
        self.points = [point1, point2, point3]
        self.pointSet = frozenset({point1, point2, point3})
        self.sides = [Edge(point1, point2), Edge(
            point2, point3), Edge(point1, point3)]

        self.distA = distanceBetweenPoints(self.pointB, self.pointC)
        self.distB = distanceBetweenPoints(self.pointA, self.pointC)
        self.distC = distanceBetweenPoints(self.pointA, self.pointB)

        self.angleA = acos((self.distB**2 + self.distC**2 -
                           self.distA**2)/(2 * self.distB * self.distC))
        self.angleB = acos((self.distA**2 + self.distC**2 -
                           self.distB**2)/(2 * self.distA * self.distC))
        self.angleC = acos((self.distA**2 + self.distB**2 -
                           self.distC**2)/(2 * self.distA * self.distB))

        self.circumCenterX = (self.pointA[0]*sin(2*self.angleA)+self.pointB[0]*sin(2*self.angleB) +
                              self.pointC[0]*sin(2*self.angleC))/(sin(2*self.angleA)+sin(2*self.angleB)+sin(2*self.angleC))
        self.circumCenterY = (self.pointA[1]*sin(2*self.angleA)+self.pointB[1]*sin(2*self.angleB) +
                              self.pointC[1]*sin(2*self.angleC))/(sin(2*self.angleA)+sin(2*self.angleB)+sin(2*self.angleC))

        self.circleCenter = (self.circumCenterX, self.circumCenterY)
        self.radius = distanceBetweenPoints(self.circleCenter, self.pointA)

    def __str__(self):
        return f"{self.pointA} ,{self.pointB}, {self.pointC}"

    def __eq__(self, other):
        return self.pointSet == other.pointSet

    def __hash__(self,):
        return hash((self.pointA, self.pointB, self.pointC))

    def checkIfPointIsWithinCirle(self, point):
        """This method tells whether the given point is within the circum circle of the triangle

        Args:
            point (tuple): the point we want to check

        Returns:
            bool: true if the point is within the circumcircle, false if it is not
        """
        return distanceBetweenPoints(point, self.circleCenter) <= self.radius
