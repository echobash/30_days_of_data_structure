class Solution:
    def judgeCircle(self, moves: str) -> bool:
        cords = [0, 0]
        for move in moves:
            if move ==   "U":
                cords[1] += 1
            elif move == "D":
                cords[1] -= 1
            elif move == "L":
                cords[0] -= 1
            elif move == "R":
                cords[0] += 1
        return cords == [0,0]


sol = Solution()

moves = "UD"
print(f"{moves = }  {sol.judgeCircle(moves) = }")

moves = "LL"
print(f"{moves = }  {sol.judgeCircle(moves) = }")