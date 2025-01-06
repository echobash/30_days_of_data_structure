from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(heights)
        age_name_mapping = {}
        result = []

        for i in range(n):
            age_name_mapping[heights[i]] = names[i]

        heights = sorted(heights, reverse=True)
        for height in heights:
            result.append(age_name_mapping[height])
        return result


solution = Solution()

names = ["Mary","John","Emma"]
heights = [180,165,170]
print(names, heights, solution.sortPeople(names, heights))

names = ["Alice","Bob","Bob"]
heights = [155,185,150]
print(names, heights, solution.sortPeople(names, heights))
