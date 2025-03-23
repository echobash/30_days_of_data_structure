from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)

        result_set = set()

        for num in nums2:
            if num in set1:
                result_set.add(num)

        return list(result_set)



sol = Solution()

nums1 = [1,2,2,1]
nums2 = [2,2]
print(f" {nums1 = } | {nums2 = } | {sol.intersection(nums1, nums2) = }")

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(f" {nums1 = } | {nums2 = } | {sol.intersection(nums1, nums2) = }")

nums1 = [4,3,1,6]
nums2 = [4,3,1,6]
print(f" {nums1 = } | {nums2 = } | {sol.intersection(nums1, nums2) = }")

nums1 = [4,3,1,6]
nums2 = [14,13,11,62]
print(f" {nums1 = } | {nums2 = } | {sol.intersection(nums1, nums2) = }")