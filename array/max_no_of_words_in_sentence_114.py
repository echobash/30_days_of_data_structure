from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words = 1
        for sentence in sentences:
            if len(sentence.split()) > max_words:
                max_words = len(sentence.split())
        return max_words



sol = Solution()

sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
print(sentences , sol.mostWordsFound(sentences))

sentences = ["please wait", "continue to fight", "continue to win"]
print(sentences , sol.mostWordsFound(sentences))

