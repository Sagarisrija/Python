n=int(input()) 
r=0
t=n
while n:
    x=n%10
    r=r*10+x
    n=n//10
if r==t:
    print('The given number is Palindrome')
else:
    print('The given number is not a Palindrome')
