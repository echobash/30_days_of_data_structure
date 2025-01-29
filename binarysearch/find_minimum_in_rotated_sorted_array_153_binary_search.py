from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n-1
        result = float('inf')
        while left<=right:
            mid = (left+right)//2
            """
            1. Initalise result = float('inf')
            2. Find the sorted half
            3. Get minimum from that half
            4. If Left half is sorted, update minimum by result = min(result,nums[left])
            5. If Right half is sorted, update minimum by result = min(result,nums[mid])
            6. Once the minimum result is updated, discard that half, since we already have min from here
            7. Go to the other half
            8. And repeat the same
            """
            if nums[left] <= nums[mid]:
                # Left part is sorted
                result = min(result, nums[left])
                left = mid + 1
            elif nums[mid] <= nums[right]:
                # Right Part is sorted
                result = min(result, nums[mid])
                right = mid - 1
        return result


sol = Solution()

nums = [4,5,6,7,0,1,2]
print(f"{nums = } {sol.findMin(nums,) = }")

nums = [4,5,6,7,9,1,2]
print(f"{nums = } {sol.findMin(nums,) = }")

nums = [1]
print(f"{nums = } {sol.findMin(nums,) = }")

nums = [3,4,5,1,2]
print(f"{nums = } {sol.findMin(nums,) = }")

nums = [15,18,20,25,30,35,40,45,5,10,12,14]
print(f"{nums = } {sol.findMin(nums,) = }")

nums = [20,25,30,35,40,45]
print(f"{nums = } {sol.findMin(nums,) = }")



