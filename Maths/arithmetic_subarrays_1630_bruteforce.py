from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        no_of_queries = len(l)
        result = [True] * no_of_queries
        for i in range(no_of_queries):
            len_temp = r[i] - l[i] + 1
            temp_array = [0] * len_temp
            for j in range(l[i], r[i] + 1):
                temp_array[l[i] - j] = nums[j]

            temp_array = sorted(temp_array)

            common_difference = temp_array[0] - temp_array[1]
            for k in range(len_temp - 1):
                if temp_array[k] - temp_array[k + 1] != common_difference:
                    result[i] = False
                    break
        return result



sol = Solution()

nums = [4,6,5,9,3,7]
l = [0,0,2]
r = [2,3,5]
print(sol.checkArithmeticSubarrays(nums, l, r))

nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10]
l = [0,1,6,4,8,7]
r = [4,4,9,7,9,10]
print(sol.checkArithmeticSubarrays(nums, l, r))