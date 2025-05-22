from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Bruteforce n ^ 2
        # Slightly Better n*logn

        # We'll use hare and tortoise approach here when elements can be used as indices and duplicacy is there
        # Start with slow moving one step and Fast movie two steps so advance while s != f does not break initially
        slow = fast = nums[0]
        slow, fast = nums[slow], nums[nums[fast]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        # Here slow = fast, it means there is the circle for sure. But necessarily at slow or fast

        # Reset slow to head/first element
        slow = nums[0]

        # Move both pointers by 1 step at a time now
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow


sol = Solution()

nums = [1,3,4,2,2]
print(f"{nums = } {sol.findDuplicate(nums) = } ")

nums = [3,1,3,4,2]
print(f"{nums = } {sol.findDuplicate(nums) = } ")

nums = [3,3,3,3,3]
print(f"{nums = } {sol.findDuplicate(nums) = } ")
