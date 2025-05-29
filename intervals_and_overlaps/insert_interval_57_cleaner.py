from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        n = len(intervals)
        if n == 0:
            return [newInterval]

        # Write both non-overlapping conditions first then handle the overlapping conditions
        for i, interval in enumerate(intervals):
            # non-overlapping condition - 1
            if interval[1] < newInterval[0]:
                result.append(interval)
            # non-overlapping condition - 2
            elif newInterval[1] < interval[0]:
                # found the correct location of newInterval
                result.append(newInterval)
                return result + intervals[i:]
            else:
                # Overlapping conditions
                newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
        # Special case - when the newInterval is after the intervals[n-1][1]
        result.append(newInterval)
        return result


sol = Solution()

intervals = [[1,3],[6,9]]
newInterval = [2,5]
print(f"{intervals = }{newInterval = }  {sol.insert(intervals, newInterval) = } ")

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
print(f"{intervals = }{newInterval = }  {sol.insert(intervals, newInterval) = } ")

intervals = [[1,5]]
newInterval = [2,7]
print(f"{intervals = }{newInterval = }  {sol.insert(intervals, newInterval) = } ")

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [13,22]
print(f"{intervals = }{newInterval = }  {sol.insert(intervals, newInterval) = } ")

intervals = [[1,5]]
newInterval = [6,8]
print(f"{intervals = }{newInterval = }  {sol.insert(intervals, newInterval) = } ")

intervals = [[1,5]]
newInterval = [0,3]
print(f"{intervals = }{newInterval = }  {sol.insert(intervals, newInterval) = } ")
