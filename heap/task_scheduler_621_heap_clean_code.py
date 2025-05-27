from typing import List
import heapq
from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq_mapping = Counter(tasks)
        count = 0
        temp = []

        freqs = [-freq for freq in freq_mapping.values()]
        heapq.heapify(freqs)

        # We'll push a popped element only after n+1 i.e n wait time and 1 while it was popped
        while len(freqs) > 0:
            # Pop n+1 elements from max-heap
            for _ in range(n + 1):
                if len(freqs) > 0:
                    max_frequency = -heapq.heappop(freqs)
                    max_frequency -= 1
                    temp.append(-max_frequency)

            # Push temp to max-heap
            for freq in temp:
                if freq != 0:
                    heapq.heappush(freqs, freq)

            if len(freqs) != 0:
                count += n + 1
            else:
                count += len(temp)
            temp = []
        return count


sol = Solution()

tasks = ["A", "A", "A", "A", "A", "B", "B", "B", "C", "C"]
n = 3
print(f"{tasks = } | {n = } | {sol.leastInterval(tasks, n) = }")

tasks = ["A","A","A","B","B","B","C","D","E","F"]
n = 2
print(f"{tasks = } | {n = } | {sol.leastInterval(tasks, n) = }")

tasks = ["A", "A", "A", "B", "B", "B"]
n = 2
print(f"{tasks = } | {n = } | {sol.leastInterval(tasks, n) = }")

tasks = ["A", "B", "C", "D", "E"]
n = 3
print(f"{tasks = } | {n = } | {sol.leastInterval(tasks, n) = }")

tasks = ["A"] * 6 + ["B"] * 2 + ["C"] * 2
n = 2
print(f"{tasks = } | {n = } | {sol.leastInterval(tasks, n) = }")

tasks = ["A", "A", "A", "B", "B", "B", "C", "C", "C"]
n = 1
print(f"{tasks = } | {n = } | {sol.leastInterval(tasks, n) = }")

tasks = ["A", "A", "A"]
n = 5
print(f"{tasks = } | {n = } | {sol.leastInterval(tasks, n) = }")
