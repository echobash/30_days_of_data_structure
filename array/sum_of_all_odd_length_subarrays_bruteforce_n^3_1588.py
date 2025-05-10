from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        result = []
        count = 0
        for i in range(n):
            subarrays = []
            for j in range(i,n):
                subarrays.append(arr[j])
                if len(subarrays) % 2 == 1:
                    count += sum(subarrays)
        return count


sol = Solution()

arr = [1,4,2,5,3]
print(f" {arr = } | {sol.sumOddLengthSubarrays(arr) = }")

arr = [1,2]
print(f" {arr = } | {sol.sumOddLengthSubarrays(arr) = }")

arr = [10,11,12]
print(f" {arr = } | {sol.sumOddLengthSubarrays(arr) = }")

arr = [10]
print(f" {arr = } | {sol.sumOddLengthSubarrays(arr) = }")
