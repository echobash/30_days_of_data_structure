from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        result = []
        no_bigger_than_pivot = []
        count_pivot = 0
        for num in nums:
            if num > pivot:
                no_bigger_than_pivot.append(num)
            elif num == pivot:
                count_pivot += 1
            else:
                result.append(num)

        result.extend([pivot]*count_pivot)
        result.extend(no_bigger_than_pivot)
        return result


sol = Solution()

nums = [9,12,5,10,14,3,10]
pivot = 10
print(f" {nums = } | {pivot = } | {sol.pivotArray(nums, pivot) = }")

nums = [-3,4,3,2]
pivot = 2
print(f" {nums = } | {pivot = } | {sol.pivotArray(nums, pivot) = }")
