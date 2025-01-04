from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # 8,1,2,2,3
        # 1,2,2,3,8
        result = []
        n = len(nums)
        frequency_counter = [0] * 101

        # Store the frequency of each element in the frequency_counter array
        for num in nums:
            frequency_counter[num] += 1

        # Initialise an empty array commulative_less_than_counter for storing commulative sum of count of
        # no less than current no

        commulative_less_than_counter = [0] * 101

        # 0 1 2 1 0 0 0 0 1 0 0
        # 0 1 2 3 4 5 6 7 8 9 10
        # 0 0 1 3 4 4 4 4 4 5 5

        # Initialise first element i.e 0 with 0 since there will be no element smaller than 0.
        commulative_less_than_counter[0] = 0

        # Commulative count of less than current no = Commulative count till previous of current no +    frequency of previous element

        for i in range(1, 101):
            commulative_less_than_counter[i] = commulative_less_than_counter[i - 1] + frequency_counter[i - 1]
        for num in nums:
            result.append(commulative_less_than_counter[num])

        return result


solution = Solution()

nums = [8,1,2,2,3]
print(solution.smallerNumbersThanCurrent(nums))

nums = [6,5,4,8]
print(solution.smallerNumbersThanCurrent(nums))

nums = [7,7,7,7]
print(solution.smallerNumbersThanCurrent(nums))
