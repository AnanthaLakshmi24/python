# cook your dish here
for i in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    s=0
    ans=0
    for i in a:
        if i<m:
            s+=i
            if s>=m:
                ans+=1
                s=0
        else:
            ans+=1
            s=0
    print(ans)