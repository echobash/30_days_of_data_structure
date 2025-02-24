from collections import Counter
from typing import List


class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer1 = answer2 = 0
        nums1_map = Counter(nums1)
        nums2_map = Counter(nums2)

        for num1, occurence1 in nums1_map.items():
            if num1 in nums2_map:
                answer1 += occurence1

        for num2, occurence2 in nums2_map.items():
            if num2 in nums1_map:
                answer2 += occurence2
        return [answer1, answer2]


solution = Solution()

nums1 = [2,3,2]
nums2 = [1,2]
print(f"{nums1 = } {nums2 = } {solution.findIntersectionValues(nums1, nums2) = }")

nums1 = [4,3,2,3,1]
nums2 = [2,2,5,2,3,6]
print(f"{nums1 = } {nums2 = } {solution.findIntersectionValues(nums1, nums2) = }")

nums1 = [3,4,2,3]
nums2 = [1,5]
print(f"{nums1 = } {nums2 = } {solution.findIntersectionValues(nums1, nums2) = }")