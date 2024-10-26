# *
# * *
# * * *
# * * * *
# * * * * *

rows = 5
columns = 5
for row in range(rows):
    for col in range(columns):
        if(row >= col):
            print('*', end='')
    print()

# *
# * *
# * * *
# * * * *
# * * * * *

for row in range(1,6):
    for col in range(1, row+1):
        print('*', end='')
    print()