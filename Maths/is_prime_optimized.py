def isPrime(N):
    if(N<=1):
        return "Not Prime"

    if(N<=3):
        return "Prime"

    if(N%2 == 0):
        return "Not Prime"

    if(N%3 == 0):
        return "Not Prime"

    for i in range(5, int(N**0.5)+1, 2):
        if(N%i ==0):
            return "Not Prime"

    return "Prime"

print(isPrime(14537))
print(isPrime(9))
