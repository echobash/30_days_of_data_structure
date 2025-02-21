class Solution:
    def countKeyChanges(self, s: str) -> int:
        change_keys_count = 0
        for i in range(len(s) - 1):
            if abs(ord(s[i]) - ord(s[i+1])) != 32 and abs(ord(s[i]) - ord(s[i+1])) != 0:
                change_keys_count += 1
        return change_keys_count


sol = Solution()

s = "aAbBcC"
print(f"{s = } {sol.countKeyChanges(s) = }")

s = "AaAaAaaA"
print(f"{s = } {sol.countKeyChanges(s) = }")