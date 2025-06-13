def isBadVersion(version: int) -> bool:
    # Simulating hard code just to run it
    if version == 4:
        return True
    return False


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        ans = -1
        while left <= right:
            mid = (left + right ) //2
            if isBadVersion(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans


sol = Solution()

n = 5
print(f"{n = } {sol.firstBadVersion(n) = }")
