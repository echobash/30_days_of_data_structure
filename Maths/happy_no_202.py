class Solution:
    def isHappy(self, n: int) -> bool:
        """
        If we keep on doing a^2 + b^2 + c^2 .., then two possibilities -
        - If it ends at 1 (Always) (End at 2,3,4,5,6,7,8,9 not possible since they will again give next no)
        - Or it runs into a cycle and never stops
        - So keep the track of all intermediate sums into a visited set.
        - If any any no comes again, it means cycle is there, return false
        """
        visited_set = {n}

        sum = 0
        while n not in visited_set or n != 1:
            sum += (n % 10) ** 2
            n //= 10

            if n == 0:
                n = sum
                sum = 0
                if n in visited_set:
                    return False
                visited_set.add(n)

        return True


sol = Solution()

num = 19
print(f"{num = } | {sol.isHappy(num) = }")

num = 2
print(f"{num = } | {sol.isHappy(num) = }")

num = 7
print(f"{num = } | {sol.isHappy(num) = }")

num = 888
print(f"{num = } | {sol.isHappy(num) = }")