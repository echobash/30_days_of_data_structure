from typing import List


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        bad_pairs_count = 0
        n = len(nums)

        for i in range(n-1):
            for j in range(i+1, n):
                if j - i != nums[j] - nums[i]:
                    bad_pairs_count += 1
        return bad_pairs_count


sol = Solution()

nums = [4,1,3,3]
print(f"{nums = } | {sol.countBadPairs(nums) = }")

nums = [1,2,3,4,5]
print(f"{nums = } | {sol.countBadPairs(nums) = }")