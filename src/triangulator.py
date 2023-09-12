from math import sqrt, acos, sin



testingArray = [(812, 422), (686, 311), (782, 512), (288, 67), (793, 234), (756, 354), (65, 406), (853, 493), (395, 442), (630, 478)]

class Edge:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

def findCircumCenter(point1, point2, point3):
    centerX = (point1[0] + point2[0] + point3[0])/3
    centerY = (point1[0] + point2[0] + point3[0])/3

def distanceBetweenPoints(point1: tuple, point2: tuple):
    return sqrt(((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2))

class Triangle:
    def __init__(self, point1, point2, point3):
        self.pointA = point1
        self.pointB = point2
        self.pointC = point3
        
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

    def checkIfPointIsWithinCirle(self, point):
        return distanceBetweenPoints(point, self.circleCenter) <= self.radius

    



def BowyerWatson(roomCenters):
    pass


if __name__ == "__main__":
    triangleboi = Triangle((0,0),(0,4),(4,0))

    print(triangleboi.circumCenterX)
    print(triangleboi.circumCenterY)
    print(triangleboi.radius)

    print(triangleboi.checkIfPointIsWithinCirle((1,1)))
    print(triangleboi.checkIfPointIsWithinCirle((5,3)))