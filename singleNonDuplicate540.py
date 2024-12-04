class Solution:
    def singleNonDuplicate(self, nums: [int]) -> int:
        unique = 0
        for num in nums:
            unique ^= num

        return unique


nums = [1,1,2,3,3,4,4,8,8]
solution = Solution()
print(solution.singleNonDuplicate(nums))