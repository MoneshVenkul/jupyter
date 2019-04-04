def evendigit(l,u):
    items =  []
    for i in range(l,u):
        s =str(i)
        if(int(s[0])%2==0)and(int(s[1])%2==0)and (int(s[2])%2==0) and (int(s[3])%2==0):
            items.append(s)
        print(",".join(items))
l=int(input('enter     the     lower     limit'))
u=int(input('enter     the     upper     limit'))
evendigit(l,u)
