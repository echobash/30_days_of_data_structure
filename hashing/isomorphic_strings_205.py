class Isomorphic:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_mapping = {}
        transpose_char_mapping = {}
#s=ab t=cc
        for i in range(len(s)):
            if s[i] in char_mapping:
                if(char_mapping[s[i]] != t[i]):
                    return False
            else:
                if(t[i] not in transpose_char_mapping):
                    char_mapping[s[i]] = t[i]
                    transpose_char_mapping[t[i]] = s[i]
                else:
                    return False
        return True


s = "egg"
t = "add"

s="ab"
t="cc"
isomorphic = Isomorphic()
print(isomorphic.isIsomorphic(s,t))