class Solution:
    def binaryGap(self, n: int) -> int:
        binary_string = bin(n)[2:]
        found1 = False
        dist = 1
        maxDist = 0
        for char in binary_string:
            # found1 = False
            # dist = 0
            # maxDist = 0
            # if 0 and found1 is False -> skip ->  i += 1
            # if 0 and found1 is True -> dist += 1
            # if 1 and found1 is False -> found1 = True -> i += 1
            # if 1 and found1 is True  -> maxDist = max(maxDist, dist) -> i += 1 -> dist = 0
            if char == '0':
                if not found1:
                    continue
                else:
                    dist += 1
            else:
                if not found1:
                    found1 = True
                else:
                    maxDist = max(maxDist, dist)
                    dist = 1
        return maxDist


sol = Solution()

n = 22
print(f" {n = } {sol.binaryGap(n) = }")

n = 8
print(f" {n = } {sol.binaryGap(n) = }")

n = 5
print(f" {n = } {sol.binaryGap(n) = }")

n = 21
print(f" {n = } {sol.binaryGap(n) = }")
