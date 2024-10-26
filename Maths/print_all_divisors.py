N = 203
divisors = set()

for i in range(1, int(N**(1/2)+1)):
    if(N % i == 0):
        divisors.add(i)
        divisors.add(N//i)
print(divisors)