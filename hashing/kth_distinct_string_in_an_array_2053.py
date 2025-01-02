from collections import defaultdict
from typing import List

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        character_count_mapping = defaultdict(int)

        for character in arr:
            character_count_mapping[character] += 1

        for character in arr:
            if character_count_mapping[character] == 1:
                k -= 1
                if k == 0:
                    return character
        return ""


solution = Solution()

arr = ["d","b","c","b","c","a"]
k = 2
print(arr, k, solution.kthDistinct(arr, k))

arr = ["a","b","a"]
k = 3
print(arr, k, solution.kthDistinct(arr, k))

arr = ["aaa","aa","a"]
k = 1
print(arr, k, solution.kthDistinct(arr, k))