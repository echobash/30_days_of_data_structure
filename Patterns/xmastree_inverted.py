# * * * * * * *
# _ * * * * * _
# _ _ * * * _ _
# _ _ _ * _ _ _

n = 4
gap = 0

for row in range(1, n+1):
    for i in range(0, gap):
        print("_", end="")
    for j in range(1, 2*n-2*row+2):
        print("*", end="")
    print()
    gap = gap + 1