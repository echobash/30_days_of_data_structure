from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Find total sum of natural no if everything was correct
        total_actual_sum = n * (n + 1) // 2

        # Find sum of given after it's messed up
        total_array_sum = 0
        for num in nums:
            total_array_sum += num

        # Find sum of all unique no
        unique_no = set(nums)

        unique_array_sum = 0
        for num in unique_no:
            unique_array_sum += num

        # twice_no = total_array_sum - unique_array_sum
        # missing_no = total_actual_sum - unique_array_sum

        twice_no = total_array_sum - unique_array_sum
        missing_no = total_actual_sum - unique_array_sum

        return [twice_no, missing_no]


sol = Solution()

nums = [1,2,2,4]
print(nums, sol.findErrorNums(nums))

nums = [1,1]
print(nums, sol.findErrorNums(nums))

nums = [2,2]
print(nums, sol.findErrorNums(nums))
