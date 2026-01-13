# cook your dish here
a,b,c=map(int,input().split())
if a+b>c and b+c>a and a+c>b:
    print("Yes")
elif a==b and b==c and a==c:
    print("Yes")
else:
    print("NO")
