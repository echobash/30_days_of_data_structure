from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        # Bruteforce -  O(n*log n × log n)
        result = []
        for i in range(1,n + 1):
            result.append(str(i))
        result = sorted(result)
        for i in range(len(result)):
            result[i] = int(result[i])
        return result


sol = Solution()

n = 13
print(f"{n = } {sol.lexicalOrder(n) = }")

n = 2
print(f"{n = } {sol.lexicalOrder(n) = }")
