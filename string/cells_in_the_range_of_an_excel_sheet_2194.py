from typing import List


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        col1 = s[0]
        row1 = int(s[1])
        col2 = s[3]
        row2 = int(s[4])
        result = []
        for i in range(ord(col1), ord(col2)+1):
            for j in range(row1,row2+1):
                result.append(chr(i)+str(j))
        return result



sol = Solution()

s = "K1:L2"
print(f"{s = } {sol.cellsInRange(s) = }")

s = "A1:F1"
print(f"{s = } {sol.cellsInRange(s) = }")

s = "K2:P4"
print(f"{s = } {sol.cellsInRange(s) = }")

s = "K2:K8"
print(f"{s = } {sol.cellsInRange(s) = }")

s = "K2:P2"
print(f"{s = } {sol.cellsInRange(s) = }")
