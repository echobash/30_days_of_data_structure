class Solution:
    def pivotInteger(self, n: int) -> int:
        result = (n*(n+1)/2) ** 0.5
        if not result.is_integer():
            return -1
        return int(result)


    # 1,2,3,4,5,x,7,8 n =8
    # 1,2,3,4,5,   x,   7,8 n =8
    # sum of 1 to x-1 = [(sum of 1 to n) -x] /1/2
    # 2(x*(x-1)/2) = n*(n+1)/2 -x
    # x^2 -x = n*(n+1)/2 -x
    # x = n*(n+1)/2 ** 0.5

    # Second approach AP way
    # Sum of(1, x) = x(x + 1) / 2
    # Sum of(x, 8) = N / 2(2
    # x + (N - 1))
    #
    # # Here N = n - x + 1
    # x(x + 1) / 2 = N / 2(2
    # x + (N - 1))
    #
    # # Replace N by n-x+1
    # x(x + 1) / 2 = (n - x + 1) / 2(2
    # x + (n - x + 1 - 1))
    # x(x + 1) / 2 = (n - x + 1) / 2(2
    # x + (n - x))
    # x(x + 1) / 2 = (n - x + 1)(x + n) / 2
    # x(x + 1) = (n - x + 1)(x + n)
    # x(x + 1) = nx + n ^ 2 - x ^ 2 - nx + x + n
    # x ^ 2 + x = n ^ 2 - x ^ 2 + x + n
    # 2x ^ 2 = n ^ 2 + n
    # x = [n(n + 1) / 2] ** 0.5



sol = Solution()

n = 8
print(n,sol.pivotInteger(n))

n = 1
print(n,sol.pivotInteger(n))

n = 4
print(n,sol.pivotInteger(n))
