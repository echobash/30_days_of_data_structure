class Solution:
    def diagonalSum(self, mat: [[int]]) -> int:
        diagonal_sum = 0
        n = len(mat[0])

        for i in range(n):
            diagonal_sum += a[i][i] + a[i][n - 1 - i]

        if n % 2 == 1:
            diagonal_sum = diagonal_sum - a[n//2][n//2]
        return diagonal_sum

a = [
    [1,  2,  3,  4, 5],
    [6,  7,  8,  9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]
sol = Solution()

print(sol.diagonalSum(a))

a = [
      [1, 2, 3, 10],
      [4, 5, 6, 11],
      [7, 8, 9, 12],
      [13,14,15, 16]
      ]
print(sol.diagonalSum(a))