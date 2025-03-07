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

        is_last_number_prime = self.is_prime(n)

        for j in range(1, n + 1):
            if self.is_prime(j):
                prime_count += 1
        """
        if say given n = 3, then we know that 2, 3 are both primes but we don't want to include 3 as the question says we want primes strictly less than n so return prime_count - 1
        But say given n = 4, we will definitely include 2,3 so just return prime_count
        return prime_count if is_last_number_prime == False else prime_count - 1
        """
        return prime_count if is_last_number_prime == False else prime_count - 1


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
