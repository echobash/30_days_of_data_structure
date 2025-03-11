class Solution:
    def hammingWeight(self, n: int) -> int:
        set_bit_count = 0
        while n > 0:
            if n % 2 == 1:
                set_bit_count += 1
            n = n //2
        return set_bit_count



sol = Solution()

n = 11
print(f"{n = } | {sol.hammingWeight(n) = }")

n = 128
print(f"{n = } | {sol.hammingWeight(n) = }")

n = 2147483645
print(f"{n = } | {sol.hammingWeight(n) = }")