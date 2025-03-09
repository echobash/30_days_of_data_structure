from typing import List


class Solution:
    def isPrime(self, N):
        if (N <= 1):
            return False

        if (N <= 3):
            return True

        if (N % 2 == 0):
            return False

        if (N % 3 == 0):
            return False

        for i in range(5, int(N ** 0.5) + 1, 2):
            if (N % i == 0):
                return False
        return True

    def closestPrimes(self, left: int, right: int) -> List[int]:
        previous_prime = -1
        min_diff = float('inf')
        result = [-1, -1]
        for i in range(left, right + 1):
            if self.isPrime(i):
                if previous_prime == -1:
                    previous_prime = i
                    continue
                else:
                    if i - previous_prime < min_diff:
                        min_diff = i - previous_prime
                        result[0] = previous_prime
                        result[1] = i
                    previous_prime = i
        return result


sol = Solution()

left = 10
right = 19
print(f" {left = } {right = } {sol.closestPrimes(left, right) = }")

left = 12
right = 24
print(f" {left = } {right = } {sol.closestPrimes(left, right) = }")

left = 19
right = 31
print(f" {left = } {right = } {sol.closestPrimes(left, right) = }")

left = 4
right = 6
print(f" {left = } {right = } {sol.closestPrimes(left, right) = }")