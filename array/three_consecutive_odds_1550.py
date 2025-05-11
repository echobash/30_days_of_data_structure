from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        n = len(arr)

        for i in range(n-2):
            if arr[i] % 2 and arr[i+1] % 2 and arr[i+2] % 2:
                return True
        return False


sol = Solution()

arr = [2,6,4,1]
print(f" {arr = } | {sol.threeConsecutiveOdds(arr) = }")

arr = [1,2,34,3,4,5,7,23,12]
print(f" {arr = } | {sol.threeConsecutiveOdds(arr) = }")

arr = [2,6,4]
print(f" {arr = } | {sol.threeConsecutiveOdds(arr) = }")

arr = [21,63,45]
print(f" {arr = } | {sol.threeConsecutiveOdds(arr) = }")

arr = [21,63]
print(f" {arr = } | {sol.threeConsecutiveOdds(arr) = }")

arr = [63]
print(f" {arr = } | {sol.threeConsecutiveOdds(arr) = }")

arr = []
print(f" {arr = } | {sol.threeConsecutiveOdds(arr) = }")
