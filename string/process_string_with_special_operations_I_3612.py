class Solution:
    def processStr(self, s: str) -> str:
        result = []
        for char in s:
            if char.islower():
                result.append(char)
            elif char == '*' and len(result):
                result.pop()
            elif char == '#':
                # result *= 2 -> This works too but creates new list
                result.extend(result)  # In place extending
            elif char == '%':
                """
                result = result[::-1] -> This works too but creates new list
                result.reverse() -> Reverse in place. So we can prefer this
                """
                result.reverse()

        return "".join(result)


sol = Solution()

s = "a#b%*"
print(f"{s = } {sol.processStr(s) = }")

s = "z*#"
print(f"{s = } {sol.processStr(s) = }")
