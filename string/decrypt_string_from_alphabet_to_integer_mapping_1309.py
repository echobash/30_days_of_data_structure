class Solution:
    def freqAlphabets(self, s: str) -> str:
        no_to_letter_map = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i',
                            '10': 'j', '11': 'k', '12': 'l', '13': 'm', '14': 'n', '15': 'o', '16': 'p', '17': 'q',
                            '18': 'r', '19': 's', '20': 't', '21': 'u', '22': 'v', '23': 'w', '24': 'x', '25': 'y',
                            '26': 'z'}

        n = len(s)
        i = n - 1
        result = []
        while i >= 0:
            if s[i] != '#':
                result.append(no_to_letter_map[s[i]])
                i -= 1
            else:
                result.append(no_to_letter_map[s[i - 2:i]])
                i -= 3

        return "".join(result[::-1])


sol = Solution()

s = "10#11#12"
print(f"{s = }  {sol.freqAlphabets(s) = }")

s = "1326#"
print(f"{s = }  {sol.freqAlphabets(s) = }")

s = "121311#10#"
print(f"{s = }  {sol.freqAlphabets(s) = }")
