n=int(input("Enter the size of array"))
l=[]
for i in range(n):
    e=int(input("Enter element"))
    l.insert(i,e)
print(l)
res=l[0]
for i in range(1,n):
    res=res^l[i]
print(res)
