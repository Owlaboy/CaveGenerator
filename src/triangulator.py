
from classes.triangle import Triangle
import random
import pygameTestRenderer

def badTrianglesList(triangleList, point):
    badTriangles = []

    for triangle in triangleList: # First find all the triangles that are no longer valid due to the insertion
            if triangle.checkIfPointIsWithinCirle(point):
                badTriangles.append(triangle) # tarkistetaan oikeat boolean arvot.
    
    return badTriangles

def polygonEdges(badTriangleList):
    allSides = []
    for triangle in badTriangleList:
        for side in triangle.sides:
            allSides.append(side)

    polygon = set()
    for side in allSides:
        if allSides.count(side) == 1:
            polygon.add(side)

    return polygon

def BowyerWatson(roomCenterPoints, sizeX, sizeY):
    superTriangle = Triangle((0,0), (sizeX*2, 0), (0, sizeY*2))

    triangulation = [superTriangle]

    for point in roomCenterPoints:

        badTriangles = badTrianglesList(triangulation, point) # This function selects the bad triangles from the triangulation.
        
        polygon = polygonEdges(badTriangles) # This function generates the polygon from the bad triangles.
        
        for triangle in badTriangles: # This loop removes the bad triangles from the triangulation.
            i = 0
            while i < len(triangulation): # voidaan mennä lopusta alkuun!!!
                if triangle == triangulation[i]:
                    triangulation.pop(i)
                else:
                    i += 1

        for edge in polygon: # This loop adds a new triagle to the triangulation for every edge in the polygon.
            newTriangle = Triangle(edge.point1, edge.point2, point)
            triangulation.append(newTriangle)

    finalTriangulation = []

    for triangle in triangulation:
        if ((0,0) in triangle.points) or ((sizeX*2,0) in triangle.points) or ((0, sizeY*2) in triangle.points):
            continue
        else:
            finalTriangulation.append(triangle)

    return finalTriangulation


if __name__ == "__main__":
    triangleboi = Triangle((0,0),(0,4),(4,0))

    testingArray = [(812, 422), (686, 311), (782, 512), (288, 67), (793, 234), (756, 354), (65, 406), (853, 493), (395, 442), (630, 478)]
    mixedTestintArray = testingArray.copy()
    random.shuffle(mixedTestintArray)
    
    print(testingArray)
    print(mixedTestintArray)

    a = BowyerWatson(testingArray, 1000, 500)
    b = BowyerWatson(mixedTestintArray, 1000, 500)
    
    pygameTestRenderer.drawTriangles(a)
    pygameTestRenderer.drawTriangles(b)