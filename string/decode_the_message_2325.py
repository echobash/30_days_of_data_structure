class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        n = len(key)
        i = 0
        current_char = 0
        cipher_text_mapping = dict()

        while i <= n - 1:
            if key[i] != ' ' and key[i] not in cipher_text_mapping:
                cipher_text_mapping[key[i]] = chr(current_char + 97)
                current_char += 1
            i += 1

        result = []
        for character in message:
            if character == " ":
                result.append(" ")
            else:
                result.append(cipher_text_mapping[character])

        return "".join(result)


sol = Solution()

key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"
print(f"{key = } | {message = }|   {sol.decodeMessage(key, message) = }")

key = "eljuxhpwnyrdgtqkviszcfmabo"
message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"
print(f"{key = } | {message = }|   {sol.decodeMessage(key, message) = }")
