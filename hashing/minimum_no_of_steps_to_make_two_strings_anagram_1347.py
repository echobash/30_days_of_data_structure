from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums) -> bool:
        freq_dict = defaultdict(int)
        for num in nums:
            freq_dict[num] += 1

        for count in  freq_dict.values():
            if count > 1:
                return True
        return False


nums = [1,1,1,3,3,4,3,2,4,2]
solution = Solution()
print(solution.containsDuplicate(nums))