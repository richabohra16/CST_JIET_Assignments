a=[[0, 0, 1, 0],
[1, 0, 0, 1],
[1, 1, 1, 0]]
count=0
for j in range(4):
    sum=0
    for i in  range(3):
        sum+=a[i][j]
    if sum%2==1:
        count+=1

print("Output",count)
