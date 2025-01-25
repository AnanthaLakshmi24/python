# cook your dish here
a=int(input())
for _ in range(a):
    a,b,c,d,e,f=list(map(str, input().split()))
    if  c==b==a=='W' or b==c==d=='W' or c==d==e=='W' or d==e==f=='W':
        print("YES")
    else:
        print("NO")