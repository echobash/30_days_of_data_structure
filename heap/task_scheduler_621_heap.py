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
        global_count = 0
        # print(freqs)

        # We'll push a popped element only after n+1 i.e n wait time and 1 while it was popped
        while len(temp) > 0 or len(freqs) > 0:
            if len(freqs) != 0:
                most_frequent = -heapq.heappop(freqs)
                count += 1
                if most_frequent > 1:
                    temp.append(-(most_frequent - 1))
                    # don't push zero
            if count == n + 1:
                # Push temp on max-heap
                for num in temp:
                    heapq.heappush(freqs, num)
                # Empty the temp
                temp = []
                global_count += count
                count = 0

            if len(freqs) == 0:
                if len(temp) != 0 and 0 < count < n + 1:
                    count = n + 1

            if len(freqs) == 0 and len(temp) == 0:
                global_count += count
        return global_count


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
