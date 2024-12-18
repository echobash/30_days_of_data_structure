class Solution:
    def shuffle(self, nums: [int], n: int) -> [int]:
        arr = []

        for i in range(n):
            arr.append(nums[i])
            arr.append(nums[i + n])

        return arr


sol = Solution()

nums = [2,5,1,3,4,7]
n = 3
print(nums, sol.shuffle(nums, n))

nums = [1,2,3,4,4,3,2,1]
n = 4
print(nums, sol.shuffle(nums, n))

nums = [1,1,2,2]
n = 2
print(nums, sol.shuffle(nums, n))