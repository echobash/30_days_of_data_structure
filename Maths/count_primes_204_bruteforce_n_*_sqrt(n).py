class Solution:
    def is_prime(self, number):
        if number <= 1:
            return False

        if number <= 3:
            return True

        if number % 2 == 0:
            return False

        if number % 3 == 0:
            return False

        for i in range(5, int(number ** 0.5) + 1, 2):
            if number % i == 0:
                return False

        return True

    def countPrimes(self, n: int) -> int:
        prime_count = 0

        # We have to check prime less than n i.e without including n
        for j in range(1, n):
            if self.is_prime(j):
                prime_count += 1
        return prime_count


sol = Solution()

n = 10
print(f" {n = } {sol.countPrimes(n) = }")

n = 0
print(f" {n = } {sol.countPrimes(n) = }")

n = 1
print(f" {n = } {sol.countPrimes(n) = }")

n = 2
print(f" {n = } {sol.countPrimes(n) = }")

n = 3
print(f" {n = } {sol.countPrimes(n) = }")

n = 999983
print(f" {n = } {sol.countPrimes(n) = }")

# Time complexity n * sqrt(n)
