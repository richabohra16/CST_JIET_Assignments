l=[]
n=int(input("Enter the range of numbers"))
for i in range(n):
    e=int(input("Enter number"))
    l.insert(i,e)
l.sort()
minxor=999999
val=0
for i in range(n-1):
    for j in range(i+1,n-1):
        val=l[i]^l[j]
        minxor=min(minxor,val)
print(minxor)



