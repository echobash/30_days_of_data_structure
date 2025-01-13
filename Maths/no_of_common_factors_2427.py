class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        # we want to proceed assuming a > b so we are swapping if that's not the case
        if a < b :
            (a,b) = (b,a)

        count = 0

        for i in range(1, a+1):
            if a % i == 0 and b % i == 0:
                count += 1
        return count


a = 12
b = 6
sol = Solution()

print(a,b,sol.commonFactors(a, b))

a = 25
b = 30
print(a,b,sol.commonFactors(a, b))

a = 18
b = 64
print(a,b,sol.commonFactors(a, b))

a = 100
b = 8
print(a,b,sol.commonFactors(a, b))
