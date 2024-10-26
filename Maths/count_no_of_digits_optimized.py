def count_no_of_digits(n):
    import math
    if n==0:
        return  1
    return math.floor(math.log10(n))+1


n = 12345
print(count_no_of_digits(n))