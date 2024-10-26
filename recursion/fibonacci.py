def fibonacci(n):
    if(n == 1):
        return 0
    if(n == 2):
        return 1

    return fibonacci(n-1) + fibonacci(n-2)

n = 7
print("the", n, "th fibonacci number is",fibonacci(n),end="")