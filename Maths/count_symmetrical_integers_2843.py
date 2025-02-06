class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        angle = abs(30 * hour - 5.5 * minutes)
        return min(angle, 360-angle)


sol = Solution()

hour = 12
minutes = 30
print(f"{hour = } | {minutes = } | {sol.angleClock(hour,minutes) = }")

hour = 3
minutes = 30
print(f"{hour = } | {minutes = } | {sol.angleClock(hour,minutes) = }")

hour = 3
minutes = 15
print(f"{hour = } | {minutes = } | {sol.angleClock(hour,minutes) = }")

hour = 6
minutes = 0
print(f"{hour = } | {minutes = } | {sol.angleClock(hour,minutes) = }")

hour = 12
minutes = 0
print(f"{hour = } | {minutes = } | {sol.angleClock(hour,minutes) = }")

