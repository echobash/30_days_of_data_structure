from typing import List


class Solution:
    def getEncyptedElement(self, num):
        original_no = num
        largest_digit = 0
        no_of_digits = 0
        while num > 0:
            largest_digit = max(largest_digit, num % 10)
            num //= 10
            no_of_digits += 1

        encrypted_no = 0
        for i in range(no_of_digits):
            encrypted_no = encrypted_no * 10 + largest_digit
        return encrypted_no

    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        total_sum = 0
        for num in nums:
            total_sum += self.getEncyptedElement(num)
        return total_sum


sol = Solution()

nums = [1,2,3]
print(f"{nums = } {sol.sumOfEncryptedInt(nums) = }")

nums = [10,21,31]
print(f"{nums = } {sol.sumOfEncryptedInt(nums) = }")


nums = [10,782,31]
print(f"{nums = } {sol.sumOfEncryptedInt(nums) = }")