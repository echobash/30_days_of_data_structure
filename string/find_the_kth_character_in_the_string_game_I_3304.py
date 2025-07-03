class Solution:
    def kthCharacter(self, k: int) -> str:
        next_char = {'a':'b','b':'c','c':'d','d':'e','e':'f','f':'g','g':'h','h':'i','i':'j','j':'k','k':'l','l':'m','m':'n','n':'o','o':'p','p':'q','q':'r','r':'s','s':'t','t':'u','u':'v','v':'w','w':'x','x':'y','y':'z','z':'a'}
        count = 0
        start = 'a'
        while count <= k:
            next = ""
            for char in start:
                next += next_char[char]
            start += next
            count = len(start)
        return start[k-1]


sol = Solution()

k = 5
print(f"{k = } {sol.kthCharacter(k) = }")

k = 7
print(f"{k = } {sol.kthCharacter(k) = }")

k = 50
print(f"{k = } {sol.kthCharacter(k) = }")
