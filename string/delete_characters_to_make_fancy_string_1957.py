class Solution:
    def makeFancyString(self, s: str) -> str:
        consecutive_count = 1
        n = len(s)
        i = 0
        result = []
        while i < n - 1:
            if s[i] == s[i + 1]:
                consecutive_count += 1
            else:
                consecutive_count = 1

            if consecutive_count > 2:
                i += 1
                continue

            result.append(s[i])
            i += 1
        result.append(s[-1])
        return "".join(result)


sol = Solution()

s = "leeetcode"
print(f"{s = } {sol.makeFancyString(s) = }")

s = "aaabaaaa"
print(f"{s = } {sol.makeFancyString(s) = }")

s = "aab"
print(f"{s = } {sol.makeFancyString(s) = }")

s = "aaaaaa"
print(f"{s = } {sol.makeFancyString(s) = }")

s = "ab"
print(f"{s = } {sol.makeFancyString(s) = }")
