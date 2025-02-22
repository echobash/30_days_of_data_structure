from collections import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:
        counter_map = Counter(word)
        no_of_pushes = 0
        index = 1

        for char, freq in counter_map.most_common():
            if index % 8 != 0:
                no_of_pushes += (freq * (index // 8 + 1))
            else:
                no_of_pushes += (freq * (index // 8))
            index += 1
        return no_of_pushes


sol = Solution()

word = "abcde"
print(f"{word = } {sol.minimumPushes(word) = }")

word = "xyzxyzxyzxyz"
print(f"{word = } {sol.minimumPushes(word) = }")

word = "aabbccddeeffgghhiiiiii"
print(f"{word = } {sol.minimumPushes(word) = }")