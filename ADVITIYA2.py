# cook your dish here
t=int(input())
for i in range(t):
    a,b,c,d,e=map(int,input().split())
    s=a+b+c+d+e 
    if s>=4:
        print("YES")
    else:
        print("NO")
    