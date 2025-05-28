from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        n = len(intervals)

        if n == 0:
            return [newInterval]

        # Case 1 - Interval to be inserted at the first node
        if newInterval[0] <= intervals[0][0]:
            result.append(newInterval)
        else:
            result.append(intervals[0])
        # Case 2 - Interval to be inserted in the middle
        for i in range(n):
            last_end_time = result[-1][1]
            if newInterval[0] <= intervals[i][0]:
                # insert here
                if last_end_time < newInterval[0]:
                    result.append(newInterval)
                else:
                    result[-1][1] = max(last_end_time, newInterval[1])

            # Normal code for merging
            last_end_time = result[-1][1]
            if last_end_time < intervals[i][0]:
                result.append(intervals[i])
            else:
                result[-1][1] = max(last_end_time, intervals[i][1])

        # Case 3 - Interval to be inserted at the last node
        if newInterval[0] > intervals[n - 1][0]:
            last_end_time = result[-1][1]
            if last_end_time < newInterval[0]:
                result.append(newInterval)
            else:
                result[-1][1] = max(last_end_time, newInterval[1])

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
