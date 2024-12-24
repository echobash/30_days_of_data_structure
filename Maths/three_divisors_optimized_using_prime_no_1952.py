class Solution:
    def isThree(self, n: int) -> bool:
        # check if perfect square
        # check if sqrt is prime

        if n in [1, 2]:
            return False

        # check if perfect square
        sqrt = int(n ** 0.5)
        if sqrt ** 2 != n:
            return False

        # Check if square_root is a prime no
        for i in range(2, int(sqrt ** 0.5) + 1):
            if sqrt % i == 0:
                return False

        return True


n = 2
sol = Solution()

print(n,sol.isThree(n))

n = 4
print(n,sol.isThree(n))

n = 36
print(n,sol.isThree(n))

n = 121
print(n,sol.isThree(n))