import textwrap
value=input("enter the string")
w=int(input("Enter width"))
Wrapper=textwrap.TextWrapper(width=w)
String=Wrapper.fill(text=value)
print(String)
