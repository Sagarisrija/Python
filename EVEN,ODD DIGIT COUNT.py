n=int(input())
e=0
s=0
o=0
while n:
    r=n%10
    if(r%2==0):
        e+=1
    else:
        o+=1
    n//=10
print("Even=",e)
print("Odd=",o)
