from typing import  List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left = 0
        right = n - 1

        while left < right:
            sum_of_no = numbers[left] + numbers[right]
            if sum_of_no == target:
                return [left + 1, right + 1]
            elif sum_of_no > target:
                right -= 1
            else:
                left += 1

        return [left + 1, right + 1]


sol = Solution()

nums = [2,7,11,15]
target = 9
print(nums, sol.twoSum(nums, target))

nums = [2,3,4]
target = 6
print(nums, sol.twoSum(nums, target))

nums = [-1,0]
target = -1
print(nums, sol.twoSum(nums, target))