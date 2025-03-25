from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                return i


sol = Solution()

arr = [0,1,0]
print(sol.peakIndexInMountainArray(arr))

arr = [0,2,1,0]
print(sol.peakIndexInMountainArray(arr))

arr = [0,10,5,2]
print(sol.peakIndexInMountainArray(arr))