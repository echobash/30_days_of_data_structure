from typing import List


class Sorting:
    def selection_sort(self, nums: List[int]) -> List[int]:
        # Find minimum of the array in first pass 0 to n
        # Once the whole array is parsed, keep this minimum on starting of the array a[0]
        # Similarly for next iteration, find the minimum from 1 to n
        # Once the whole array is parsed, keep this minimum on starting of the array a[1]
        # Similarly for next iteration, find the minimum from 2 to n
        # Once the whole array is parsed, keep this minimum on starting of the array a[2]
        n = len(nums)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if nums[j] < nums[min_index]:
                    min_index = j
            (nums[i], nums[min_index]) = (nums[min_index], nums[i])
        return nums


sorting = Sorting()

nums = [12, 7, 19, 7, 23, 12, 45, 19, 34, 12, 9, 23, 56, 45, 67, 34, 78, 23, 67, 89, 12, 7, 9, 23, 56, 45, 12, 19, 34, 78, 67, 89, 9, 23, 45, 34, 78, 67, 12]
print(sorting.selection_sort(nums))

nums = [3, 1, 2, 3, 4, 4, 2, 2, 4, 5, 6, 6, 7, 8, 6, 4, -2, 3]
print(sorting.selection_sort(nums))

nums = [10,9,8,7,6,5,4,3,2,1]
print(sorting.selection_sort(nums))
