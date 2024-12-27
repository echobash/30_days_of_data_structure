from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges)

        # In an star graph all node have degree one and only center node has degree > 1 and i.e n-1 degree
        # So the node which appears common in any two edges is definitely our center of star graph

        edge1 = edges[0]
        edge2 = edges[1]

        if edge1[0] == edge2[0] or edge1[0] == edge2[1]:
            return edge1[0]
        else:
            return edge1[1]



solution = Solution()

edges = [[1,2],[2,3],[4,2]]
print(solution.findCenter(edges))

edges = [[1,2],[5,1],[1,3],[1,4]]
print(solution.findCenter(edges))
