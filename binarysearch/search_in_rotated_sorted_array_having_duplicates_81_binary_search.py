from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return True
            elif nums[left] == nums[mid] == nums[right]:
                """
                # the case when left, mid and right all three have equal value, we don't know
                that which side to go.
                So we'll try to trim down and lessen our sample space.
                The reason we're able to do this is that, since these three are already not equal to target,
                we can already eliminate them and move the pointers towards mid.
                """
                left += 1
                right -= 1
                continue
            elif nums[left] <= nums[mid]:
                # Left part is sorted
                if nums[left] <= target <= nums[mid]:
                    # Look in left
                    right = mid - 1
                else:
                    # Look in right
                    left = mid + 1
            elif nums[mid] <= nums[right]:
                # Right part is sorted
                if nums[mid] <= target <= nums[right]:
                    # Look in right
                    left = mid + 1
                else:
                    # Look in left
                    right = mid - 1
        return False


sol = Solution()

nums = [2,5,6,0,0,1,2]
target = 0
print(f"{nums = } {sol.search(nums, target) = }")

nums = [2,5,6,0,0,1,2]
target = 3
print(f"{nums = } {sol.search(nums, target) = }")

nums = [15,18,20,25,30,35,40,45,5,10,12,14]
target = 13
print(f"{nums = } {sol.search(nums, target) = }")

nums = [1,0,1,1,1]
target = 0
print(f"{nums = } {sol.search(nums, target) = }")
