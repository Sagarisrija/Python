n=int(input("Enter the number: "))
m=int(input('Enter another number: '))
p=int(input('Enter third number: '))
if n>m & n>p:
    print(n,"is bigger")
elif m>n & m>p:
    print(m,"is bigger")
else:
    print(p,"is bigger")
