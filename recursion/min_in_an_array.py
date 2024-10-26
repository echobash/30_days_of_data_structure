def findmin(start,a, minm):
    if start == len(a):
        return minm

    minm = min(minm, a[start])

    return findmin(start+1, a, minm)

a = [31,12,2,19,3]
minm = a[0]
print(findmin(0, a, minm))