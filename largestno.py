a=[]
    n=10
    for i in range(0,n):
        b=int(input("enter elements:"))
        a.append(b)
    a.sort()
    print("largest element",a[n-1])
