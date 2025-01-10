class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words = s.split()
        result = ""
        for i in range(k):
            result +=  words[i]
            if i != k - 1:
                result += " "
        return result


sol = Solution()

s = "Hello how are you Contestant"
k = 4
print(s,k, sol.truncateSentence(s,k))

s = "What is the solution to this problem"
k = 4
print(s,k, sol.truncateSentence(s,k))
