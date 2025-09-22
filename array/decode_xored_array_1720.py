from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        result = [first]
        for num in encoded:
            result.append(num ^ first)
            first = num ^ first
        return result


sol = Solution()

encoded = [1,2,3]
first = 1
print(f" {encoded = } | {first = } | {sol.decode(encoded, first) = }")


encoded = [6,2,7,3]
first = 4
print(f" {encoded = } | {first = } | {sol.decode(encoded, first) = }")

encoded = [6,2,7,3]
first = 2
print(f" {encoded = } | {first = } | {sol.decode(encoded, first) = }")