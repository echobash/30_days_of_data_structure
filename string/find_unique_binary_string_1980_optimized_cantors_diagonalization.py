from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        result = []
        """
        Here if if make one bit difference from each of the given numbers, new no will be different from
        all the given nos.
        e.g for nums = ["111","011","001"]
        our ans will be something like $$$
        For 1st binary no, 1st digit is 1. So if we change that 1 to 0, the new no will definitely
        be different from first.

        ~ly For 2nd binary no, 2nd digit is 1. So if we change that 1 to 0, the new no will definitely
        be different from second.

        ~ly For 3rd binary no, 3rd digit is 1. So if we change that 1 to 0, the new no will definitely
        be different from third.

        Now we already no that the new 3-digit no is not same with any given no, so it can be our answer.
        That's why we are trying to toggle every a[i][i] digit of the given binary nos.
        """
        for i in range(len(nums)):
            result.append(str(1 - int(nums[i][i])))
        return "".join(result)
    # Time complexity - O(n)
    # Also known as Cantor's Diagonalization


sol = Solution()

nums = ["01","10"]
print(f"{nums = }  {sol.findDifferentBinaryString(nums) = }")

nums = ["00","01"]
print(f"{nums = }  {sol.findDifferentBinaryString(nums) = }")

nums = ["111","011","001"]
print(f"{nums = }  {sol.findDifferentBinaryString(nums) = }")
