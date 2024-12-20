from collections import defaultdict


class ArrayDiff:
    def get_pair_with_abs_diff_k(self, nums, k):
        count_mapping = defaultdict(int)

        # Add all no in the dictionary
        for num in nums:
            count_mapping[num] += 1

        # Dictionary
        # {3:1, 2:1, 1:1, 5:1, 4:1}

        # Solution Pair
        # 3,1 diff = 2
        # 3,5 diff = -2
        # 2,4 diff = -2

        # 3-x = +-2 => x = 3+-2 = 1 or 5

        # Traverse the input array in forward direction and count pairs by count stored in dictionary
        # Also, as soon as this current no (nums[i]) is traversed, we should not use this current no
        # to form more pairs when we traverse ahead.
        # So we will decrease this current no's count by one everytime

        total_pairs = 0
        for num in nums:
            target = num - k
            target2 = num + k

            if count_mapping[target] > 0:
                total_pairs += count_mapping[target]

            if count_mapping[target2] > 0:
                total_pairs += count_mapping[target2]

            if count_mapping[target] > 0 or count_mapping[target2] > 0:
                count_mapping[num] -= 1

        return total_pairs


nums = [3,2,1,5,4]
k = 2
arrSum = ArrayDiff()
print(arrSum.get_pair_with_abs_diff_k(nums, k))


# 3,1
# 3,5
# 2,4



