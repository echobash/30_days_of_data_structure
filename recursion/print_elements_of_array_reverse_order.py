def printarray(end,a):
    if end == -1:
        return
    print(a[end], end=" ")
    printarray(end-1,a)

a = [31,12,2,19,3]
printarray(len(a)-1,a)