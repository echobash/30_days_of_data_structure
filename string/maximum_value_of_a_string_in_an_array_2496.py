from typing import List


class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        max_value = -1
        for s in strs:
            if s.isdigit():
                value = int(s)
            else:
                value = len(s)
            max_value = max(max_value, value)
        return max_value



sol = Solution()

strs = ["alic3","bob","3","4","00000"]
print(f"{strs = } {sol.maximumValue(strs) = }")

strs = ["1","01","001","0001"]
print(f"{strs = } {sol.maximumValue(strs) = }")