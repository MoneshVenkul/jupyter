def evendigit(l,u):
    items =  []
    for i in range(2000,3000):
        s =str(i)
        if(int(s[0])%2==0)and(int(s[1])%2==0)and (int(s[2])%2==0) and (int(s[3])%2==0):
            items.append(s)
        print(",".join(items))
l=input('enter     the     lower     limit')
u=input('enter     the     upper     limit')
evendigit(l,u)
