# _ _ _ * _ _ _
# _ _ * * * _ _
# _ * * * * * _
# * * * * * * *

n = 4
gaps = n - 1

for row in range(1, n+1):
    for i in range(1, gaps+1):
        print(" ", end="")
    for j in range(1, 2*row):
        print("*", end="")
    print()
    gaps = gaps -1