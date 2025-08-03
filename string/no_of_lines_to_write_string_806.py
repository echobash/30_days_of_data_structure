from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        i = 0
        n = len(s)
        no_of_lines = 1
        alphabet_dict = {chr(i + 97): i for i in range(26)}
        width = 0
        while i < n:
            if width + widths[alphabet_dict[s[i]]] > 100:
                no_of_lines += 1
                width = widths[alphabet_dict[s[i]]]
            else:
                width += widths[alphabet_dict[s[i]]]
            i += 1
        return [no_of_lines, width]


sol = Solution()

widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
s = "abcdefghijklmnopqrstuvwxyz"
print(f"{widths = } {s = } {sol.numberOfLines(widths,s) = }")

widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
s = "bbbcccdddaaa"
print(f"{widths = } {s = } {sol.numberOfLines(widths,s) = }")
