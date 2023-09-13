from math import sqrt, acos, sin

testingArray = [(812, 422), (686, 311), (782, 512), (288, 67), (793, 234), (756, 354), (65, 406), (853, 493), (395, 442), (630, 478)]

class Edge:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

        self.length = sqrt(((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2))

def distanceBetweenPoints(point1: tuple, point2: tuple):
    return sqrt(((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2))

class Triangle:
    def __init__(self, point1, point2, point3):
        self.pointA = point1
        self.pointB = point2
        self.pointC = point3
        self.sides = [Edge(point1,point2), Edge(point2,point3), Edge(point1,point3)]
        
        self.distA = distanceBetweenPoints(self.pointB, self.pointC)
        self.distB = distanceBetweenPoints(self.pointA, self.pointC)
        self.distC = distanceBetweenPoints(self.pointA, self.pointB)

        self.angleA = acos((self.distB**2 + self.distC**2 - self.distA**2)/(2 * self.distB * self.distC))
        self.angleB = acos((self.distA**2 + self.distC**2 - self.distB**2)/(2 * self.distA * self.distC))
        self.angleC = acos((self.distA**2 + self.distB**2 - self.distC**2)/(2 * self.distA * self.distB))

        self.circumCenterX = (self.pointA[0]*sin(2*self.angleA)+self.pointB[0]*sin(2*self.angleB)+self.pointC[0]*sin(2*self.angleC))/(sin(2*self.angleA)+sin(2*self.angleB)+sin(2*self.angleC))
        self.circumCenterY = (self.pointA[1]*sin(2*self.angleA)+self.pointB[1]*sin(2*self.angleB)+self.pointC[1]*sin(2*self.angleC))/(sin(2*self.angleA)+sin(2*self.angleB)+sin(2*self.angleC))

        self.circleCenter = (self.circumCenterX, self.circumCenterY)
        self.radius = distanceBetweenPoints(self.circleCenter, self.pointA)

    def __str__(self):
        return f"{self.pointA} ,{self.pointB}, {self.pointC}"

    def checkIfPointIsWithinCirle(self, point):
        return distanceBetweenPoints(point, self.circleCenter) <= self.radius

    

def BowyerWatson(roomCenterPoints):
    SuperTriangle = Triangle((0,0), (2000,0), (0,1000))

    triangulation = [SuperTriangle]

    for point in roomCenterPoints:
        badTriangles = []

        for triangle in triangulation: # First find all the triangles that are no longer valid due to the insertion
            if triangle.checkIfPointIsWithinCirle(point):
                badTriangles.append(triangle)
        
        polygon = []
        if len(badTriangles) == 1:
            polygon = badTriangles[0].sides
        else:
            for triangle in badTriangles: # Find the boundary of the polygonal hole
                for side in triangle.sides:
                    for otherTriangles in badTriangles:
                        if otherTriangles == triangle:
                            continue
                        for otherSide in otherTriangles:
                            if otherSide != side:
                                polygon.append(side)
        
        for triangle in badTriangles:
            triangulation.remove(triangle)
        
        for edge in polygon:
            newTriangle = Triangle(edge.point1, edge.point2, point)
            triangulation.append(newTriangle)

    for triangle in triangulation:
        pass

    return triangulation


if __name__ == "__main__":
    triangleboi = Triangle((0,0),(0,4),(4,0))
    

    a = BowyerWatson(testingArray[:4])
    print(a)
    for triangle in a:
        print(str(triangle))

    print(triangleboi.circumCenterX)
    print(triangleboi.circumCenterY)
    print(triangleboi.radius)

    print(triangleboi.checkIfPointIsWithinCirle((1,1)))
    print(triangleboi.checkIfPointIsWithinCirle((5,3)))