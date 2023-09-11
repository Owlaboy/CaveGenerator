
testingArray = [(812, 422), (686, 311), (782, 512), (288, 67), (793, 234), (756, 354), (65, 406), (853, 493), (395, 442), (630, 478)]

class Edge:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

class Triangle:
    def __init__(self, point1, point2, point3):
        self.pointa = point1
        self.pointb = point2
        self.pointc = point3
        
        


        self.cirumCenter = findCircumCenter(point1, point2, point3)

    def findCircumCenter(point1, point2, point3):
        centerX = (point1[0] + point2[0] + point3[0])/3
        centerY = (point1[0] + point2[0] + point3[0])/3
    



def BowyerWatson(roomCenters):
    pass
