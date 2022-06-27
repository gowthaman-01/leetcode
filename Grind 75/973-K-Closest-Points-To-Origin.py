import heapq


def kClosest(points, k):
    output = []
    for i, point in enumerate(points):
        distance = point[0] ** 2 + point[1] ** 2
        points[i] = (distance, point)
    heapq.heapify(points)
    for i in range(k):
        output.append(heapq.heappop(points)[1])
    return output
