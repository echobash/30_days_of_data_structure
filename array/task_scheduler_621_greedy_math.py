from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq_mapping = Counter(tasks)
        max_freq = max(freq_mapping.values())

        no_of_elements_with_max_freq = 0
        for item, freq in freq_mapping.items():
            if freq == max_freq:
                no_of_elements_with_max_freq += 1
        return max(len(tasks),(max_freq-1)*(n+1)+no_of_elements_with_max_freq)


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
