# cook your dish here
t=int(input())
for _ in range(t):
    w=120
    days=int(input())
    s=input()
    c=0
    for i in s:
        if i=="1":
            c=c+1 
    if c+(w-days)>=90:
        print("YES")
    else:
        print("NO")