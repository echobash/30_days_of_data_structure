# *
# * *
# * * *
# * * * *
# * * *
# * *
# *

n = 4


for row in range(1, 2*n):
    stars = 2 * n - row if row > n else row
    for i in range(1, stars + 1):
        print("*", end=" ")
    print()