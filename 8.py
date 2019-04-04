import re
str1=input("Enter a string")
cd=cs=cl=cu=ca=0
for i in str1:
    if i.isdigit():
        cd+=1
    if i.isalpha():
        ca+=1
    if i.islower():
        cl+=1
    if i.isupper():
        cu+=1
    if re.findall('[r"^@#$%&*"]',i):
        cs+=1
print('digit\t',cd,'\t','\n','alphabets \t',ca,'\t','\n','lowercase\t',cl, '\t','\n','uppercase\t',cu ,'\t','\n','special characters\t',cs)
