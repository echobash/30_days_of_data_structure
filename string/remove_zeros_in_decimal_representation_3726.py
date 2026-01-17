class Solution:
    def removeZeros(self, n: int) -> int:
        num = str(n)
        result = []
        for char in num:
            if char != '0':
                result.append(char)
        return int("".join(result))


sol = Solution()

n = 1020030
print(f"{n = } {sol.removeZeros(n) = }")

n = 1
print(f"{n = } {sol.removeZeros(n) = }")

n = 19
print(f"{n = } {sol.removeZeros(n) = }")
