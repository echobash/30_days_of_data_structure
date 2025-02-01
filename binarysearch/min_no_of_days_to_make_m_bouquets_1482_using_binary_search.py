from math import ceil
from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        max_day = max(bloomDay)
        min_day = min(bloomDay)
        bouquet_count = 0

        if m * k > n:
            return -1

        ans = -1
        left, right = min_day, max_day
        while left <= right:
            mid = (left+right)//2
            flower_count = 0
            bouquet_count = 0
            for j in range(n):
                if mid >= bloomDay[j]:
                    flower_count += 1
                    if flower_count == k:
                        bouquet_count += 1
                        flower_count = 0
                        if bouquet_count == m:
                            ans = mid
                else:
                    flower_count = 0
            if bouquet_count >= m:
                right = mid - 1
            else:
                left = mid + 1
        return ans


sol = Solution()

bloomDay = [1,10,3,10,2]
m = 3
k = 1
print(f"{bloomDay = } | {m = } | {k = } | {sol.minDays(bloomDay, m, k) = }")

bloomDay = [1,10,3,10,2]
m = 3
k = 2
print(f"{bloomDay = } | {m = } | {k = } | {sol.minDays(bloomDay, m, k) = }")

bloomDay = [7,7,7,7,12,7,7]
m = 2
k = 3
print(f"{bloomDay = } | {m = } | {k = } | {sol.minDays(bloomDay, m, k) = }")

bloomDay = [10000000000,10000000000]
m = 1
k = 1
print(f"{bloomDay = } | {m = } | {k = } | {sol.minDays(bloomDay, m, k) = }")
