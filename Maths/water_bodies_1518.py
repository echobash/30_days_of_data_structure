class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        no_of_unused_bottles = numBottles
        no_of_bottles_count = numBottles
        while no_of_unused_bottles >= numExchange:
            extra_bottles_used = no_of_unused_bottles // numExchange
            no_of_bottles_count += extra_bottles_used
            no_of_unused_bottles = (no_of_unused_bottles % numExchange) + extra_bottles_used
            print(extra_bottles_used,no_of_bottles_count)
        return no_of_bottles_count


sol = Solution()

numBottles = 9
numExchange = 3
print(f"{numBottles = } | {numExchange = } | {sol.numWaterBottles(numBottles,numExchange) = }")

numBottles = 15
numExchange = 4
print(f"{numBottles = } | {numExchange = } | {sol.numWaterBottles(numBottles,numExchange) = }")
