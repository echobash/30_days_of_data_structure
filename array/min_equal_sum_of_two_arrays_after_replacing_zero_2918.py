from typing import List


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        no_of_zeroes1 = nums1.count(0)
        no_of_zeroes2 = nums2.count(0)

        agg_nums1_sum = sum(nums1) + no_of_zeroes1
        agg_nums2_sum = sum(nums2) + no_of_zeroes2

        if agg_nums2_sum == agg_nums1_sum:
            return agg_nums1_sum
        elif agg_nums2_sum > agg_nums1_sum:
            if no_of_zeroes1 > 0:
                return agg_nums2_sum
            return -1
        else:
            if no_of_zeroes2 > 0:
                return agg_nums1_sum
            return -1


sol = Solution()

nums1 = [3,2,0,1,0]
nums2 = [6,5,0]
print(f" {nums1 = } | {nums2 = } | {sol.minSum(nums1,nums2) = }")

nums1 = [2,0,2,0]
nums2 = [1,4]
print(f" {nums1 = } | {nums2 = } | {sol.minSum(nums1,nums2) = }")
