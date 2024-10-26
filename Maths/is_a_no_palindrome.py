n=123454321
m = 0
original = n
while(n>0):
    m = m*10+n%10
    n = n//10

if m == original:
    print("Palindrome")
else:
    print("Not Palindrome")