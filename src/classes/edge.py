from math import sqrt

class Edge:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

        # self.length = distanceBetweenPoints(point1, point2)

    def length(self):
        return sqrt(((self.point1[0] - self.point2[0])**2 + (self.point1[1] - self.point2[1])**2))

    def __eq__(self, other):
        return (((self.point1 == other.point1) and (self.point2 == other.point2)) or ((self.point1 == other.point2) and (self.point2 == other.point1)))
    
    def __hash__(self):
        return hash((self.point1, self.point2))
    
    def __str__(self):
        return str((self.point1, self.point2))
    
if __name__ == "__main__":
    a = Edge((0,1), (1,0))
    b = Edge((1,0),(0,1))

    print((a == b))
    print(a.length())