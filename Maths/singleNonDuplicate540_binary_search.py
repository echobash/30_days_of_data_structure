from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]):
        pass
        # [1,1,2,2, 3, 4,4,8,8]
        # [1,1,2,3, 3, 4,4,8,8]
        # [1,1,2,2, 3, 3,4,8,8]
        left, right = 0, len(nums) - 1
        # while left <= right:
            # mid = (left+right)//2
            # if nums[mi]

nums = [1,1,2,3,3,4,4,8,8]
solution = Solution()
print(solution.singleNonDuplicate(nums))