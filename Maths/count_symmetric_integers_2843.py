class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for x in range(low, high+1):
            no_digits = len(str(x))

            if no_digits in [1,3,5]:
                continue
            elif no_digits == 2:
                if x % 11 == 0:
                    count += 1
            else:
                if int(str(x)[0]) + int(str(x)[1]) ==  int(str(x)[2]) + int(str(x)[3]):
                    count += 1
        return count


sol = Solution()

low = 1
high = 100
print(f"{low = } | {high = } | {sol.countSymmetricIntegers(low,high) = }")

low = 1200
high = 1230
print(f"{low = } | {high = } | {sol.countSymmetricIntegers(low,high) = }")
