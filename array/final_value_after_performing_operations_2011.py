from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        count = 0
        for operation in operations:
            if operation == "--X" or operation == "X--":
                count -= 1
            else:
                count += 1
        return count


sol = Solution()

operations = ["--X","X++","X++"]
print(operations, sol.finalValueAfterOperations(operations))

operations = ["++X","++X","X++"]
print(operations, sol.finalValueAfterOperations(operations))

operations = ["X++","++X","--X","X--"]
print(operations, sol.finalValueAfterOperations(operations))
