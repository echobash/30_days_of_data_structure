from typing import List


class Solution:
    def find_first_occurence(self, nums, target):
        n = len(nums)
        left, right = 0, n - 1
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans

    def find_last_occurence(self, nums, target):
        n = len(nums)
        left, right = 0, n - 1
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans

    def findLHS(self, nums: List[int]) -> int:
        n = len(nums)
        min_max_set = set()
        """
        Sort the nums
        Traverse linearly to find the tuple/pair with diff = 1, they will be together
        add in a set as (min1,max1),(min2,max2)
        traverse the set and find the first occurence of min1 and last occurence of max1 and so on and keep updating max count
        """
        nums = sorted(nums)

        for i in range(n - 1):
            if nums[i] - nums[i + 1] == -1:
                min_max_set.add((nums[i], nums[i + 1]))

        max_count = 0
        for minimum, maximum in min_max_set:
            first_occ = self.find_first_occurence(nums, minimum)
            last_occ = self.find_last_occurence(nums, maximum)
            count = last_occ - first_occ + 1
            # print(minimum, maximum,first_occ,last_occ,count)
            max_count = max(max_count, count)
            # print(count, max_count)
        # 1,2,2,2,3,3,5,7
        return max_count


sol = Solution()

nums = [1,3,2,2,5,2,3,7]
print(f" {nums = } | {sol.findLHS(nums) = }")

nums = [1,2,3,4]
print(f" {nums = } | {sol.findLHS(nums) = }")

nums = [1,1,1,1]
print(f" {nums = } | {sol.findLHS(nums) = }")