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



sol = Solution()

n = 8
print(n,sol.pivotInteger(n))

n = 1
print(n,sol.pivotInteger(n))

n = 4
print(n,sol.pivotInteger(n))
