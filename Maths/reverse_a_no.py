n=14500000
n=1234567890
m = 0
while(n>0):
    m = m*10+n%10
    n = n//10
print(m)