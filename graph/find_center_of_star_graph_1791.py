from collections import defaultdict
from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        node_count_mapping = defaultdict(int)

        n = len(edges)
        for edge in edges:
            node_count_mapping[edge[0]] += 1
            node_count_mapping[edge[1]] += 1

        print(node_count_mapping)
        for node, edges in node_count_mapping.items():
            if edges == n:
                return node


solution = Solution()

edges = [[1,2],[2,3],[4,2]]
print(solution.findCenter(edges))

edges = [[1,2],[5,1],[1,3],[1,4]]
print(solution.findCenter(edges))
