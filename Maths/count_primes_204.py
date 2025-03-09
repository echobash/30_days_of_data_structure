class Solution:
    def countPrimes(self, n: int) -> int:
        """
        1. Make an array of size n with values as True for each
        2. Run a loop from 2 to sqrt(n)
        3. Check the current no value
        4. If it is False, it means, it's not prime, so continue and skip this iteration
        5. If it is True, update all its multiple as False except for the current no. Current no will be prime so no need to update it.
        6. Once 2 to sqrt(n) loop is ended, count the no of True values from 2 to n
        """
        if n <= 2:
            return 0

        all_elements = [True] * n
        for i in range(2, int(n ** 0.5) + 1):
            if all_elements[i] == True:
                for j in range(i * i, n, i):
                    all_elements[j] = False

        prime_no_count = 0
        for k in range(2, n):
            if all_elements[k] == True:
                prime_no_count += 1

        return prime_no_count


sol = Solution()

n = 10
print(f" {n = } {sol.countPrimes(n) = }")

n = 0
print(f" {n = } {sol.countPrimes(n) = }")

n = 1
print(f" {n = } {sol.countPrimes(n) = }")