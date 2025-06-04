from collections import defaultdict


class Solution:
    def countDistinct(self, arr, k):
        n = len(arr)
        if k > n:
            return -1
        result = []
        freq_mapping = defaultdict(int)
        for i in range(k):
            freq_mapping[arr[i]] += 1
        result.append(len(freq_mapping))

        for i in range(k, n):
            freq_mapping[arr[i - k]] -= 1
            if freq_mapping[arr[i - k]] == 0:
                del freq_mapping[arr[i - k]]

            freq_mapping[arr[i]] += 1
            result.append(len(freq_mapping))
        return result


sol = Solution()

arr = [1, 2, 1, 3, 4, 2, 3]
k = 4
print(f" {arr = } | {k = } | {sol.countDistinct(arr, k) = }")

arr = [4, 1, 1]
k = 2
print(f" {arr = } | {k = } | {sol.countDistinct(arr, k) = }")

arr = [1, 1, 1, 1, 1]
k = 3
print(f" {arr = } | {k = } | {sol.countDistinct(arr, k) = }")
