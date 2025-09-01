from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        count = 0
        m = len(spaces)
        for i,char in enumerate(s):
            if count <= m-1 and i == spaces[count]:
                result.append(" ")
                result.append(char)
                count += 1
            else:
                result.append(char)
        return "".join(result)


sol = Solution()

s = "LeetcodeHelpsMeLearn"
spaces = [8,13,15]
print(f"{s = } | {spaces = }|   {sol.addSpaces(s, spaces) = }")

s = "icodeinpython"
spaces = [1,5,7,9]
print(f"{s = } | {spaces = }|   {sol.addSpaces(s, spaces) = }")

s = "spacing"
spaces = [0,1,2,3,4,5,6]
print(f"{s = } | {spaces = }|   {sol.addSpaces(s, spaces) = }")
