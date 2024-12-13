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

# FYI This solution can lead to integer overflow in some other languages like cpp and java
# Explanation ->

# If we reverse the complete the full integer no then it's possible that the reverse no can be
# causing integer overflow.
# e.g x = 2^31 -1 is the constraint in this question and also biggest integer of 32 bit
# 2^31 -1 = 2,147,483,647 (10 digit no) and reverse of it will be 7,463,847,412
# But we can't store 7,463,847,412 into an integer variable
# Same with any random no e.g 1,000,000,006 will again cause integer overflow.
# So instead of reversing complete no, we can reverse half of the no and compare it with other half.
# And we won't get any integer overflow as reversing a 5 digit will never cause integer overflow
