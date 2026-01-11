from typing import List


class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        min_no = min(nums)
        max_no = max(nums)
        missing_elements = []

        all_num = set(nums)
        for number in range(min_no, max_no + 1):
            if number not in all_num:
                missing_elements.append(number)

        return missing_elements


sol = Solution()

nums = [1,4,2,5]
print(f"{nums = }  {sol.findMissingElements(nums) = }")

nums = [7,8,6,9]
print(f"{nums = }  {sol.findMissingElements(nums) = }")

nums = [5,1]
print(f"{nums = }  {sol.findMissingElements(nums) = }")
