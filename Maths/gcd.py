
def gcd(a, b):
    if(a>b):
        (a,b) = (b,a) # we want b>a

    while(b%a > 0):
        a = b%a

        print(a,b,b%a)
    return a

gcd(12,9)
