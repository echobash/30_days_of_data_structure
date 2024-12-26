from typing import List


class Sorting:
    def selection_sort(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if nums[j] < nums[min_index]:
                    min_index = j
            (nums[i], nums[min_index]) = (nums[min_index], nums[i])
        return nums


sorting = Sorting()

nums = [3,1,2,3]
print(sorting.selection_sort(nums))

nums = [3, 1, 2, 3, 4, 4, 2, 2, 4, 5, 6, 6, 7, 8, 6, 4, -2, 3]
print(sorting.selection_sort(nums))

nums = [10,9,8,7,6,5,4,3,2,1]
print(sorting.selection_sort(nums))
