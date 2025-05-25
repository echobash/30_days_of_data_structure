from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        unique_elements_set = sorted(set(arr))
        val_index_mappnig = dict()

        result = []

        for i, value in enumerate(unique_elements_set):
            val_index_mappnig[value] = i+1

        for num in arr:
            result.append(val_index_mappnig[num])
        return result


sol = Solution()

arr = [40,10,20,30]
print(f" {arr = } | {sol.arrayRankTransform(arr) = }")

arr = [100,100,100]
print(f" {arr = } | {sol.arrayRankTransform(arr) = }")

arr = [37,12,28,9,100,56,80,5,12]
print(f" {arr = } | {sol.arrayRankTransform(arr) = }")

arr = [36,12,28,9,12,12,12,5,12]
print(f" {arr = } | {sol.arrayRankTransform(arr) = }")
