from typing import List


# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Just check if even a single overlapping occurs, return False
        # Else return True
        intervals.sort(key=lambda i: i.start)
        n = len(intervals)
        for i in range(n-1):
            if intervals[i+1].start < intervals[i].end:
                return False
        return True






sol = Solution()

intervals = [(0,30),(5,10),(15,20)]
print(f"{intervals = } {sol.canAttendMeetings(intervals) = } ")
