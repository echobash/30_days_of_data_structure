# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

rows = 5
columns = 5
for row in range(rows):
    for col in range(columns):
        if(row >= col):
            print(col+1, end='')
    print()