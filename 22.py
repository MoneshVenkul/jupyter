def lastline(f,n):
    with open(f) as file:
        print('The     last',n,'lines     from     file:',f)
        for line in(file.readlines()[-n:]):
            print(line,end='')
fname=input('enter     file     name')
n=int(input('no.of     last     lines     to     read'))
try:
    lastline(fname,n)
except:
    print('Error:no     such     File')
