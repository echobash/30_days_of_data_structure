class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + 2*t


sol = Solution()

num = 4
t = 1
print(f"{num = } | {t = } | {sol.theMaximumAchievableX(num, t) = }")

num = 3
t = 2
print(f"{num = } | {t = } | {sol.theMaximumAchievableX(num, t) = }")