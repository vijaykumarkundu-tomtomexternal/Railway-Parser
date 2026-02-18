import math


def polyline_length(points):
    total = 0
    for i in range(1, len(points)):
        total += math.dist(points[i-1], points[i])
    return total


def distance(p1, p2):
    return math.dist(p1, p2)