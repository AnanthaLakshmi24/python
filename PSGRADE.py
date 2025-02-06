# cook your dish here
for i in range(int(input())):
    ma,mb,mc,mt,a,b,c = map(int,input().split())
    print("YES" if  ma<=a and mb<=b and mc<=c and (a+b+c)>=mt else "NO")