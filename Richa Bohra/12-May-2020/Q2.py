def lsearch(mat,n,x):
    i=0
    j=n-1
    while(i<n and j>=0):
        if mat[i][j]==x:
            print("Found at (", i,",", j,")")
            return 1
        if(mat[i][j]>x):
            j-=1
        else:
            i+=1
    print("Not found")
    return 0

a = [ [10, 20, 30, 40],
        [15, 25, 35, 45],
        [27, 29, 37, 48],
        [32, 33, 39, 50] ]
b=int(input("Enter the element to be searched"))
lsearch(a, 4, b)
