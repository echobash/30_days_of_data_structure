class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        max_no = -1
        set_of_no = set()
        for i in range(1,101):
            set_of_no.add(str(i))

        tokens = s.split()
        for token in tokens:
            if token in set_of_no:
                if int(token) <= max_no:
                    return False
                else:
                    max_no = int(token)
        return True


sol = Solution()

s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"
print(f"{s = }  {sol.areNumbersAscending(s) = }")

s = "hello world 5 x 5"
print(f"{s = }  {sol.areNumbersAscending(s) = }")

s = "sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"
print(f"{s = }  {sol.areNumbersAscending(s) = }")
