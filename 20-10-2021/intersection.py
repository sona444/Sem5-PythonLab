a=[1,2]
b=[2,3]
intersection=[]
for i in a:
    for j in b:
        if i==j and i not in intersection:
            intersection.append(i)
print(intersection)