class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        num1 = str(num1)
        num2 = str(num2)
        num3 = str(num3)

        n1 = len(num1)
        n2 = len(num2)
        n3 = len(num3)

        num1 = '0' * (4 - n1) + num1
        num2 = '0' * (4 - n2) + num2
        num3 = '0' * (4 - n3) + num3

        result = ['0'] * 4

        for i in range(4):
            result[i] = min(num1[i], num2[i], num3[i])

        return int("".join(result))


sol = Solution()

num1 = 1
num2 = 10
num3 = 1000
print(f"{num1 = } {num2 = } {num3 = } {sol.generateKey(num1, num2, num3) = }")

num1 = 987
num2 = 879
num3 = 798
print(f"{num1 = } {num2 = } {num3 = } {sol.generateKey(num1, num2, num3) = }")

num1 = 1
num2 = 2
num3 = 3
print(f"{num1 = } {num2 = } {num3 = } {sol.generateKey(num1, num2, num3) = }")
