a=[1,2]
b=[2,3]
union=a+b
union1=[]
[union1.append(x) for x in union if x not in union1]
print(union1)