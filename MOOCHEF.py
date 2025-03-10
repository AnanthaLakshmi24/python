# cook your dish here
a = int(input())
for i in range(a):
    n,l,r=map(int,input().split())
    k = list(map(int,input().split()))
    h=0
    ma,mi=0,0
    for i in k:
        if i<=r and i>=l:
            h+=1
        else:
            h-=1
        ma=max(h,ma)
        mi = min(h,mi)
    print(ma, mi)





