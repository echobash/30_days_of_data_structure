from typing import List

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        visited = defaultdict(list)  # defaultdict(list) -> if word does not exist, create empty list []

        # {
        #     "aet" : ["ate","eat","tea"]
        #     "ant" : ["tan","nat"]
        #     "abt" : ["bat"]
        # }

        for i in range(n):
            sorted_word = "".join(sorted(strs[i]))
            visited[sorted_word].append(strs[i])

        return list(visited.values())


sol = Solution()

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(f"{strs = }  {sol.groupAnagrams(strs) = }")

strs = [""]
print(f"{strs = }  {sol.groupAnagrams(strs) = }")

strs = ["a"]
print(f"{strs = }  {sol.groupAnagrams(strs) = }")
