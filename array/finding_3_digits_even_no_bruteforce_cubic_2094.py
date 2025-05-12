from typing import List


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        n = len(digits)

        result_set = set()
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i == j or j == k or k == i or digits[i] == 0 or digits[k] % 2 == 1:
                        continue
                    number = int(str(digits[i]) + str(digits[j]) + str(digits[k]))
                    result_set.add(number)

        return sorted(list(result_set))


sol = Solution()

digits = [2,1,3,0]
print(f"{digits = }  {sol.findEvenNumbers(digits) = }")

digits = [2,2,8,8,2]
print(f"{digits = }  {sol.findEvenNumbers(digits) = }")

digits = [3,7,5]
print(f"{digits = }  {sol.findEvenNumbers(digits) = }")
