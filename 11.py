n=int(input("Enter the value of n"))
z=int(input("enter the value of z"))
a=[]
s=0
for i in range(0,n):
    n=[int(x)for x in input("Enter the value of N").split()]
    b=int(max(n))
    print(b)
    s=s+(pow(b,3))
    result=s%z
print("result:",result)
