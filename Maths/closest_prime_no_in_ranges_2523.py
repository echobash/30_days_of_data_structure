from typing import List


class Solution:
    def sieve(self, n):
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
        return is_prime

    def closestPrimes(self, left: int, right: int) -> List[int]:
        is_prime = self.sieve(right)
        prev = -1
        result = [-1, -1]
        min_diff = float('inf')

        for i in range(left, right + 1):
            if is_prime[i]:
                if prev != -1 and (i - prev) < min_diff:
                    min_diff = i - prev
                    result = [prev, i]
                prev = i

        return result



sol = Solution()

left = 10
right = 19
print(f" {left = } {right = } {sol.closestPrimes(left, right) = }")

left = 4
right = 6
print(f" {left = } {right = } {sol.closestPrimes(left, right) = }")