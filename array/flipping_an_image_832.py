from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)

        # Flip Horizontally
        for i in range(n):
            for j in range(n // 2):
                (image[i][j], image[i][n - j - 1]) = (image[i][n - j - 1], image[i][j])

        # Invert the image
        for i in range(n):
            for j in range(n):
                image[i][j] = 1 - image[i][j]

        return image


sol = Solution()

image = [[1,1,0],[1,0,1],[0,0,0]]
print(f"{image = } {sol.flipAndInvertImage(image) = } ")

image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
print(f"{image = } {sol.flipAndInvertImage(image) = } ")

image = [[1,1,1],[1,1,1],[0,0,0]]
print(f"{image = } {sol.flipAndInvertImage(image) = } ")
