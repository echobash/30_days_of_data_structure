from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        difference_a_and_b = []
        difference_b_and_a = []

        num1_set = set(nums1)
        num2_set = set(nums2)

        for num in num1_set:
            if num not in num2_set:
                difference_a_and_b.append(num)

        for num in num2_set:
            if num not in num1_set:
                difference_b_and_a.append(num)

        return [difference_a_and_b, difference_b_and_a]

sol = Solution()

nums1 = [1,2,3]
nums2 = [2,4,6]
print(f" {nums1 = } | {nums2 = } | {sol.findDifference(nums1, nums2) = }")

nums1 = [1,2,3,3]
nums2 = [1,1,2,2]
print(f" {nums1 = } | {nums2 = } | {sol.findDifference(nums1, nums2) = }")
