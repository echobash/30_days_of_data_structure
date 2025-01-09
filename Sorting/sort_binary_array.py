class BinarySorter:
    def do_binary_sort(self, nums):
        n = len(nums)
        # 3, 1, 2, 3
        left = 0
        right = n - 1
        while left < right:
            if nums[left] == 0:
                left += 1
            if nums[right] == 1:
                right -= 1
            if nums[left] == 1 and nums[right] == 0:
                (nums[left], nums[right]) = (nums[right], nums[left])
                left += 1
                right -= 1
        return nums

nums = [0, 1, 1, 0, 1, 0, 0, 1, 1, 0]
binary_sorter = BinarySorter()
print("Sorted array- ",binary_sorter.do_binary_sort(nums))