from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        positives = []
        negatives = []
        result = []

        for num in nums:
            if num > 0:
                positives.append(num)
            else:
                negatives.append(num)

        for i in range(n // 2):
            result.append(positives[i])
            result.append(negatives[i])

        return result


sol = Solution()

nums = [3,1,-2,-5,2,-4]
print(f" {nums = } | {sol.rearrangeArray(nums) = }")

nums = [-1,1]
print(f" {nums = } | {sol.rearrangeArray(nums) = }")