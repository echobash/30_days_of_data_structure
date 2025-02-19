class Solution:
    def isBalanced(self, num: str) -> bool:
        total_sum = 0
        for i in range(len(num)):
            total_sum += ((-1) ** i) * int(num[i])
        return total_sum == 0


sol = Solution()

num = "1234"
print(f"{num = }  {sol.isBalanced(num) = }")

num = "24123"
print(f"{num = }  {sol.isBalanced(num) = }")
