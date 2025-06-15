class Solution:
    def maxDiff(self, num: int) -> int:
        num = str(num)

        # For max, replace first non-9 digit and all its occurrences by 9
        first_non_9 = '1'
        for digit in num:
            if digit != '9':
                first_non_9 = digit
                break
        largest_no = num.replace(first_non_9, "9")

        first_non_1_and_non_zero = '1'
        for digit in num:
            if digit != '1' and digit != '0':
                first_non_1_and_non_zero = digit
                break
        """
        For min, If first non-1 digit is first digit only then replace first digit and all its
        occurences by 1 else replace by 0
        """

        if first_non_1_and_non_zero == num[0]:
            replace_with = "1"
        else:
            replace_with = "0"
        smallest_no = num.replace(first_non_1_and_non_zero, replace_with)

        return int(largest_no) - int(smallest_no)


sol = Solution()

n = 555
print(f"{n = } {sol.maxDiff(n) = }")

n = 9
print(f"{n = } {sol.maxDiff(n) = }")

n = 1001
print(f"{n = } {sol.maxDiff(n) = }")

n = 5
print(f"{n = } {sol.maxDiff(n) = }")

n = 123456
print(f"{n = } {sol.maxDiff(n) = }")

n = 1101057
print(f"{n = } {sol.maxDiff(n) = }")
