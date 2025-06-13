# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    # Simulating hardcode for one input
    picked_no = 6
    if num == picked_no:
        return 0
    elif num > picked_no:
        return -1
    return 1


class Solution:
    def guessNumber(self, n: int) -> int:
        # 1,1,1,1,1,1,0,-1,-1,-1,-1,-1
        left, right = 1, n
        while left <= right:
            mid = (left + right ) //2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                right = mid - 1
            else:
                left = mid + 1


sol = Solution()

n = 10
print(f"{n = } {sol.guessNumber(n) = }")
