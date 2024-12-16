from collections import defaultdict


class Solution:
    def find_the_difference(self, s: str, t: str) -> str:
        # if s is empty and t has only character. It means t is what was added
        if len(t) == 1:
            return t

        s = sorted(s)
        t = sorted(t)

        ls = len(s)
        lt = len(t)

        # Compare character by character both the strings.
        # Since s has one char less than t. We'll run loop on s and compare with characters of t
        # If all the characters didn't match with t. This implies that t's last character is the new one

        for i in range(ls):
            if t[i] != s[i]:
                return t[i]

        return t[lt - 1]


s = "abcd"
t = "abcde"
sol = Solution()

print(sol.find_the_difference(s, t))

s = 'abab'
t = "ababb"
print(sol.find_the_difference(s, t))

s = ""
t = "x"
print(sol.find_the_difference(s, t))