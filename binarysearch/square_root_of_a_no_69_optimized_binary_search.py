class Solution:
    def mySqrt(self, x: int) -> int:
        # nums=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        # target = 24
        # l,r,mid = 0,13,6
        # l,r,mid = 0,5,2
        # l,r,mid = 3,5,4
        # l,r,mid = 5,5,5
        # l,r,mid = 5,4,4

        left, right = 0, x // 2 + 1
        while left <= right:
            mid = (left + right) // 2

            if mid * mid == x:
                return mid
            elif mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1
        return right


sol = Solution()

x = 4
print(f"{x=} | {sol.mySqrt(x)=}")

x = 8
print(f"{x=} | {sol.mySqrt(x)=}")
x = 444
print(f"{x=} | {sol.mySqrt(x)=}")
x = 24
print(f"{x=} | {sol.mySqrt(x)=}")
x = 25
print(f"{x=} | {sol.mySqrt(x)=}")
x = 1
print(f"{x=} | {sol.mySqrt(x)=}")
x = 0
print(f"{x=} | {sol.mySqrt(x)=}")