from typing import List


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        # Bruteforce
        # run two loops i,j
        # check if hours[i]+hours[j] % 24 == 0:
        # count += 1
        n = len(hours)
        pair_count = 0
        for i in range(n-1):
            for j in range(i+1, n):
                if (hours[i]+hours[j]) % 24 == 0:
                    pair_count += 1
        return pair_count


sol = Solution()

hours = [12,12,30,24,24]
print(f"{hours = } {sol.countCompleteDayPairs(hours) = } ")

hours = [72,48,24,3]
print(f"{hours = } {sol.countCompleteDayPairs(hours) = } ")
