class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        freq_list_s1 = [0] * 26
        freq_list_s2 = [0] * 26

        for char in s1:
            freq_list_s1[ord(char) - 97] += 1

        for char in s2:
            freq_list_s2[ord(char) - 97] += 1

        result = 0

        # print(freq_list_s1,freq_list_s2)

        for i in range(26):
            result += (abs(freq_list_s1[i] - freq_list_s2[i])) * (97 + i)

        return result


sol = Solution()

s1 = "sea"
s2 = "eat"
print(f"{s1 = } {s1 = } {sol.minimumDeleteSum(s1, s2) = }")

s1 = "delete"
s2 = "leet"
print(f"{s1 = } {s1 = } {sol.minimumDeleteSum(s1, s2) = }")
