from typing import List

from collections import defaultdict

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        visited = defaultdict(list)  # defaultdict(list) -> if word does not exist, create empty list []

        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            visited[tuple(count)].append(word)
        return list(visited.values())


sol = Solution()

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(f"{strs = }  {sol.groupAnagrams(strs) = }")

strs = [""]
print(f"{strs = }  {sol.groupAnagrams(strs) = }")

strs = ["a"]
print(f"{strs = }  {sol.groupAnagrams(strs) = }")
