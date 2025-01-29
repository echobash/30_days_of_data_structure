from math import ceil
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        piles = [7,15,6,3]
        h = 8
        k = ?
        """
        max_piles = max(piles)
        for k in range(1, max_piles+1):
            if sum([ceil(i/k) for i in piles]) <= h:
                return k


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

piles = [312884470]
h = 312884469
print(f"{piles = } | {sol.minEatingSpeed(piles, h) = }")
