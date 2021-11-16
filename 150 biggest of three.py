n=int(input("Enter the number: "))
m=int(input('Enter another number: '))
p=int(input('Enter third number: '))
if n>m & n>p:
    print(n,"is the biggest")
elif m>n & m>p:
    print(m,"is the biggest")
else:
    print(p,"is the biggest")
