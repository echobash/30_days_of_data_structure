from collections import defaultdict


class ArraySum:
    def get_pair_with_sum_k(self, nums, k):
        count_mapping = defaultdict(int)

        # Add all no in the dictionary
        for num in nums:
            count_mapping[num] += 1

        # {1:3,
        # 2:2}

        # Traverse the input array in forward direction and count pairs by count stored in dictionary
        # Also, as soon as this current no (nums[i]) is traversed, we should not use this current no
        # to form more pairs when we traverse ahead.
        # So we will decrease this current no's count by one everytime

        total_pairs = 0
        for num in nums:
            target = k - num
            if count_mapping[target] > 0:
                total_pairs += count_mapping[target]
                count_mapping[num] -= 1

        return total_pairs




nums = [1,2,2,1,1]
k = 3
arrSum = ArraySum()
print(arrSum.get_pair_with_sum_k(nums, k))



