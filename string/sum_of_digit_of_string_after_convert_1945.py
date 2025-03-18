class Solution:
    def getLucky(self, s: str, k: int) -> int:
        aphabets_mapping = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '10', 'k': '11', 'l': '12', 'm': '13', 'n': '14', 'o': '15', 'p': '16', 'q': '17', 'r': '18', 's': '19', 't': '20', 'u': '21', 'v': '22', 'w': '23', 'x': '24', 'y': '25', 'z': '26'}

        total_sum = 0
        result = []
        for char in s:
            result.append(aphabets_mapping[char])
        final_no = "".join(result)

        for _ in range(k):
            total_sum = 0
            for char in final_no:
                total_sum += int(char)
            final_no = str(total_sum)

        return total_sum


sol = Solution()

s = "iiii"
k = 1
print(f"{s = }  {k = }  {sol.getLucky(s, k) = }")
