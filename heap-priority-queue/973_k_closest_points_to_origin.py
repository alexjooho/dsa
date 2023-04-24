class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # for every point in points, calculate distance to origin and add that to the array
        # sort by shortest distance

        # create an array and add the k closest points without their distance
        # O(n log n) time complexity

        import math

        for i in range(len(points)):
            x, y = points[i][0], points[i][1]
            distance = math.sqrt(x ** 2 + y ** 2)
            # technically don't need to do sqrt since we're just finding relative distance
            # but still need to do the **'s
            points[i].append(distance)

        points.sort(key = lambda x: x[2])

        res = []

        for i in range(k):
            res.append([points[i][0], points[i][1]])

        return res
    
# neetcode heap solution (better):
# create an array of points with the distance from origin as the first value: [distance, x, y]
# heapify this array and then heappop k times and append to result array for each popped point

# time complexity: O(n + klogk) -> O(k log k)
    # this heap solution is better if there are many points n
# since each pop from heap is logk time complexity, and we have to pop k times
# creating the heap costs n time

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pts = []
        # have to make a new array since we have to create augmented arrays with the
        # distance being the first value, since heap sorts by first value
        for x, y in points:
            dist = (abs(x - 0) ** 2) + (abs(y - 0) ** 2)
            pts.append([dist, x, y])

        res = []
        heapq.heapify(pts)
        for i in range(k):
            dist, x, y = heapq.heappop(pts)
            res.append([x, y])
        return res
