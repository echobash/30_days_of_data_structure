class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 0 or num == 1:
            return True

        left, right = 1, num//2+1
        while left <= right:
            mid = (left+right)//2
            if mid * mid == num:
                return True
            elif mid * mid > num:
                right = mid-1
            else:
                left = mid+1
        return False


sol = Solution()

x = 4
print(f"{x=} | {sol.isPerfectSquare(x)=}")

x = 8
print(f"{x=} | {sol.isPerfectSquare(x)=}")
x = 444
print(f"{x=} | {sol.isPerfectSquare(x)=}")
x = 24
print(f"{x=} | {sol.isPerfectSquare(x)=}")
x = 25
print(f"{x=} | {sol.isPerfectSquare(x)=}")
x = 1
print(f"{x=} | {sol.isPerfectSquare(x)=}")
x = 0
print(f"{x=} | {sol.isPerfectSquare(x)=}")

x = 16
print(f"{x=} | {sol.isPerfectSquare(x)=}")

x = 14
print(f"{x=} | {sol.isPerfectSquare(x)=}")
