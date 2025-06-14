class Solution:
    def minMaxDifference(self, num: int) -> int:
        if num < 10:
            return 9

        num = str(num)

        # For max, replace first non-9 digit and all its occurrences by 9
        first_non_9 = '0'
        for digit in num:
            if digit != '9':
                first_non_9 = digit
                break
        largest_no = num.replace(first_non_9, "9")

        # For min, replace first digit and all its occurrences by 0
        smallest_no = num.replace(num[0], "0")

        return int(largest_no) - int(smallest_no)


sol = Solution()

n = 11891
print(f"{n = } {sol.minMaxDifference(n) = }")

n = 90
print(f"{n = } {sol.minMaxDifference(n) = }")

n = 5
print(f"{n = } {sol.minMaxDifference(n) = }")