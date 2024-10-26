# * * * * *
# * * * *
# * * *
# * *
# *

# for rows in range(5,0,-1):
#     for cols in range(1, rows+1):
#         print('*',end=' ')
#     print()

for rows in range(1,6):
    for cols in range(1,6-rows+1):
        print('*', end=" ")
    print()

for rows in range(1,6):
    for cols in range(1,6-rows+1):
        print(cols, end=" ")
    print()