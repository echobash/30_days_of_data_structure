class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        """
        Convert into base-3 and this way, we can understand how many times did a particular 3^x occured.
        e.g 91 base 10 = (10101) base 3
        i.e 91 base 10 = 1*3^4 + 0*3^3 + 1*3^2 + 0*3^1 + 1*3^0

        it means -
        3^4 occured once
        3^3 didn't occur or occured zero times
        3^2 occured once
        3^1 didn't occur or occured zero times
        3^0 occured once

        So it should be returned True

        On the other hand, if we check for the no 21
        e.g 21 base 10 = (210) base 3
        i.e 21 base 10 = 2*3^2 + 1*3^1 + 0*3^0
        i.e 21 base 10 = 3^2 + 3^2 + 1*3^1 + 0*3^0

        it means -
        3^2 occured twice
        3^1 occured once
        3^0 didn't occur or occured zero times

        Now since 3^2 occurs twice, we should return False.

        So the idea/approach here will be to -
        1. Convert the decimal into base-3
        2. We know something % 3 will be 0, 1 or 2
        3. While converting, if we get even if a single 2, return False
        4. Otherwise Return True
        """
        while n > 0:
            if n % 3 == 2:
                return False
            n //= 3
        return True


sol = Solution()

n = 12
print(n,sol.checkPowersOfThree(n))

n = 91
print(n,sol.checkPowersOfThree(n))

n = 21
print(n,sol.checkPowersOfThree(n))

