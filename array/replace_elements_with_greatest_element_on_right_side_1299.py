from typing import List
from collections import defaultdict


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        product_count_mapping = defaultdict(int)
        for i in range(n - 1):
            for j in range(i + 1, n):
                product_count_mapping[nums[i] * nums[j]] += 1

        total_no_of_pair_of_product_tuples = 0
        for product, count in product_count_mapping.items():
            if count > 1:
                total_no_of_pair_of_product_tuples += (count * (count - 1) // 2)
        # Say count = 4 => there are 4 pairs who have equal products i.e 4 tuples.
        # but we need only 2 tuples at a time only as per the questions
        # So we will have count-C-2 pair of tuples ie 4C2 pair of tuples
        # ie. count(count-1)//2

        # Two pair of tuples will have 8 permutations
        return 8 * total_no_of_pair_of_product_tuples


sol = Solution()

nums = [2, 3, 4, 6]
print(f"{nums = } | {sol.tupleSameProduct(nums) = }")

nums = [1,2,4,5,10]
print(f"{nums = } | {sol.tupleSameProduct(nums) = }")

nums = [2,3,4,6,8,12]
print(f"{nums = } | {sol.tupleSameProduct(nums) = }")

