from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        for num in nums:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        return even + odd


solution = Solution()

nums = [3,1,2,4]
print(nums, solution.sortArrayByParity(nums))

nums = [1,2]
print(nums, solution.sortArrayByParity(nums))

nums = [2,2,3,1]
print(nums, solution.sortArrayByParity(nums))

nums = [0]
print(nums, solution.sortArrayByParity(nums))
