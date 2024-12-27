from typing import List


from collections import defaultdict


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # 8,1,2,2,3
        # 1,2,2,3,8
        count_mapping = defaultdict(int)

        result = []
        n = len(nums)
        sorted_array = sorted(nums)

        last_count = 0
        first_occurence_of_duplicate = 0

        count_mapping[nums[0]] = last_count

        for i in range(1, n):
            if sorted_array[i] !=  sorted_array[i-1]:
                last_count += (i - first_occurence_of_duplicate)
                first_occurence_of_duplicate = i
            count_mapping[sorted_array[i]] = last_count

        for num in nums:
            result.append(count_mapping[num])

        return result


solution = Solution()

nums = [8,1,2,2,3]
print(solution.smallerNumbersThanCurrent(nums))

nums = [6,5,4,8]
print(solution.smallerNumbersThanCurrent(nums))

nums = [7,7,7,7]
print(solution.smallerNumbersThanCurrent(nums))
