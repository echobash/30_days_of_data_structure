from typing import List


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        n = len(nums)
        result_set = set()
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[j] - nums[i] == nums[k] - nums[j] == diff:
                        result_set.add(tuple(sorted([nums[i], nums[j],nums[k]])))
        return len(result_set)


sol = Solution()

nums = [0,1,4,6,7,10]
diff = 3
print(f" {nums = } | {diff = } | {sol.arithmeticTriplets(nums,diff) = }")

nums = [4,5,6,7,8,9]
diff = 2
print(f" {nums = } | {diff = } | {sol.arithmeticTriplets(nums,diff) = }")

nums = [4,5,6,7,8,9]
diff = 99
print(f" {nums = } | {diff = } | {sol.arithmeticTriplets(nums,diff) = }")
