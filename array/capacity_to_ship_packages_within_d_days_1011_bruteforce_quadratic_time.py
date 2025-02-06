from math import ceil
from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # We know that the ans will definitely lie b/w max(w) and sum(w)
        if days == 1:
            return sum(weights)

        left, right = max(weights), sum(weights) + 1

        for min_cap in range(left, right):
            current_sum = 0
            day = 1
            for weight in weights:
                if current_sum + weight <= min_cap:
                    current_sum += weight
                else:
                    day += 1
                    current_sum = weight
            if day <= days:
                return min_cap


sol = Solution()

weights = [3,2,2,4,1,4]
days = 3
print(f"{weights = }  | {days = } | {sol.shipWithinDays(weights, days) = }")

weights = [5,4,4,5,2,3,4,5,6]
days = 5
print(f"{weights = }  | {days = } | {sol.shipWithinDays(weights, days) = }")

weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
print(f"{weights = }  | {days = } | {sol.shipWithinDays(weights, days) = }")

weights = [1,2,3,1,1]
days = 4
print(f"{weights = }  | {days = } | {sol.shipWithinDays(weights, days) = }")
