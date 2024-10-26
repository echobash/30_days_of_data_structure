def printarray(start,a):
    if start == len(a):
        return
    print(a[start], end=" ")
    printarray(start+1,a)

a = [31,12,2,19,3]
printarray(0,a)