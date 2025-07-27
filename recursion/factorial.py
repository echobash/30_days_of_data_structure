class Factorial:
    def getFactorial(self, n):
        if n == 0:
            return 1
        return n * self.getFactorial(n-1)


factorial = Factorial()

n = 10
print(f"{n = } {factorial.getFactorial(n) = }")

n = 8
print(f"{n = } {factorial.getFactorial(n) = }")

n = 6
print(f"{n = } {factorial.getFactorial(n) = }")

n = 0
print(f"{n = } {factorial.getFactorial(n) = }")
#
# f(x) = x.(x-1)! if x >=1
#     = 1 if x == 0