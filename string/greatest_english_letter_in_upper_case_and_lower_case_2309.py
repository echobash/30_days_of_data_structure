from collections import Counter


class Solution:
    def greatestLetter(self, s: str) -> str:
        char_freq = Counter(s)
        result = []
        for char in s:
            if char in char_freq:
                ord_value = ord(char)
                if 97 <= ord_value <= 122:
                    if chr(ord_value - 32) in char_freq:
                        result.append(ord_value - 32)
                elif 65 <= ord_value <= 90:
                    if chr(ord_value + 32) in char_freq:
                        result.append(ord_value)

        if len(result) == 0:
            return ""
        else:
            return chr(max(result))


sol = Solution()

s = "lEeTcOdE"
print(f"{s = }  {sol.greatestLetter(s) = }")

s = "arRAzFif"
print(f"{s = }  {sol.greatestLetter(s) = }")

s = "AbCdEfGhIjK"
print(f"{s = }  {sol.greatestLetter(s) = }")