from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        result = []
        for i in range(n):
            warmer_temp_found = False
            for j in range(i+1, n):
                if temperatures[j] > temperatures[i]:
                    result.append(j - i)
                    warmer_temp_found = True
                    break
            if not warmer_temp_found:
                result.append(0)
        return result


sol = Solution()

temperatures = [73,74,75,71,69,72,76,73]
print(f" {temperatures = } | {sol.dailyTemperatures(temperatures) = }")

temperatures = [30,40,50,60]
print(f" {temperatures = } | {sol.dailyTemperatures(temperatures) = }")

temperatures = [30,60,90]
print(f" {temperatures = } | {sol.dailyTemperatures(temperatures) = }")
