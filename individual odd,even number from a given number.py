n=int(input())
e=0
o=0
b=0
while n:
    r=n%10
    b=b*10+r
    n=n//10
print(b)
while b:
    r=b%10
    if(r%2==0):
        e=e*10+r
    else:
        o=o*10+r
    b=b//10
print(e,o)
a=e*e+o*o
print(a)
        
