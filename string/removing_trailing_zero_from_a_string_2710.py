class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        n = len(num) #8
        trailing_zero_count = 0
        for i in range(n-1, -1, -1):
            if num[i] == '0':
                trailing_zero_count += 1
            else:
                break
        return num[:n - trailing_zero_count]


sol = Solution()

num = "51230100"
print(f"{num = } {sol.removeTrailingZeros(num) = }")

num = "123"
print(f"{num = } {sol.removeTrailingZeros(num) = }")

num = "123000010000000"
print(f"{num = } {sol.removeTrailingZeros(num) = }")