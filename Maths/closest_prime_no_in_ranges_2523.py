from typing import List


class Solution:
    def sieve_of_eratosthenes(self, n: int):
        result = []
        if n < 2:
            return result

        all_elements = [True] * n
        for i in range(2, int(n ** 0.5) + 1):
            if all_elements[i]:
                for j in range(i * i, n, i):
                    all_elements[j] = False

        for k in range(2, n):
            if all_elements[k]:
                result.append(k)

        return result

    def closestPrimes(self, left: int, right: int) -> List[int]:
        all_primes_upto_right = self.sieve_of_eratosthenes(right + 1)
        min_diff = float('inf')
        result = [-1, -1]

        l = len(all_primes_upto_right)
        for i in range(l - 1):
            if all_primes_upto_right[i] < left:
                continue

            if all_primes_upto_right[i + 1] - all_primes_upto_right[i] < min_diff:
                min_diff = all_primes_upto_right[i + 1] - all_primes_upto_right[i]
                result[0] = all_primes_upto_right[i]
                result[1] = all_primes_upto_right[i + 1]

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