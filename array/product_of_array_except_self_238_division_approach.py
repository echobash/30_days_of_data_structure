from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        product_without_zero = 1
        count_zero = 0

        for num in nums:
            if num != 0:
                product_without_zero *= num
            if num == 0:
                count_zero += 1

        result = []

        # If there is more than one zero in the array, then all elements will be zero in the result
        if count_zero > 1:
            return [0] * n

        for num in nums:
            if count_zero == 1:
                # If only one zero is there and that's current element, return product_without_zero
                if num == 0:
                    result.append(product_without_zero)
                else:
                    # If only one zero is there and that's not the current element, return 0
                    result.append(0)
            else:
                # If there are no zeroes, return product_without_zero// num blindly
                result.append(product_without_zero // num)
        return result


sol = Solution()

nums = [1, 2, 3, 4]
print(f" {nums = } | {sol.productExceptSelf(nums) = }")

nums = [-1, 1, 0, -3, 3]
print(f" {nums = } | {sol.productExceptSelf(nums) = }")

nums = [-1, 1, 0, -3, 0, 3]
print(f" {nums = } | {sol.productExceptSelf(nums) = }")
