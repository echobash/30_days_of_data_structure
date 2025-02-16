from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # arr = [2,3,4,7,11]
        n = len(arr)
        missing_count = 0
        set_of_given_no = set(arr)
        # the missing no will always lie b/w 1, len(arr) + k
        for i in range(1, n+k+1):
            if i not in set_of_given_no:
                missing_count += 1
            if missing_count == k:
                return i


sol = Solution()

arr = [2,3,4,7,11]
k = 5
print(f"{arr= } | {k = } {sol.findKthPositive(arr,k)= }")

arr = [1,2,3,4]
k = 2
print(f"{arr= } | {k = } {sol.findKthPositive(arr,k)= }")

arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
k = 999
print(f"{arr= } | {k = } {sol.findKthPositive(arr,k)= }")

