from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # 8,1,2,2,3
        # 1,2,2,3,8
        result = []
        n = len(nums)
        for i in range(n):
            smaller_no_count = 0
            for j in range(n):
                if i !=j and nums[i] > nums[j]:
                    smaller_no_count += 1
            result.append(smaller_no_count)
        return result


solution = Solution()

nums = [8,1,2,2,3]
print(solution.smallerNumbersThanCurrent(nums))

nums = [6,5,4,8]
print(solution.smallerNumbersThanCurrent(nums))

nums = [7,7,7,7]
print(solution.smallerNumbersThanCurrent(nums))
