class Solution:
    def floorSqrt(self, n):
        left, right = 0, n // 2 + 1
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= n:
                ans = mid
                left= mid + 1
            else:
                right = mid - 1
        return ans


sol = Solution()

x = 4
print(f"{x=} | {sol.floorSqrt(x)=}")

x = 8
print(f"{x=} | {sol.floorSqrt(x)=}")
x = 444
print(f"{x=} | {sol.floorSqrt(x)=}")
x = 24
print(f"{x=} | {sol.floorSqrt(x)=}")
x = 25
print(f"{x=} | {sol.floorSqrt(x)=}")
x = 1
print(f"{x=} | {sol.floorSqrt(x)=}")
x = 0
print(f"{x=} | {sol.floorSqrt(x)=}")