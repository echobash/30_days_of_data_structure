class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        result = []
        original_no = num
        if num < 0:
            num *= -1
        while num > 0:
            result.append(str(num % 7))
            num //= 7
        return ("-" if original_no < 0 else "") + "".join(result)[::-1]


sol = Solution()

num = 100
print(f"{num = } | {sol.convertToBase7(num) = }")

num = 0
print(f"{num = } | {sol.convertToBase7(num) = }")

num = -100
print(f"{num = } | {sol.convertToBase7(num) = }")

num = 7
print(f"{num = } | {sol.convertToBase7(num) = }")

num = -7
print(f"{num = } | {sol.convertToBase7(num) = }")
