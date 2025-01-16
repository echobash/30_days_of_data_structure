from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # max[(x-1)(y-1)]
        # max[xy -(x+y) +1]
        # max[xy -(x+y)]
        # xy is always >= than x+y for x>=2. So we just need to find max and second max of array
        # and for x==1 or y==1, they will already come in last ie smaller in value

        #So our aim here is just to find max and second max of array say max_no, second_max_no
        # and return max_no * second_max_no - max_no - second_max_no + 1
        nums = sorted(nums, reverse = True)
        return nums[0] * nums[1] - nums[0] - nums[1] + 1



sol = Solution()

nums = [3,4,5,2]
print(nums, sol.maxProduct(nums))


nums = [1,5,4,5]
print(nums, sol.maxProduct(nums))


nums = [3,7]
print(nums, sol.maxProduct(nums))

