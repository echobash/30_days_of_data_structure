from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        critical_points_count = 0
        """
        We can check every pair of elements for critical point by
        if nums[i] > nums[i+1]:
        But this won't work on last element of array
        But we have to check that too since it the array was one less rotated, the first element would have been the last element and we had to compare that to
        so if we do nums[i+1] where i = n, it will give index out of range, that's why in the description of the question, we have A[i] == A[(i+1) % A.length] so that even on i=n, it can give its next element too i.e the first one.
        So we will use A[i] == A[(i+1) % A.length] instead of nums[i] > nums[i+1]
        """

        for i in range(n):
            if nums[i] > nums[(i+1) % n]:
                print(f"{i =} {critical_points_count = }")
                critical_points_count += 1
        return critical_points_count < 2

        # The array can have duplicates too.
        # So critical_points_count can be equal to 0 for 3,3,3,3
        # That's why we need critical_points_count < 2 i.e
        # critical_points_count == 1 (for all cases but below edge case)
        # critical_points_count == 0 (for edge case where all elements are equal and no critical points are there)

sol = Solution()

nums = [3,4,5,1,2]
print(f"{nums = } | {sol.check(nums) = }")

nums = [2,1,3,4]
print(f"{nums = } | {sol.check(nums) = }")

nums = [1,2,3]
print(f"{nums = } | {sol.check(nums) = }")

nums = [4,3,2,1]
print(f"{nums = } | {sol.check(nums) = }")

nums = [5,2]
print(f"{nums = } | {sol.check(nums) = }")

nums = [2,5]
print(f"{nums = } | {sol.check(nums) = }")
