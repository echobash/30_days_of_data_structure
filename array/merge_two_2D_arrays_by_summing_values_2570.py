from typing import List
from collections import defaultdict


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        result = []
        id_value_mapping = defaultdict(int)

        # Traverse first array and store the ids and values
        for num in nums1:
            id_value_mapping[num[0]] = num[1]

        # Traverse second array and store the sum of values
        for num in nums2:
            id_value_mapping[num[0]] += num[1]

        for id in range(1, 1001):
            if id in id_value_mapping:
                result.append([id, id_value_mapping[id]])
        return result

sol = Solution()

nums1 = [[1,2],[2,3],[4,5]]
nums2 = [[1,4],[3,2],[4,1]]
print(f" {nums1 = } | {nums2 = } | {sol.mergeArrays(nums1, nums2) = }")

nums1 = [[2,4],[3,6],[5,5]]
nums2 = [[1,3],[4,3]]
print(f" {nums1 = } | {nums2 = } | {sol.mergeArrays(nums1, nums2) = }")
