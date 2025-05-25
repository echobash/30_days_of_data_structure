from typing import List
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Iterate on points array and add (distance, [point]) on max-heap
        Then put keys in a max-heap and get kth smallest distance
        If there are duplicate distances, no worry, heap handles that well as a new entry
        """

        heap = []
        for point in points:
            distance = point[0] ** 2 + point[1] ** 2
            if len(heap) < k:
                heapq.heappush(heap, (-distance, point))
            elif -distance > heap[0][0]:
                heapq.heapreplace(heap, (-distance, point))

        result = []
        for distance, point in heap:
            result.append(point)
        return result


sol = Solution()

points = [[1,3],[-2,2]]
k = 1
print(f"{points = } {sol.kClosest(points, k) = }")

points = [[3,3],[5,-1],[-2,4]]
k = 1
print(f"{points = } {sol.kClosest(points, k) = }")

points = [[1,3],[-2,2],[2,-2]]
k = 2
print(f"{points = } {sol.kClosest(points, k) = }")
