from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        num_frequency_arr = [0] * 501

        for num in nums:
            num_frequency_arr[num] += 1

        """
        Traverse the array and check if there is atleast one such case where the count is odd
        """
        for frequency in num_frequency_arr:
            if frequency % 2 == 1:
                return False
        return True


sol = Solution()

nums = [3,2,3,2,2,2]
print(nums, sol.divideArray(nums))

nums = [1,2,3,4]
print(nums, sol.divideArray(nums))
