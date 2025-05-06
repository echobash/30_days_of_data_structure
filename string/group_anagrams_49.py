from typing import List


class Solution:
    def checkAnagram(self, word1, word2):
        return sorted(word1) == sorted(word2)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        n = len(strs)
        visited = dict()

        # {
        #     "aet" : ["ate","eat","tea"]
        #     "ant" : ["tan","nat"]
        #     "abt" : ["bat"]
        # }

        for i in range(n):
            sorted_word = "".join(sorted(strs[i]))
            if sorted_word not in visited:
                visited[sorted_word] = [strs[i]]
            else:
                visited[sorted_word].append(strs[i])

        for val in visited.values():
            result.append(val)

        return result

sol = Solution()

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(f"{strs = }  {sol.groupAnagrams(strs) = }")

strs = [""]
print(f"{strs = }  {sol.groupAnagrams(strs) = }")

strs = ["a"]
print(f"{strs = }  {sol.groupAnagrams(strs) = }")
