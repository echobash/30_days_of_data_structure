from typing import List


class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        return nums2[0]-nums1[0]


sol = Solution()

nums1 = [2,6,4]
nums2 = [9,7,5]
print(f" {nums1 = } |  {nums2 = } | {sol.addedInteger(nums1, nums2) = }")

nums1 = [10]
nums2 = [5]
print(f" {nums1 = } |  {nums2 = } | {sol.addedInteger(nums1, nums2) = }")

nums1 = [1,1,1,1]
nums2 = [1,1,1,1]
print(f" {nums1 = } |  {nums2 = } | {sol.addedInteger(nums1, nums2) = }")