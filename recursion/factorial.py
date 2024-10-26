def factorial(n):
    if(n == 0):
        return 1

    return n * factorial(n-1)

n = 0
print("the factorial of",n,"is",factorial(n),end="")