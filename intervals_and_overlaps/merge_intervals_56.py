from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals = sorted(intervals)
        for interval in intervals:
            if len(result) == 0:
                # Add first interval as it is
                result.append(interval)
            else:
                """
                Do comparasion b/w last entry in result say s and current interval say t
                if t[0] <= s[1] -> overlap possible 
                Again Two possible overlap possible -
                1. s i.e result last completely overlaps current transaction t i.e t[1] <= s[1].
                So we don't need to push anything since s is already there.
                2. t[1] > s[1] -> s partially overlaps t so new (s[0],t[1]) will be inserted after popping
                the last element from result
                pop last result element and append new (s[0],t[1])
                otherwise -> overlap not possible -> Add current interval as it is
                """
                s, t = result[-1], interval
                if t[0] <= s[1]:
                    if t[1] <= s[1]:
                        continue
                    else:
                        result.pop()
                        result.append([s[0], t[1]])
                else:
                    result.append(t)
        return result


sol = Solution()

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(f"{intervals = } {sol.merge(intervals) = } ")

intervals = [[2,6],[1,3],[8,10],[15,18]]
print(f"{intervals = } {sol.merge(intervals) = } ")

intervals = [[1,4],[4,5]]
print(f"{intervals = } {sol.merge(intervals) = } ")

intervals = [[1,4],[2,3]]
print(f"{intervals = } {sol.merge(intervals) = } ")
