from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        local_maxima_count = 0
        for i in range(1, n - 1):
            # count the no. of local maxima
            if arr[i - 1] < arr[i] > arr[i + 1]:
                local_maxima_count += 1
            # There shouldn't be any local minima and no two consecutive no should be equal
            if arr[i - 1] >= arr[i] <= arr[i + 1]:
                return False

        return local_maxima_count == 1


sol = Solution()

arr = [2,1]
print(arr, sol.validMountainArray(arr))

arr = [3,5,5]
print(arr, sol.validMountainArray(arr))

arr = [0,3,2,1]
print(arr, sol.validMountainArray(arr))

arr =[0,2,3,3,5,2,1,0]
print(arr, sol.validMountainArray(arr))

arr = [0,3,2,1,2]
print(arr, sol.validMountainArray(arr))
