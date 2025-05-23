from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        # Find prefix prod
        # Find suffix prod
        # result[i] = prefix_prod[i-1] * suffix_prod[i+1]
        """
        prefix_prod[i-1] * suffix_prod[i+1]
        this will do prod of all items in right of current element and all element in left of current
        element. 
        This way, the total prod of both of these will include the prod of total array except the current
        element
        """

        # nums   = [1,      2,       3,    4,    5,   6]
        # pref   = [1,      2,       6,    24,   120, 720]
        # suff   = [720,    720,     360,  120,  30,  6]
        # result = [720,     360,     240,  180,  144, 120

        # Generate Prefix Array
        pref = []
        prod = 1
        for num in nums:
            prod *= num
            pref.append(prod)

        # Generate Suffix Array
        suff = []
        prod = 1
        for i in range(n - 1, -1, -1):
            prod *= nums[i]
            suff.append(prod)

        # Reverse the suffix array to get in reverse cumulative order
        suff = suff[::-1]

        # Handle extreme left and extreme right edge cases
        result[0] = suff[1]
        result[n - 1] = pref[n - 2]

        for i in range(1, n - 1):
            result[i] = pref[i - 1] * suff[i + 1]
        return result


sol = Solution()

nums = [1, 2, 3, 4]
print(f" {nums = } | {sol.productExceptSelf(nums) = }")

nums = [-1, 1, 0, -3, 3]
print(f" {nums = } | {sol.productExceptSelf(nums) = }")

nums = [-1, 1, 0, -3, 0, 3]
print(f" {nums = } | {sol.productExceptSelf(nums) = }")
