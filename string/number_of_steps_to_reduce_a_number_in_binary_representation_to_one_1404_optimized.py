class Solution:
    def numSteps(self, s: str) -> int:
        # Do no convert bin to decimal since the integer range crosses for larger binary nos

        if number == 1:
            return 0

        count = 0
        while number != 1:
            if number % 2 == 1:
                number += 1
            else:
                number /= 2
            count += 1
        return count


sol = Solution()

s = "1101"
print(f" {s = } {sol.numSteps(s) = }")

s = "10"
print(f" {s = } {sol.numSteps(s) = }")

s = "1"
print(f" {s = } {sol.numSteps(s) = }")

s = "11110111100000111000001100010110"
print(f" {s = } {sol.numSteps(s) = }")

s = "1111011110000011100000110001011011110010111001010111110001"
print(f" {s = } {sol.numSteps(s) = }")
