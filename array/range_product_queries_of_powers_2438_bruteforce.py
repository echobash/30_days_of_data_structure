from typing import List


class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        x = bin(n)
        binary_string = x[2:]
        binary_string = binary_string[::-1]
        powers = []

        l = len(binary_string)
        for i in range(l):
            if binary_string[i] == "1":
                powers.append(2 ** i)

        result = []
        for query in queries:
            product = 1
            for i in range(query[0], query[1] + 1):
                product *= powers[i]
            result.append(product % (10 ** 9 + 7))
        return result


sol = Solution()

n = 15
queries = [[0,1],[2,2],[0,3]]
print(f" {n = } | {queries = } | {sol.productQueries(n,queries) = }")

n = 2
queries = [[0,0]]
print(f" {n = } | {queries = } | {sol.productQueries(n,queries) = }")

n = 19
queries = [[0,1],[2,2]]
print(f" {n = } | {queries = } | {sol.productQueries(n,queries) = }")
