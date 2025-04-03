class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        return self.fib(n-1) + self.fib(n-2)


sol = Solution()

n = 2
print(f" {n = } {sol.fib(n) = }")

n = 3
print(f" {n = } {sol.fib(n) = }")

n = 4
print(f" {n = } {sol.fib(n) = }")

n = 1
print(f" {n = } {sol.fib(n) = }")

n = 5
print(f" {n = } {sol.fib(n) = }")
