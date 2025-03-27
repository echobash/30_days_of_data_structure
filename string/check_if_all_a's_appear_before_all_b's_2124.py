class Solution:
    def checkString(self, s: str) -> bool:
        flag = 0
        # keep flag as 0.
        # As soon as you get s[i] == 'b': update flag = 1
        # As soon as you get s[i] == 'a': check if flag is 0 then update flag = 0
        # As soon as you get s[i] == 'a': check if flag is 1 then it means a came after b, so return False
        # At last return True, since if flag == 0, it means there are all a's. Similarly if flag == 0, it means there are all b's

        for char in s:
            if char == 'b':
                flag = 1
            else:
                if flag == 0:
                    flag = 0
                else:
                    return False
        return True


sol = Solution()

s = "aaabbb"
print(f"{s = }  {sol.checkString(s) = }")

s = "abab"
print(f"{s = }  {sol.checkString(s) = }")

s = "bbb"
print(f"{s = }  {sol.checkString(s) = }")

s = "aaa"
print(f"{s = }  {sol.checkString(s) = }")
