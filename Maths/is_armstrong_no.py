def isArmstrongNo(n):
    if(n>=0 and n <= 9):
        return True

    digits = find_no_of_digits(n)

    sum = do_calculation(n, digits)

    if(sum == n):
        return True
    else:
        return False


def find_no_of_digits(n):
    digits = 0
    while(n>0):
        digits = digits + 1
        n = n // 10
    return digits

def do_calculation(n, digits):
    sum = 0
    while(n>0):
        sum = sum + (n%10)**digits
        n = n // 10
    return sum

print(isArmstrongNo(1634))
