import math
x=int(input("Enter operation to be performed:\n1)Addition\n2)Subtraction\n3)Multiplication\n4)Division\n5)Modulus\n6)Percentage\n7)Logarithm\n8)Sin\n9)Cos\n10)Tan\n11)Cosec\n12)Sec\n13)Cot\n14)Square root\n15)Cube root"))
if x>=7:
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
        c=math.sin(a)
        print(c)
    elif x==9:
        c=math.cos(a)
        print(c)
    elif x==10:
        print(math.tan(a))
    elif x==11:
        print(1/math.sin(a))
    elif x==12:
        print(1/math.cos(a))
    elif x==13:
        print(1/math.tan(a))
    elif x==14:
        print(math.sqrt(a))
    elif x==15:
        print(a**(1/3))