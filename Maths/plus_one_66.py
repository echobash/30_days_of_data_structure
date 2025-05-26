from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        adding 1 to a number is easier when we have to add to lsb (right) since in case of carry or 9, we can add
        one more element in right
        """
        digits = digits[::-1]
        n = len(digits)
        # [4,3,2,1] -> [1,2,3,4] + 1 -> [2,2,3,4] -> [4,3,2,2]
        # [9,9] -> [9,9] + 1 -> [0,0,1] -> [1,0,0]
        carry = 1
        for i in range(n):
            sum = digits[i] + carry
            digits[i] = sum % 10
            carry = sum // 10
            if i == n - 1 and carry == 1:
                digits.append(carry)
        return digits[::-1]


sol = Solution()

digits = [1,2,3]
print(f"{digits = } | {sol.plusOne(digits) = }")

digits = [4,3,2,1]
print(f"{digits = } | {sol.plusOne(digits) = }")

digits = [9]
print(f"{digits = } | {sol.plusOne(digits) = }")

digits = [9,9,9]
print(f"{digits = } | {sol.plusOne(digits) = }")


