from typing import List


class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            for j in range(len(str(num))):
                result.append(int(str(num)[j]))
        return result


sol = Solution()

nums = [13,25,83,77]

print(f" {nums = } | {sol.separateDigits(nums) = }")