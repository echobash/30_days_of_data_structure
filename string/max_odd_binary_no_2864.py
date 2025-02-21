class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = len(s)
        occurrence_of_one = 0

        for char in s:
            if char == '1':
                occurrence_of_one += 1

        occurrence_of_zero = n - occurrence_of_one
        return '1' * (occurrence_of_one - 1) + '0' * occurrence_of_zero + '1'

        # occurrence_of_one = 10 , occurrence_of_zero = 12, n = 22
        # 9 ones - 12 zeros - 1 one

        # (occurrence_of_one - 1) 1 - (occurrence_of_zero) 0 - 1




sol = Solution()

s = "010"
print(f"{s = }  {sol.maximumOddBinaryNumber(s) = }")

s = "0101"
print(f"{s = }  {sol.maximumOddBinaryNumber(s) = }")

s = "10110011001001101010"
print(f"{s = }  {sol.maximumOddBinaryNumber(s) = }")

