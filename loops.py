# Print from 1 to 10
for i in range(1,11):
    print(i,end=" ")

print("\n")

# Print from 0 to 10
for i in range(11):
    print(i, end=" ")

print("\n")

# Print 0,2,4,6,8,10,12,14,16,18,20
for i in range(0,21,2):
    print(i, end=" ")

print("\n")

# Print 1,3,5,7,9,11,13,15,17,19
for i in range(1,20,2):
    print(i, end=" ")

print("\n")

# Print 10,9,8,7,6,5,4,3,2,1
for i in range(10,0,-1):
    print(i, end=" ")

print("\n")

# Print 10,9,8,7,6,5,4,3,2,1,0
for i in range(10,-1,-1):
    print(i, end=" ")

print("\n")

# Print 11,9,7,5,3,1
for i in range(11,0,-2):
    print(i, end=" ")

print("\n")

# Print the list - [2,5,1,7,8,12]
prices =  [2,5,1,7,8,12]
for i in prices:
    print(i, end=" ")

print("\n")

# Print the reverse of the list - [2,5,1,7,8,12]
prices =  [2,5,1,7,8,12]
for i in range(len(prices), 0, -1):
    print(prices[i-1], end=" ")