from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        result = []

        n = len(intervals)
        if n <= 1:
            return 0
        intervals = sorted(intervals)
        result.append(intervals[0])
        count = 0

        for i in range(1, n):
            last_element_end_time = result[-1][1]
            if last_element_end_time > intervals[i][0]:
                # Overlapping encountered
                # Either remove result[-1][1] or remove intervals[i]
                # Remove the one which has bigger end_time. In this case
                if last_element_end_time > intervals[i][1]:
                        # result[-1][1] to be removed
                        result[-1] = intervals[i]
                        count += 1
                else:
                    # intervals[i] to be removed but it was never pushed so no need to update result but we will definitely increment count and do count += 1
                    count += 1
            else:
                result.append(intervals[i])
        return count


sol = Solution()

intervals = [[1,2],[2,3],[3,4],[1,3]]
print(f"{intervals = } {sol.eraseOverlapIntervals(intervals) = } ")

intervals = [[1,2],[1,2],[1,2]]
print(f"{intervals = } {sol.eraseOverlapIntervals(intervals) = } ")

intervals = [[1,2],[2,3]]
print(f"{intervals = } {sol.eraseOverlapIntervals(intervals) = } ")

intervals = [[1, 5], [2, 6], [3, 7], [8, 10]]
print(f"{intervals = } {sol.eraseOverlapIntervals(intervals) = } ")

intervals = [[1, 5], [2, 6], [3, 7], [8, 10]]
print(f"{intervals = } {sol.eraseOverlapIntervals(intervals) = } ")

intervals = [[0,2],[1,3],[2,4],[3,5],[4,6]]
print(f"{intervals = } {sol.eraseOverlapIntervals(intervals) = } ")

intervals = [[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]
print(f"{intervals = } {sol.eraseOverlapIntervals(intervals) = } ")
