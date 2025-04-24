from typing import List


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        no_of_distinct_element_array = len(set(nums))
        count_of_complete_subarray = 0
        n = len(nums)

        for i in range(n):
            temp = []
            for j in range(i, n):
                temp.append(nums[j])
                if len(set(temp)) == no_of_distinct_element_array:
                    count_of_complete_subarray += 1
        return count_of_complete_subarray


sol = Solution()

nums = [1,3,1,2,2]
print(f" {nums = } | {sol.countCompleteSubarrays(nums) = }")

nums = [5,5,5,5]
print(f" {nums = } | {sol.countCompleteSubarrays(nums) = }")


nums = [1,1,533,5]
print(f" {nums = } | {sol.countCompleteSubarrays(nums) = }")
