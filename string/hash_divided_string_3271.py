class Solution:
    def stringHash(self, s: str, k: int) -> str:
        n = len(s)
        result = []
        for i in range(0,n,k):
            hash_sum = 0
            for j in range(i,i+k):
                hash_sum += ord(s[j])-97
            result.append(chr((hash_sum % 26) + 97))
        return "".join(result)


sol = Solution()

s = "abcd"
k = 2
print(f"{s = } {k = }  {sol.stringHash(s,k) = }")

s = "mxz"
k = 3
print(f"{s = } {k = }  {sol.stringHash(s,k) = }")
