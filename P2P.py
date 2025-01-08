# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    a=input()
    b=input()
    s=0 
    c=0
    for i in range(n):
        if a[i]=="1" and b[i]=="1":
            s=s+1
        elif a[i]=="1" or b[i]=="1":
            c=c+1
    if s%2!=0:
        print("YES")
    elif c>0:
        print("YES")
    else:
        print("NO")