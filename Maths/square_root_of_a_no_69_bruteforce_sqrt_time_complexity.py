class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        # 1,2,3,4
        # 1,4,9
        for i in range(1, x // 2 + 1):
            if i * i <= x < (i + 1) * (i + 1):
                return i


sol = Solution()

x = 4
print(f"{x=} {sol.mySqrt(x)=}")

x = 8
print(f"{x=} {sol.mySqrt(x)=}")

x = 444
print(f"{x=} {sol.mySqrt(x)=}")
