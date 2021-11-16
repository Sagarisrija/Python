n=int(input())
e=0
s=0
o=0
while n:
    r=n%10
    if(r%2==0):
        e+=r
    else:
        o+=r
    n//=10
print("Even sum=",e)
print("Odd sum=",o)
