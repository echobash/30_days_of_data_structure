def count_no_of_digits(n):
    c = 0
    if n==0:
        return 1

    while(n>0):
        n = n//10
        c = c + 1
    return c


n = 12345
print(count_no_of_digits(n))