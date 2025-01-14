from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        no_of_queries = len(l)
        result = [True] * no_of_queries
        for i in range(no_of_queries):
            temp_array = nums[l[i]:r[i] + 1]
            n = len(temp_array)
            max_no = max(temp_array)
            min_no = min(temp_array)
            temp_hash = set(temp_array)

            common_difference = (max_no - min_no) / (n - 1)
            if not common_difference.is_integer():
                result[i] = False
                continue
            for j in range(n):
                if min_no + j * common_difference not in temp_hash:
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