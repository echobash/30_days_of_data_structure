from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(indices)
        indices_char_mapping = dict()
        for i in range(n):
            indices_char_mapping[indices[i]] = s[i]

        result = ""
        for j in range(n):
            result += indices_char_mapping[j]
        return result


sol = Solution()

s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
print(s,indices, sol.restoreString(s, indices))
