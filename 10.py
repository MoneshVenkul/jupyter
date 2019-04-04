N=int(input("enter n value"))
M=3*n 
T=[(k*'.|.').center(M,'-') for k in range(1,N, 2)]
print('\n'.join(T))
print('WELCOME'.center(M,'-'))
print('\n'.join(T[::-1]))
