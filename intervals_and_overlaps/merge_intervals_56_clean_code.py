from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals = sorted(intervals)
        result.append(intervals[0])

        for interval in intervals:
            last_end_time = result[-1][1]
            if last_end_time < interval[0]:
                # No overlapping possible
                result.append(interval)
            else:
                """
                last_end_time >= interval[0]
                Overlapping is possible for sure (be it partial or complete)
                If it's overlapping then the last_start_time will still be same, only end time will be 
                changing in the result.

                If partially overlapping - new_end_time = interval[1]
                If fully overlapping - new_end_time = last_end_time only
                so basically new_end_time = max(last_end_time only, interval[1])
                """
                result[-1][1] = max(last_end_time, interval[1])
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
