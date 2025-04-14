from typing import List


class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        max_value = 0
        for str in strs:
            if str.isnumeric():
                max_value = max(max_value,int(str))
            else:
                max_value = max(max_value,len(str))
        return max_value



sol = Solution()

strs = ["alic3","bob","3","4","00000"]
print(f"{strs = } {sol.maximumValue(strs) = }")

strs = ["1","01","001","0001"]
print(f"{strs = } {sol.maximumValue(strs) = }")