from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        decimal_binary_mapping = set()
        n = len(nums)
        for num in nums:
            decimal_binary_mapping.add(int(num ,2))
        for i in range(n + 1):
            if i not in decimal_binary_mapping:
                missing_binary_number = bin(i)[2:]
                return "0" * (n - len(missing_binary_number)) + missing_binary_number
    # Time complexity - n^2


sol = Solution()

nums = ["01","10"]
print(f"{nums = }  {sol.findDifferentBinaryString(nums) = }")

nums = ["00","01"]
print(f"{nums = }  {sol.findDifferentBinaryString(nums) = }")

nums = ["111","011","001"]
print(f"{nums = }  {sol.findDifferentBinaryString(nums) = }")
