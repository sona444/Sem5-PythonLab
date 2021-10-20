import math
x=int(input("Enter operation to be performed:\n1)Addition\n2)Subtraction\n3)Multiplication\n4)Division\n5)Modulus\n6)Percentage\n7)Logarithm\n8)Increment\n9)Decrement\n"))
if x!=7 and x!=8 and x!=9:
    a=int(input("Enter a number"))
    b=int(input("Enter another number"))
    if x==1:
        c=a+b
        print(c)
    elif x==2:
        c=a-b
        print(c)
    elif x==3:
        c=a*b
        print(c)
    elif x==4:
        c=a/b
        print(c)
    elif x==5:
        c=a%b
        print(c)
    elif x==6:
        c=a/b*100
        print(int(c),"%")
else:
    a=int(input("Enter a Number"))
    if x==7:
        c=math.log(a,2)
        print(c)
    elif x==8:
        c=a+1
        print(c)
    elif x==9:
        c=a-1
        print(c)
