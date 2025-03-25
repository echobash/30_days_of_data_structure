from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        left, right = 0, n-1
        ans = -1
        # 0, 7, 10, 5, 2
        # If we compare a[i] and a[i+1] and
        # a[i] < a[i+1] => We'll get peak in right since the arr still is increasing and will decrease after some elements
        # a[i] > a[i+1] => We'll get peak in left since the arr is decreasing now that means it has already increased in past
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                ans = mid
                right = mid - 1
        return ans





sol = Solution()

arr = [0,1,0]
print(f"{arr = } {sol.peakIndexInMountainArray(arr) = }")

arr = [0,2,1,0]
print(f"{arr = } {sol.peakIndexInMountainArray(arr) = }")

arr = [0,7,10,5,2]
print(f"{arr = } {sol.peakIndexInMountainArray(arr) = }")