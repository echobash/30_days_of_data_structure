from typing import List
from collections import defaultdict


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        in_out_count = defaultdict(int)
        source_or_destination = []

        # we know that only source and destination will have 1 count and rest all will be twice

        for source, destination in paths:
            in_out_count[source] += 1

        for source, destination in paths:
            in_out_count[destination] += 1

        for location, freq in in_out_count.items():
            if freq == 1:
                source_or_destination.append(location)

        for source, destination in paths:
            if destination == source_or_destination[0]:
                return source_or_destination[0]
        return source_or_destination[1]


sol = Solution()

paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
print(f"{paths = } {sol.destCity(paths) = }")

paths = [["B","C"],["D","B"],["C","A"]]
print(f"{paths = } {sol.destCity(paths) = }")

paths = [["A","Z"]]
print(f"{paths = } {sol.destCity(paths) = }")
