from math import ceil
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        piles = [7,15,6,3]
        h = 8
        k = ?
        """
        counter = 0
        result = float('inf')
        while result > h:
            counter += 1
            result = sum([ceil(i / counter) for i in piles])
        return counter


sol = Solution()

piles = [7,15,6,3]
h = 8
print(f"{piles = } | {sol.minEatingSpeed(piles, h) = }")

piles = [3,6,7,11]
h = 8
print(f"{piles = } | {sol.minEatingSpeed(piles, h) = }")

piles = [30,11,23,4,20]
h = 5
print(f"{piles = } | {sol.minEatingSpeed(piles, h) = }")

piles = [30,11,23,4,20]
h = 6
print(f"{piles = } | {sol.minEatingSpeed(piles, h) = }")
