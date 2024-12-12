class Solution:
    def targetIndices(self, nums: [int], target: int) -> [int]:
        nums = sorted(nums)

        result = []
        for i in range(len(nums)):
            if nums[i] == target:
                result.append(i)
        return result


nums = [1,2,5,2,3]
target = 2
solution = Solution()
print(solution.targetIndices(nums, target))