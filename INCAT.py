# cook your dish here
s=input()
c=0
for i in s:
    if (i=="c" or i=="a" or i=="t"):
        c=c+1
if c==3:
    print("Yes")
else:
    print("No")