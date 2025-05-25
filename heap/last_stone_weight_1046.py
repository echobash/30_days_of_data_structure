import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Use max-heap to continuously get two heaviest
        # Pop/remove and adjust it too.
        # remove x -> pop x
        # update y-x -> remove y and push y-x
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            first  = - heapq.heappop(stones)
            second = - heapq.heappop(stones)
            if first != second:
                heapq.heappush(stones, -1 * abs(first - second))
        return -stones[0] if len(stones) == 1 else 0


sol = Solution()

stones = [2,7,4,1,8,1]
print(f"{stones = } {sol.lastStoneWeight(stones) = }")

stones = [1]
print(f"{stones = } {sol.lastStoneWeight(stones) = }")

stones = [2,7,4,1,8,1]
print(f"{stones = } {sol.lastStoneWeight(stones) = }")

stones = [5,5,5]
print(f"{stones = } {sol.lastStoneWeight(stones) = }")

stones = [5,1,5,5]
print(f"{stones = } {sol.lastStoneWeight(stones) = }")

stones = [7,5,8]
print(f"{stones = } {sol.lastStoneWeight(stones) = }")
