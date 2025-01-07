from typing import List

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        piles= sorted(piles)

        # If there are only three piles, then the middle one will be our maximum case
        if n == 3:
            return piles[1]

        # If there are more than three piles -
        # Then the maxium will always go to Alice and we can't do anything in that
        # But if we manage to give the lowest to Bob, then we can defintely have maximum for us otherwise Bob will make our count lesser
        # So firstly we give all the minimum piles to Bob, then whatever is left, take all second last from the array because all the lasts will go to Alice

        # No of lots = n//3
        # So n//3 is what we will give to Bob or ignore and run loop after that i.e after n//3

        count = 0
        no_of_distributions = n//3
        for i in range(no_of_distributions, n, 2):
            count += piles[i]
        return count


sol = Solution()

piles = [2,4,1,2,7,8]
print(piles, sol.maxCoins(piles))

piles = [2,4,5]
print(piles, sol.maxCoins(piles))

piles = [9,8,7,6,5,1,2,3,4]
print(piles, sol.maxCoins(piles))
