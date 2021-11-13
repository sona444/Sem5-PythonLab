n=int(input("size of array"))
list=[]
for i in range(n):
    x=int(input())
    list.append(x)
print("your entered list=",list)
t=[]
fo=[]
fi=[]
for i in range(n):
    if list[i]%3==0:
        t.append(list[i])
    if list[i]%4==0:
        fo.append(list[i])
    if list[i]%5==0:
        fi.append(list[i])
print("Three=",t,"\nFour=",fo,"\nFive",fi)
