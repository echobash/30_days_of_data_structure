class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        all_words = s.split()
        print(all_words)
        return " ".join(all_words[::-1])


sol = Solution()

s = "the sky is blue"
print(f"{s = } {sol.reverseWords(s) = }")

s = "  hello world  "
print(f"{s = } {sol.reverseWords(s) = }")

s = "a good   example"
print(f"{s = } {sol.reverseWords(s) = }")
