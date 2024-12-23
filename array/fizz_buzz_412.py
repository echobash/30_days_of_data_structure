from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n+1):
            if i % 15 == 0:
                result.append("FizzBuzz")
            elif i % 5 == 0:
                result.append("Buzz")
            elif i % 3 == 0:
                result.append("Fizz")
            else:
                result.append(str(i))
        return result



sol = Solution()

n = 3
print(n , sol.fizzBuzz(n))

n = 5
print(n, sol.fizzBuzz(n))

n = 15
print(n, sol.fizzBuzz(n))