class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        # (x+yi) * (a+bi) = x*a - b*y + (x*b + a*y)i
        first_num_parts = num1.split('+')
        x = int(first_num_parts[0])
        y = int(first_num_parts[1][:len(first_num_parts[1])-1])

        second_num_parts = num2.split('+')
        a = int(second_num_parts[0])
        b = int(second_num_parts[1][:len(second_num_parts[1])-1])

        return str(x*a - b*y) + "+" + str(x*b + a*y) + "i"


sol = Solution()

num1 = "1+1i"
num2 = "1+1i"
print(f"{num1 = } {num2 = } {sol.complexNumberMultiply(num1, num2) = }")

num1 = "1+-1i"
num2 = "1+-1i"
print(f"{num1 = } {num2 = } {sol.complexNumberMultiply(num1, num2) = }")