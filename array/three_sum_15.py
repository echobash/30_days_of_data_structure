from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        nums = sorted(nums)
        for i in range(n-2):
            target = -1 * nums[i]
            left,right = i+1, n-1

            # Make sure duplicate starting no not taken
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while left < right:
                if nums[left] + nums[right] == target:
                    # Make sure duplicate last no not taken
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1

                    # Make sure duplicate second no not taken
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    left += 1
        return result


sol = Solution()

nums = [-1,0,1,2,-1,-4]
print(f"{nums = }  {sol.threeSum(nums) = }")

nums = [0,1,1]
print(f"{nums = }  {sol.threeSum(nums) = }")

nums = [0,0,0]
print(f"{nums = }  {sol.threeSum(nums) = }")

nums = [2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]
print(f"{nums = }  {sol.threeSum(nums) = }")

nums = [-4,-1,-1,0,0,1,2,2]
print(f"{nums = }  {sol.threeSum(nums) = }")