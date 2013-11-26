sort = [5,4,7,8,3]
i=0
j=0
for i in range(len(sort)-1):
    for j in range(len(sort)-i-1):
        if sort[j]>sort[j+1]:
            sort[j],sort[j+1]=sort[j+1],sort[j]
print sort
