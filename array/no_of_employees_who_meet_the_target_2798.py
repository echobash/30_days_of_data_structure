from typing import List


class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        target_met_employees_count = 0
        for hour in hours:
            if hour >= target:
                target_met_employees_count += 1
        return target_met_employees_count


sol = Solution()

hours = [0,1,2,3,4]
target = 2
print(f"{hours = } | {target = } | {sol.numberOfEmployeesWhoMetTarget(hours, target) = } |")

hours = [5,1,4,2,2]
target = 6
print(f"{hours = } | {target = } | {sol.numberOfEmployeesWhoMetTarget(hours, target) = } |")
