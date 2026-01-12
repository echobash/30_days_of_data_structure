class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        return n

        """
        Logic
        sumOdd = n * n
        sumEven = (n * n) + n = n * (n + 1)
        gcd of n * n and n * (n + 1) = n
        """



sol = Solution()

n = 25
print(f"{n = } | {sol.gcdOfOddEvenSums(n) = }")

n = 5
print(f"{n = } | {sol.gcdOfOddEvenSums(n) = }")

n = 10
print(f"{n = } | {sol.gcdOfOddEvenSums(n) = }")

n = 13
print(f"{n = } | {sol.gcdOfOddEvenSums(n) = }")

n = 14
print(f"{n = } | {sol.gcdOfOddEvenSums(n) = }")

n = 11
print(f"{n = } | {sol.gcdOfOddEvenSums(n) = }")

n = 15
print(f"{n = } | {sol.gcdOfOddEvenSums(n) = }")
