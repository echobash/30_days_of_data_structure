from typing import List
from collections import Counter


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums1_freq = Counter(nums1)
        ans = float('inf')
        for num in nums2:
            if num in nums1_freq:
                ans = min(num, ans)
        return ans if ans != float('inf') else -1


sol = Solution()

nums1 = [1,2,3]
nums2 = [2,4]
print(f" {nums1 = } | {nums2 = } | {sol.getCommon(nums1, nums2) = }")

nums1 = [1,2,3,6]
nums2 = [2,3,4,5]
print(f" {nums1 = } | {nums2 = } | {sol.getCommon(nums1, nums2) = }")
