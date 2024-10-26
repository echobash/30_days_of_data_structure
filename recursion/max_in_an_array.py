def findmax(start,a, maxim):
    if start == len(a):
        return maxim

    maxim = max(maxim, a[start])

    return findmax(start+1, a, maxim)

a = [-31,12,2,19,3]
maxim = a[0]
print(findmax(0, a, maxim))