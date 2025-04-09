class Solution:
    def isFascinating(self, n: int) -> bool:
        result = str(n)
        first = str(2 * n)
        second = str(3 * n)
        result += first + second
        return "".join(sorted(list(result))) == "123456789"


sol = Solution()

n = 192
print(f"{n }  {sol.isFascinating(n) = }")

n = 100
print(f"{n }  {sol.isFascinating(n) = }")