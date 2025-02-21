from typing import List


class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        """
        i,j   #origin
        i,j+1 #RIGHT
        i,j-1 #LEFT
        i-1,j #UP
        i+1,j #DOWN
        """
        i = j = 0
        for command in commands:
            if command == "RIGHT":
                j = j + 1
            elif command == "LEFT":
                j = j - 1
            elif command == "UP":
                i = i - 1
            else:
                i = i + 1
        return i * n + j



sol = Solution()

n = 2
commands = ["RIGHT","DOWN"]
print(f"{n = } {commands = } {sol.finalPositionOfSnake(n, commands) = }")

n = 3
commands = ["DOWN","RIGHT","UP"]
print(f"{n = } {commands = } {sol.finalPositionOfSnake(n, commands) = }")
