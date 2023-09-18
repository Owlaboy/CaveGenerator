
from classes.triangle import Triangle

def BowyerWatson(roomCenterPoints, sizeX, sizeY):
    superTriangle = Triangle((0,0), (sizeX*2, 0), (0, sizeY*2))

    triangulation = [superTriangle]

    for point in roomCenterPoints:
        badTriangles = []

        for triangle in triangulation: # First find all the triangles that are no longer valid due to the insertion
            if triangle.checkIfPointIsWithinCirle(point):
                badTriangles.append(triangle)
        
        polygon = set()
        if len(badTriangles) == 1:
            polygon = badTriangles[0].sides
        else:
            i = 0
            while i < len(badTriangles):
                for side in badTriangles[i].sides:
                    for otherBadTriangle in badTriangles[i:]:
                        for otherSide in otherBadTriangle.sides:
                            print(f"side: {side} and otherside: {otherSide}")
                            if (((side.point1 == otherSide.point1) and (side.point2 == otherSide.point2)) or ((side.point1 == otherSide.point2) and (side.point2 == otherSide.point1))):
                                print("added side")
                                polygon.add(side)
                i+=1
                            # else:
                            #     print("didnt add side")

            # for triangle in badTriangles: # Find the boundary of the polygonal hole
            #     for side in triangle.sides:
            #         for otherBadTriangle in badTriangles:
            #             if otherBadTriangle == triangle:
            #                 continue
            #             for otherSide in otherBadTriangle.sides:
            #                 print(f"side: {side} and otherside: {side}")
            #                 if (((side.point1 == otherSide.point1) and (side.point2 == otherSide.point2)) or ((side.point1 == otherSide.point2) and (side.point2 == otherSide.point1))):
            #                     print("added side")
            #                     polygon.add(side)
            #                 else:
            #                     print("didnt add side")

        for triangle in badTriangles:
            i = 0
            while i < len(triangulation):
                if triangle == triangulation[i]:
                    triangulation.pop(i)
                else:
                    i += 1
        
        for edge in polygon:
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
    a = BowyerWatson(testingArray[:4], 1000, 500)
    print(a)
    for triangle in a:
        print(str(triangle))

    print(triangleboi.circumCenterX)
    print(triangleboi.circumCenterY)
    print(triangleboi.radius)

    print(triangleboi.checkIfPointIsWithinCirle((1,1)))
    print(triangleboi.checkIfPointIsWithinCirle((5,3)))