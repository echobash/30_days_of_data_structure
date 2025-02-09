from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(indices)
        result = [""] * n
        for i in range(n):
            result[indices[i]] = s[i]
        return "".join(result)

sol = Solution()

s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
print(s,indices, sol.restoreString(s, indices))
