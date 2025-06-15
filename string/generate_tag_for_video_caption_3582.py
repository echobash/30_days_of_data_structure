class Solution:
    def generateTag(self, caption: str) -> str:
        words = caption.split()
        n = len(words)
        result = ["#"]

        for i, word in enumerate(words):
            if i == 0:
                result.append(word.lower())
            else:
                result.append(word.title())

        final_string = "".join(result)

        return final_string if len(final_string) <= 100 else final_string[:100]


sol = Solution()

caption = "Leetcode daily streak achieved"
print(f"{caption = } {sol.generateTag(caption) = }")

caption = "can I Go There"
print(f"{caption = } {sol.generateTag(caption) = }")

caption = "   "
print(f"{caption = } {sol.generateTag(caption) = }")

caption = "hhhhhhhhhhhhhjkhkjhkjfhjkshfkjhskjhfkjhsdfhskdfhkhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"
print(f"{caption = } {sol.generateTag(caption) = }")
