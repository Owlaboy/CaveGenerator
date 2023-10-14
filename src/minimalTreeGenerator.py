from classes.edge import Edge
from functions.distanceBetweenPoints import distanceBetweenPoints

# just for testing
from functions.pygameTestRenderer import drawEdges, drawPoints
from triangulator import BowyerWatson

MAXDIST = 99999999999999999


def prim(triangulationEdges):
    """This function  generates a minimum spanning tree out of the given triangulation

    Args:
        triangulationEdges (list): list of all the triangulation edges

    Returns:
        list: list of all the edges in the tree
    """
    pointList = []
    nodeHash = {}
    for triangle in triangulationEdges:
        for edge in triangle.sides:
            if edge.point1 not in pointList:
                pointList.append(edge.point1)
                nodeHash[edge.point1] = []
            if edge.point2 not in pointList:
                pointList.append(edge.point2)
                nodeHash[edge.point2] = []

            if (edge.point2) in nodeHash[edge.point1]:
                continue
            else:
                nodeHash[edge.point1].append((edge.point2))
            if (edge.point1) in nodeHash[edge.point2]:
                continue
            else:
                nodeHash[edge.point2].append((edge.point1))

    minimumSpanningTree = []
    addedPoints = [pointList[0]]
    notAddedPoints = pointList[1:]

    for point in notAddedPoints:
        if pointList[0] in nodeHash[point]:
            nodeHash[point].remove(pointList[0])

    while len(minimumSpanningTree) < len(pointList)-1:
        shortestDist = MAXDIST
        for addedPoint in addedPoints:
            for point in nodeHash[addedPoint]:
                distance = distanceBetweenPoints(addedPoint, point)
                if distance < shortestDist:
                    shortestDist = distance
                    sourceNode = addedPoint
                    nextToAdd = point

        addedPoints.append(nextToAdd)
        minimumSpanningTree.append(Edge(sourceNode, nextToAdd))
        for point in pointList:
            if nextToAdd in nodeHash[point]:
                nodeHash[point].remove(nextToAdd)

    return minimumSpanningTree


if __name__ == "__main__":
    testingArray = [(812, 422), (686, 311), (782, 512), (288, 67), (793, 234),
                    (756, 354), (65, 406), (853, 493), (395, 442), (630, 478)]
    a = BowyerWatson(testingArray[:], 1000, 500)

    edges = prim(a)
    drawEdges(edges)
