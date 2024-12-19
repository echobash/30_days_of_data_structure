from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count_mapping = [0] * 501

        # Store count of the nums in the list at their index
        for num in nums:
            count_mapping[num] += 1

        # Traverse the array and check if there is atleast one such case where...
        # ... the count is odd

        for count in count_mapping:
            if count % 2 == 1:
                return False
        return True


sol = Solution()

nums = [3,2,3,2,2,2]
print(nums, sol.divideArray(nums))

nums = [1,2,3,4]
print(nums, sol.divideArray(nums))
