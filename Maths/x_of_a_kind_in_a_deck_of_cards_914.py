from typing import List
from collections import Counter
from math import gcd

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        counts = Counter(deck).values()
        g = 0
        for c in counts:
            g = gcd(g, c)   # gcd(0, c) == c for the first item
            if g == 1:      # early exit: once GCD is 1, it can’t recover
                return False
        return g >= 2


sol = Solution()

deck = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,4,4,5,5,5,5,6,6,7,7,8,8]
print(f"{deck = } | {sol.hasGroupsSizeX(deck) = }")

deck = [1,1,1,1,2,2,2,2,2,2]
print(f"{deck = } | {sol.hasGroupsSizeX(deck) = }")

deck = [1,2,3,4,4,3,2,1]
print(f"{deck = } | {sol.hasGroupsSizeX(deck) = }")

deck = [1,1,1,2,2,2,3,3]
print(f"{deck = } | {sol.hasGroupsSizeX(deck) = }")

deck = [1,1]
print(f"{deck = } | {sol.hasGroupsSizeX(deck) = }")

deck = [0,0,0,0,0,1,1,2,3,4]
print(f"{deck = } | {sol.hasGroupsSizeX(deck) = }")




