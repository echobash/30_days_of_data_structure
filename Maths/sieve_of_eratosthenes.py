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


sol = Solution()

n = 10
print(f" {n = } {sol.sieve_of_eratosthenes(n) = }")

n = 0
print(f" {n = } {sol.sieve_of_eratosthenes(n) = }")

n = 1
print(f" {n = } {sol.sieve_of_eratosthenes(n) = }")