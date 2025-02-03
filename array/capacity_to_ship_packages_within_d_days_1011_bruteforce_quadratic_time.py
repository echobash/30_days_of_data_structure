from math import ceil
from typing import List


class Solution:
    def get_no_of_days(self,w,cap):
        sum = 0
        d = 0
        i = 0
        while i < len(w):
            sum += w[i]
            if sum <= cap:
                i += 1
                if i == len(w)-1:
                    d += 1
                continue
            else:
                d += 1
                sum = 0
        return d

    def shipWithinDays(self, w: List[int], days: int) -> int:
        if days == 1:
            return sum(w)
        left, right = max(w), sum(w)+1
        for cap in range(left, right):
            days_required = self.get_no_of_days(w,cap)
            if days_required <= days:
                return cap



sol = Solution()

weights = [3,2,2,4,1,4]
days = 3
print(f"{weights = } | {sol.shipWithinDays(weights, days) = }")

weights = [5,4,4,5,2,3,4,5,6]
days = 5
print(f"{weights = } | {sol.shipWithinDays(weights, days) = }")

weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
print(f"{weights = } | {sol.shipWithinDays(weights, days) = }")