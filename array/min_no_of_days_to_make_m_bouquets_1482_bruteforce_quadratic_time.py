from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        max_day = max(bloomDay)
        min_day = min(bloomDay)
        bouquet_count = 0

        if m * k > n:
            return -1

        for i in range(min_day, max_day+1):
            flower_count = 0
            for j in range(n):
                if i >= bloomDay[j]:
                    flower_count += 1
                    if flower_count == k:
                        bouquet_count += 1
                        flower_count = 0
                        if bouquet_count == m:
                            return i
                else:
                    flower_count = 0
            if bouquet_count != m:
                bouquet_count = 0
        return -1



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
