class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber > 0:
            columnNumber -= 1
            remainder = columnNumber % 26
            result = chr(65 + remainder) + result
            columnNumber //= 26
        return result


sol = Solution()

columnNumber = 1
print(f"{columnNumber = } {sol.convertToTitle(columnNumber) = }")

columnNumber = 701
print(f"{columnNumber = } {sol.convertToTitle(columnNumber) = }")

columnNumber = 28
print(f"{columnNumber = } {sol.convertToTitle(columnNumber) = }")

columnNumber = 2147483647
print(f"{columnNumber = } {sol.convertToTitle(columnNumber) = }")
