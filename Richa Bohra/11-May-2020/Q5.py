def sqrt(n):
    temp=0
    while True:
        if temp**2<=n:
            temp+=1
        else:
            temp-=1
            break
    return temp
a=int(input("Enter number"))
print("Sqaure root ",sqrt(a))
