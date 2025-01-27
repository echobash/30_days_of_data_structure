from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        current_set = set(arr)
        count = 0
        for i in range(1,2001):
            if i not in current_set:
                count += 1
                if count == k:
                    return i


sol = Solution()

arr = [2,3,4,7,11]
k = 5
print(f"{arr= } {sol.findKthPositive(arr,k)= }")

arr = [1,2,3,4]
k = 2
print(f"{arr= } {sol.findKthPositive(arr,k)= }")

arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
k = 999
print(f"{arr= } {sol.findKthPositive(arr,k)= }")

