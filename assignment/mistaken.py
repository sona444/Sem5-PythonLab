n=int(input("size of array"))
list=[]
for i in range(n):
    x=input()
    list.append(x)
print("your entered list=",list)
check=input("Are the inputed elements correct?")
if check=='n':
    locate=int(input("What is the location of the list element starting from 0"))
    correct=input("Enter correct element")
    list[locate]=correct
print(list)